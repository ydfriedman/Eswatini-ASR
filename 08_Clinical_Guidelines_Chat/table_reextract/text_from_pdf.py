"""Rebuild running text (sections) from the PDF text layer, for guidelines where the old parse dropped lines.

Lines are classified by font: body (Calibri 11), headings (purple ArialNarrow-Bold / Calibri), callout boxes (white
ArialNarrow text on coloured boxes -> 'Key message:' lines), captions (blue italic: used only as section breaks),
footers and figure labels (small or light fonts: dropped). Words inside ruled tables (pdfplumber find_tables) and
inside per-page exclusion boxes (figures whose labels use body fonts) are dropped; those are re-extracted as items.

Usage: python3 -I text_from_pdf.py PDF FIRST LAST OFFSET EXCLUDE.json > sections.json
EXCLUDE.json: {"page": [[x0, top, x1, bottom], ...]}   (PDF points)
Output: list of {"page", "page_end", "heading", "level", "lines": [...]} in reading order.
"""
import json, re, sys
import pdfplumber

pdf_path, first, last, off = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
EXCL = json.load(open(sys.argv[5])) if len(sys.argv) > 5 else {}
PURPLE = (0.439, 0.188, 0.627)


def col(c):
    c = c.get('non_stroking_color')
    if isinstance(c, (list, tuple)):
        return tuple(round(x, 3) for x in c)
    return (c,)


def kind(ch):
    f, s, c = ch['fontname'].split('+')[-1], ch['size'], col(ch)
    if f.startswith('Calibri-Light'):
        return 'footer'
    if s < 9.8:
        return 'small'
    if 'Italic' in f and f.startswith('ArialNarrow'):
        return 'caption'
    if c == PURPLE:
        return 'heading'
    if c in ((1.0,), (1, 1, 1), (1.0, 1.0, 1.0)):     # white text on a coloured box
        return 'callout'
    if f.startswith('ArialNarrow') or f.startswith('Arial'):
        return 'callout' if s >= 9.8 else 'small'
    return 'body'


def inside(b, boxes, pad=2):
    x = (b['x0'] + b['x1']) / 2
    y = (b['top'] + b['bottom']) / 2
    return any(x0 - pad <= x <= x1 + pad and t - pad <= y <= bt + pad for x0, t, x1, bt in boxes)


pdf = pdfplumber.open(pdf_path)
out, cur = [], None
for p in range(first, last + 1):
    pg = pdf.pages[p - off - 1]
    boxes = [tb.bbox for tb in pg.find_tables()] + [tuple(b) for b in EXCL.get(str(p), [])]
    words = pg.extract_words(extra_attrs=['fontname', 'size', 'non_stroking_color'], keep_blank_chars=False, use_text_flow=False)
    words.sort(key=lambda w: (round(w['top'] / 3), w['x0']))   # reading order by position (content-stream order is unreliable)
    lines = []
    for w in words:
        if inside(w, boxes):
            continue
        k = kind(w)
        if k in ('footer', 'small'):
            continue
        if lines and abs(lines[-1]['top'] - w['top']) < 3 and lines[-1]['kind'] == k:
            lines[-1]['text'] += ' ' + w['text']; lines[-1]['x1'] = w['x1']
        else:
            lines.append({'top': w['top'], 'x0': w['x0'], 'x1': w['x1'], 'kind': k, 'text': w['text'], 'bottom': w['bottom']})
    for ln in lines:
        t = ln['text'].strip()
        if not t:
            continue
        if ln['kind'] == 'caption':
            cur = None                       # a figure/table caption ends the running section
            continue
        if ln['kind'] == 'heading':
            if cur and cur['lines'] == [] and cur['page'] == p:
                cur['heading'] += ' ' + t; continue
            cur = {'page': p, 'page_end': p, 'heading': t, 'lines': []}
            out.append(cur); continue
        if cur is None:
            cur = {'page': p, 'page_end': p, 'heading': None, 'lines': []}
            out.append(cur)
        cur['page_end'] = p
        if ln['kind'] == 'callout':
            if cur['lines'] and cur['lines'][-1].startswith('Key message: ') and ln['top'] - prev_bottom < 8:
                cur['lines'][-1] += ' ' + t
            else:
                cur['lines'].append('Key message: ' + t)
        else:
            new_para = (not cur['lines'] or cur['lines'][-1].startswith('Key message: ') or re.match(r'^([•▪●]|o\s|\d+\.\s|[IVX]+\.)', t)
                        or ln['top'] - prev_bottom > 6 or prev_kind != 'body')
            if new_para:
                cur['lines'].append(t)
            else:
                last = cur['lines'][-1]
                cur['lines'][-1] = (last if last.endswith('-') and not last.endswith(' -') else last + ' ') + t
        prev_bottom, prev_kind = ln['bottom'], ln['kind']
    if lines:
        prev_bottom, prev_kind = -100, 'body'
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
