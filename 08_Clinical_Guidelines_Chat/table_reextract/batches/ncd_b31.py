exec(open('batches/ncd_common.py').read())
AC = CH3 + " > Acute Coronary Syndromes"
AL = AC + " > Algorithm for ACS Management"
def L(*xs): return C("<br/>".join("- " + x for x in xs))
ITEMS = [
 D("fig-acs-visual-illustration", 125, AC + " > Visual Illustration for Acute Coronary Syndromes (ACS)",
   "Visual illustration of acute coronary syndromes: clinical setting, ECG, troponin level and change, triage decision and diagnosis (from low to high probability of MI)", ["0346"],
   "A chart running from LOW to HIGH probability of myocardial infarction:\n"
   "I. Clinical setting, symptoms and vital signs: from localised chest discomfort (low) to widespread pain (higher) to cardiac arrest needing CPR/shock (high).\n"
   "II. ECG: normal ECG → mild ST depression → ST depression → ST elevation.\n"
   "III. Troponin level at 0 h: − (low); −/+; +; ++; +++ (high).\n"
   "IV. Troponin change within 1, 2 or 3 h: −; −/+; +; ++; at the highest level, if any of the above, consider direct rule-in.\n"
   "Triage decision:\n"
   "- Troponin − at 0 h and no change: rule out MI.\n"
   "- Troponin −/+ or +: observe.\n"
   "- Troponin ++ or more, or ST elevation: rule in MI.\n"
   "Diagnosis: rule-out → mostly noncardiac (some unstable angina or other cardiac); observe → unstable angina, other cardiac, or NSTEMI; rule-in → NSTEMI or STEMI (some other cardiac).",
   ["Image in the PDF. The diagnosis arrows cross between columns; their mapping is summarised. 'viral signs' is printed (vital signs)."]),
 T("tbl-nste-acs-risk-strategy", 126, AC + " > NSTE-ACS risk stratification and invasive strategy",
   "NSTE-ACS risk stratification: very high and high-risk criteria, timing of invasive strategy, and initial treatment", ["0347", "0348"],
   [[C("Risk"), C("Criteria"), C("Invasive strategy"), C("Treatment")]],
   [[C("Very High Risk"), L("Hemodynamic instability or cardiogenic shock", "Refractory or recurrent chest pain despite treatment", "Life-threatening arrhythmias", "Mechanical complications of MI", "Heart failure due to NSTE-ACS", "ST depression >1 mm in ≥6 leads plus ST elevation in aVR and/or V1"),
     C("Immediate invasive strategy (within 2 hours)"),
     L("Dual antiplatelet therapy (Aspirin + P2Y12 inhibitor)", "Anticoagulant (e.g. enoxaparin or UFH)", "Beta-blocker (if not contraindicated)", "Nitrates", "Statins", "Oxygen if SpO2 <90%")],
    [C("High Risk"), L("Diagnosis of NSTEMI", "Dynamic or new contiguous ST/T changes", "Transient ST-segment elevation", "GRACE risk score >140"),
     C("Early invasive strategy (within 24 hours)"),
     L("Dual antiplatelet therapy (Aspirin + P2Y12 inhibitor)", "Anticoagulant (e.g. enoxaparin or UFH)", "Beta-blocker (if not contraindicated)", "Nitrates", "Statins", "Oxygen if SpO2 <90%")]],
   table_note="Refer all patients with very high and high-risk criteria to a tertiary care center after initial stabilization.",
   source_flags=["The PDF table has no header row; column names added."]),
 T("tbl-acs-algorithm-steps-1-3", 126, AL + " > Steps 1-3: suspect ACS, immediate actions, ECG and troponins",
   "ACS management algorithm, steps 1-3: presentations, immediate actions in the first 10 minutes (monitoring, oxygen, aspirin, nitrates, morphine, labs), 12-lead ECG and serial troponins", ["0349", "0350", "0351"],
   [[C("Item"), C("Action")]],
   [{"section": "STEP 1: SUSPECT ACS — Presentations"},
    [C("Classic presentations"), L("Chest pain, pressure, tightness, or heaviness", "Radiation to left arm, jaw, neck, or back", "Dyspnea, diaphoresis, palpitations", "Nausea/vomiting, epigastric discomfort", "Syncope or near-syncope")],
    [C("Atypical (especially in women, elderly, diabetics)"), L("Fatigue, weakness, malaise", "Isolated dyspnea without chest pain", "Epigastric pain resembling indigestion", "Jaw or arm pain without chest discomfort")],
    {"section": "STEP 2: IMMEDIATE ACTIONS (0–10 minutes)"},
    [C("Monitoring"), L("Continuous 12-lead ECG, cardiac monitoring", "Blood pressure, SpO2, HR monitoring", "IV access × 2 — large bore")],
    [C("Oxygen"), L("Administer ONLY if SpO2 < 90%; avoid routine O2")],
    [C("Aspirin"), L("162–325 mg PO — chewed immediately", "Hold if true allergy (use Clopidogrel 300 mg instead)")],
    [C("Nitrates"), L("SL NTG 0.4 mg q5 min × 3 doses", "HOLD if: SBP < 90 mmHg, HR < 50 or > 100, RV infarct, recent PDE5 inhibitor use")],
    [C("Morphine"), L("2–4 mg IV if pain uncontrolled after nitrates", "Use cautiously — associated with possible increased mortality in some studies")],
    [C("Labs"), L("Troponin I or T (high-sensitivity preferred), CK-MB", "BMP, CBC, coagulation (PT/INR/aPTT), BNP/NT-proBNP", "Lipid panel, HbA1c if diabetic history", "Type & Screen")],
    {"section": "STEP 3: 12-LEAD ECG + SERIAL TROPONINS (< 10 minutes)"},
    [C("ECG and imaging"), L("Obtain and interpret 12-lead ECG within 10 minutes of arrival", "Repeat ECG every 15–30 min if initial non-diagnostic", "Right-sided leads (V3R–V4R) if inferior ST elevation — rule out RV infarct", "Serial troponins: 0h, 3h, 6h (standard) OR 0h and 1–2h (high-sensitivity)", "Chest X-ray (portable) to assess for pulmonary edema, aortic dissection", "Bedside echo if hemodynamically unstable")]],
   pages=[126, 127],
   source_flags=["'Oxygen Monitoring' is the printed row label; shortened to Oxygen."]),
 T("tbl-acs-algorithm-step-4-classify", 127, AL + " > Step 4: interpret ECG and classify ACS type (STEMI vs NSTEMI/unstable angina)",
   "ACS management, step 4: interpret the ECG and classify (STEMI/new LBBB vs NSTEMI/unstable angina) with reperfusion or risk stratification, antiplatelet, anticoagulant and adjunctive doses", ["0352", "0353"],
   [[C(""), C("STEMI / New LBBB"), C("NSTEMI / Unstable Angina")]],
   [[C("Diagnosis"), C("ECG criteria:<br/>- ST elevation ≥1mm in ≥2 contiguous leads<br/>- New or presumed new LBBB<br/>- Posterior ST depression in V1–V3"),
     C("ECG + Troponin:<br/>- ST depression or T-wave inversion ± ↑Troponin = NSTEMI<br/>- Normal ECG + ↑Troponin = NSTEMI<br/>- Normal ECG + normal Troponin + symptoms = UA")],
    [C("Reperfusion / risk"), C("ACTIVATE CATH LAB NOW.<br/>Primary PCI (preferred):<br/>- Door-to-balloon < 90 min (first medical contact < 120 min)<br/>- Transfer to PCI-capable center if needed<br/>Fibrinolysis (if PCI not available):<br/>- Door-to-needle < 30 min<br/>- No contraindications (recent surgery, stroke, bleeding)<br/>- Transfer post-lysis within 3–24h for angiography"),
     C("RISK STRATIFY — TIMI or GRACE score.<br/>High-risk features (early invasive strategy):<br/>- Ongoing/refractory chest pain<br/>- Hemodynamic or electrical instability<br/>- Elevated troponin or rising pattern<br/>- New ST changes > 0.5 mm<br/>- TIMI score ≥3 or GRACE score > 140<br/>- → Angiography within 2–24 hours<br/>Low-risk (conservative/ischemia-guided):<br/>- No high-risk features<br/>- TIMI score 0–2, GRACE score < 109<br/>- → Stress testing before discharge or outpatient")],
    [C("Antiplatelet"), C("ASA 162–325 mg PLUS P2Y12 inhibitor:<br/>- Ticagrelor 180 mg loading (preferred) OR<br/>- Clopidogrel 600 mg loading"), C("ASA + Ticagrelor 180 mg OR Clopidogrel 300–600 mg")],
    [C("Anticoagulation"), C("- UFH: 60 units/kg IV bolus (max 4000 units)<br/>- Enoxaparin 0.5 mg/kg IV<br/>- Bivalirudin (alternative for PCI)"),
     C("- Enoxaparin 1 mg/kg SC q12h<br/>- Fondaparinux 2.5 mg SC daily (preferred if conservative)<br/>- UFH infusion if invasive strategy planned")],
    [C("Adjunctive / beta-blocker"), C("Adjunctive:<br/>- GP IIb/IIIa inhibitor if high thrombus burden<br/>- DO NOT delay reperfusion for workup"),
     C("Beta-blocker:<br/>- Start within 24h if no contraindications (HF, bradycardia, heart block, severe reactive airway disease)")]],
   pages=[127, 128],
   source_flags=["This part has no 'STEP 4' label in the PDF (it is headed 'Interpret ECG → classify ACS type' between steps 3 and 5).",
                 "GRACE 109-140 is not assigned to either risk group.", "Table continues onto p.128 with the header repeated."]),
 T("tbl-acs-algorithm-step-5-inhospital", 128, AL + " > Step 5: in-hospital management (all ACS)",
   "ACS management, step 5: in-hospital management for all ACS (beta-blocker, ACEi/ARB, statin, monitoring, complications)", ["0354"],
   [[C("Item"), C("Action")]],
   [[C("Beta-Blocker"), L("Metoprolol succinate/tartrate — initiate orally within 24h", "Target HR 50–60 bpm; avoid if decompensated HF, bradycardia, or high-degree AV block")],
    [C("ACEi / ARB"), L("Start within 24h in all ACS, especially EF < 40%, HTN, or DM", "Ramipril, Lisinopril, or Enalapril preferred; use ARB if ACEi intolerant")],
    [C("Statin"), L("High-intensity: Atorvastatin 40–80 mg OR Rosuvastatin 20–40 mg", "Initiate regardless of baseline LDL; target LDL < 70 mg/dL (< 55 preferred)")],
    [C("Monitoring"), L("Continuous telemetry ≥ 24h; watch for arrhythmias, AV block", "Serial ECGs and troponins until peak identified", "Echocardiogram to assess EF and wall motion", "Daily weights; strict fluid balance")],
    [C("Complications"), L("Arrhythmias: VF/VT → defibrillation; AV block → pacing", "Acute HF/Pulmonary edema: diuresis, afterload reduction, consider IABP", "Cardiogenic shock: vasopressors, mechanical support (IABP, Impella)", "Mechanical (papillary rupture, VSD, free wall rupture): urgent surgery", "Pericarditis / Dressler syndrome: NSAIDs, colchicine")]],
   source_flags=["Two rows are both labelled 'Complications' in the PDF; the first (telemetry, serial ECGs, echo, weights) is labelled Monitoring here."]),
 T("tbl-acs-algorithm-step-6-discharge", 129, AL + " > Step 6: discharge and secondary prevention",
   "ACS management, step 6: discharge and secondary prevention (DAPT, medications, lifestyle, follow-up)", ["0355"],
   [[C("Item"), C("Action")]],
   [[C("DAPT"), L("ASA 75–100 mg indefinitely", "P2Y12 (Ticagrelor or Clopidogrel) for 12 months post-ACS", "Consider extended DAPT (> 12 months) in high ischemic, low bleeding risk patients")],
    [C("Medications"), L("High-intensity statin therapy — lifelong", "ACEi or ARB — especially if EF ≤40%", "Beta-blocker — continue for minimum 3 years, indefinitely if reduced EF", "Aldosterone antagonist (Eplerenone/Spironolactone) if EF ≤35% + HF or DM", "SGLT2 inhibitor if DM or HFrEF for added cardioprotection")],
    [C("Lifestyle"), L("Smoking cessation — most effective single intervention", "Mediterranean or DASH diet", "Moderate aerobic exercise 150 min/week after cardiac rehab clearance", "Weight management: target BMI 18.5–24.9", "Blood pressure control: target < 130/80 mmHg", "Diabetes management: HbA1c < 7% target")],
    [C("Follow-up"), L("Cardiac rehabilitation enrollment — strongly recommended for all ACS", "Cardiology follow-up within 1–2 weeks of discharge", "Repeat echo at 6–12 weeks if EF reduced or not assessed", "Assess for ICD if EF remains ≤35% after 3 months of optimal therapy", "Ongoing lipid and renal function monitoring")]],
   source_flags=["The old chunk for this table was headed 'STEP 5: IN-HOSPITAL MANAGEMENT' instead of Step 6."]),
]
ITEMS += [
 T("tbl-fibrinolysis-contraindications", 130, AC + " > Contraindications for Fibrinolytic Therapy",
   "Contraindications for fibrinolytic therapy in STEMI: absolute and relative", ["0357"],
   [[C("Absolute Contraindications"), C("Relative Contraindications")]],
   [[L("Previous intra-cranial hemorrhage (ICH)", "Stroke of unknown origin at any time", "Ischemic stroke in the past 6 months", "Central nervous system damage", "Malignant intracranial neoplasm", "Other intracranial lesions (aneurysm or AV malformation)", "History of closed head or facial trauma within 3 months", "Major trauma/surgery within the preceding 3 weeks", "Suspected aortic dissection", "Active bleeding or known bleeding diathesis (excluding menses)", "Gastrointestinal bleeding within the past month", "Non-compressible punctures in [the past 24 hours]"),
     L("Previous ischemic stroke beyond 12 months", "Transient ischemic attack in the preceding 6 months", "Oral anticoagulation therapy", "Pregnancy or within 1 week postpartum", "Recent (2-4 weeks) internal bleeding", "Prolonged or traumatic CPR", "Active peptic ulcer (only if the ulcer is actively bleeding; if only stool occult blood positivity, may be considered for thrombolysis)", "Severe uncontrolled hypertension (SBP >180 mm Hg and/or DBP > 110 mm Hg). Patients presenting with hypertension should be given beta-blockers, nitroglycerin and analgesics promptly to lower blood pressure and reduce the risk of ICH following thrombolysis", "Patients on warfarin therapy have higher rates of hemorrhage: the higher the INR, the higher the risk", "Advanced liver disease", "Infective endocarditis")]],
   source_flags=["Several items run together in the PDF and were split: 'within the preceding 3 weeks suspected aortic dissection'; 'GI bleeding within the past month non-compressible punctures in' (cut off; '[the past 24 hours]' added from the usual ESC wording); 'the higher the INH, the higher risk of advanced liver disease' (read as INR, and advanced liver disease as its own item). Clinician to confirm."]),
]
