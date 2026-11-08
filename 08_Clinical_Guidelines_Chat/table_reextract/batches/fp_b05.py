exec(open('batches/fp_common.py').read())
# FP 2021 tables re-transcribed from the page images (second pass over the tables first rebuilt from the
# old chunks; same table_ids). Everything not given here (replaces_chunks, heading path, context_before, flags) is carried
# over from the item as left by fp_b04, so apply this batch once, after fp_b04.
import json as _j
_prev = {t['table_id']: t for t in _j.load(open('fp-2021_tables.json'))['tables']}
def X(tid, header, body, cap=None, flags=(), **kw):
    p = _prev['fp-2021-' + tid]
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
ITEMS = [
 X("tbl-p96-0188", None,
   lambda b: STEPSEC(UNWRAP([row for i, row in enumerate(b) if not (isinstance(row, list) and row[0]['t'].startswith("5. Recommendations for CHC use among women with known dyslipidaemias") and any(isinstance(x, list) and x[0]['t'] == row[0]['t'] for x in b[:i]))])),
   cap="14.1 Appendix 1: Summary of Recommendation - Medical Eligibility Criteria (sections 1-10)", pages=[96, 97, 98, 99, 100, 101, 102],
   footnotes=["Printed rotated over several pages. The GRADE evidence rating is printed once per group of rows (a merged cell) and applies to the rows below it until the next rating. Section 11 onwards is in the next item."]),
 X("tbl-p103-0195", [r("TOPIC", "MEC RECOMMENDATION", "GRADE ASSESSMENT OF QUALITY OF EVIDENCE")],
   lambda b: STEPSEC(UNWRAP([[C("11. Recommendations for use of progesterone-releasing vaginal ring – new method added to the guideline"), C(""), C("")]] + b)),
   cap="14.1 Appendix 1: Summary of Recommendation - Medical Eligibility Criteria (sections 11-12)",
   footnotes=["Continuation of Appendix 1. The GRADE rating is printed once per group of rows and applies to the rows below it."]),
 X("tbl-p114-0206", [r("NO", "Question", "YES")],
   [r("", q, "") for q in [
     "1. Did you have a baby less than 6 months ago, are you exclusive breastfeeding, and had amenorrhea since then?",
     "2. Have you abstained from sexual intercourse since your last monthly bleeding or delivery?",
     "3. Have you had a baby in the last 4 weeks?",
     "4. Did your last monthly bleeding start within the past 7 days (or within the past 12 days if the client is planning to use an IUD)?",
     "5. Have you had a miscarriage or abortion in the last 7 days (or within the past 12 days if the client is planning to use an IUD)?",
     "6. Have you been using a reliable contraceptive method consistently and correctly?"]],
   cap="14.4 Appendix 4: Pregnancy Checklist",
   footnotes=["NO and YES are tick-box columns either side of each question.",
              "If the client answered “yes” to at least one of the questions, and she has no signs or symptoms of pregnancy, you can give her the method she has chosen.",
              "If the client answered “no” to all questions, pregnancy cannot be ruled out. The client should wait for her next monthly bleeding or use a pregnancy test."]),
 X("tbl-p107-0201", None,
   lambda b: [[dict(c, t=_re.sub(r'\s*<br/>\s*', ' ', c['t'].replace('<br/><br/>', '\x00')).replace('\x00', '<br/>').replace('  ', ' ')) for c in row] for row in
              [b[0], [b[1][0], C("Condom"), b[1][2]], b[2],
               [b[3][0], C("POIs, COCs, CICs, Implants, IUCD"), b[3][2]],
               [b[8][0], C("POPs, POIs, CICs, Implants"), b[8][2]]] + b[12:25] + [[b[25][0], C("BTL"), b[25][2]], [b[26][0], C("BTL"), b[26][2]]] + b[27:]],
   pages=[107, 108, 109, 110, 111, 112, 113],
   footnotes=["Where several methods (commodities) share one management cell in the source, they are listed together in one row. 'BTL' (bilateral tubal ligation) covers wound infection, abscess and haematoma; 'Pain at incision' has no commodity printed."],
   flags=("Condom spillage or breakage: the only action given is 'Offer comprehensive PEP'; emergency contraception (within 120 hours) should also be offered, and PEP applies only where HIV exposure is possible.",)),
 X("tbl-p116-0210", None, None,
   flags=("Appendix 6 covers efavirenz, nevirapine and protease inhibitors but not dolutegravir, now the preferred first-line ARV in Eswatini; dolutegravir has no clinically significant interaction with hormonal contraceptives, and efavirenz with implants (the main concern listed) applies only to clients still on EFV-based regimens.",)),
]
