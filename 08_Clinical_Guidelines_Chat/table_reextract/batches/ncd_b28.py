exec(open('batches/ncd_common.py').read())
HF = CH3 + " > Heart Failure"
ITEMS = [
 T("tbl-ross-hf-children", 116, HF + " > The Modified Ross Classification of Heart Failure in Children",
   "Modified Ross classification of heart failure in children (class I-IV by symptoms)", ["0318"],
   [[C("Class of Symptoms"), C("Symptoms noted on history")]],
   [[C("Class I"), C("No symptoms/limitations")],
    [C("Class II"), C("Mild tachypnea/sweating during feeds in infants/dyspnea on exertion in older children but no growth failure")],
    [C("Class III"), C("Significant tachypnea or sweating during feeds/marked dyspnea on exertion/prolonged feeding time with growth failure")],
    [C("Class IV"), C("Symptoms (tachypnea, retractions, grunting, and sweating) even at rest with growth failure")]]),
]
ITEMS += [
 D("fig-hf-diagnosis-management", 117, HF + " > Algorithm for Diagnosis and Management of Heart Failure",
   "Algorithm for diagnosis and management of heart failure (by facility level, echo availability, congestion; guideline-directed therapy and CRT)", ["0320"],
   "1. Suspected heart failure? Take a history and examine.\n"
   "   - Clinic history: symptoms (acute: raised JVD, PND, lower limb swelling); function limitation (NYHA class); prior cardiac disease, pregnancies; prior comorbidities (HTN, disease, others); drugs, toxins.\n"
   "   - Physical exam: vital signs; signs of congestion (raised JVD, hepatomegaly); lower limb swelling; murmur; crackles.\n"
   "2. Investigations by facility level:\n"
   "   - Health Center: LABS: U&Es, CBC, glycemia, CXR, ECG. If congested with SatO2 <90%: give IV Lasix (furosemide) 40 mg and transfer to the regional hospital.\n"
   "   - Regional Hospital: U&Es, CBC, glycemia, HbA1c, chest X-ray, ECG, +/- cardiac ultrasound. Refer on to the referral hospital as needed.\n"
   "   - Referral Hospital: U&Es, CBC, glycemia, HbA1c, ferritin, chest X-ray, cardiac ultrasound, ECG, coronary CTA, cardiac MRI.\n"
   "3. Still suspect heart failure? (at DH/PH/referral hospital) Yes → Is heart ultrasound (echo) available?\n"
   "   - No: treat as HFrEF (EF ≤40%) and refer to cardiology.\n"
   "   - Yes: HFrEF & HFmrEF on echo → look for cardiomyopathy or valvular heart disease.\n"
   "     - Not congested: work up causes (genetics, inflammatory, toxins, pregnancy, metabolic).\n"
   "4. If congested (from either path): IV Lasix (8-hourly), morphine (if no low BP), nitrates (if available), oxygen (if low SpO2).\n"
   "   - Cardiogenic shock: IV inotropes/pressors, until euvolemic.\n"
   "5. When euvolemic, start guideline-directed medical therapy: 1. RAASi; 2. beta-blocker; 3. MRA (EF ≤35%); 4. SGLT2i → RAASi + BB + MRA ± SGLT2i.\n"
   "6. After 3 months of GDMT, if EF ≤35% plus LBBB: CRT (cardiac resynchronisation therapy).",
   ["'Cardiac U/C' (referral hospital) is read as cardiac ultrasound; 'GDME' as GDMT (guideline-directed medical therapy).",
    "The final box reads 'RAASi + BB + MRA + SGL T2i±'; the position of '±' is ambiguous."]),
]
ITEMS += [
 D("fig-hf-preserved-ef", 118, HF + " > Algorithm for Diagnosis and Management of Heart Failure > Preserved ejection fraction",
   "Heart failure with LVEF >50%: hypertensive heart disease (HFpEF) and mitral stenosis (algorithm, continued)", ["0322"],
   "Still suspect heart failure? (at HC/PH/referral hospital) → Heart ultrasound available? Yes → LVEF >50%:\n"
   "- With BP >180/110 mmHg: hypertensive heart disease (HFpEF); calculate the H2FPEF score.\n"
   "  - If congested: IV Lasix (8-hourly), oxygen (if low SpO2), position semi-sitting.\n"
   "  - Screen for comorbidities: diabetes, dyslipidemia, AF, CAD, HTN.\n"
   "  - BP control: 1. SGLT2i; 2. beta-blocker (if AF); 3. RAASi; 4. CCB.\n"
   "- With mitral restricted opening, hockey-stick deformity, dilated LA on echo, and an apical diastolic murmur: mitral stenosis.\n"
   "  - Causes: 1. rheumatic; 2. calcific; 3. congenital; 4. valvulitis.\n"
   "  - Treat: Lasix (if congested); penicillin V (rheumatic); beta-blocker (atenolol).",
   ["The comorbidity list ends 'Afib, CAD, HTN, and' (incomplete in the PDF).", "'Lasis' and 'Penni v' printed; read as Lasix and penicillin V."]),
]
ITEMS += [
 D("fig-hf-other-causes", 119, HF + " > Algorithm for Diagnosis and Management of Heart Failure > Valvular, right heart and pericardial disease",
   "Heart failure algorithm (continued): valvular heart disease, right heart failure, pericardial disease, other diagnoses and precipitants of acute heart failure; inotrope dosing", ["0324", "0325"],
   "Still suspect heart failure? (at HC/PH/referral hospital) → Heart ultrasound available? Yes → LVEF >50%:\n"
   "- BP normal or high, valvular heart disease & CHD: 1. Lasix (if overloaded); 2. RAASi (high BP or LV remodelling); 3. +/- penicillin V; 4. cardiology consult.\n"
   "  - If congested: IV Lasix (8-hourly), oxygen (if low SpO2), position semi-sitting.\n"
   "- Dilated RV + D-shape sign, TAPSE <1.7 cm, loud P2: right heart failure. 1. Lasix (if congested); 2. screen for the cause of pulmonary HTN (acute/chronic lung disease, PE, other).\n"
   "- Pericardial effusion: pericardial disease. 1. Pericardiocentesis (if tamponade): refer to cardiologist; 2. screen for and treat the cause: infections (TB, HIV, CMV, EBV), metabolic (thyroid disorders, uremia), malignancy, connective tissue disease; 3. others.\n"
   "- Heart failure unlikely and normal heart ultrasound: consider other plausible diagnoses.\n\n"
   "Precipitants of acute heart failure: 1. dietary indiscretion (alcohol, high salt); 2. medical non-adherence; 3. renal failure (acute/CKD progression); 4. new drugs (BB, CCB, NSAIDs, others); 5. arrhythmias, valve dysfunction; 6. new infection (pneumonia, others); 7. myocardial ischemia/infarction, PE; 8. metabolic (thyroid, DKA, pancreatitis); 9. hypertensive crisis.\n\n"
   "Inotropes: IV dobutamine or dopamine 200 mg. Dose: 10-20 mcg/kg/min. Example for a 70 kg adult: 2 ampoules in 50 cc NS by syringe pump at 5.25-10.5 cc/h; or, if no syringe pump, 5 ampoules in 500 cc NS over 24 hours = 21 cc/h ≈ 7 drops/min. Keep MAP ≥ 65.",
   ["'Pericardial Affusion' and 'Penniv' printed; read as effusion and penicillin V."]),
]
