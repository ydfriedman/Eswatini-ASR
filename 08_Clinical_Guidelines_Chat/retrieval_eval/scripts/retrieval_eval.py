"""Retrieval test for the guideline chat: which benchmark questions get their gold source passages in front of the model?

Runs the app's real ai_answer() (search, Amendment step, expansion, caps, high-risk gate) with the model calls
replaced: the planner returns the question itself as the only search query (or queries from --queries), and the
answer call records the sources it would have been given. Nothing is generated.

usage: python3 retrieval_eval.py APP_DIR REVISED_QUESTIONS REVIEW_DATA OUT.json [--label X] [--queries planner.json]
Settings come from the environment (RETRIEVAL_TOP_K, RETRIEVAL_EXPANSION, RETRIEVAL_MODE, AMENDMENT_SCORE_MARGIN).
"""
import argparse, json, os, sys, sqlite3, time
from array import array

ap = argparse.ArgumentParser()
ap.add_argument('app_dir'); ap.add_argument('revised'); ap.add_argument('review_data'); ap.add_argument('out')
ap.add_argument('--label', default='')
ap.add_argument('--queries', help='JSON {qid: [query, ...]} from a planner run; default: the question only')
args = ap.parse_args()
sys.path.insert(0, args.app_dir)
import app  # noqa: E402

os.environ['LLM_MODEL'] = 'llama3.1:8b'     # the deployed model name (switches on the llama-only branches)

# Query embeddings are cached so repeated runs only embed each search query once.
_real_embed = app.embedding_request
_cache = {}
def cached_embed(texts):
    if len(texts) == 1:
        if texts[0] not in _cache:
            _cache[texts[0]] = _real_embed(texts)[0]
        return [_cache[texts[0]]]
    return _real_embed(texts)
app.embedding_request = cached_embed

planner_queries = json.load(open(args.queries)) if args.queries else {}
current = {}

class Captured(Exception):
    pass

def fake_llm(instructions, content, schema, name):
    if name == 'retrieval_queries':
        qs = planner_queries.get(current['id'], [current['question']])
        return {'route': 'answer', 'clarifying_question': '', 'queries': qs}
    if name == 'guideline_answer':
        current['sources'] = content['sources']
        raise Captured()
    raise RuntimeError(name)
app.llm_json = fake_llm

# evidence_is_ambiguous() receives the final source list just before the answer call: record it there.
_real_ambiguous = app.evidence_is_ambiguous
def recording_ambiguous(question, sources, search_queries):
    current['final'] = [{'chunk_id': s.get('chunk_id'), 'type': s.get('type'),
                         'approx_tokens': s.get('approx_tokens') or 0, 'doc': s['document']['id']} for s in sources]
    current['queries'] = list(search_queries)
    reason = _real_ambiguous(question, sources, search_queries)
    current['ambiguity'] = reason
    return reason
app.evidence_is_ambiguous = recording_ambiguous

# chunk_id -> table_id, and approx tokens, from the index the app built
db = sqlite3.connect(app.INDEX)
table_of = dict(db.execute("SELECT chunk_id, table_id FROM chunks"))
db.close()

rev = [json.loads(l) for l in open(args.revised, encoding='utf-8') if l.strip()]
area = {q['id']: q.get('area', '') for q in json.load(open(args.review_data, encoding='utf-8'))}
results = []
t0 = time.time()
for r in rev:
    gold = [s.split()[0] for s in r.get('sources') or []]
    current.clear(); current.update(id=r['id'], question=r['question'])
    outcome = 'answer_call'
    try:
        res = app.ai_answer(r['question'], [], 'All programs', True)
        outcome = 'source_only' if res.get('mode') == 'sources' else 'routed:' + res.get('kind', '')
    except Captured:
        pass
    sources = current.get('final', [])
    for s in sources:
        s['table_id'] = table_of.get(s['chunk_id']) or ''
    prompt_chars = sum(len(p['passage']) for p in current.get('sources', [])) if outcome == 'answer_call' else 0
    results.append({'id': r['id'], 'area': area.get(r['id'], ''), 'gold': gold, 'outcome': outcome,
                    'ambiguity': current.get('ambiguity', ''), 'queries': current.get('queries', []),
                    'sources': sources, 'passage_chars': prompt_chars})
print(f'{len(results)} questions in {time.time() - t0:.0f}s', file=sys.stderr)
json.dump({'label': args.label, 'env': {k: os.environ.get(k) for k in
           ('RETRIEVAL_TOP_K', 'RETRIEVAL_EXPANSION', 'RETRIEVAL_MODE', 'AMENDMENT_SCORE_MARGIN', 'RETRIEVAL_EXPANSION_HITS')},
           'results': results}, open(args.out, 'w'), indent=1)
