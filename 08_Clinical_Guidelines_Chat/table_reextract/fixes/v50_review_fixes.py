"""Fixes from the user's review of the 50-item validation sample (Nov 2026).

Edits the spec files in place (idempotent). Run from table_reextract/ AFTER the batches tb_b11, fp_b06, lk_b05 have been added:
    python3 fixes/v50_review_fixes.py
"""
import json, re

def load(doc): return json.load(open(doc + '_tables.json'))
def save(doc, d): json.dump(d, open(doc + '_tables.json', 'w'), ensure_ascii=False, indent=1)
def item(d, doc, tid):
    return next(t for t in d['tables'] if t['table_id'] == doc + '-' + tid)

C3 = "Chapter 3: Overview of Different Psychiatric Conditions"
C4 = "Chapter 4: Job Aids for Different Psychiatric Conditions"
TB11 = "Chapter 11: Tuberculosis Preventive Treatment"

HEADINGS = {
 'mental-health-deskguide': {
  'tbl-p17-0027': f"{C3} > Major Depressive Disorder > Table 1: Summary of Classification and Management of Depressive Disorders",
  'tbl-p24-0036': f"{C3} > Major Depressive Disorder > Table 2: Stepwise Management of Major Depressive Disorders",
  'tbl-p25-0040': f"{C3} > Generalized Anxiety Disorder (GAD) and Panic Disorder > Table 4: Stepwise Management of GAD and Panic Disorder",
  'tbl-p28-0050': f"{C3} > Trauma and Stressor Related Disorders > Table 6: Stepwise Management of Trauma and Stressor Related Disorders",
  'tbl-p34-0064': f"{C3} > Suicide and Self-Harm > Table 7: Stepwise Management of Suicide and Self Harm",
  'tbl-p39-0074': f"{C3} > Sexual Assault and Psychiatry > Table 10: Stepwise Management of Sexual Assault in Psychiatry",
  'tbl-p40-0082': f"{C3} > Bipolar and Related Disorders > Table 11 (continued): Bipolar I hypomanic and major depressive episodes, Bipolar II disorder",
  'tbl-p43-0085': f"{C3} > Bipolar and Related Disorders > Table 12: Stepwise Management of Bipolar I and II Disorders",
  'tbl-p49-0105': f"{C3} > Neurocognitive Disorders (dementia) > Table 16: Stepwise Management of Dementia (Neurocognitive Disorders)",
  'tbl-p60-0129': f"{C3} > Substance-Related and Addictive Disorders > Table 18: Stepwise Management of Substance-Related and Addictive Disorders",
  'tbl-p62-0137': f"{C3} > Common Childhood Psychiatric Conditions > Table 19: Summary of Classification and Management of Childhood Psychiatric Conditions",
  'tbl-p66-0143': f"{C3} > Common Childhood Psychiatric Conditions > Table 19 (continued): Enuresis, Encopresis, Oppositional Defiant and Conduct Disorders",
  'tbl-p69-0147': f"{C3} > Common Childhood Psychiatric Conditions > Table 20: Stepwise Management for Childhood Psychiatric Conditions",
  'tbl-p85-0204': f"{C4} > Pharmacological Management of Autism Spectrum Disorder > Seizures: Table 41 Anticonvulsants",
  'tbl-p86-0208': f"{C4} > Pharmacological Management of Autism Spectrum Disorder > Aggression/Uncontrolled Behaviour: Table 42 Antipsychotics",
  'tbl-p87-0210': f"{C4} > Pharmacological Management of Autism Spectrum Disorder > Major Depressive Disorder (12 years or above): Table 43 Antidepressants",
  'tbl-p87-0212': f"{C4} > Pharmacological Management of Autism Spectrum Disorder > Anxiety Disorder: Table 44",
  'tbl-p87-0214': f"{C4} > Pharmacological Management of Neurocognitive Disorders > Table 45: Medications for Neurocognitive Disorders (donepezil)",
  'tbl-p88-0216': f"{C4} > Pharmacological Management of Neurocognitive Disorders > Severe agitation or psychotic symptoms: Table 46 Antipsychotics",
  'tbl-p88-0218': f"{C4} > Pharmacological Management of Neurocognitive Disorders > Major Depressive Disorder: Table 47 Antidepressants",
  'tbl-p89-0220': f"{C4} > Managing Side Effects of Psychiatric Medicines > Mentally Stable with Mild Side Effects: Table 48",
  'tbl-p90-0222': f"{C4} > Managing Side Effects of Psychiatric Medicines > Mentally Stable with Moderate Side Effects: Table 49",
  'tbl-p90-0224': f"{C4} > Managing Side Effects of Psychiatric Medicines > Mentally Stable/Unstable with Severe Side Effects: Tables 50-51",
  'tbl-p91-0228': f"{C4} > Alcohol Intoxication > Table 52: Thiamine for Thiamine Deficiency Secondary to Alcohol",
  'tbl-p91-0230': f"{C4} > Alcohol Withdraw > Short term management: Table 53",
  'tbl-p92-0232': f"{C4} > Alcohol Withdraw > Long term management: Table 54",
  'tbl-p111-0266': "Appendices > Appendix I: Suicide Risk Assessment Form (Adapted from Becks Suicidal Intent Scale)",
  'tbl-p112-0268': "Appendices > Appendix I: Suicide Risk Assessment Form > Recommendations (scoring and risk)",
  'tbl-p113-0269': "Appendices > Appendix I: Suicide Risk Assessment Form > Action Taken",
  'tbl-p114-0271': "Appendices > Appendix II: Depression Screening Form PHQ-9 > Patient Health Questionnaire (PHQ-9)",
  'tbl-p115-0274': "Appendices > Appendix II: Depression Screening Form PHQ-9 > Guide for Interpreting PHQ-9 Scores",
  'tbl-p118-0278': "Appendices > Psychiatric History Taking Sheet > Mental Status Evaluation",
 },
 'tb-2025': {
  'tbl-p214-0554': f"{TB11} > 11.8 TPT Regimens and Dosing > Table 55: TPT regimen and drug dosing",
  'tbl-p215-0557': f"{TB11} > 11.8 TPT Regimens and Dosing > Table 56: TPT dosing by body size",
  'tbl-p216-0559': f"{TB11} > 11.8 TPT Regimens and Dosing > Table 57: Dosing of DS-TB TPT regimens for HIV not infected when Rifapentine 150 mg or individual molecules are not available",
  'tbl-p221-0573': f"{TB11} > 11.11 Monitoring and management of Adverse events > Table 60: Management strategies for adverse events of TPT",
  'tbl-p227-0589': f"{TB11} > 11.16 Community-based care and support for people taking TPT > Table 64: The checklist for monitoring adverse events and TB signs and symptoms",
  'tbl-p227-0591': f"{TB11} > 11.17 Recording, reporting and monitoring of TPT implementation > Table 65: TPT cascade for regular review and timely action",
  'tbl-p230-0597': f"{TB11} > 11.18 Performing TB Infection Tests > Table 66: Interpretation of IGRA results (QuantiFERON GlodPlus)",
 },
 'unaids-linkages-sop': {
  'tbl-p28-0040': "10 Client referred without ART initiation",
  'tbl-p54-0087': "12.19 Day 170-175: Sixth Telephonic Call > During telephone call",
  'tbl-p73-0118': "12 Linkage Case Management for Special Populations > 12.31 Differentiated Service Delivery for Priority Populations Linkages",
  'tbl-p88-0140': "13.9 List of LCM Reporting Indicators",
 },
}
TEXT_LABELS = {'mental-health-deskguide': {
  'mental-health-deskguide-0206': f"{C4} > Pharmacological Management of Autism Spectrum Disorder > Seizures: caution with anticonvulsants",
  'mental-health-deskguide-0229': f"{C4} > Alcohol Withdraw > Short term management",
  'mental-health-deskguide-0272': "Appendices > Appendix II: Depression Screening Form PHQ-9 > Patient Health Questionnaire (PHQ-9)",
  'mental-health-deskguide-0273': "Appendices > Appendix II: Depression Screening Form PHQ-9 > Total Score: how to score the PHQ-9",
  'mental-health-deskguide-0275': "Appendices > Appendix II: Depression Screening Form PHQ-9 > Functional Health Assessment",
  'mental-health-deskguide-0276': "Appendices > Psychiatric History Taking Sheet",
  'mental-health-deskguide-0277': "Appendices > Psychiatric History Taking Sheet",
  'mental-health-deskguide-0256': "Chapter 5: Non Pharmacological Intervetions > Developmental Disorders Job Aid > Assessment",
}}

for doc, m in HEADINGS.items():
    d = load(doc)
    for tid, hp in m.items():
        item(d, doc, tid)['heading_path'] = hp
    for cid, lab in TEXT_LABELS.get(doc, {}).items():
        d.setdefault('text_labels', {})[cid] = lab
    save(doc, d)

# --- arrows written out (NCDIMH diabetes/ARV table; TB Table 68 is the same table) ---
d = load('ncdimh'); t = item(d, 'ncdimh', 'tbl-antidiabetic-arv-interactions')
for row in t['body']:
    if isinstance(row, list):
        for c in row:
            c['t'] = re.sub(r'^↑ potential interaction', '↑ antidiabetic level increased – potential interaction', c['t'])
            c['t'] = re.sub(r'^↓ potential interaction', '↓ antidiabetic level decreased – potential interaction', c['t'])
f = t['source_flags']
t['footnotes'] = [x for x in t['footnotes'] if not x.startswith('↑ =')] + ['↑ = increase in antidiabetic agent level; ↓ = decrease in antidiabetic agent level (arrow legend printed under the table).']
# naloxone flag: make clear that 'PO' is what the guideline prints
a = item(d, 'ncdimh', 'tbl-antidotes')
a['source_flags'] = ["The antidote cell for opioids is printed 'Naloxone 0.4–2mg PO depending on opioid amount; repeat in 2–3 min if needed' (p.189 of the guideline). Naloxone is given IV, IM or intranasally; oral naloxone is not effective for overdose, so 'PO' is probably an error in the guideline." if x.startswith('Naloxone is printed') else x for x in a['source_flags']]
save('ncdimh', d)

d = load('tb-2025'); t = item(d, 'tb-2025', 'tbl-p247-0639')
for row in t['body']:
    if isinstance(row, list):
        for c in row:
            c['t'] = {'↑ potential': '↑ potential (antidiabetic level increased)', '↓ potential': '↓ potential (antidiabetic level decreased)',
                      '↑ CAUTION': '↑ CAUTION (metformin level increased)'}.get(c['t'], c['t'])
# Table 55/57 inequality flags, worded precisely
t = item(d, 'tb-2025', 'tbl-p214-0554')
t['source_flags'] = ["The first two weight columns are printed '3-5.9 kg (> 3 months)' and '3-5.9 kg (≥ 3 months)'; the first should read '< 3 months' (as in the 6-9.9 kg pair, '< 6 months' / '≥ 6 months'). The last weight column is printed '< 50 kg' after 45-49.9 kg; it should read '≥ 50 kg'." if x.startswith('The last weight column') else x for x in t['source_flags']]
t = item(d, 'tb-2025', 'tbl-p216-0559')
t['source_flags'] = ["In both levofloxacin sub-tables the two 3-5.9 kg rows are both printed '<3 months old'; the second should read '≥3 months old'. The 6-9.9 kg pair is printed '<6 months' / '>6 months' (presumably '≥6 months')." if x.startswith('The second 3-5.9 kg row') else x for x in t['source_flags']]
save('tb-2025', d)

# --- FP MEC appendix: one item for sections 1-12; GRADE rating spans its rows ---
d = load('fp-2021')
ids = [t['table_id'] for t in d['tables']]
a = item(d, 'fp-2021', 'tbl-p96-0188')
if 'fp-2021-tbl-p103-0195' in ids:
    b = item(d, 'fp-2021', 'tbl-p103-0195')
    a['body'] = a['body'] + b['body']
    a['replaces_chunks'] = a['replaces_chunks'] + [c for c in b['replaces_chunks'] if c not in a['replaces_chunks']]
    a['pages'] = sorted(set(a['pages']) | set(b.get('pages', [b['page']])) | {104, 105})
    d['tables'] = [t for t in d['tables'] if t['table_id'] != 'fp-2021-tbl-p103-0195']
a['caption'] = "14.1 Appendix 1: Summary of Recommendation - Medical Eligibility Criteria (sections 1-12)"
body, i = a['body'], 0
while i < len(body):
    row = body[i]
    if isinstance(row, list) and len(row) == 3 and row[2]['t'].strip() and not row[2].get('rs'):
        j = i + 1
        while j < len(body) and isinstance(body[j], list) and len(body[j]) == 3 and not body[j][2]['t'].strip():
            j += 1
        if j - i > 1:
            row[2]['rs'] = j - i
            for k in range(i + 1, j):
                body[k] = body[k][:2]
        i = j
    else:
        i += 1
a['footnotes'] = ["Printed rotated over several pages. The GRADE evidence rating is printed once per group of rows (a merged cell) and applies to every row in that group."]
save('fp-2021', d)

# --- HIV 2022: short text chunks that only introduce the next figure/table travel with it ---
d = load('hiv-2022'); T = d['tables']
caps = {}
for t in T:
    if t.get('kind') != 'section':
        m = re.match(r'(Figure|Table|Chart)\s+([\d.]+[a-z]?)', t['caption'])
        if m: caps[(m.group(1).lower(), m.group(2).rstrip('.'))] = t
drop = set()
for t in T:
    if t.get('kind') != 'section': continue
    body = t.get('content') or ''
    for kind, num in re.findall(r'(Figure|Table|Chart)\s+([\d.]+\d)\s*(?:below|\(below\))', body):
        tgt = caps.get((kind.lower(), num))
        if tgt and abs(int(tgt['page']) - int(t['page'])) <= 1 and len(body) < 700 and t['table_id'] not in drop:
            intro = re.sub(r'^#+\s*', '', body).strip()
            cb = tgt.get('context_before', '')
            if intro not in cb:
                tgt['context_before'] = (cb + '\n\n' + intro).strip() if cb else intro
            tgt['replaces_chunks'] = tgt['replaces_chunks'] + [c for c in t['replaces_chunks'] if c not in tgt['replaces_chunks']]
            drop.add(t['table_id'])
d['tables'] = [t for t in T if t['table_id'] not in drop]
save('hiv-2022', d)
print('done; HIV intro sections folded into figures/tables:', len(drop))

# --- FP: page-banner junk chunk (method icons) next to Appendix 2 ---
d = load('fp-2021')
if 'fp-2021-0194' not in d.setdefault('text_drop', []):
    d['text_drop'].append('fp-2021-0194')
save('fp-2021', d)
