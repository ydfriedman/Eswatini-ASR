"""Clinician review of the guideline-chat benchmark, hosted as a Hugging Face Space.

Serves the review page and stores each reviewer's answers in a private Hugging Face dataset repo: one file per
reviewer (responses/<name>-<id>.jsonl) with one line per question, holding that reviewer's latest answer. The page
saves a question when the reviewer clicks Save and next or moves on; each save rewrites the reviewer's file, and
CommitScheduler pushes changed files to the dataset about once a minute.
The dataset is the record: on start-up the Space reads it back, so reviewers can continue after a restart or on
another device by entering the same name.

Space settings (Settings -> Variables and secrets):
  DATASET_REPO        variable, e.g. "your-org/eswatini-benchmark-reviews" (created private if it does not exist)
  HF_TOKEN            secret, a token with write access to that dataset
  REVIEW_ACCESS_CODE  secret, optional; if set, reviewers must enter it before anything is read or saved
Without DATASET_REPO the app runs locally and only writes to DATA_DIR (for testing).
"""
import hashlib
import hmac
import json
import os
import re
import threading
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse

HERE = Path(__file__).resolve().parent
DATASET_REPO = os.environ.get('DATASET_REPO', '').strip()
TOKEN = os.environ.get('HF_TOKEN') or None
ACCESS_CODE = os.environ.get('REVIEW_ACCESS_CODE', '').strip()
DATA_DIR = Path(os.environ.get('DATA_DIR', '/tmp/review_data'))
OUTBOX = DATA_DIR / 'outbox'                     # folder CommitScheduler mirrors into the dataset
QORDER = {qid: i for i, qid in enumerate(json.loads((HERE / 'qids.json').read_text()))}
QIDS = set(QORDER)

DECISIONS = {'question_decision': {'', 'keep', 'rewrite'}, 'reference_decision': {'', 'approve', 'edit', 'reject'}}
TEXT_LIMITS = {'question_suggestion': 3000, 'reference_edit': 8000, 'comments': 8000, 'reviewed_at': 40}
MAX_ITEMS, MAX_ITEM_LEN, MAX_BODY = 40, 1000, 2_000_000

lock = threading.Lock()
latest = {}                                      # (reviewer key, question id) -> record
scheduler = None
setup_error = ''                                 # why saving is off, shown on /healthz


def scoped_api(token):
    """HfApi whose create_repo accepts an existing repo when the token may not create repos.

    CommitScheduler always calls create_repo(exist_ok=True). A fine-grained token limited to the responses dataset
    (the safest choice for this Space) is refused that call with 403 even though the dataset exists, so on 403 we
    check the dataset is reachable and use it as is. The dataset itself is created once by its owner.
    """
    from huggingface_hub import HfApi
    from huggingface_hub.errors import HfHubHTTPError
    from huggingface_hub.hf_api import RepoUrl

    class Api(HfApi):
        def create_repo(self, repo_id, *, repo_type=None, **kwargs):
            try:
                return super().create_repo(repo_id, repo_type=repo_type, **kwargs)
            except HfHubHTTPError as exc:
                if getattr(exc.response, 'status_code', None) != 403:
                    raise
                self.repo_info(repo_id, repo_type=repo_type)      # raises if the token cannot reach it
                prefix = 'datasets/' if repo_type == 'dataset' else 'spaces/' if repo_type == 'space' else ''
                return RepoUrl(f'{self.endpoint}/{prefix}{repo_id}', endpoint=self.endpoint)

    return Api(token=token)


def reviewer_key(name):
    return re.sub(r'\s+', ' ', name).strip().lower()


def reviewer_file(key):
    """responses/<readable name>-<short hash>.jsonl: readable in the dataset, and unique per reviewer."""
    slug = re.sub(r'[^a-z0-9]+', '-', key).strip('-')[:40] or 'reviewer'
    return OUTBOX / 'responses' / f'{slug}-{hashlib.sha1(key.encode()).hexdigest()[:6]}.jsonl'


def write_reviewer(key):
    """Rewrite one reviewer's file: one line per question they have answered (latest answer), in question order."""
    recs = sorted((r for (k, _), r in latest.items() if k == key), key=lambda r: QORDER.get(r['question_id'], 9999))
    path = reviewer_file(key)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in recs), encoding='utf-8')
    tmp.replace(path)


def remember(rec):
    k = (rec['reviewer_key'], rec['question_id'])
    old = latest.get(k)
    if old is None or (rec.get('reviewed_at') or '', rec['saved_at']) >= (old.get('reviewed_at') or '', old['saved_at']):
        latest[k] = rec


def load_existing():
    """Read every response already in the dataset (and any local file) so saved work survives restarts."""
    files = list(OUTBOX.glob('responses/*.jsonl'))
    if DATASET_REPO:
        from huggingface_hub import snapshot_download
        try:
            snap = snapshot_download(DATASET_REPO, repo_type='dataset', token=TOKEN, allow_patterns='responses/*.jsonl',
                                     local_dir=DATA_DIR / 'remote')
            files += list(Path(snap).glob('responses/*.jsonl'))
        except Exception as exc:                 # first run: the dataset does not exist yet
            print(f'No existing responses loaded from {DATASET_REPO}: {type(exc).__name__}', flush=True)
    for f in files:
        for line in f.read_text(encoding='utf-8').splitlines():
            if line.strip():
                remember(json.loads(line))
    print(f'Loaded {len(latest)} saved answers from {len(files)} files', flush=True)


def describe_token():
    """Log what HF_TOKEN may do (name, role, repo scopes; never its value) to diagnose permission problems."""
    from huggingface_hub import HfApi
    try:
        who = HfApi(token=TOKEN).whoami()
        tok = (who.get('auth') or {}).get('accessToken') or {}
        fg = tok.get('fineGrained') or {}
        scopes = [(s.get('entity', {}).get('type'), s.get('entity', {}).get('name'), s.get('permissions'))
                  for s in fg.get('scoped', [])]
        print(f"HF_TOKEN: account {who.get('name')}, token '{tok.get('displayName')}', role {tok.get('role')}, "
              f"scopes {scopes}, global {fg.get('global')}", flush=True)
    except Exception as exc:
        print(f'HF_TOKEN is not accepted by Hugging Face: {type(exc).__name__}', flush=True)


def start():
    global scheduler, setup_error
    (OUTBOX / 'responses').mkdir(parents=True, exist_ok=True)
    load_existing()
    if DATASET_REPO and not TOKEN:
        setup_error = 'HF_TOKEN secret is not set'
        print('DATASET_REPO is set but HF_TOKEN is not: saving is disabled until the secret is added', flush=True)
        return
    if DATASET_REPO:
        describe_token()
        from huggingface_hub import CommitScheduler
        card = OUTBOX / 'README.md'
        if not card.exists():
            card.write_text(DATASET_CARD, encoding='utf-8')
        try:
            scheduler = CommitScheduler(repo_id=DATASET_REPO, repo_type='dataset', folder_path=OUTBOX, every=1,
                                        private=True, token=TOKEN, hf_api=scoped_api(TOKEN))
        except Exception as exc:                 # keep serving the page; saving stays off (503) until fixed
            setup_error = f'{type(exc).__name__}: {str(exc).splitlines()[-1][:200]}'
            print(f'Saving disabled: could not connect to {DATASET_REPO}: {exc}', flush=True)


DATASET_CARD = '''---
pretty_name: Eswatini guideline-chat benchmark reviews
---
# Clinician reviews of the guideline-chat benchmark

Written by the review Space. Each reviewer has one file, `responses/<name>-<id>.jsonl`, with one line per question
they have answered (their latest answer; saving a question again replaces its line):
`saved_at` (server time), `reviewer`, `reviewer_key` (lower-case name used to match a reviewer across devices),
`question_id`, `question_decision` (keep / rewrite), `question_suggestion`, `reference_decision` (approve / edit /
reject), `reference_edit`, `must_include`, `must_not_include`, `comments`, `reviewed_at` (reviewer's clock).
`export_responses.py` in the benchmark folder combines all reviewers into one CSV. Contains reviewer names: keep
this dataset private.
'''

app = FastAPI(title='Guideline answer review', docs_url=None, redoc_url=None, openapi_url=None)
start()


def check_code(code):
    if ACCESS_CODE and not hmac.compare_digest((code or '').encode(), ACCESS_CODE.encode()):
        raise HTTPException(401, 'Access code required')


def clean_answer(a):
    if not isinstance(a, dict):
        raise HTTPException(400, 'Bad answer')
    out = {}
    for field, allowed in DECISIONS.items():
        v = a.get(field, '')
        if v not in allowed:
            raise HTTPException(400, f'Bad {field}')
        out[field] = v
    for field, limit in TEXT_LIMITS.items():
        v = a.get(field, '')
        if not isinstance(v, str):
            raise HTTPException(400, f'Bad {field}')
        out[field] = v[:limit]
    for field in ('must_include', 'must_not_include'):
        v = a.get(field, [])
        if not isinstance(v, list) or len(v) > MAX_ITEMS or not all(isinstance(x, str) for x in v):
            raise HTTPException(400, f'Bad {field}')
        out[field] = [x[:MAX_ITEM_LEN] for x in v]
    return out


@app.get('/')
def index():
    return FileResponse(HERE / 'static' / 'index.html', headers={'Cache-Control': 'no-cache'})


@app.get('/api/config')
def config():
    return {'code_required': bool(ACCESS_CODE)}


@app.get('/api/responses')
def get_responses(reviewer: str = '', code: str = ''):
    check_code(code)
    key = reviewer_key(reviewer)
    if not key:
        raise HTTPException(400, 'Reviewer name required')
    with lock:
        answers = {qid: {f: rec[f] for f in ('question_decision', 'question_suggestion', 'reference_decision',
                                             'reference_edit', 'must_include', 'must_not_include', 'comments',
                                             'reviewed_at')}
                   for (k, qid), rec in latest.items() if k == key}
    return {'answers': answers}


@app.post('/api/responses')
async def post_responses(request: Request):
    if int(request.headers.get('content-length') or 0) > MAX_BODY:
        raise HTTPException(413, 'Too large')
    try:
        body = await request.json()
    except ValueError:
        raise HTTPException(400, 'Bad JSON')
    check_code(body.get('code'))
    if DATASET_REPO and scheduler is None:
        raise HTTPException(503, 'Saving is not set up yet')
    name = body.get('reviewer')
    if not isinstance(name, str) or not reviewer_key(name) or len(name) > 120:
        raise HTTPException(400, 'Reviewer name required')
    answers = body.get('answers')
    if not isinstance(answers, dict) or not answers or len(answers) > len(QIDS):
        raise HTTPException(400, 'No answers')
    now = datetime.now(timezone.utc).isoformat(timespec='seconds')
    recs = []
    for qid, a in answers.items():
        if qid not in QIDS:
            raise HTTPException(400, f'Unknown question {qid}')
        recs.append({'saved_at': now, 'reviewer': name.strip(), 'reviewer_key': reviewer_key(name),
                     'question_id': qid, **clean_answer(a)})
    key = reviewer_key(name)
    with lock:
        for r in recs:
            remember(r)
        if scheduler is not None:
            with scheduler.lock:                 # do not write while a commit is being prepared
                write_reviewer(key)
        else:
            write_reviewer(key)
    return JSONResponse({'saved': len(recs)})


@app.get('/healthz')
def healthz():
    return {'ok': True, 'answers': len(latest), 'saving': scheduler is not None or not DATASET_REPO,
            'access_code': bool(ACCESS_CODE), 'problem': setup_error}
