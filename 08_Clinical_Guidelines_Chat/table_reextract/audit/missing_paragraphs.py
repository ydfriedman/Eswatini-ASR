"""Find prose paragraphs on each PDF page that no chunk of the document contains.

A page's text layer (pdftotext -layout, pN.txt) is split into blocks at blank lines. Table-like lines (cells separated
by runs of 3+ spaces) are left out: tables are separate items and are checked against the page images. A block of
>= 8 words counts as MISSING when fewer than half of its word trigrams occur anywhere in the document's chunks.
Lines recurring on >= 15% of pages, page numbers aside (headers/footers, overprinted lists), are ignored.

Usage: python3 audit/missing_paragraphs.py CHUNKS OUT_JSON [doc ...]
Output: {doc: [{"page", "block_index", "text", "prev_text", "covered_by_prev"}]}  (prev = the nearest covered block before it)
"""
import collections, json, os, re, sys

S = os.environ.get('PAGE_TEXT_ROOT', 'page_text') + '/'   # folder holding one sub-folder of pN.txt files per guideline (RAW below)
RAW = {'hiv-2022': 'hiv_raw', 'hiv-amendment-2024': 'amd_work', 'ncdimh': 'ncd_work', 'prep-2025': 'prep_work',
       'anc': 'anc_work', 'sti-vh-draft-2026': 'sti_raw', 'unaids-linkages-sop': 'lk_work4', 'tb-2025': 'tb_raw',
       'fp-2021': 'fp_raw', 'mental-health-deskguide': 'mh_raw'}
tok = lambda s: re.findall(r'[a-z]+|[0-9]+', re.sub(r'</?[a-z][^>]*>', ' ', (s or '').lower()))
TABLE_LINE = re.compile(r'\S {3,}\S.* {3,}\S|\S {6,}\S|\.{6,}|…{3,}')


def blocks(text):
    out, cur = [], []
    for ln in text.split('\n'):
        if not ln.strip():
            if cur: out.append(cur); cur = []
        else:
            cur.append(ln)
    if cur: out.append(cur)
    return out


chunks_path, out_path = sys.argv[1], sys.argv[2]
docs = sys.argv[3:] or list(RAW)
K = [json.loads(l) for l in open(chunks_path)]
result = {}
for doc in docs:
    raw = S + RAW[doc]
    pages = sorted(int(f[1:-4]) for f in os.listdir(raw) if re.fullmatch(r'p\d+\.txt', f))
    ptext = {p: open(f'{raw}/p{p}.txt', errors='ignore').read() for p in pages}
    lc = collections.Counter()
    for p in pages:
        lc.update({' '.join(x for x in tok(l) if not x.isdigit()) for l in ptext[p].split('\n') if tok(l)})
    boiler = {l for l, c in lc.items() if c >= max(3, 0.15 * len(pages)) or re.fullmatch(r'[\d ]+', l)}
    grams = set()
    for k in K:
        if k['doc_id'] == doc:
            t = tok(k['text']); grams.update(tuple(t[i:i + 3]) for i in range(len(t) - 2))
    miss = []
    for p in pages:
        prev = None
        for bi, b in enumerate(blocks(ptext[p])):
            lines = [l for l in b if not TABLE_LINE.search(l.strip()) and ' '.join(x for x in tok(l) if not x.isdigit()) not in boiler]
            w = tok(' '.join(lines))
            if len(w) < 3: continue
            g = [tuple(w[i:i + 3]) for i in range(len(w) - 2)]
            cov = sum(x in grams for x in g) / max(1, len(g))
            if cov < 0.5 and len(w) >= 8:
                miss.append({'page': p, 'block_index': bi, 'text': '\n'.join(l.strip() for l in lines),
                             'prev_text': prev, 'coverage': round(cov, 2)})
            elif cov >= 0.5:
                prev = ' '.join(l.strip() for l in lines)[-160:]
    result[doc] = miss
    print(f'{doc:26} missing blocks {len(miss):4}  words {sum(len(tok(m["text"])) for m in miss):6}  pages {len({m["page"] for m in miss})}')
json.dump(result, open(out_path, 'w'), ensure_ascii=False, indent=1)
