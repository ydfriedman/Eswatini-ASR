"""Propose cell repairs for a spec table from the ruled grid in the PDF.

For every cell of the spec item, the PDF grid cell holding its words is found; when the PDF cell has
words the spec cell lacks (runs of >=2 words, or any number), the PDF cell text is proposed as the
replacement. PDF grid cells inside the table that match no spec cell are listed (rows continued over
a page break, rows the old parse dropped).

Usage: python3 -I grid_repair.py SPEC.json PAGEMAP.json OUT.json TABLE_ID [TABLE_ID ...]
OUT.json: {table_id: {"cells": {"b:3:2": "new text", ...}, "unmatched": [[page, text], ...]}}
Review the proposals, edit OUT.json if needed, then apply with a batch that calls apply_grid_patch().
"""
import difflib, json, re, sys
import pdfplumber

spec_path, pm_path, out_path, *tids = sys.argv[1:]
spec = json.load(open(spec_path))
PM = json.load(open(pm_path))
T = {t['table_id']: t for t in spec['tables']}
tok = lambda s: [t for t in re.findall(r'[a-z]+|[0-9]+', s.lower()) if t not in ('x', 'o')]
BUL = re.compile(r'^\s*([•●▪■◦\-–*]|\d+[.)]|[a-z][.)]|o\s)\s*')
_pdf = {}


def page(doc, p):
    for a, b, path, i0 in PM[doc]:
        if a <= p <= b:
            if path not in _pdf:
                _pdf[path] = pdfplumber.open(path)
            return _pdf[path].pages[i0 + p - a]


def cell_text(pg, bb):
    txt = pg.crop((bb[0] + 0.5, bb[1] + 0.5, bb[2] - 0.5, bb[3] - 0.5)).extract_text() or ''
    out = []
    for line in txt.split('\n'):
        line = line.strip()
        if not line:
            continue
        if out and not BUL.match(line) and not out[-1].endswith(':'):
            out[-1] = (out[-1][:-1] if out[-1].endswith('-') and not out[-1].endswith(' -') else out[-1] + ' ') + line
        else:
            out.append(re.sub(r'^[•●▪■◦]\s*', '• ', line))
    return '<br/>'.join(out)


def missing(ours, pdf):
    a, b = tok(pdf), tok(ours)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    cov = [False] * len(a)
    for bl in sm.get_matching_blocks():
        if bl.size >= 2 or (bl.size == 1 and len(a[bl.a]) >= 5):
            for i in range(bl.a, bl.a + bl.size):
                cov[i] = True
    miss = [w for w, c in zip(a, cov) if not c]
    return miss


res = {}
for tid in tids:
    t = T[tid]
    doc = spec['doc_id']
    cells = [('h', ri, ci, c) for ri, row in enumerate(t.get('header', [])) for ci, c in enumerate(row)] + \
            [('b', ri, ci, c) for ri, row in enumerate(t.get('body', [])) for ci, c in enumerate(row)]
    grid = []
    for p in t.get('pages', [t['page']]):
        pg = page(doc, p)
        for tb in pg.find_tables():
            for row in tb.rows:
                for bb in row.cells:
                    if bb:
                        grid.append((p, bb, cell_text(pg, bb)))
    used, patch = set(), {}
    for kind, ri, ci, c in cells:
        ours = c.get('t', '') if isinstance(c, dict) else str(c)
        ot = tok(ours)
        if len(ot) < 1:
            continue
        best, score = None, 0
        for gi, (p, bb, gt) in enumerate(grid):
            g = tok(gt)
            if not g:
                continue
            m = sum(bl.size for bl in difflib.SequenceMatcher(None, ot, g, autojunk=False).get_matching_blocks())
            s = m / max(len(ot), 1) - 0.01 * gi / 1000
            if m >= min(3, len(ot)) and s > score:
                best, score = gi, s
        if best is None or score < 0.6:
            continue
        used.add(best)
        miss = missing(ours, grid[best][2])
        if len([w for w in miss if not w.isdigit()]) >= 2 or any(w.isdigit() for w in miss):
            patch[f'{kind}:{ri}:{ci}'] = {'ours': ours, 'pdf': grid[best][2], 'missing': ' '.join(miss)}
    region_tokens = set(w for _, _, _, c in cells for w in tok(c.get('t', '') if isinstance(c, dict) else str(c)))
    unmatched = []
    for gi, (p, bb, gt) in enumerate(grid):
        g = tok(gt)
        if gi in used or len(g) < 2:
            continue
        frac = sum(1 for w in g if w in region_tokens) / len(g)
        if frac >= 0.3:  # inside this table (shares vocabulary) but no spec cell maps to it
            unmatched.append([p, gt])
    res[tid] = {'cells': patch, 'unmatched': unmatched}
    print(f'\n##### {tid}  ({len(patch)} cell proposals, {len(unmatched)} unmatched PDF cells)')
    for k, v in patch.items():
        print(f'  [{k}] missing: {v["missing"][:160]}\n     PDF: {v["pdf"][:400]}')
    for p, gt in unmatched[:15]:
        print(f'  [unmatched p{p}] {gt[:300]}')
json.dump(res, open(out_path, 'w'), ensure_ascii=False, indent=1)
