"""Page coverage: runs of >=N words on a PDF page (pdftotext) that occur in none of the chunks covering that page (+/-1).
Usage: python3 page_coverage.py CHUNKS DOC_ID PAGE_TEXT_DIR FIRST LAST [N]"""
import json, re, sys, collections, difflib
chunks, doc, d, first, last = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
N = int(sys.argv[6]) if len(sys.argv) > 6 else 4
tok = lambda s: re.findall(r'[a-z]+|[0-9]+', re.sub(r'</?[a-z][^>]*>', ' ', s.lower()))
K = [json.loads(l) for l in open(chunks)]
K = [k for k in K if k['doc_id'] == doc]
seen, bypage = set(), collections.defaultdict(list)
for k in K:
    key = k.get('table_id') or k['chunk_id']
    if key in seen: continue
    seen.add(key)
    for p in range(k['page_start'] - 1, (k.get('page_end') or k['page_start']) + 2):
        bypage[p].append(tok(k['text']))
tot = 0
for p in range(first, last + 1):
    words = tok(open(f'{d}/p{p}.txt').read())
    grams = set()
    for t in bypage[p]:
        grams.update(tuple(t[i:i + 3]) for i in range(len(t) - 2))
    cov = [False] * len(words)
    for i in range(len(words) - 2):
        if tuple(words[i:i + 3]) in grams:
            cov[i] = cov[i + 1] = cov[i + 2] = True
    runs, cur = [], []
    for w, c in zip(words, cov):
        if not c: cur.append(w)
        else:
            if len(cur) >= N: runs.append(' '.join(cur))
            cur = []
    if len(cur) >= N: runs.append(' '.join(cur))
    runs = [r for r in runs if not re.fullmatch(r'(\d+ )?\d* ?integrated hiv management guidelines( \d+)?', r)]
    if runs:
        tot += sum(len(r.split()) for r in runs)
        print(f'p{p}:', ' // '.join(runs)[:400])
print('uncovered words:', tot)
