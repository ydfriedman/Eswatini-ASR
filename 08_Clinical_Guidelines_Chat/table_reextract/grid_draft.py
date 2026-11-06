"""Draft table items from ruled PDF grids (pdfplumber), to be checked against the page images and corrected by hand.

Merged cells: pdfplumber gives None for positions covered by a merged cell. A None with a real cell to its left in the same
row extends that cell's colspan; otherwise it extends the rowspan of the cell above. Narrow side tables (page furniture, the
chapter tabs) are skipped. Captions are taken from the 'Table N.N ...' line just above the grid in the page text.

Usage: python3 -I grid_draft.py PDF FIRST LAST OFFSET MIN_WIDTH > drafts.json
Output: [{"page", "bbox", "caption", "rows": [[{"t", "cs", "rs"}, ...], ...]}]
"""
import json, re, sys
import pdfplumber

pdf_path, first, last, off = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
minw = float(sys.argv[5]) if len(sys.argv) > 5 else 250
BUL = re.compile(r'^\s*([•●▪■◦∞➢✓]|-\s?|o\s|\d+[.)]\s|[a-z][.)]\s)')


def cell_text(pg, bb):
    txt = pg.crop((max(bb[0] + 0.5, 0), max(bb[1] + 0.5, 0), min(bb[2] - 0.5, pg.width), min(bb[3] - 0.5, pg.height))).extract_text() or ''
    out = []
    for line in txt.split('\n'):
        line = line.strip()
        if not line:
            continue
        if out and not BUL.match(line) and not out[-1].endswith(':'):
            out[-1] = (out[-1] if out[-1].endswith('-') else out[-1] + ' ') + line
        else:
            out.append(re.sub(r'^[•●▪■◦∞➢]\s*', '• ', line))
    return '<br/>'.join(out)


pdf = pdfplumber.open(pdf_path)
res = []
for p in range(first, last + 1):
    pg = pdf.pages[p - off - 1]
    words = pg.extract_words()
    for tb in pg.find_tables():
        x0, top, x1, bot = tb.bbox
        if x1 - x0 < minw:
            continue
        grid = []
        for row in tb.rows:
            grid.append([{'t': cell_text(pg, bb)} if bb else None for bb in row.cells])
        out = []
        for ri, row in enumerate(grid):
            cur = []
            for ci, c in enumerate(row):
                if c is not None:
                    c = dict(c, _c=ci); cur.append(c); continue
                if cur and cur[-1]['_c'] + cur[-1].get('cs', 1) == ci:
                    cur[-1]['cs'] = cur[-1].get('cs', 1) + 1
                else:
                    for prev in reversed(out):   # extend the rowspan of the cell above that covers this column
                        hit = [d for d in prev if d['_c'] == ci]
                        if hit:
                            hit[0]['rs'] = hit[0].get('rs', 1) + 1
                            break
            if cur:
                out.append(cur)
        rows = [[{k: v for k, v in c.items() if k != '_c'} for c in r] for r in out]
        # caption: nearest line above the grid starting with 'Table'
        above = sorted([w for w in words if w['bottom'] <= top + 2 and w['top'] > top - 40], key=lambda w: (round(w['top']), w['x0']))
        line = ' '.join(w['text'] for w in above if abs(w['top'] - (above[-1]['top'] if above else 0)) < 3) if above else ''
        cap_m = re.search(r'(Table\.?\s?\d+\.\d+.*)', ' '.join(w['text'] for w in above))
        res.append({'page': p, 'bbox': [round(v) for v in tb.bbox], 'caption': cap_m.group(1).strip() if cap_m else '', 'rows': rows})
json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
