exec(open('batches/mh_common.py').read())
# Mental Health desk guide tables re-transcribed from the page images (second pass over the tables first rebuilt from the
# old chunks; same table_ids). Everything not given here (replaces_chunks, heading path, context_before, flags) is carried
# over from the item as left by mh_b05, so apply this batch once, after mh_b05.
import json as _j
_prev = {t['table_id']: t for t in _j.load(open('mental-health-deskguide_tables.json'))['tables']}
def X(tid, header, body, cap=None, flags=(), **kw):
    p = _prev['mental-health-deskguide-' + tid]
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
ITEMS = [
 # Table 25 compared with the page image (Nov 2026): content matches; caption tidied.
 X("tbl-p72-0159", None, None, cap="TABLE 25: SPECIAL CONSIDERATIONS IN THE MANAGEMENT OF MAJOR DEPRESSIVE DISORDERS"),
]
