"""Ceiling check: rank of the best gold passage in the raw rankings over ALL chunks, before the app's caps,
dedup, expansion and top-k. Shows whether a miss is the embedding/keyword search itself or a later step.

usage: python3 rank_eval.py APP_DIR REVISED_QUESTIONS OUT.json
"""
import json, sys, sqlite3
from array import array
sys.path.insert(0, sys.argv[1])
import app  # noqa: E402

db = sqlite3.connect(app.INDEX)
rows = db.execute('SELECT chunk_id, doc_id, table_id, vector FROM chunks').fetchall()
db.close()
ids = [r[0] for r in rows]
table_of = {r[0]: r[2] or '' for r in rows}
vecs = []
for r in rows:
    v = array('f'); v.frombytes(r[3]); vecs.append(v)
allowed = sorted({r[1] for r in rows})

def best_rank(order, gold):
    for i, cid in enumerate(order, 1):
        if cid in gold or (table_of.get(cid) and table_of[cid] in gold):
            return i
    return None

out = []
for line in open(sys.argv[2], encoding='utf-8'):
    q = json.loads(line)
    gold = {s.split()[0] for s in q.get('sources') or []}
    if not gold:
        continue
    qv = app.embedding_request([q['question'][:2000]])[0]
    sims = sorted(((sum(a * b for a, b in zip(qv, v)), cid) for v, cid in zip(vecs, ids)), reverse=True)
    sem = [cid for _, cid in sims]
    kw = app.keyword_ranking(q['question'], allowed, limit=len(ids))
    fused = {cid: 1 / (60 + i) for i, cid in enumerate(sem, 1)}
    for i, cid in enumerate(kw[:40], 1):          # the app fuses only the top 40 keyword hits
        fused[cid] += 1 / (60 + i)
    hyb = sorted(fused, key=fused.get, reverse=True)
    out.append({'id': q['id'], 'semantic': best_rank(sem, gold), 'keyword': best_rank(kw, gold),
                'hybrid': best_rank(hyb, gold)})
json.dump(out, open(sys.argv[3], 'w'), indent=1)
for k in ('semantic', 'keyword', 'hybrid'):
    rk = [o[k] for o in out]
    print(f"{k:9} gold in top 1: {sum(1 for r in rk if r and r <= 1):3}  top 6: {sum(1 for r in rk if r and r <= 6):3}  "
          f"top 20: {sum(1 for r in rk if r and r <= 20):3}  top 50: {sum(1 for r in rk if r and r <= 50):3}  of {len(rk)}")
