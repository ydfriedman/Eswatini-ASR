"""Rebuild running text (sections) from the PDF text layer - variant for guidelines that mark headings by bold font size
(STI/VH draft: Century Gothic Bold 12-20 headings, Century Gothic 10-11 body, Helvetica/Symbol bullets, Times italic captions).

Lines: page header/footer bands dropped (top < HEAD or top > FOOT); bold lines of size >= HMIN are headings; italic Times lines
starting 'Figure'/'Table' are captions (end the running section); white text is table header text (dropped); everything else is body.
Words inside ruled tables (pdfplumber find_tables) and per-page exclusion boxes are dropped (those are re-extracted as items).

Usage: python3 -I text_from_pdf2.py PDF FIRST LAST OFFSET EXCLUDE.json > sections.json
EXCLUDE.json: {"page": [[x0, top, x1, bottom], ...]}  (PDF points)
Output: list of {"page", "page_end", "heading", "size", "lines": [...]} in reading order.
"""
import json, re, sys
import pdfplumber

pdf_path, first, last, off = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
EXCL = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
HEAD, FOOT, HMIN = 50, 790, 11.5
BUL = re.compile(r'^([•●▪◦○]|o\s|\d+[.)]\s|[a-z][.)]\s)')


def kind(w):
    f, s, c = w['fontname'].split('+')[-1], w['size'], w.get('non_stroking_color')
    if w['top'] < HEAD or w['top'] > FOOT:
        return 'furniture'
    if isinstance(c, (list, tuple)) and len(c) == 3 and all(x > 0.95 for x in c):
        return 'callout'                      # white text on a coloured box (table headers are removed with the tables)
    if 'Italic' in f and f.startswith('TimesNewRoman'):
        return 'caption'
    if 'Bold' in f and s >= HMIN:
        return 'heading'
    return 'body'


def inside(b, boxes, pad=2):
    x, y = (b['x0'] + b['x1']) / 2, (b['top'] + b['bottom']) / 2
    return any(x0 - pad <= x <= x1 + pad and t - pad <= y <= bt + pad for x0, t, x1, bt in boxes)


pdf = pdfplumber.open(pdf_path)
out, cur = [], None
for p in range(first, last + 1):
    pg = pdf.pages[p - off - 1]
    boxes = [tb.bbox for tb in pg.find_tables() if tb.bbox[3] - tb.bbox[1] > 20] + [tuple(b) for b in EXCL.get(str(p), [])]
    words = pg.extract_words(extra_attrs=['fontname', 'size', 'non_stroking_color'], keep_blank_chars=False, use_text_flow=False)
    keep = []
    for w in words:
        if inside(w, boxes):
            continue
        w['kind'] = kind(w)
        if w['kind'] != 'furniture':
            keep.append(w)
    keep.sort(key=lambda w: (w['top'] + w['bottom']) / 2)
    rows = []                                   # cluster words into visual lines by vertical centre, then order by x
    for w in keep:
        c = (w['top'] + w['bottom']) / 2
        if rows and abs(rows[-1]['c'] - c) < 4:
            rows[-1]['w'].append(w)
        else:
            rows.append({'c': c, 'w': [w]})
    lines = []
    for row in rows:
        ws = sorted(row['w'], key=lambda w: w['x0'])
        kinds = {w['kind'] for w in ws if w['text'] not in ('●', '•', '▪', '◦', '○')}
        k = ('caption' if 'caption' in kinds else 'heading' if kinds == {'heading'} else 'callout' if kinds == {'callout'} else 'body')
        main = [w for w in ws if w['text'] not in ('●', '•', '▪', '◦', '○')] or ws
        lines.append({'top': min(w['top'] for w in ws), 'bottom': max(w['bottom'] for w in ws), 'x0': ws[0]['x0'], 'kind': k,
                      'text': ' '.join(w['text'] for w in ws), 'size': max(w['size'] for w in main),
                      'bold': all('Bold' in w['fontname'] for w in main)})
    gaps = sorted(b['top'] - a['bottom'] for a, b in zip(lines, lines[1:]) if a['kind'] == b['kind'] == 'body' and 0 < b['top'] - a['bottom'] < 30)
    gap_max = max(7, gaps[len(gaps) // 2] + 5) if gaps else 7     # line spacing varies by page (single / 1.5): paragraph gap is relative
    prev_bottom, prev_kind, prev_bold, prev_x0 = -100, 'body', False, 0
    for ln in lines:
        t = re.sub(r'\s+', ' ', ln['text']).strip()
        if not t:
            continue
        if ln['kind'] == 'caption':
            cur = None
            prev_bottom, prev_kind = ln['bottom'], 'caption'
            continue
        if ln['kind'] == 'heading':
            if cur and cur['page'] == p and not cur['lines'] and prev_kind == 'heading' and ln['top'] - prev_bottom < 15 and cur['size'] == round(ln['size']):
                cur['heading'] += ' ' + t
            else:
                cur = {'page': p, 'page_end': p, 'heading': t, 'size': round(ln['size']), 'lines': []}
                out.append(cur)
            prev_bottom, prev_kind = ln['bottom'], 'heading'
            continue
        if cur is None:
            cur = {'page': p, 'page_end': p, 'heading': None, 'size': 0, 'lines': []}
            out.append(cur)
        cur['page_end'] = p
        if ln['kind'] == 'callout':
            if cur['lines'] and cur['lines'][-1].startswith('Key message: ') and prev_kind == 'callout' and ln['top'] - prev_bottom < 8:
                cur['lines'][-1] += ' ' + t
            else:
                cur['lines'].append('Key message: ' + t)
            prev_bottom, prev_kind = ln['bottom'], 'callout'
            continue
        t = re.sub(r'^[●•▪◦]\s*', '• ', t)
        t = re.sub(r'^○\s*', 'o ', t)
        new_para = (not cur['lines'] or BUL.match(t) or ln['top'] - prev_bottom > gap_max or prev_kind != 'body'
                    or cur['lines'][-1].endswith(':') or ln['bold'] or prev_bold
                    or (re.match(r'^(• |o |\d+[.)] )', cur['lines'][-1]) and ln['x0'] < prev_x0 - 8))   # back at the margin after a list item
        if new_para:
            cur['lines'].append(t)
        else:
            last = cur['lines'][-1]
            cur['lines'][-1] = (last if last.endswith('-') and not last.endswith(' -') else last + ' ') + t
        prev_bottom, prev_kind, prev_bold, prev_x0 = ln['bottom'], 'body', ln['bold'] and len(t) < 80, ln['x0']
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
