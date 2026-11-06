exec(open('batches/ncd_common.py').read())
AP = CH7 + " > Acute Kidney Injury in Adults and Children > Pharmacological Management of Acute Kidney Injury"
ITEMS = [
 T("tbl-aki-fluid-challenge", 206, AP + " > Fluid Challenge/Inotropes",
   "AKI fluid challenge and inotropes: adults (500 ml boluses up to 2 L, adrenaline infusion) vs children (oral rehydration by dehydration severity, 20 ml/kg bolus)", ["0588"],
   [[C("Adults"), C("Children")]],
   [[C("Fluid bolus of 500 ml isotonic fluid (preferably Ringer Lactate) over 15 minutes and reassess (BP, pulse, JVP, urine output), up to a total of 2 litres, to achieve mean arterial pressure >65 mmHg.<br/>Start inotropes if adequate fluid challenge but still hypotensive, to avoid fluid overload and ensure tissue perfusion, e.g. adrenaline 4 mg (4 amps) in 200 ml of N/S IV at 10 ml/hr.<br/>REMEMBER to look for hypoglycaemia/sepsis/other associated complications and start treatment as indicated. Request Intensive Care Unit review urgently."),
     C("Rehydrate per protocol for age and body weight.<br/>Mild dehydration: oral rehydration solution 5 ml (1 teaspoon) every 5 minutes to replace losses, OR 10 ml/kg body weight for each loose stool.<br/>Moderate dehydration: 5 ml oral rehydration solution every 5 minutes to a total of 50-100 ml/kg body weight over 2-4 hours.<br/>Severe dehydration and failed oral rehydration: start cautious rehydration with a bolus of 20 ml/kg isotonic fluid such as Ringer Lactate IV, followed by maintenance IV fluids per paediatric protocols.<br/>URGENT REFERRAL FOR ICU CARE. DO NOT OVERHYDRATE, AS IT IS LINKED TO INCREASED MORTALITY.")]],
   context_before="Adjunct therapies are directed by the underlying cause: crystalloids for rehydration (preferably balanced solutions such as Ringer Lactate); relieve obstruction urgently; treat sepsis; immunosuppression as directed; treat electrolytes (hypercalcaemia); treat right heart failure (diuretics); relieve intra-abdominal pressure. Furosemide stress test: IV furosemide 1 mg/kg (furosemide-naïve) or 1.5 mg/kg (already on it); >200 ml urine over the next 2 hours suggests intact tubular function and likely recovery; <200 ml predicts ongoing dysfunction that may need dialysis."),
 T("tbl-aki-hyperkalaemia", 207, AP + " > Hyperkalaemia in AKI",
   "Hyperkalaemia (K ≥6 mmol/l) in AKI: adults vs children: calcium gluconate, insulin-dextrose, bicarbonate, salbutamol, potassium binder, furosemide, dialysis", ["0590", "0591"],
   [[C("Adults"), C("Children")]],
   [[L("Stabilize myocardium with bolus IV calcium gluconate 10% at 10 ml over 2 minutes (maximum 20 ml). DO NOT GIVE AT THE SAME TIME/SAME DRIP AS SODIUM BICARBONATE.",
       "Shift potassium with ONLY 5 units (five units) short acting insulin (Actrapid) in 50 ml of dextrose 50% over 30 minutes (higher insulin amounts can accumulate in kidney failure and cause dangerous hypoglycaemia).",
       "Shift with salbutamol nebulizer at 10-20 mg every 1-2 hours (MONITOR FOR TACHYCARDIA AND ARRHYTHMIAS).",
       "Potassium binder such as sodium polystyrene sulfonate (Kayexalate) 15 g mixed in 100 ml water once daily (CAUTION – DO NOT GIVE IF BOWEL PATHOLOGY).",
       "If overloaded, give furosemide IV 40-80 mg to aid urinary potassium loss.",
       "Urgent referral for dialysis, or acute peritoneal dialysis locally per protocol."),
     L("Stabilize myocardium with bolus IV calcium gluconate 0.5 ml/kg over 2-5 minutes.",
       "Shift potassium with dextrose 10% at 5 ml/kg IV bolus; if severe hyperkalemia, dextrose 10% 5 ml/kg IV bolus + Actrapid (short acting insulin) 0.1 units/kg (ESSENTIAL TO CHECK GLUCOSE EVERY 15-30 MINUTES AND CORRECT IF LOWER THAN 4 MMOL/L).",
       "Shift potassium with sodium bicarbonate (8.4%) 1-2 mmol/kg IV over 5 minutes.",
       "Shift potassium with salbutamol nebulizer – 2.5 mg if <25 kg and 5 mg if >25 kg, given 1-2 hourly (MONITOR FOR TACHYCARDIA AND ARRHYTHMIAS).",
       "DO NOT GIVE KAYEXALATE TO CHILDREN, AS IT CAN CAUSE NECROTISING ENTEROCOLITIS.",
       "If fluid overloaded, give furosemide IV 1-2 mg/kg; can repeat after 6 hours (individual dose not to exceed 6 mg/kg).",
       "Urgent referral for dialysis, or acute peritoneal dialysis locally per protocol while awaiting transfer or specialist review.")]],
   context_before="If hyperkalemia (≥6 mmol/l): cardiac monitor (risk of bradycardia, asystole, and ventricular arrhythmias). Fluid overload in kidney failure: IV furosemide at high doses (at least 120 mg, maximum 500 mg in 24 hours in adults); oxygen; isordil 5 mg sublingually; IV nitrate; morphine 2.5 mg IV titrated, maximum 10 mg, monitoring BP; urgent dialysis (referral to a centre with haemodialysis).",
   source_flags=["Children: Kayexalate is contraindicated here ('DO NOT GIVE'), while the paediatric AKI chart on p.203 gives calcium resonium (kayexalate) 1 g/kg 4-hourly. Clinician to confirm."]),
 T("tbl-aki-fluid-contexts", 208, AP + " > Clinical contexts for fluid administration in patients with or at risk of AKI",
   "Clinical contexts for fluid administration in patients with or at risk of AKI: reasons, benefits, challenges and risks by age, setting, comorbidity and acute condition", ["0593", "0594", "0595", "0596", "0597"],
   [[C("Clinical context"), C("Reasons for fluid administration and potential benefits"), C("Challenges and risks of fluid administration")]],
   [[C("Age and demographics: children, adults"), L("Diseases with volume losses", "Indications likely to be context-dependent"),
     L("Narrow window between hypovolemia and fluid overload", "Clear adverse effects of fluid overload", "Adverse effects of 'one size fits all' approach to fluid management", "Uncertain definition of clinically significant fluid overload", "In patients with heart disease, poor cardiac reserve to tolerate hypovolemia and hypervolemia", "In patients with diastolic dysfunction, risk of potentiating venous hypertension and renal congestion in fluid overload")],
    [C("Settings: resource-limited; pre-hospital, ward, ICU"), L("Specific conditions including diarrheal illness", "Impetus toward early resuscitation", "Dynamic phases of illness associated with hypovolemia"),
     L("Differing spectrum of disease", "Potentially delayed presentation to secondary care", "Limited range of therapeutic options", "Lack of advanced hemodynamic monitoring", "Inappropriate administration of maintenance fluid", "Risk of 'fluid-creep' leading to insidious fluid overload")],
    [C("Comorbid diseases: CKD; CHF or severe valvular disease"), L("Inability to conserve salt and water", "Poor cardiac reserve to tolerate hypovolemia"),
     L("Risk of hypovolemia", "Inability to handle fluid excess", "Predisposition to AKI", "Potentiation of adverse effects of fluid overload", "Potentially pre-existing interstitial edema", "Higher CVP associated with worsening kidney function", "Precipitation of fluid accumulation")],
    [C("Acute conditions: dehydration, hypovolemia, hemorrhage, sepsis, cardiogenic shock, major surgery, nephrotoxic exposure, abdominal compartment syndrome, ARDS, rhabdomyolysis/crush injury"),
     L("Acute free water deficit", "Salt and water deficit", "Acutely impaired oxygen delivery", "Intravascular hypovolemia", "Inability to tolerate hypovolemia", "Venodilation due to inotropic drugs", "Anesthesia-induced venodilation and vasodilation", "Perioperative fluid losses", "Dilution of filtered toxins", "Maintenance of visceral and renal perfusion", "Reduced cardiac preload due to high intrathoracic pressure", "Dilution of myoglobin", "Intravascular hypovolemia due to fluid losses to injured muscle"),
     L("Challenges of managing relative water and sodium deficits", "Need for consensus on optimal endpoints of resuscitation", "Dilution of hemoglobin may offset effects of fluid resuscitation on oxygen delivery", "Endothelial dysfunction, capillary leak, fluid losses to interstitium and vasodilation", "Lack of evidence for goal-directed hemodynamic therapy", "Risk of pulmonary edema", "Association between high CVP and adverse kidney outcome", "Inappropriate administration of maintenance fluid and 'fluid creep' leading to insidious fluid overload", "Risk of fluid overload", "Risk of venous hypertension", "Risk of worsening alveolar edema", "Development/worsening of compartment syndrome")],
    [C("Timing: biomarker-positive states; AKI stage"), L("Prevention of progression to overt AKI", "Reversal of early AKI"), L("Presence of early renal injury does not signify need for volume replacement", "Inappropriate attempts to 'reverse' established AKI resulting in fluid overload")],
    [C("Oliguria/anuria"), L("Oliguria as an indication of acute compensated hypovolemia"), L("Multiple etiologies of oliguria beyond hypovolemia", "Vicious cycle of fluid overload resulting in worsening kidney function")]],
   pages=[208, 209],
   footnotes=["AKI, acute kidney injury; ARDS, acute respiratory distress syndrome; CHF, congestive heart failure; CVP, central venous pressure; ICU, intensive care unit. Source: Kidney International (2020) 98, 294-309."],
   source_flags=["In the PDF the bullets in each block are not matched to individual sub-contexts (e.g. which reason belongs to sepsis vs ARDS); kept as one row per block.", "Table continues onto p.209 (timing and oliguria rows), which were missing from the old chunks. The abbreviation list expands CKD as 'central venous pressure'."]),
]

CK = CH7 + " > Chronic Kidney Disease"
ITEMS += [
 T("tbl-aki-complications", 209, CH7 + " > Acute Kidney Injury in Adults and Children > Complications of Acute Kidney Injury",
   "Complications of acute kidney injury: short term (fluid overload, hyperkalaemia, acidosis, uraemia, hypocalcaemia, drug toxicity) and long term (CKD, mortality, CV risk)", ["0598"],
   [[C("Short Term"), C("Long Term")]],
   [[C("1. Fluid overload related – pulmonary edema, hypertension<br/>2. Electrolyte related – hyperkalemia with risks of bradycardia and asystole or ventricular fibrillation<br/>3. Metabolic acidosis – Kussmaul respiration<br/>4. Uraemic – uraemic pericarditis (risk of tamponade, especially following haemorrhagic conversion from heparin use during haemodialysis); uraemic encephalopathy (tremor, confusion, coma, seizures)<br/>5. Electrolyte related – may have hypocalcaemia (seizures, tetany – though commoner in CKD)<br/>6. Systemic toxicity from accumulation of renally cleared pharmacologic agents – e.g. gadolinium, ethambutol"),
     C("1. Progression to CKD<br/>2. Worsening of underlying CKD<br/>3. Mortality risk<br/>4. Cardiovascular risk")]]),
 D("fig-pr-aki-causes-timeline", 210, CH7 + " > Acute Kidney Injury in Adults and Children > Pregnancy-Related AKI > Causes of PR-AKI",
   "Causes of pregnancy-related acute kidney injury by trimester and postpartum (timeline), with disease-specific treatment and management of PR-AKI", ["0600", "0601"],
   "Timeline of causes (bars across first, second, third trimester and postpartum):\n"
   "- First trimester: hyperemesis gravidarum; septic abortion.\n"
   "- Glomerulonephritis: from the first trimester through the third trimester.\n"
   "- Urinary tract infection/pyelonephritis: late first trimester through the second and early third trimester.\n"
   "- Preeclampsia/eclampsia/HELLP syndrome: from the second trimester into early postpartum.\n"
   "- Thrombotic thrombocytopenic purpura: second and third trimester.\n"
   "- Placental abruption/haemorrhage: late second and third trimester.\n"
   "- Obstruction: second and third trimester.\n"
   "- Acute fatty liver: third trimester and postpartum.\n"
   "- Atypical haemolytic uraemic syndrome: third trimester and postpartum.\n\n"
   "Disease-specific treatment of AKI in pregnancy:\n"
   "| Cause | Treatment |\n|---|---|\n"
   "| Hyperemesis gravidarum/prerenal causes | Hydration |\n| Septic abortion/urinary tract infection | Antibiotics |\n"
   "| Preeclampsia/HELLP/acute fatty liver of pregnancy | Delivery |\n| Thrombotic thrombocytopenic purpura | Plasma exchange, rituximab |\n"
   "| Atypical haemolytic uraemic syndrome | Eculizumab |\n| Obstructive uropathy | Analgesics, stent, nephrostomy |\n"
   "| Placental abruption and haemorrhage | Control bleeding, delivery |\n| Glomerulonephritis | Steroids, immunosuppression |\n\n"
   "HELLP: hemolysis, elevated liver enzymes, and low platelets.\n"
   "Management of PR-AKI: 1. risk reduction – close monitoring and hydration for hyperemesis gravidarum; 2. monitor for urosepsis and treat early; 3. reduce pre-eclampsia risk in patients with underlying CKD – aspirin, calcium, BP control.",
   ["The timeline is an image; bar positions are approximate. 'Ecelizumab', 'Control building', 'Septyic', 'Glamerulonephritis' printed."]),
 T("tbl-ckd-causes", 211, CK + " > Causes of CKD",
   "Causes of chronic kidney disease by category: vascular, glomerular, tubulointerstitial, structural, others (CKDu, COVAN, chronic infections)", ["0602", "0603"],
   [[C("Category"), C("Example")]],
   [[C("Vascular"), C("Hypertension, vasculitis etc. Atherosclerotic renal artery stenosis, Takayasu's arteritis, fibromuscular dysplasia etc.")],
    [C("Glomerular Diseases"), C("Diabetes, autoimmune diseases (e.g. lupus nephritis), chronic systemic infections (e.g. HIV, HBV, syphilis), drugs, neoplasia, glomerulonephritis, glomerulopathies")],
    [C("Tubulointerstitial Diseases"), C("UTI, drug-induced interstitial nephritis (e.g. traditional herbs (timbita), rifampicin, allopurinol, fluoroquinolones, sulphonamides, beta-lactam antibiotics, proton pump inhibitors, NSAIDs), infective, autoimmune, toxins, neoplasms e.g. myeloma")],
    [C("Structural"), C("Hereditary - polycystic kidneys, renal masses, obstruction (stones, strictures), CAKUT in children (congenital abnormalities of the kidney and urinary tract)")],
    [C("Others"), C("Congenital - other congenital diseases (glomerular or tubular), e.g. Alport's syndrome. CKDu – CKD of unknown etiology amongst laborers in hot climates with no other traditional CKD risk factors (? due to heat and dehydration). COVAN – COVID-19 nephropathy with proteinuria. Chronic infections – HIV, hepatitis B, hepatitis C, syphilis, malaria etc. (can affect all areas of renal parenchyma). Chronic obstruction/posterior urethral valves (developmental)/vesicoureteric reflux (developmental), nephrolithiasis (kidney stones)")]],
   context_before="Chronic kidney disease is structural or functional kidney damage present for >3 months, with or without a decreased glomerular filtration rate (GFR).",
   footnotes=["A previous episode of acute kidney injury or acute kidney disease can lead to CKD; therefore all patients with a history of AKI require follow-up of renal function.", "Many causes are potentially preventable or modifiable if detected early."]),
 T("tbl-ckd-criteria", 211, CK + " > Definition(s) and Classification of Chronic Kidney Disease",
   "Criteria for CKD (either present for >3 months): markers of kidney damage or decreased GFR", ["0604"],
   [[C("Criteria for CKD (either of the following present for >3 months)", cs=2)]],
   [[C("Markers of kidney damage (one or more)"), L("Albuminuria (AER >30 mg/24 hours; ACR >30 mg/g [>3 mg/mmol])", "Urine sediment abnormalities", "Electrolyte and other abnormalities due to tubular disorders", "Abnormalities detected by histology", "Structural abnormalities detected by imaging", "History of kidney transplant")],
    [C("Decreased GFR"), C("GFR <60 ml/min/1.73 m2 (GFR categories G3a-G5)")]],
   source_flags=["ACR is printed '> 30 mg/mg'; written as mg/g (KDIGO)."]),
 T("tbl-ckd-prognosis-heatmap", 212, CK + " > Prognosis of CKD and Albuminuria",
   "Prognosis of CKD by GFR and albuminuria categories (KDIGO 2012 heat map): risk colour for each GFR stage G1-G5 x albuminuria A1-A3", ["0605", "0606"],
   [[C("GFR category (ml/min per 1.73 m2)", rs=2), C("Description", rs=2), C("Range", rs=2), C("A1: normal to mildly increased (<30 mg/g; <3 mg/mmol)"), C("A2: moderately increased (30-300 mg/g; 3-30 mg/mmol)"), C("A3: severely increased (>300 mg/g; >30 mg/mmol)")],
    [C("Risk (colour)"), C("Risk (colour)"), C("Risk (colour)")]],
   [[C("G1"), C("Normal or high"), C("≥90"), C("Green (low)"), C("Yellow (moderately increased)"), C("Orange (high)")],
    [C("G2"), C("Mildly decreased"), C("60-89"), C("Green (low)"), C("Yellow (moderately increased)"), C("Orange (high)")],
    [C("G3a"), C("Mildly to moderately decreased"), C("45-59"), C("Yellow (moderately increased)"), C("Orange (high)"), C("Red (very high)")],
    [C("G3b"), C("Moderately to severely decreased"), C("30-44"), C("Orange (high)"), C("Red (very high)"), C("Red (very high)")],
    [C("G4"), C("Severely decreased"), C("15-29"), C("Red (very high)"), C("Red (very high)"), C("Red (very high)")],
    [C("G5"), C("Kidney failure"), C("<15"), C("Red (very high)"), C("Red (very high)"), C("Red (very high)")]],
   footnotes=["Green, low risk (if no other markers of kidney disease, no CKD); yellow, moderately increased risk; orange [high risk; red, very high risk]."],
   source_flags=["Misprints: G3a range '45-49' (KDIGO 45-59); A1 '<300 mg/g' (KDIGO <30 mg/g); G3b 'Mildly to severely decreased' (moderately to severely); axis label 'GDF categories'. The colour legend is cut off after 'orange'.",
                 "This heat map matches KDIGO (G1-G2 with A3 orange), unlike the CKD screening heat map in Chapter 1 (p.30), which shows those cells red."]),
]
ITEMS += [
 T("tbl-kidney-function-measures", 212, CK + " > Measuring kidney function",
   "Measures of kidney function: direct measures (creatinine clearance, measured GFR), estimating equations for adults and children (Cockcroft-Gault, MDRD, CKD-EPI, FAS, Schwartz), and limitations", ["0607", "0608"],
   [[C("Direct measures of kidney function"), C("Indirect measures of kidney function: estimating equation"), C("Limitation")]],
   [[C("- Creatinine clearance<br/>- 24h urine creatinine"), C("- eGFR"),
     C("- No estimate of kidney function has been specifically validated for glomerular disease and/or nephrotic syndrome<br/>- Ethnicity is often a confounding influence<br/>- In creatinine-based formulas, hypoalbuminemia may lead to overestimation of true GFR due to increased tubular creatinine secretion (8)<br/>- Glucocorticoids may increase serum cystatin C, potentially underestimating eGFR (9)<br/>- Low muscle mass overestimates eGFR using creatinine-based formulae (10)<br/>- AKI confounds all estimates, which are valid only in steady state", rs=2)],
    [C("- Measured GFR*: inulin clearance (gold standard); radioisotopic plasma clearance (1): 125I-iothalamate, 99mTc-DTPA, 51Cr-EDTA; non-radioisotopic plasma clearance: iohexol (2)"),
     C("Adults:<br/>- Cockcroft-Gault (3): (140 - age) x weight [kg] (x 0.85 if female) / (serum creatinine [mg/dl] x 72)<br/>- Modification of diet in renal disease (MDRD) equations (4) (not valid for eGFR > 60 ml/min/1.73 m2)<br/>- CKD-EPI creatinine equation (preferred); valid with eGFR > 60 ml/min/1.73 m2<br/>- CKD-EPI cystatin C equations (5) (valid for eGFR > 60 ml/min/1.73 m2)<br/>- Full Age Spectrum (FAS) equation (7); valid even in eGFR > 60 ml/min/1.73 m2<br/>Children:<br/>- Schwartz equation and its modifications (6)<br/>- Full-age spectrum (FAS) formulae (7)")]],
   footnotes=["Assessment of kidney function in glomerular disease. *In ml/min per 1.73 m2. The correct coefficient for race in GFR estimating equations is controversial (see the KDIGO CKD guideline). References: 1 Perrone et al.; 2 Gaspari et al.; 3 Cockcroft and Gault; 4 and 5 Stevens et al.; 6 Schwartz et al.; 7 Pottel et al.; 8 Branten et al.; 9 Zhai et al.; 10 Levey et al. CKD-EPI, Chronic Kidney Disease Epidemiology Collaboration; 51Cr-EDTA, chromium-51 labelled ethylenediamine tetraacetic acid; 99mTc-DTPA, technetium-diethylenetriamine pentaacetic acid."],
   pages=[212, 213],
   source_flags=["The Cockcroft-Gault formula is printed with '9' in place of '(' ('(140-age) 9WT[kg]) x 0.85, if female/serum creatinine 9mg/dl) x 72'); written out correctly. '125 lothalamate', 'Tc-DRPA', 'Lohexol' printed."]),
]
