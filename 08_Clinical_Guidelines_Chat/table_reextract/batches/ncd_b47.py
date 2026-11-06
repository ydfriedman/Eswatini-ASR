exec(open('batches/ncd_common.py').read())
AK = CH7 + " > Acute Kidney Injury in Adults and Children"
ITEMS = [
 D("fig-aki-fluids-electrolytes", 203, AK + " > Algorithm for Diagnosis and Management of Acute Kidney Injury > Fluid, hypertension, electrolyte and nutrition management; urgent dialysis",
   "AKI management (algorithm, continued): fluid management, hypertension, electrolytes and acidosis (hyperkalaemia, hyponatraemia, hypocalcaemia, acidosis), nutrition, and indications for urgent dialysis", ["0577"],
   "Fluid management:\n"
   "- Volume status: hypovolemia: fluid bolus NaCl 0.9% 20 ml/kg and rehydration.\n"
   "- Euvolemic: insensible losses (400 ml/m2 or 30 ml/kg/day) + urine and GI losses.\n"
   "- Hypervolemia: insensible losses; furosemide 2-4 mg/kg.\n"
   "- If nephrotic syndrome: consider 25% albumin 0.5 to 1 g/kg/dose over 30 to 60 (min), followed by a diuretic: Lasix 1-2 mg/kg.\n"
   "Hypertension:\n"
   "- Furosemide if fluid overload: IV, start 1 to 2 mg/kg/dose, 2nd dose 6 hours later (max 6 mg/kg).\n"
   "- Calcium channel blockers: amlodipine oral 0.05 to 0.3 mg/kg/dose OD (max 0.6 mg/kg/dose or 10 mg).\n"
   "- IV labetalol 0.2 to 1 mg/kg/dose if severe hypertension.\n"
   "- N.B. Avoid ACEI & ARBs in AKI.\n"
   "Electrolytes and acidosis:\n"
   "- Hyperkalemia: 10% calcium gluconate 0.5-1 ml/kg over 10 min + glucose ('25-5 mls' of D10W, as printed) with insulin 0.1 IU/kg; +/- salbutamol nebulised 2.5 mg (<25 kg) and 5 mg (>25 kg); +/- sodium bicarbonate 1-2 mmol (ml)/kg over 10-30 min; / calcium resonium (kayexalate) 1 g/kg 4-hourly with oral lactulose 2.5 ml (<1 year), 5 ml (1-5 years), 10 ml (>5 years).\n"
   "- Hyponatremia: if Na <118 mmol/l, calculate the sodium deficit: Na deficit = (125 - measured Na) x weight x 0.6; give over 2 hours as hypertonic saline 3%, target 125 mmol/l.\n"
   "- Hypocalcemia: 10% calcium gluconate 0.1 mg/kg (0.5 ml/kg), as printed.\n"
   "- Acidosis: 8.4% NaHCO3 deficit = (18 - measured HCO3) x 0.5 x weight, or NaHCO3 1-2 mmol/kg/dose TDS.\n"
   "Nutrition: adequate nutrition is mandatory; from day 2 introduce protein gradually. Requirements: 95-115 kcal/kg and protein 1.5-2 g/kg ('1.5-21 g/kg' printed). Treat underlying causes.\n\n"
   "Urgent dialysis if: hyperkalemia > 6.5 mmol/L ('605mmol/L' printed) not responding to medical treatment; severe fluid overload with pulmonary edema resistant to furosemide; urea > 40 mmol/L (30 mmol/L in neonates); severe hyponatremia (Na <120 mEq/L) or hypernatremia (Na >160 mEq/L) or severe acidosis pH <7.2 that cannot be corrected with HCO3 due to fluid overload, or refractory; multi-system failure; anticipation of prolonged oliguria. → Refer to tertiary renal replacement therapy. All referrals requiring urgent RRT must be discussed with the physician and the receiving facility before referral.",
   ["Several doses are misprinted: hyperkalaemia threshold '605mmol/L' (6.5); glucose '25-5 mls of D10W'; hypocalcaemia '0.1 mg/kg (0.5ml/kg)' (mg and ml do not match); protein '1.5-21 g/kg'; albumin 'over 30 to 60' with no unit. Clinician to confirm.",
    "These doses are weight-based (paediatric) but the section is titled for adults and children; adult doses are not given.", "'calcium inesonium', 'Hypocacemia', 'Hypermatremia', 'inebu' printed."]),
 T("tbl-aki-ckd-akd-definitions", 203, AK + " > Definitions of AKI, CKD and AKD",
   "Definitions of AKI, AKD (acute kidney diseases and disorders), CKD and NKD (no kidney disease): functional and structural criteria", ["0578", "0579"],
   [[C("Acronym"), C("Functional Criteria"), C("Structural Criteria")]],
   [[C("AKI"), C("Increase in SCr by > 50% within 7 d, OR increase in SCr by > 0.3 mg/dl (>26.5 umol/l) within 48 h, OR oliguria"), C("No criteria")],
    [C("CKD"), C("GFR < 60 ml/min per 1.73 m² for < 3 mo (as printed)"), C("")],
    [C("AKD"), C("AKI, OR decrease in GFR by > 35% or increase in SCr by > 50% for < 3 mo"), C("Kidney damage > 3 mo (as printed)")],
    [C("NKD"), C("GFR > 60 ml/min per 1.73 m²; stable SCr without AKI/AKD/CKD"), C("No damage")]],
   footnotes=["AKD, acute kidney diseases and disorders; AKI, acute kidney injury; CKD, chronic kidney disease; GFR, glomerular filtration rate; NKD, no kidney disease; SCr, serum creatinine."],
   source_flags=["The CKD and AKD rows appear misaligned: CKD should be GFR <60 for >3 months or kidney damage >3 months, and AKD kidney damage for <3 months (KDIGO). As printed, CKD reads '< 3 mo' with no structural criterion and AKD has 'Kidney damage > 3 mo' twice. Clinician to confirm."]),
 T("tbl-aki-screening-by-level", 204, AK + " > Requirements for AKI screening by level of health facility",
   "AKI screening requirements by level of health facility: primary care clinic, health centre/regional hospital, tertiary care", ["0580"],
   [[C("Primary Care Clinic"), C("Health Center/Regional Hospital"), C("Tertiary Care")]],
   [[L("Vital signs", "Weight (kg)", "Height (m or cm)", "Urine dipstick", "Good history & physical exam", "Medication & OTC review"),
     L("Includes all primary care assessments", "Urine analysis", "Urine microscopy, culture & sensitivity", "Blood tests: FBC, BUN, electrolytes, CO2/bicarbonate, calcium, magnesium, phosphate, glucose, LFTs, uric acid, HIV, hepatitis B & C, RPR", "Estimate GFR (Cockcroft-Gault if no lab eGFR)", "Blood cultures", "Abdominal ultrasound scan", "Cardiac monitoring"),
     L("Includes all health centre/regional hospital assessments", "Autoimmune serology (ANA, ANCA, anti-GBM)", "Myeloma screen (serum protein electrophoresis, urine Bence Jones proteins, serum free light chains)", "Urine stone analysis", "CT scan, intravenous pyelogram (IVP), urodynamic studies", "Urologist for de-obstruction", "Kidney biopsy (histopathology within 1 week)")]]),
 D("fig-aki-akd-follow-up", 204, AK + " > Schematic for AKI/AKD Follow up According to Level of Health Facility",
   "AKI/AKD follow-up by severity: who follows up and when, from short stage 1 AKI (non-nephrology care) to stage 3D or prior CKD 4 (nephrology within 1 week) (ADQI schematic)", ["0581", "0582", "0583"],
   "Follow-up after AKI/AKD, from least to most severe (left to right in the schematic; non-nephrology care providers at the mild end, nephrology at the severe end):\n"
   "1. Stage 1 AKI of short duration (1 day); SCr normal or returns to baseline; hospital-limited event in a healthy patient → consider KAMPS bundle within 1 year.\n"
   "2. Stage 1 AKI lasting 1-2 days; limited comorbidities; no prior CKD; SCr not returning to baseline → consider KAMPS in 6 months.\n"
   "3. Prolonged stage 1 AKI (3-6 days) or stage 2 AKI of shorter duration (1-3 days); increasing comorbidities (advancing age); SCr persistently elevated (<25% above pre-existing baseline) → labs in the next 3-6 weeks with long-term KAMPS/nephrology appointment (within the next several months).\n"
   "4. Prolonged stage 2 AKI with urine analysis showing injury (duration >7 days); multiple comorbidities (cancer, prior AKIs, mild CKD at baseline); SCr persistently elevated >25% above prior baseline in some recovery → labs within days of discharge and follow-up with nephrology; appointment/KAMPS within weeks.\n"
   "5. Prolonged stage 3 AKI and persistent other forms of AKI or kidney disease; history of prior AKI, significant CV disease, hypertension, diabetes mellitus, and advanced CKD → labs within days of discharge and follow-up with nephrology.\n"
   "6. AKI stage 3D (dialysis), recovered and non-recovered; prior CKD 4; recurrent AKI/AKD → KAMPS or WATCH-ME labs within days of discharge and follow-up with nephrology within 1 week.\n\n"
   "Example: a patient with CKD G4, regardless of AKI severity, should be followed by a nephrologist within 1 week. Abbreviations: 3D, dialysis; SCr, serum creatinine; UA, urine analysis; WATCH-ME, weight assessment, access, teaching, clearance, hypotension, medications; KAMPS (kidney function, awareness, medications, pressure, sick-day protocol). Reproduced from Acute Dialysis Quality Initiative (ADQI) XXII.",
   ["'<2% 5 of pre-existing baseline' printed; read as <25%. 'KAPMS' and 'KAMPS' are both used; neither is defined in full (the legend gives 'pressure-sick day protocol')."]),
 T("tbl-aki-assessment", 205, AK + " > Patient Assessment",
   "AKI patient assessment: vital signs targets, history, life-threatening effects, cardiac monitoring, ultrasound, urine analysis, chest X-ray", ["0584", "0585"],
   [[C("Assessment Domain"), C("Details")]],
   [[C("Vital Signs"), L("Pulse", "Blood pressure: aim MAP > 65 mmHg and < 110 mmHg (MAP = DBP + 1/3 PP; PP = SBP - DBP)", "Urine output: aim > 0.5 mL/kg/hour")],
    [C("Patient History"), L("Presenting complaint", "Past medical, surgical, OBGYN, urology history", "Systems enquiry: nervous, musculoskeletal, endocrine, respiratory, cardiovascular, GI, ENT, dermatological", "Drug/toxin history (including OTC and herbal remedies)", "Urine output history", "Occupational history (e.g., laborer in hot weather)")],
    [C("Life-Threatening AKI Effects"), L("Pulmonary edema: SpO2, clinical signs, arterial blood gas (ABG)", "Hyperkalemia: ABG, electrolytes", "Metabolic acidosis: ABG")],
    [C("Cardiac Monitoring"), L("ECG for hyperkalemia signs, LV hypertrophy, heart block, myocardial ischemia")],
    [C("Imaging: Abdominal Ultrasound"), L("Exclude urinary tract obstruction (urgent de-obstruction needed)", "Assess kidney size (normal: 9–12 cm), appearance, and echogenicity")],
    [C("Urine Analysis"), L("Dipstick: specific gravity, protein, blood, leukocytes", "Microscopy: granular casts → ATN / GN; red cell casts / dysmorphic RBCs → RPGN; leukocytes → pyelonephritis / AIN")],
    [C("Chest X-ray"), L("Assess for fluid overload (pulmonary edema), cardiomegaly, pericardial effusion, or cardiomyopathy", "Exclude pulmonary-renal syndrome (look for infiltrates)")]]),
 T("tbl-aki-nonpharm", 205, AK + " > Non-Pharmacological Management of Acute Kidney Injury",
   "Non-pharmacological management of AKI by level of care: primary care clinic vs health centre and hospitals", ["0586"],
   [[C("Primary Care Clinic"), C("Health Center, Regional Hospital, Referral Hospital")]],
   [[L("Stop intake of all salt and potassium containing foods and fluids", "For dehydration (watch out for tachycardia, hypotension, capillary refill > 2 seconds, low jugular venous pressure, dry armpits): encourage fluid intake, to 10 mL/kg/day plus visible fluid losses, to avoid fluid overload", "Remove nephrotoxic medications", "Avoid fluid overload in heart failure and advanced kidney failure", "Avoid nephrotoxins – avoid use of herbal remedy mixes"),
     L("As previous PLUS:", "Give oxygen, and nurse in semi-Fowler's position if patient has respiratory distress", "Adequate nutritional support: enough energy and adequate protein. Consider enteral/parenteral nutrition", "Monitor fluid input and output", "MDT client care depending on underlying cause of AKI")]],
   source_flags=["'Encourage fluid intake, to 10 mL/kg/day plus visible fluid losses' for dehydration is printed as is; the sentence mixes rehydration with fluid restriction. Clinician to confirm.",
                 "The health centre column text spans the health centre, regional and referral hospital columns in the PDF."]),
]
