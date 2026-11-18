"""Clinician review of the guideline-chat benchmark, hosted as a Hugging Face Space.

Serves the review page and stores each reviewer's answers in a private Hugging Face dataset repo.
Every save is appended to a JSONL file; CommitScheduler pushes new lines to the dataset about once a minute.
The dataset is the record: on start-up the Space reads it back, so reviewers can continue after a restart or on
another device by entering the same name.

Space settings (Settings -> Variables and secrets):
  DATASET_REPO        variable, e.g. "your-org/eswatini-benchmark-reviews" (created private if it does not exist)
  HF_TOKEN            secret, a token with write access to that dataset
  REVIEW_ACCESS_CODE  secret, optional; if set, reviewers must enter it before anything is read or saved
Without DATASET_REPO the app runs locally and only writes to DATA_DIR (for testing).
"""
import hmac
import json
import os
import re
import threading
import uuid
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
OUT_FILE = OUTBOX / 'responses' / f'{datetime.now(timezone.utc):%Y%m%dT%H%M%S}-{uuid.uuid4().hex[:8]}.jsonl'
QIDS = set(json.loads((HERE / 'qids.json').read_text()))

DECISIONS = {'question_decision': {'', 'keep', 'rewrite'}, 'reference_decision': {'', 'approve', 'edit', 'reject'}}
TEXT_LIMITS = {'question_suggestion': 3000, 'reference_edit': 8000, 'comments': 8000, 'reviewed_at': 40}
MAX_ITEMS, MAX_ITEM_LEN, MAX_BODY = 40, 1000, 2_000_000

lock = threading.Lock()
latest = {}                                      # (reviewer key, question id) -> record
scheduler = None


def reviewer_key(name):
    return re.sub(r'\s+', ' ', name).strip().lower()


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


def start():
    global scheduler
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    load_existing()
    if DATASET_REPO and not TOKEN:
        print('DATASET_REPO is set but HF_TOKEN is not: saving is disabled until the secret is added', flush=True)
        return
    if DATASET_REPO:
        from huggingface_hub import CommitScheduler
        card = OUTBOX / 'README.md'
        if not card.exists():
            card.write_text(DATASET_CARD, encoding='utf-8')
        scheduler = CommitScheduler(repo_id=DATASET_REPO, repo_type='dataset', folder_path=OUTBOX, every=1,
                                    private=True, token=TOKEN)


DATASET_CARD = '''---
pretty_name: Eswatini guideline-chat benchmark reviews
---
# Clinician reviews of the guideline-chat benchmark

Written by the review Space. Each line of `responses/*.jsonl` is one saved answer:
`saved_at` (server time), `reviewer`, `reviewer_key` (lower-case name used to match a reviewer across devices),
`question_id`, `question_decision` (keep / rewrite), `question_suggestion`, `reference_decision` (approve / edit /
reject), `reference_edit`, `must_include`, `must_not_include`, `comments`, `reviewed_at` (reviewer's clock).
A reviewer may save the same question many times; the latest line per reviewer and question is the current answer
(`export_responses.py` in the benchmark folder builds the CSV). Contains reviewer names: keep this dataset private.
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
    lines = ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in recs)
    with lock:
        if scheduler is not None:
            with scheduler.lock:                 # do not write while a commit is being prepared
                with OUT_FILE.open('a', encoding='utf-8') as f:
                    f.write(lines)
        else:
            with OUT_FILE.open('a', encoding='utf-8') as f:
                f.write(lines)
        for r in recs:
            remember(r)
    return JSONResponse({'saved': len(recs)})


@app.get('/healthz')
def healthz():
    return {'ok': True, 'answers': len(latest), 'saving': scheduler is not None or not DATASET_REPO,
            'access_code': bool(ACCESS_CODE)}
