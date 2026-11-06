"""Classify audit missing-word runs: 'elsewhere' (found in another chunk of the same doc),
'rotated' (reversed text from a rotated page), or 'lost'. Usage: classify_missing.py CHUNKS AUDIT.json OUT.json"""
import json, re, sys, collections
tok = lambda s: [t for t in re.findall(r'[a-z]+|[0-9]+', s.lower()) if t not in ('x', 'o')]
chunks, audit, out = sys.argv[1:4]
R = json.load(open(audit))
bydoc = collections.defaultdict(list)
for l in open(chunks):
    k = json.loads(l)
    bydoc[k['doc_id']].append(k)
docstr = {}
def present(doc, tid, seq):
    key = (doc, tid)
    if key not in docstr:
        docstr[key] = ' ' + ' '.join(' '.join(tok(k['text'])) for k in bydoc[doc] if k.get('table_id') != tid) + ' '
    return (' ' + ' '.join(seq) + ' ') in docstr[key]
vocab = {}
def garbled(doc, seq):
    if doc not in vocab:
        vocab[doc] = set(t for k in bydoc[doc] for t in tok(k['text']))
    long = [w for w in seq if len(w) >= 4]
    return len(long) >= 2 and sum(1 for w in long if w not in vocab[doc]) / len(long) > 0.3
res = {}
for tid, v in R.items():
    lost, elsewhere, rotated = [], [], []
    for run in v.get('missing_runs_all', v.get('missing_runs', [])):
        seq = run.split()
        rev = [w[::-1] for w in seq]
        if garbled(v['doc'], seq):
            rotated.append(run)
        elif any(present(v['doc'], tid, seq[i:i + 4]) for i in range(0, max(1, len(seq) - 3), 2)) and len(seq) >= 2:
            elsewhere.append(run)
        elif sum(1 for w in rev if w in ('kg', 'mg', 'weight', 'date', 'name', 'number', 'height')) or any(present(v['doc'], tid, rev[i:i + 2]) for i in range(len(rev) - 1)):
            rotated.append(run)
        else:
            lost.append(run)
    res[tid] = dict(v, lost=lost, elsewhere=elsewhere, rotated=rotated, lost_words=sum(len(r.split()) for r in lost))
json.dump(res, open(out, 'w'), indent=1)
bad = sorted((v for v in res.values() if v['lost_words'] >= 3), key=lambda v: -v['lost_words'])
print(len(bad), 'tables with >=3 lost words;', sum(1 for v in res.values() if v['elsewhere']), 'with text found elsewhere')
for v in bad:
    print(v['lost_words'], v['doc'], v['page'], v['caption'][:50], '|', ' / '.join(v['lost'])[:200])
