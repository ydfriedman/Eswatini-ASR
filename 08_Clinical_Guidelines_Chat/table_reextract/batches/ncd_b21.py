exec(open('batches/ncd_common.py').read())
RH = CH1 + " > Routine Health Examinations"
G, Yl, O, R_ = C("Green: low risk"), C("Yellow: moderately increased risk"), C("Orange: high risk"), C("Red: very high risk")
ITEMS = [
 D("fig-diabetes-screening", 28, RH + " > Diabetes Mellitus > Algorithm for diabetes mellitus screening",
   "Algorithm for diabetes mellitus screening in adults", ["0063", "0064"],
   "All clients >18 years attending a health facility should be screened for diabetes using the known risk factors below.\n"
   "- No risk factors: re-evaluate.\n"
   "- Risk factors present: test (HbA1c, fasting plasma glucose, oral glucose tolerance test, or random glucose):\n"
   "  - HbA1c <5.7% / FPG <100 mg/dl: encourage healthy lifestyle maintenance; retest at least annually.\n"
   "  - HbA1c 5.6-6.4% / FPG 100-125 mg/dl / OGTT 140-199 mg/dl: encourage lifestyle modification and retest every 6-12 months.\n"
   "  - HbA1c ≥ 6.5% / FPG ≥ 126 mg/dl: retest with a different test, and refer for treatment if still positive.\n\n"
   "*Known risk factors for diabetes: physical inactivity; family history of diabetes; high-risk race or ethnicity (African, Indian); hypertension (≥ 140/90); HDL-C <35 or triglyceride > 250 mg/dL; history of gestational diabetes or gave birth to a baby ≥4.5 kg; history of heart disease; conditions associated with insulin resistance; polycystic ovary syndrome; malnutrition.\n\n"
   "Adapted from the American Diabetes Association Standards of Medical Care in Diabetes. N.B.: the Ministry of Health recommends measuring glycaemia yearly in adults ≥ 18 years of age.",
   ["The pre-diabetes HbA1c band is printed '5.6-6.4%' while the normal band is '<5.7%' (overlap at 5.6); the screening table on p.13 uses 5.7-6.4%.",
    "Thresholds here are in mg/dl, unlike the mmol/L tables elsewhere."]),
 D("fig-lipid-management", 29, RH + " > Lipids Disorders > Lipid management clinical decision pathway",
   "Lipid management: clinical decision pathway (CV risk, comorbidities, lipid targets)", ["0066", "0067"],
   "Obtain fasting lipids at baseline and annually. Then three parallel assessments, then treat to the target:\n"
   "1. Calculate and categorize CV risk using the Framingham risk score (mdcalc.com - Framingham Risk Score). Risk categories: low risk < 10%; moderate risk 10%-19%; high risk > 20%.\n"
   "2. Assess comorbidities: diabetes; CAD; previous CV event; atherosclerosis; aneurysm. *Any = high risk.\n"
   "3. Determine lipid targets:\n"
   "   - LDL-C: optimal <100 mg/dL; near or above optimal 100-129 mg/dL; borderline high 130-159 mg/dL; high 160-189 mg/dL; very high ≥190 mg/dL.\n"
   "   - Total cholesterol: desirable <200 mg/dL; borderline high 200-239 mg/dL; high ≥240 mg/dL.\n"
   "   - Triglycerides: normal <150 mg/dL; borderline high ≥150-199 mg/dL; high 200-499 mg/dL; very high ≥500 mg/dL.\n"
   "Then: treat to the target.",
   ["CV risk categories leave a gap between 19% and 20%, as printed."]),
 D("fig-ckd-clinical-protocol", 29, RH + " > Chronic Kidney Disease > CKD clinical protocol (kidney health check)",
   "Chronic kidney disease clinical protocol: kidney health check, confirmation and staging", ["0068", "0069"],
   "Offer a kidney health check to people with: diabetes; hypertension; established CVD; family history of kidney failure; obesity (BMI ≥30); current or past smoker/vaper; history of AKI aged ≥60 years; high index of suspicion in clients, especially paediatrics, with oedema and recurrent puffiness.\n\n"
   "Tests: uACR, eGFR, and trace protein on urine dipstick.\n"
   "- uACR ≥3 mg/mmol (yes): repeat uACR within 3 months. If uACR normal, complete a third test (preferably first morning void). CKD if a minimum of two uACRs ≥3 mg/mmol over 3 months.\n"
   "- eGFR <60 mL/min/1.73m2 (yes): repeat eGFR within 7 days; if ≥20% reduction in eGFR, possible AKI: discuss with nephrologist. Repeat eGFR within 3 months. CKD if a minimum of two eGFRs <60 mL/min/1.73m2 over 3 months.\n"
   "- No to both: repeat kidney health check (annually if aged ≥18, people with diabetes or hypertension).\n"
   "If either (and/or) criterion is met: stage CKD with the staging table, using eGFR and uACR results.",
   ["The 'two eGFRs <60 over 3 months' window is implied by the 3-month repeat; the PDF box reads 'If minimum of two eGFRs <60mL/min.1.73m2'."]),
 T("tbl-ckd-staging-heatmap", 30, RH + " > Chronic Kidney Disease > CKD staging by eGFR and albuminuria",
   "CKD staging by GFR and albuminuria (KDIGO-style colour grid: risk category for each GFR stage x albuminuria stage)", ["0070", "0072"],
   [[C("Kidney function stage"), C("GFR (mL/min/1.73m2)"), C("A1 normal: uACR <3.0 mg/mmol"), C("A2 microalbuminuria: uACR 3.0-30 mg/mmol"), C("A3 macroalbuminuria: uACR >30 mg/mmol")]],
   [[C("1"), C("≥90"), C("Green: not CKD unless haematuria, structural or pathological abnormalities present", rs=2), Yl, R_],
    [C("2"), C("60-89"), Yl, R_],
    [C("3a"), C("45-59"), Yl, O, R_],
    [C("3b"), C("30-44"), O, O, R_],
    [C("4"), C("15-29"), R_, R_, R_],
    [C("5"), C("<15 or on dialysis"), R_, R_, R_]],
   footnotes=["**Undertake investigations to determine the underlying diagnosis. **Fully specify the CKD diagnosis, e.g. CKD stage 2 with microalbuminuria (A2) in the presence of type 2 diabetes. **Refer to the colour-coded clinical action plans for CKD management."],
   source_flags=["Risk is shown only by cell colour in the PDF, with no legend; colours are written out with the usual KDIGO meaning (green low, yellow moderately increased, orange high, red very high). Clinician to confirm.",
                 "A2 range is printed 'uACR 3.0-3.0 mg/mmol' and A3 is headed 'Microalbuminuria (A3)'; written as 3.0-30 and macroalbuminuria.",
                 "G1-G2 with A3 are red here; KDIGO uses orange for these cells."]),
 D("fig-ckd-screening", 30, RH + " > Chronic Kidney Disease > Algorithm for CKD screening",
   "Algorithm for chronic kidney disease (CKD) screening", ["0071"],
   "Target population:\n"
   "- No markers of risk: do not screen.\n"
   "- Risk factors (high blood pressure, diabetes, cardiovascular diseases, family history, HIV): screen.\n\n"
   "Screen: test (urine dipstick, blood glucose, blood pressure, family history) and measure kidney function (serum creatinine; estimate the eGFR).\n"
   "Determine if test results indicate CKD (eGFR <60 ml/min/1.73m2 or presence of albuminuria):\n"
   "- No: rescreen based on the risks.\n"
   "- Yes: lifestyle modification (smoking cessation; balanced diet; regular exercise; limit salt intake to <2 g/day); medical treatment (diabetes, BP and lipid control: SGLT2, ACEI/ARB, statins, metformin...); considerations (drug dosing; use of contrast media; CKD complications: anaemia, hyperkalaemia, bone disease, CVD...).\n"
   "Then: retesting; follow-up visits; referral to nephrology when appropriate."),
]
