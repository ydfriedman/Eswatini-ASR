exec(open('batches/ncd_common.py').read())
CK = CH7 + " > Chronic Kidney Disease"
ITEMS = [
 D("fig-ckd-screening-algorithm", 213, CK + " > Screening and Diagnosis of Chronic Kidney Disease > Screening Algorithm for Kidney Disease",
   "Screening algorithm for chronic kidney disease: who to screen, tests, CKD criteria, and lifestyle, medical treatment and other considerations", ["0611"],
   "1. Area population:\n"
   "   - No markers of risk: do not screen; rescreen based on future patient assessment.\n"
   "   - Risk factors (high blood pressure; diabetes; cardiovascular disease; family history of CKD): screen.\n"
   "2. Tests: blood glucose; spot urine; blood pressure; family history. Measure kidney function (serum creatinine or cystatin C; calculate eGFR) and kidney injury (albuminuria/proteinuria).\n"
   "3. Do the results indicate CKD (eGFR <60 ml/min/1.73 m2 or albuminuria/proteinuria, ACR >30 mg/mmol as printed)?\n"
   "   - No: rescreen based on future patient assessment.\n"
   "   - Yes:\n"
   "     - Lifestyle modification: smoking cessation; well-balanced diet; regular exercise; limit sodium intake to <2 g/day.\n"
   "     - Medical treatment: blood pressure, diabetes and lipid control: ACEi/ARB therapy; SGLT2 inhibition; metformin; statins.\n"
   "     - Considerations: drug dosing; contrast media use; hyperkalemia; CKD/CVD factors: anaemia, bone disease, heart failure, other (hepatitis C, metabolic acidosis, etc.).\n"
   "     - Retesting; follow-up office visits; referral to a nephrologist when appropriate.",
   ["The CKD threshold is printed 'ACR > 30mg/mmol'; elsewhere (pp.211, 215) albuminuria is ACR >30 mg/g or >3 mg/mmol. Clinician to confirm.", "'Serum creatine', 'Albu,inuria' printed."]),
 D("fig-ckd-risk-management-algorithm", 215, CK + " > Algorithm to screen, risk stratify and treat CKD",
   "Algorithm to screen, risk-stratify and treat CKD (KDIGO-based): conditions of CKD risk, testing, classification, patient safety by eGFR, slowing progression and complications, CVD risk reduction, and when to refer to nephrology", ["0613", "0614"],
   "1. Conditions of CKD risk: hypertension; diabetes; cardiovascular disease; AKI/hospitalisation history; family history of kidney disease; obesity; older age*; other high-risk comorbidities, environmental exposures, or genetic factors.\n"
   "2. Consider screening for CKD: urinary albumin-creatinine ratio (ACR) to detect albuminuria; serum creatinine and cystatin C to estimate GFR.\n"
   "3. Is any of the following present for 3 months or more: eGFR <60 ml/min/1.73 m²; ACR >30 mg/g (3 mg/mmol); markers of kidney disease?\n"
   "   - No: periodically repeat evaluation.\n"
   "   - Yes: classify/risk-stratify the CKD stage; identify and treat the specific cause of CKD.\n"
   "     - eGFR category (ml/min/1.73 m²): G1 ≥90; G2 60-89; G3b 30-44; G4 15-29; G5 <15 (G3a is not listed).\n"
   "     - Albuminuria category: A1 (normal or mild) <30 mg/g or <3 mg/mmol; A2 (moderate) 30-300 mg/g or 3-30 mg/mmol; A3 (severe) >300 mg/g or >30 mg/mmol.\n\n"
   "Patient safety (all patients with eGFR <60): dose medications based on eGFR; reduce the risk of AKI from volume depletion; adopt 'sick day rules' as needed; avoid dual ACEi and ARB blockade; prevent contrast-associated AKI (lowest possible radiocontrast dose; adequate hydration before, during and after the procedure, consider isotonic saline; withhold ACEi or ARBs, diuretics and other nephrotoxic agents before and after the procedure).\n"
   "- eGFR 45-59: avoid prolonged NSAIDs.\n"
   "- eGFR 30-44: avoid prolonged NSAIDs; use metformin with close monitoring at 50% dose.\n"
   "- eGFR <30: avoid any NSAIDs; avoid bisphosphonates; avoid metformin; avoid PICC lines (access preservation); if on warfarin, monitor PT-INR closely given increased risk of bleeding.\n\n"
   "Slowing CKD progression and reducing complications:\n"
   "- Treat high blood pressure: ACEi or ARB if ACR >30 mg/g or 3 mg/mmol; diuretic often required; dietary sodium <2000 mg/day.\n"
   "- Type 2 diabetes: target HbA1c <6.5% to <8.0%; metformin for those with CKD and type 2 diabetes; if the glycaemic target is not achieved with metformin and SGLT2 inhibition, add a GLP1-RA.\n"
   "- CKD complications testing: anaemia – evaluate if CKD G3-G5 and Hb <13 g/dl (men) or <12 g/dl (women); treat iron deficiency first; consider erythropoiesis-stimulating agents (ESAs) if Hb 9-10 g/dl (avoid Hb >11.5 g/dl). Acidosis – correct to the normal range with bicarbonate supplementation if bicarbonate <22 mmol/l in CKD G3-G5. CKD-mineral bone disease – in CKD G3-G5 check calcium, phosphate, 25-OH vitamin D and intact PTH; supplement vitamin D deficiency.\n"
   "- Influenza vaccination; pneumococcal and hepatitis B vaccination in CKD G4-G5; screen for hepatitis C.\n\n"
   "Reduction of CVD complications: CKD = CVD risk; systolic blood pressure target <120 mm Hg* (consider <130/80 mm Hg in kidney transplant recipients); start lipid-lowering therapy (CKD and age ≥50 years: statin recommended; CKD and age 18-49: statin if known CAD, diabetes mellitus, prior stroke, or high ASCVD risk); aspirin for secondary prevention unless bleeding risk outweighs benefits.\n\n"
   "When to refer to nephrology: AKI or abrupt sustained fall in GFR; eGFR <30 ml/min/1.73 m²; consistent significant albuminuria (ACR >300 mg/g or 30 mg/mmol); progression of CKD; urinary red cell casts or RBC >20 per high-power field, sustained and not readily explained; CKD and hypertension refractory to 4 or more antihypertensive agents; persistent abnormalities of serum potassium; recurrent or extensive nephrolithiasis; hereditary kidney disease.\n\n"
   "Notes (from the caption): based on KDIGO and adapted from Vassalotti et al. Care for older adults or those with limited life expectancy should be individualised. If eGFR (creatinine) is 45-59 ml/min per 1.73 m2, or in low muscle mass, chronic illness or malnutrition, order cystatin C to estimate GFR. There are no evidence-based recommendations on screening frequency; consider risk equations (e.g. CKD Prognosis Consortium). The systolic target <120 mm Hg is a level 2 recommendation; many patients may opt for a less intensive approach.",
   ["The systolic BP target <120 mm Hg here differs from the hypertension chapter (target 130-139, 'not <120'; CKD 'target to <140 to 130').",
    "G3a is missing from the eGFR category list; the caption prints the cystatin C range as 'eGFR cr 45-49' (KDIGO 45-59). 'CKD = CKD risk' printed (CKD = CVD risk). 'Urinary albumin-creatine ratio' printed."]),
]
def act(*xs): return [C(x) for x in xs]
ITEMS += [
 T("tbl-kdigo-referral-heatmap", 216, CK + " > KDIGO Heat Map > Monitor or refer",
   "KDIGO heat map for CKD: monitor or refer to nephrology by GFR category (G1-G5) and albuminuria category (A1-A3), with risk colours", ["0615", "0616", "0617"],
   [[C("GFR category"), C("Description"), C("Range (ml/min per 1.73 m2)"), C("A1: normal to mildly increased (<30 mg/g; <3 mg/mmol)"), C("A2: moderately increased (30-300 mg/g; 3-30 mg/mmol)"), C("A3: severely increased (>300 mg/g; >30 mg/mmol)")]],
   [act("G1", "Normal or high", "≥90", "— (low risk)", "Monitor (moderately increased risk)", "Refer* (high risk)"),
    act("G2", "Mildly decreased", "60-89", "— (low risk)", "Monitor (moderately increased risk)", "Refer* (high risk)"),
    act("G3a", "Mildly to moderately decreased", "45-59", "Monitor (moderately increased risk)", "Monitor (high risk)", "Refer (very high risk)"),
    act("G3b", "Moderately to severely decreased", "30-44", "Monitor (high risk)", "Monitor (very high risk)", "Refer (very high risk)"),
    act("G4", "Severely decreased", "15-29", "Refer* (very high risk)", "Refer* (very high risk)", "Refer (very high risk)"),
    act("G5", "Kidney failure", "<15", "Refer (very high risk)", "Refer (very high risk)", "Refer (very high risk)")],
   context_before="The KDIGO heat map uses the eGFR and albuminuria (albumin-to-creatinine ratio, ACR) from screening to assess the risk of CKD progression and kidney failure.",
   footnotes=["*Referring clinicians may wish to discuss with their nephrology service depending on local arrangements regarding monitoring or referring.",
              "Colours: low risk (if no other markers of kidney disease, no CKD); moderately increased risk; high risk; very high risk."],
   source_flags=["Risk colours are not printed as text; they follow the KDIGO heat map on p.212. The same misprints as p.212 apply (G3a '45-49', A1 '<300 mg/g', 'GDF categories'). Headed 'KDIGO Heart Map' in the old chunks."]),
 D("fig-ckd-interventions-by-stage", 217, CK + " > Pharmacological management of CKD to slow progression",
   "Interventions to slow CKD progression and reduce cardiovascular risk by GFR and albuminuria stage (lifestyle, smoking, RAS inhibition, BP, statins, glycaemia, SGLT2 inhibitors, GLP-1 RA, metabolic acidosis)", ["0620", "0621"],
   "Chart of interventions across CKD stages G1-G5 (each split A1-A3); bars show where each applies:\n"
   "- Lifestyle modification: all stages.\n"
   "- Smoking cessation: all stages.\n"
   "- RAS inhibition (a): G1 to G4/G5 (shaded lighter in G5).\n"
   "- Optimize blood pressure control: all stages.\n"
   "- Statins (b): all stages (lighter in G5).\n"
   "- Optimize glycemic control: all stages.\n"
   "- SGLT2 inhibitors (c): G1 to G4, continued (dotted) into G5.\n"
   "- GLP-1 receptor agonists (d): all stages.\n"
   "- Treat metabolic acidosis: G3b to G5.\n"
   "- Treat underlying cause, avoid nephrotoxins, and adjust medication dosages: all stages.\n\n"
   "Notes: (a) Unclear if and when to discontinue renin-angiotensin system (RAS) inhibition in advanced CKD. (b) Statins should be initiated for those beginning dialysis therapy (as printed); patients already receiving statins at dialysis initiation can continue them. (c) Applies to CKD patients with type 2 diabetes only. An SGLT2 inhibitor is recommended as first-line treatment with metformin and may also benefit persons with CKD and no diabetes. SGLT2 inhibitors should be initiated if eGFR ≥30 ml/min and can be continued through G4-G5 until dialysis initiation, when they should be stopped; there is no evidence for starting SGLT2 inhibitors if eGFR <30 ml/min per 1.73 m2. (d) Applies to CKD patients with type 2 diabetes only. A GLP-1 receptor agonist can be considered when an SGLT2 inhibitor and/or metformin is not tolerated or the glycaemic target is not reached. Dulaglutide can be used if eGFR >15 ml/min per 1.73 m2; exenatide if creatinine clearance >30 ml/min; there are limited data for liraglutide, lixisenatide or semaglutide in severe CKD. Consult dosing recommendations in CKD G4 and G5.\n\n"
   "Also: treat anaemia (investigate the cause to exclude non-CKD causes), aiming for Hb 10-12 g/dl.",
   ["Note (b) is printed 'stains should be initiated for those beginning dialysis therapy'; the KDIGO source says statins should NOT be initiated in patients starting dialysis. Clinician to confirm.",
    "Bar extents are read from the image and are approximate.", "'RAS inhabitation', 'metrormin', 'contrasporter' printed."]),
 T("tbl-ckd-management-principles", 218, CK + " > Principles of Chronic Kidney Disease Management",
   "Principles of CKD management by stage (all stages, stage 1-3/4, stage 4-5): goals, screening, risk factors, CV care, immunisation, medication review, AKI prevention, RRT preparation, complications", ["0622", "0623"],
   [[C("Category"), C("All Stages (CKD 1–5)"), C("Stage 1–3/4"), C("Stage 4–5")]],
   [act("Goals", "Early detection, slow progression, prevent AKI, manage CV risk, adjust meds, immunize", "Delay progression, prevent acute on chronic events, manage comorbidities", "Prepare for RRT, manage complications"),
    act("Screening", "Screen high-risk populations (e.g., DM, HTN, elderly)", "Regular renal function tests, proteinuria assessment", "As in stage 1–3, plus closer nephrology follow-up"),
    act("Risk Factor Control", "Control BP, glucose, avoid nephrotoxins, lifestyle interventions", "Use ACEi/ARB if proteinuria. Lifestyle: diet, exercise, smoking cessation", "Continue risk factor management, stricter control"),
    act("Cardiovascular Care", "Treat dyslipidaemia, hypertension, diabetes", "Initiate statins if indicated", "Intensify CV risk monitoring and treatment"),
    act("Immunisation", "Annual influenza, 5-year pneumococcal, hepatitis B if seronegative", "Same as all stages", "Same as all stages"),
    act("Medication Management", "Review all meds for renal dosing", "Monitor for dose accumulation", "Dose adjustment critical due to declining GFR"),
    act("Preventing AKI", "Educate on avoiding dehydration, NSAIDs, and nephrotoxic agents", "Monitor during infections or surgeries", "Same, with increased vulnerability"),
    act("Preparation for RRT", "—", "—", "Educate on RRT options (HD, PD, transplant), plan access"),
    act("Complication Management", "Monitor anaemia, mineral-bone disorder (CKD-MBD)", "Not usually required unless abnormalities begin to show", "ESA for anaemia, phosphate binders, vitamin D supplementation")],
   source_flags=["The immunisation row is labelled 'Medication Management' in the PDF (the same label as the next row); labelled Immunisation here."]),
]
