"""Check cell placement of re-extracted tables against word positions in the PDF.

For each table, every cell with a distinctive run of words is located on its PDF page(s).
A cell is suspicious when it sits in another column's x-band (closer to another column's
median left edge than its own) or outside its row's vertical band (above the previous row
or below the next row). Tables whose column medians are not left-to-right are flagged whole.

Usage: python3 -I audit_cell_positions.py CHUNKS PAGEMAP.json OUT.json [doc_id ...]
PAGEMAP.json: {doc_id: [[first_orig_page, last_orig_page, pdf_path, pdf_index_of_first_page], ...]}
(pdf index is 0-based). Only generated-id tables (-tbl-pNN-NNNN) are checked unless --all.
"""
import html as H, json, re, statistics, sys
import pdfplumber

args = [a for a in sys.argv[1:] if not a.startswith('--')]
ALL = '--all' in sys.argv
chunks, pagemap, out = args[:3]
docs = set(args[3:])
PM = json.load(open(pagemap))
G = re.compile(r'-tbl-p\d+-\d{4}$')
tok = lambda s: [t for t in re.findall(r'[a-z]+|[0-9]+', s.lower()) if t not in ('x', 'o')]

units = {}
for l in open(chunks):
    k = json.loads(l)
    t = k.get('table_id')
    if t and k['doc_id'] in PM and (not docs or k['doc_id'] in docs) and (ALL or G.search(t)) and t not in units and k.get('html'):
        units[t] = k

_open, _words, _grid, _tbox = {}, {}, {}, {}


def page_tokens(doc, p):
    for a, b, path, i0 in PM[doc]:
        if a <= p <= b:
            key = (path, i0 + p - a)
            if key not in _words:
                if path not in _open:
                    _open[path] = pdfplumber.open(path)
                pg = _open[path].pages[key[1]]
                ws = pg.extract_words(keep_blank_chars=False, use_text_flow=False)
                _words[key] = [(t, w['x0'], w['top'] + p * 10000, p, (w['x0'] + w['x1']) / 2, (w['top'] + w['bottom']) / 2)
                               for w in ws for t in tok(w['text'])]
                cells = []
                _tbox[p] = [tb.bbox for tb in pg.find_tables()]
                for ti, tb in enumerate(pg.find_tables()):
                    for ri, row in enumerate(tb.rows):
                        for ci, bb in enumerate(row.cells):
                            if bb:
                                cells.append((ti, ri, ci, bb))
                _grid[p] = cells
            return _words[key]
    return []


def parse(htm):
    rows = []
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', htm, re.S):
        row, col = [], 0
        for attrs, body in re.findall(r'<t[hd]([^>]*)>(.*?)</t[hd]>', tr, re.S):
            cs = int((re.search(r'colspan="(\d+)"', attrs) or [0, 1])[1])
            txt = re.sub(r'</?[a-z][^>]*>', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', body)))
            row.append((col, cs, txt))
            col += cs
        rows.append(row)
    return rows


def locate(T, stream, used):
    toks = [t[0] for t in stream]
    if not T:
        return None
    for k in sorted({min(len(T), n) for n in (2, 3, 5, 8, len(T))}):
        if k == 1 and (len(T[0]) < 4 or T[0].isdigit()):
            return None
        hits = [i for i in range(len(toks) - k + 1) if toks[i:i + k] == T[:k] and i not in used]
        if len(hits) == 1:
            used.add(hits[0])
            return stream[hits[0]]
        if not hits:
            break
    for t in T:  # fall back to a word that occurs once on the page
        if len(t) >= 5 and not t.isdigit():
            hits = [i for i in range(len(toks)) if toks[i] == t and i not in used]
            if len(hits) == 1:
                used.add(hits[0])
                return stream[hits[0]]
    return None


def missing_words(u, pages):
    """Per ruled PDF cell of this table: words not covered by a matching run (>=2 words) in the chunk."""
    import difflib
    chunk = tok(re.sub(r'</?[a-z][^>]*>', ' ', H.unescape(re.sub(r'<[^>]+>', ' ', u['html']))))
    chunkset = set(chunk)
    runs, total, inreg = [], 0, 0
    for p in pages:
        ws = page_tokens(u['doc_id'], p)
        for ti, bb in enumerate(_tbox.get(p, [])):
            region = [w for w in ws if bb[0] - 1 <= w[4] <= bb[2] + 1 and bb[1] - 1 <= w[5] <= bb[3] + 1]
            if len(region) < 5 or sum(1 for w in region if w[0] in chunkset) / len(region) < 0.6:
                continue  # a different table on the same page
            inreg += len(region)
            for (t_, ri, ci, cb) in [c for c in _grid[p] if c[0] == ti]:
                cell = [w[0] for w in region if cb[0] - 1 <= w[4] <= cb[2] + 1 and cb[1] - 1 <= w[5] <= cb[3] + 1]
                if not cell:
                    continue
                sm = difflib.SequenceMatcher(None, cell, chunk, autojunk=False)
                cov = [False] * len(cell)
                for bl in sm.get_matching_blocks():
                    if bl.size >= 2 or len(cell) == 1 or (bl.size == 1 and len(cell[bl.a]) >= 6):
                        for i in range(bl.a, bl.a + bl.size):
                            cov[i] = True
                i = 0
                while i < len(cell):
                    if cov[i]:
                        i += 1
                        continue
                    j = i
                    while j < len(cell) and not cov[j]:
                        j += 1
                    seg = cell[i:j]
                    if len(seg) >= 2 or any(c.isdigit() for c in seg[0]) and seg[0] not in chunkset:
                        total += len(seg)
                        runs.append(' '.join(seg))
                    i = j
    return inreg, total, runs


report = {}
for tid, u in units.items():
    stream = []
    for p in range(u['page_start'], (u.get('page_end') or u['page_start']) + 1):
        stream += page_tokens(u['doc_id'], p)
    if not stream:
        report[tid] = {'status': 'no-page'}
        continue
    pages = range(u['page_start'], (u.get('page_end') or u['page_start']) + 1)
    inreg, nmiss, runs = missing_words(u, pages)
    cover = {'pdf_words_in_table': inreg, 'missing_words': nmiss, 'missing_runs': runs[:12], 'missing_runs_all': runs}
    rows = parse(u['html'])
    used, loc = set(), []
    for r, row in enumerate(rows):
        for col, cs, txt in row:
            hit = locate(tok(txt), stream, used)
            if hit:
                g = next(((ti, ri, ci) for ti, ri, ci, (x0, t0, x1, b1) in _grid.get(hit[3], [])
                          if x0 - 1 <= hit[4] <= x1 + 1 and t0 - 1 <= hit[5] <= b1 + 1), None)
                loc.append((r, col, cs, txt, hit[1], hit[2], hit[3], g))
    ncells = sum(len(r) for r in rows)
    ing = [l for l in loc if l[7]]
    if loc and len(ing) >= 0.7 * len(loc):
        issues = []
        # column mapping: our column -> modal grid column (per page/table); flag cells whose grid column differs
        import collections
        cmap = collections.defaultdict(collections.Counter)
        for r, col, cs, txt, x, y, pg, g in ing:
            if cs == 1:
                cmap[(pg, g[0], col)][g[2]] += 1
        for r, col, cs, txt, x, y, pg, g in ing:
            if cs == 1 and sum(cmap[(pg, g[0], col)].values()) >= 2:
                mode, n = cmap[(pg, g[0], col)].most_common(1)[0]
                if g[2] != mode and n >= 2:
                    issues.append({'kind': 'wrong-column', 'row': r, 'col': col, 'grid_col': g[2], 'usual_grid_col': mode, 'cell': txt[:80]})
        # row order: grid position (page, table, row) must not go backwards as our row index grows
        seq = sorted(ing, key=lambda l: (l[0], l[1]))
        best = {}
        for r, col, cs, txt, x, y, pg, g in seq:
            best.setdefault(r, []).append((pg, g[0], g[1]))
        rows_sorted = sorted(best)
        for a, b in zip(rows_sorted, rows_sorted[1:]):
            if max(best[b]) < min(best[a]):
                issues.append({'kind': 'wrong-row', 'row': b, 'note': f'grid rows {sorted(set(best[b]))} come before row {a} {sorted(set(best[a]))}'})
        # two of our rows in different grid rows within one of our rows -> merged rows
        for r, gs in best.items():
            if len({(p_, t_) for p_, t_, _ in gs}) == 1 and len({g_ for *_, g_ in gs}) > 1 and len(gs) >= 2:
                spread = sorted({g_ for *_, g_ in gs})
                if spread[-1] - spread[0] >= 1:
                    issues.append({'kind': 'row-spans-grid-rows', 'row': r, 'grid_rows': spread})
        report[tid] = {'doc': u['doc_id'], 'page': u['page_start'], 'cells': ncells, 'located': len(loc), 'method': 'grid', **cover,
                       'issues': issues, 'caption': (re.search(r'<caption>(.*?)</caption>', u['html'], re.S) or [0, ''])[1][:90]}
        continue
    loc = [l[:6] for l in loc]
    cols = {}
    for r, col, cs, txt, x, y in loc:
        if cs == 1:
            cols.setdefault(col, []).append(x)
    med = {c: statistics.median(v) for c, v in cols.items() if len(v) >= 2}
    issues = []
    order = [med[c] for c in sorted(med)]
    if any(b < a - 5 for a, b in zip(order, order[1:])):
        issues.append({'kind': 'columns-out-of-order', 'medians': [round(m) for m in order]})
    rowy = {}
    for r, col, cs, txt, x, y in loc:
        rowy.setdefault(r, []).append(y)
    rmed = {r: statistics.median(v) for r, v in rowy.items()}
    rs = sorted(rmed)
    for r, col, cs, txt, x, y in loc:
        if cs == 1 and col in med and len(med) >= 2:
            near = min(med, key=lambda c: abs(med[c] - x))
            if near != col and abs(med[col] - x) - abs(med[near] - x) > 15:
                issues.append({'kind': 'wrong-column', 'row': r, 'col': col, 'looks_like_col': near, 'cell': txt[:80]})
        i = rs.index(r)
        prev = rmed[rs[i - 1]] if i > 0 else None
        nxt = rmed[rs[i + 1]] if i + 1 < len(rs) else None
        if (prev is not None and y < prev - 3 and rmed[r] > prev) or (nxt is not None and y > nxt + 3 and rmed[r] < nxt):
            issues.append({'kind': 'wrong-row', 'row': r, 'col': col, 'cell': txt[:80]})
    report[tid] = {'doc': u['doc_id'], 'page': u['page_start'], 'cells': ncells, 'located': len(loc), 'method': 'geometry', **cover,
                   'issues': issues, 'caption': (re.search(r'<caption>(.*?)</caption>', u['html'], re.S) or [0, ''])[1][:90]}

json.dump(report, open(out, 'w'), indent=1)
mm = [v for v in report.values() if v.get('missing_runs')]
print(f'{len(mm)} tables with runs of >=3 PDF words missing from the chunk; '
      f'{sum(1 for v in report.values() if not v.get("pdf_words_in_table"))} tables with no ruled grid found (not checked)')
n = [v for v in report.values() if v.get('issues')]
cov = [v['located'] / v['cells'] for v in report.values() if v.get('cells')]
print(f'{len(report)} tables, {len(n)} with issues, median located {statistics.median(cov):.0%}, '
      f'{sum(1 for c in cov if c < .3)} tables <30% located, {sum(1 for v in report.values() if v.get("status"))} no page')
