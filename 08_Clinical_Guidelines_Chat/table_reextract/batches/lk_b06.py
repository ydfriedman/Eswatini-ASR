exec(open('batches/lk_common.py').read())
# Linkages SOP tables re-transcribed from the page images (second pass over the tables first rebuilt from the
# old chunks; same table_ids). Everything not given here (replaces_chunks, heading path, context_before, flags) is carried
# over from the item as left by lk_b05, so apply this batch once, after lk_b05.
import json as _j
_prev = {t['table_id']: t for t in _j.load(open('unaids-linkages-sop_tables.json'))['tables']}
def X(tid, header, body, cap=None, flags=(), **kw):
    p = _prev['unaids-linkages-sop-' + tid]
    d = {"table_id": p['table_id'], "page": p['page'], "image_only": False, "heading_path": p['heading_path'], "caption": cap or p['caption'],
         "replaces_chunks": p['replaces_chunks'], "row_header_cols": kw.pop('rhc', p.get('row_header_cols', 1)), "header": p['header'] if header is None else header, "body": p['body'] if body is None else (body(p['body']) if callable(body) else body), "footnotes": kw.pop('footnotes', None) or (p.get('footnotes', []) if body is None or callable(body) else []),
         "source_flags": [f for f in p.get('source_flags', []) if f not in flags] + list(flags), "pages": p.get('pages', [p['page']])}
    d.update({k: v for k, v in p.items() if k not in d})
    d.update(kw); return d
def LL(*xs): return "<br/>".join("- " + x for x in xs)
BR = "<br/>".join
def STEPSEC(b):  # rows whose other cells are empty become section rows
    return [{"section": row[0]['t']} if isinstance(row, list) and all(not c['t'].strip() for c in row[1:]) else row for row in b]
def LASTSPAN(n):  # make the last body row one cell spanning n columns
    return lambda b: b[:-1] + [[C(b[-1][0]['t'], cs=n)]]
def DRUGS(*ds, sep="OR", ncol=6):
    """Drug job-aid rows: each d = (medicine, dose, frequency, duration, max dose, codes[, titration]); alternatives separated by an 'OR' row."""
    out = []
    for i, d in enumerate(ds):
        if i and sep: out.append({"section": sep})
        out.append(r(*d[:ncol]))
        if len(d) > ncol and d[ncol]: out.append([C(d[ncol], cs=ncol)])
    return out
HD = [r("Medicine", "Dose", "Frequency", "Duration", "Max dose", "Codes")]
DRUGNOTE = "Each medicine row is followed by its titration instruction where one is printed; 'OR' marks alternatives (printed in a narrow left column)."
import re as _re
def UNWRAP(b):  # join PDF line-wraps inside cells; keep breaks before bullets
    return [row if isinstance(row, dict) else [dict(c, t=_re.sub(r'<br/>(?![•\-o] )', ' ', c['t'])) for c in row] for row in b]
def REBULLET(b):  # restore line breaks lost before bullets ('... text • Next item')
    return [row if isinstance(row, dict) else [dict(c, t=_re.sub(r'(?<!<br/>)\s+• ', '<br/>• ', c['t'])) for c in row] for row in b]
def H2B(newh, cap=None, **kw):
    """Return kwargs for X(): the old header row was really the first body row; put it back and use newh as the header."""
    return dict(header=newh, body=lambda b: None, cap=cap, **kw)
def HB(tid, newh, fix=None, **kw):
    p = _prev['unaids-linkages-sop-' + tid]
    body = [list(p['header'][0])] + p['body']
    if fix: body = fix(body)
    return X(tid, newh, body, **kw)
def COLJOIN(b):  # one row per table: each column's non-empty cells joined (bullet items that had been paired across columns)
    rows = [r_ for r_ in b if isinstance(r_, list)]
    n = max(len(r_) for r_ in rows)
    return [[C("<br/>".join(r_[i]['t'] for r_ in rows if i < len(r_) and r_[i]['t'].strip())) for i in range(n)]]
ITEMS = [
 # Review of the Linkages tables the second pass had judged by length only: content matches the page images; fixes are cosmetic.
 X("tbl-p43-0063", None, None, cap="12.8 Day 14 responsibilities: client initiated on ART"),
 X("tbl-p47-0071", None, lambda b: [[C(_re.sub(r'\s+- (?=[A-Za-z])', '<br/>- ', c['t'].replace('To ensure s/ - he understands', 'To ensure s/he understands'))) for c in row] for row in b],
   cap="12.13 Clients initiated on ART (Day 30-45: second clinic visit, 2nd ARV refill)"),
 X("tbl-p48-0073", None, lambda b: [[C(_re.sub(r'\s+- (?=[A-Za-z])', '<br/>- ', _re.sub(r'(^|\s)- o ', r'\1- ', c['t']))) for c in row] for row in b],
   cap="12.14 Clients delaying initiation on ART (Day 30-45)"),
 X("tbl-p51-0078", None, lambda b: [[b[0][0], b[0][1], C(LL("To ensure s/he understands whole process.", "Call linkages facilitator if they will not be able to attend the scheduled appointment for setting another appointment date", "Contact your health care provider right away if you experience or observe anything you familiar with"))]],
   cap="12.16 Days 60-90: third clinic visit (3rd ARV refill) – clients initiated on ART",
   footnotes=["The last Linkage facilitator item is cut off in the source: '...confirm availability to discuss and help the client if they have'. 'anything you familiar with' is as printed (presumably 'unfamiliar')."]),
 X("tbl-p52-0081", [[C("Linkage Facilitator", cs=2)], r("Clients initiated on ART", "Clients delaying ART initiation")], None,
   cap="12.17 Day 120-125: fifth telephonic call – during telephone call", rhc=0),
 X("tbl-p54-0087", None, None, cap="12.19 Day 170-175: sixth telephonic call – during telephone call", rhc=0,
   footnotes=["The callout above the table: During the phone call first ascertain if it is the right client and convenient time, if yes proceed and if no reschedule."]),
 X("tbl-p55-0089", [[C("Linkage Facilitator", cs=2)], r("Clients initiated on ART", "Clients delaying ART initiation")], None,
   cap="12.20 Day 180 sixth clinical visit (6th ARV refill) – the last visit in the LCM", rhc=0),
 X("tbl-p60-0097", [[C("EC/MM/Nurse/Doctor", cs=2)], r("Clients initiating ART at referring health facility", "Clients not initiated at referring facility")], None,
   cap="12.24 Responsibilities At Receiving Facility", rhc=0),
]
