"""Phrase-level loss check: 4-word sequences in each item's replaced old chunks (chunks_v2) that occur nowhere in
the document's new chunks (chunks_v3). Reports lost runs per item. Usage: python3 lost_phrases.py [doc ...] (from 08_Clinical_Guidelines_Chat)"""
import json, re, sys, collections
tok = lambda s: re.findall(r'[a-z]+|[0-9]+', re.sub(r'</?[a-z][^>]*>', ' ', s.lower()))
old = {}
for l in open('chunks_v2/chunks.jsonl'):
    k = json.loads(l); old[k['chunk_id']] = k
new = [json.loads(l) for l in open('chunks_v3/chunks.jsonl')]
docs = sys.argv[1:] or ['hiv-amendment-2024', 'ncdimh', 'prep-2025', 'anc', 'unaids-linkages-sop', 'tb-2025', 'fp-2021', 'mental-health-deskguide']
out = []
for doc in docs:
    S = json.load(open(f'table_reextract/{doc}_tables.json'))
    grams = set()
    for k in new:
        if k['doc_id'] == doc:
            w = tok(k['text']); grams.update(tuple(w[i:i + 4]) for i in range(len(w) - 3))
    for t in S['tables']:
        if t.get('kind') == 'diagram':
            continue  # diagrams were rewritten as descriptions on purpose
        for c in t['replaces_chunks']:
            if c not in old:
                continue
            w = tok(old[c]['text'])
            miss = [i for i in range(len(w) - 3) if tuple(w[i:i + 4]) not in grams]
            runs, cur = [], []
            for i in miss:
                if cur and i > cur[-1] + 1:
                    runs.append(cur); cur = []
                cur.append(i)
            if cur: runs.append(cur)
            runs = [' '.join(w[r[0]:r[-1] + 4]) for r in runs if len(r) >= 4]
            if runs:
                out.append((sum(len(r.split()) for r in runs), t['table_id'], c, runs))
out.sort(reverse=True)
for n, tid, c, runs in out:
    print(n, tid, c, '|', ' // '.join(runs)[:260])
