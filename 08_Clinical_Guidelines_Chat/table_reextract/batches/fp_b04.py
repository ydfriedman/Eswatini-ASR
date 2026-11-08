exec(open('batches/fp_common.py').read())
# FP 2021 tables re-transcribed from the page images (second pass over the tables first rebuilt from the
# old chunks; same table_ids). Everything not given here (replaces_chunks, heading path, context_before, flags) is carried
# over from the item as left by fp_b03, so apply this batch once, after fp_b03.
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
 X("tbl-p32-0044", None, None, pages=[32, 33]),
 X("tbl-p34-0048", None, UNWRAP),
 X("tbl-p40-0060", None, None, pages=[40, 41],
   source_flags=["POP eligibility: acute DVT/pulmonary embolism is placed in category 3; the WHO MEC (2015) puts it in category 2 for progestin-only pills. Ritonavir-boosted protease inhibitors are category 3 here; WHO MEC 2015 lists them as category 2 for POPs (reduced effectiveness is less of a concern than for combined methods). Check against the current WHO MEC before relying on these two rows."],
   footnotes=["Printed rotated across pp.29-30 of the guide (PDF pp.40-41); the four category columns continue on the second page."]),
 X("tbl-p63-0115", None, UNWRAP),
 X("tbl-p51-0086", None, REBULLET, pages=[51, 52],
   footnotes=["Printed rotated across pp.40-41 of the guide (PDF pp.51-52); each column continues on the second page."],
   flags=("'Smoking, if under 35 years old' is listed under MEC category 1 and 'Smoking and age less than 35 years' under category 2; the WHO MEC puts smoking at age <35 in category 2.",)),
 X("tbl-p57-0100", None,
   [r(LL("Women of any parity", "Are of any age, including adolescents and women over 40 years old", "Have just had an abortion or miscarriage", "Smoke any number of cigarettes daily and are under 35 years old", "Smoke fewer than 15 cigarettes daily and are over 35 years old", "Have anaemia or history of anaemia", "Have varicose veins", "Are living with HIV, whether or not on antiretroviral therapy").replace("- ", "• "),
      LL("Age above 40 years", "Breastfeeding more than 6 months after delivery", "Non-breastfeeding women 21 – 42 day with no risk of venous thromboembolism", "Smoking and age less than 35 years", "Obesity", "History of high blood pressure during pregnancy where blood pressure is measured and is normal", "Family history of DVT/PE", "Major surgery without prolonged immobilization", "Superficial thrombosis", "Uncomplicated Valvular heart disease", "Systemic lupus erythematous (associated with severe thrombocytopenia or are on Immunosuppressive treatment)", "Non-migraine headache (mild or severe)", "Migraine headache without aura at age less than 35 years for Initiating clients", "Unexplained vaginal bleeding before evaluation", "Cervical intraepithelial neoplasia or cervical cancer awaiting treatment", "Undiagnosed breast mass", "Uncomplicated Diabetes Mellitus", "Asymptomatic gall bladder disease", "HIV treatment with NNRTIs and PIs").replace("- ", "• "),
      LL("Breastfeeding 6 weeks to 6 months after delivery", "Non-breastfeeding less than 21 days after delivery with or without risk of venous thromboembolism", "Smoking and age more than 35 years", "Hypertension (history of hypertension, hypertension controlled on treatment, moderate hypertension)", "Migraine headache without aura at age less than 35 years for continuing clients", "Symptomatic gall bladder disease", "Acute Viral hepatitis").replace("- ", "• "),
      LL("Breastfeeding less than 6 weeks postpartum", "Severe hypertension (systolic >160 or diastolic >100 mm Hg) and hypertension with vascular complications", "History of DVT/PE or current DVT/PE or DVT/PE on anticoagulant therapy", "Major surgery with prolonged immobilization", "History of stroke", "History of or current ischaemic heart disease", "Complicated Valvular heart disease", "Complicated Diabetes Mellitus (vascular complications e.g. nephropathy, retinopathy)", "HIV/AIDS on treatment Ritonavir boosted PIs", "TB patients on Rifampicin or Rifabutin therapy", "Systemic Lupus Erythematosus with positive antiphospholipid antibodies", "Migraine headache without aura at age more than 35 years for continuing clients", "Migraine headache with aura at any age", "Severe liver cirrhosis (decompensated)", "Current breast cancer", "Liver Cancer", "Anticonvulsant therapy (phenytoin, carbamazepine, barbiturates)", "Multiple risk factors for arterial cardiovascular disease (such as older age, smoking, diabetes and hypertension)").replace("- ", "• "))],
   pages=[57, 58],
   footnotes=["Printed rotated across pp.46-47 of the guide (PDF pp.57-58); each column continues on the second page. An empty bullet in the category 2 column on p.47 is omitted."],
   flags=("CIC eligibility differs from the WHO MEC (2015) in several rows: smoking <15 cigarettes/day at age ≥35 is category 1 here (WHO 2); ritonavir-boosted protease inhibitors, rifampicin/rifabutin and enzyme-inducing anticonvulsants are category 4 here (WHO 2 for combined injectables); migraine without aura at age ≥35 in continuing users is category 4 here (WHO 3). Check against the current WHO MEC.",)),
]
