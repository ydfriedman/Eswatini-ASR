exec(open('batches/ncd_common.py').read())
CV = CH3 + " > Hypertension > Cardiovascular Risk Assessment"
def pts(rows): return [[C(a), C(b), C(c)] for a, b, c in rows]
ITEMS = [
 T("tbl-cvd-risk-indications", 105, CV + " > Indications",
   "Cardiovascular risk assessment: indications by patient group (no established CVD, elevated BP, diabetes, renal disease, established CVD, target organ damage)", ["0282"],
   [[C("Group"), C("Criteria for Assessment")]],
   [[C("No established CVD"), C("- Total cholesterol (TC) ≥ 8 mmol/L (320 mg/dL)<br/>- LDL cholesterol ≥ 6 mmol/L (240 mg/dL)<br/>- TC/HDL-C ratio > 8<br/>- Persistent BP > 160–170 / 100–105 mmHg")],
    [C("Elevated BP (moderate)"), C("BP ≥ 140/90 mmHg → manage as per national protocols")],
    [C("Diabetes"), C("Type 1 or Type 2 with overt nephropathy or other significant renal disease")],
    [C("Renal disease"), C("Known renal failure or renal impairment")],
    [C("Established CVD"), C("Angina pectoris, coronary heart disease (CHD), myocardial infarction (MI), transient ischemic attack (TIA), stroke, peripheral vascular disease (PVD), prior coronary revascularization, or carotid endarterectomy")],
    [C("Target organ damage"), C("Left ventricular hypertrophy (LVH) on ECG or hypertensive retinopathy (Grade III or IV)")]]),
 T("tbl-cvd-risk-score-points", 106, CV + " > CVD risk score calculation",
   "CVD risk score points for men and women: age, total cholesterol, HDL cholesterol, smoking and diabetes", ["0284", "0285", "0286", "0288", "0290"],
   [[C("Factor"), C("Value"), C("Man"), C("Woman")]],
   [{"section": "1. Age (years)"}] + [[C("Age")] + r for r in pts([("30-34", "0", ""), ("35-39", "2", "2"), ("40-44", "5", "4"), ("45-49", "6", "5"), ("50-54", "8", "7"), ("55-59", "10", "8"), ("60-64", "11", "9"), ("65-69", "12", "10"), ("70-74", "14", "11"), ("75-79", "15", "12")])] +
   [{"section": "2. Total cholesterol (mmol/L)"}] + [[C("Total cholesterol")] + r for r in pts([("<4.1", "0", "0"), ("4.1-5.19", "1", "1"), ("5.2-6.19", "2", "3"), ("6.2-7.2", "3", "4"), (">7.2", "4", "5")])] +
   [{"section": "3. HDL cholesterol (mmol/L)"}] + [[C("HDL cholesterol")] + r for r in pts([(">1.5", "-2", "-2"), ("1.3-1.49", "-1", "-1"), ("1.2-1.29", "0", "0"), ("0.9-1.19", "1", "1"), ("<0.9", "2", "2")])] +
   [{"section": "Other factors"}, [C("5. Smoker"), C("Yes"), C("4"), C("3")], [C("6. Diabetes"), C("Yes"), C("3"), C("4")]],
   table_note="Calculate the score: add the points for 1. sex and age, 2. total cholesterol, 3. HDL cholesterol, 4. on-treatment systolic BP (separate table), 5. smoker, 6. diabetes = total CVD risk score. If the CVD risk score is ≥10%, manage the CVD risk. If the CVD risk score is <10% and there are no CVD risk factors, reassess the CVD risk after 5 years.",
   source_flags=["Women aged 30-34 have no points printed (blank cell)."]),
 T("tbl-cvd-risk-score-sbp", 106, CV + " > CVD risk score calculation",
   "CVD risk score points for systolic blood pressure, by sex and whether on BP treatment", ["0287"],
   [[C("4. Systolic BP (mm Hg)", rs=2), C("Man", cs=2), C("Woman", cs=2)],
    [C("Not on BP treatment"), C("On BP treatment"), C("Not on BP treatment"), C("On BP treatment")]],
   [[C(a), C(b), C(c), C(d), C(e)] for a, b, c, d, e in [("<120", "-2", "0", "-3", "-1"), ("120-129", "0", "2", "0", "2"), ("130-139", "1", "3", "1", "3"), ("140-149", "2", "4", "2", "5"), ("150-159", "2", "4", "4", "6"), ("≥160", "3", "5", "5", "7")]]),
 T("tbl-cvd-risk-interpretation", 107, CV + " > Interpreting the CVD risk score",
   "CVD risk score interpretation: total score to 10-year CVD risk for men and women, and what to explain to the patient", ["0291"],
   [[C("CVD Risk Score (man)"), C("CVD Risk Score (woman)"), C("10-year CVD Risk"), C("Explain to Patient")]],
   [[C("<11"), C("<13"), C("<10%"), C("There is less than 1 in 10 chance that in the next 10 years he/she may have a heart attack")],
    [C("11 - 14"), C("13 - 17"), C("10-20%"), C("There is a 1 in 10 to 1 in 5 chance that in the next 10 years he/she may have a heart attack")],
    [C("≥ 15"), C("≥ 18"), C(">20%"), C("There is more than 1 in 5 chance that in the next 10 years he/she may have a myocardial infarction (heart attack)")]]),
 T("tbl-cvd-risk-actions", 107, CV + " > Management by CVD risk level",
   "Management by CVD risk level (>20%, 10-20%, 5-10%, <5%): counselling, when to treat hypertension, statin", ["0292"],
   [[C("Action"), C(">20%"), C("10 - 20%"), C("5 - 10%"), C("<5%")]],
   [[C("Counsel"), C("Consultation on diet (which includes lipid-lowering diet), physical activity, smoking cessation and avoiding harmful use of alcohol", cs=4)],
    [C("Treat HTN"), C("Consider drug treatment if persistent BP ≥ 130/80 mmHg", cs=2), C("Consider if persistent BP ≥ 140/90 mmHg"), C("Consider if BP ≥ 140/90 mmHg")],
    [C("Lipid lowering"), C("Give a statin", cs=4)]],
   table_note="1. Use a formal estimation of cardiovascular risk to discuss prognosis and healthcare options with people with hypertension, both for raised blood pressure and other modifiable risk factors. 2. Estimate cardiovascular risk in line with the WHO recommendations (see desk guides). 3. Use the clinic blood pressure measurements to calculate cardiovascular risk.",
   source_flags=["Chart in the PDF: 'Give a statin' is one bar across all risk levels, so it is not clear whether a statin is meant for every risk level or only the higher ones. The 'Treat HTN' cells are placed by position. Clinician to confirm."]),
]
ITEMS += [
 D("fig-aspirin-primary-prevention", 108, CH3 + " > Hypertension > How to use Aspirin for CV Disease Primary Prevention",
   "How to use aspirin for primary prevention of cardiovascular disease (decision flowchart)", ["0296"],
   "Aspirin for primary prevention, by age:\n"
   "- 60 years or above: don't start aspirin for primary prevention.\n"
   "- 40-59 years: calculate the 10-year CV risk.\n"
   "  - Risk <10%: don't start aspirin for primary prevention.\n"
   "  - Risk >10%: share the decision with the individual, weighing:\n"
   "    - Benefits: 12% reduction in MI; 12% reduction in stroke.\n"
   "    - Risks: 58% increase in GI bleeding; 31% increase in hemorrhagic stroke; no impact on mortality; no impact on cancer.\n"
   "    - If agreed on starting: aspirin 81 mg; stop at age 75.",
   ["The flowchart does not cover a 10-year risk of exactly 10% (<10% and >10%)."]),
]
