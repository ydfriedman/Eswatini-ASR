"""Extract ruled tables from PDF pages as rows of cell text (exact text layer, bullets kept as line starts).
Used as the text source when transcribing tables; structure is checked against the page image.

Usage: python3 -I grid_extract.py PDF FIRST_PAGE LAST_PAGE [PAGE_OFFSET] > out.json
Output: [{"page": n, "table": i, "bbox": [...], "rows": [[cell, ...], ...]}, ...]  (None = merged/spanned cell)
"""
import json, re, sys
import pdfplumber

BUL = re.compile(r'^\s*([•●▪■◦∞➢✓\-–*]|\d+[.)]\s|[a-z][.)]\s|o\s)')


def cell_text(pg, bb):
    crop = pg.crop((max(bb[0] + 0.5, 0), max(bb[1] + 0.5, 0), min(bb[2] - 0.5, pg.width), min(bb[3] - 0.5, pg.height)))
    txt = crop.extract_text(layout=False) or ''
    out = []
    for line in txt.split('\n'):
        line = line.strip()
        if not line:
            continue
        if out and not BUL.match(line):
            prev = out[-1]
            out[-1] = (prev if prev.endswith('-') and not prev.endswith(' -') else prev + ' ') + line
        else:
            out.append(re.sub(r'^[•●▪■◦∞➢]\s*', '• ', line))
    return '\n'.join(out)


pdf_path, first, last = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
off = int(sys.argv[4]) if len(sys.argv) > 4 else 0
pdf = pdfplumber.open(pdf_path)
res = []
for p in range(first, last + 1):
    pg = pdf.pages[p - off - 1]
    for ti, tb in enumerate(pg.find_tables()):
        rows = [[cell_text(pg, bb) if bb else None for bb in row.cells] for row in tb.rows]
        res.append({"page": p, "table": ti, "bbox": [round(x) for x in tb.bbox], "rows": rows})
json.dump(res, sys.stdout, ensure_ascii=False, indent=1)
