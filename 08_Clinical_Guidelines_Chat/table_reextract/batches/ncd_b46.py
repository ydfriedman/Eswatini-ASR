exec(open('batches/ncd_common.py').read())
AK = CH7 + " > Acute Kidney Injury in Adults and Children"
ITEMS = [
 T("tbl-aki-causes-by-region", 200, AK + " > Acute Kidney Injury Causes",
   "Causes of acute kidney injury by kidney region: pre-renal, intrinsic renal (tubules, interstitium, glomeruli, vessels), post-renal", ["0570"],
   [[C("Kidney Region"), C("Cause of Acute Kidney Injury")]],
   [[C("Pre-Renal"), L("Dehydration - kucatseka (enema), diarrhoea, vomiting, sweating", "Shock - cardiogenic, septic, haemorrhagic", "Drugs - BP therapy, non-steroidal anti-inflammatory drugs (NSAIDs)")],
    [C("Intrinsic Renal"), L("Tubules - acute tubular necrosis (from ischaemia from untreated pre-renal causes, sepsis, toxins like myoglobin in rhabdomyolysis, light chains in myeloma, radio-iodine contrast, drugs such as aminoglycosides, rifampicin, amphotericin B, tenofovir, traditional remedies, some Chinese medicines) OR tubulitis",
                             "Interstitium - acute interstitial nephritis (from drugs, e.g. rifampicin, bactrim) and from sepsis, autoimmune",
                             "Glomeruli - glomerulonephritis, e.g. post infection/autoimmune - can be drug induced",
                             "Vessels - vasculitis, malignant hypertension, scleroderma, renal artery stenosis, pre-eclampsia")],
    [C("Post Renal"), L("Urinary tract obstruction - cancer of the cervix, rectum, or prostate (also benign prostatic enlargement), renal stones, iatrogenic ureteric laceration, retroperitoneal fibrosis, intratubular crystals (e.g. acyclovir)")]],
   context_before="Acute kidney injury: a syndrome characterized by an acute decline in renal function, with many potential causes (KDIGO 2012). It can occur with pre-existing chronic kidney disease (acute on chronic). AKI is classified into three categories by cause and location of injury.",
   footnotes=["Pre-renal AKI is not always associated with hypovolemia; fluid administration should be based on clinical signs of hypovolemia. Kucatseka = enema."]),
 T("tbl-aki-conditions", 201, AK + " > Conditions causing AKI",
   "Conditions causing acute kidney injury with examples: reduced glomerular function (pre-renal), renal parenchymal injury (intrinsic), urinary tract obstruction (post-renal)", ["0572"],
   [[C("Category"), C("Conditions"), C("Examples / Notes")]],
   [[C("1. Conditions that reduce glomerular function (pre-renal)", rs=5), C("Hypotension / Hypovolemia"), C("Dehydration, hemorrhage, shock")],
    [C("Reduced Renal Artery Perfusion"), C("Renal artery stenosis, aortic dissection")],
    [C("Excessive Diuresis"), C("Seen in diabetic emergencies, hypercalcemia, or overuse of diuretics")],
    [C("Renal Venous Congestion"), C("Common in right heart failure – may need diuretics")],
    [C("Abdominal Compartment Syndrome"), C("After bowel surgery, or in presence of tense ascites")],
    [C("2. Renal Parenchymal Injury (Intrinsic)", rs=6), C("Sepsis"), C("Sepsis-associated acute tubular necrosis (ATN)")],
    [C("Drugs"), C("NSAIDs, timbita, aminoglycosides, radiocontrast agents")],
    [C("Endogenous toxins"), C("Myoglobin (rhabdomyolysis), hemoglobin (hemolysis), uric acid")],
    [C("Exogenous toxins"), C("Ethylene glycol, heavy metals")],
    [C("Autoimmune"), C("Lupus nephritis, ANCA vasculitis")],
    [C("Neoplastic"), C("Multiple myeloma (cast nephropathy)")],
    [C("3. Urinary Tract Obstruction (post-renal)", rs=5), C("Nephrolithiasis"), C("Kidney stones")],
    [C("Blood clots"), C("May occur after trauma or surgery")],
    [C("Sloughed papillae"), C("Seen in analgesic nephropathy, diabetes")],
    [C("Intrinsic obstruction"), C("Urethral/ureteric strictures")],
    [C("Extrinsic compression"), C("Pelvic tumors, retroperitoneal fibrosis, iatrogenic (e.g., ureter injury during TAH)")]]),
 T("tbl-aki-staging", 202, AK + " > Classification of Acute Kidney Injury",
   "AKI staging (KDIGO): serum creatinine and urine output criteria for stages 1-3", ["0573"],
   [[C("Stage"), C("Serum creatinine"), C("Urine output (common to both)")]],
   [[C("Stage 1"), C("Increase of ≥0.3 mg/dl (≥26.5 umol/l) or increase to ≥150% to 200% (1.5- to 2-fold) from baseline"), C("Less than 0.5 ml/kg/h for more than 6 hours")],
    [C("Stage 2"), C("Increase to more than 200% to 300% (>2- to 3-fold) from baseline"), C("Less than 0.5 ml/kg/h for more than 12 hours")],
    [C("Stage 3"), C("Increase to more than 300% (>3-fold) from baseline, or ≥4.0 mg/dl (≥354 umol/l) with an acute increase of at least 0.5 mg/dl (44 umol/l), or on RRT"), C("Less than 0.3 ml/kg/h for 24 hours or anuria for 12 hours")]],
   source_flags=["Stage 1 is printed '(1.5-to 1-fold)' and stage 3 '(<3-fold)'; written as 1.5- to 2-fold and >3-fold (KDIGO). Stage 3 is printed 'Step 3'.",
                 "The AKI flowchart on the same page gives stage 3 as creatinine '> 356 mmol/l' and urine output <0.5 ml/kg/h for 24 hours, unlike this table (≥354 umol/l; <0.3 ml/kg/h for 24 h)."]),
 D("fig-aki-algorithm", 202, CH7 + " > Acute Kidney Injury in Adults and Children > Diagnosis of Acute Kidney Injury > Algorithm for Diagnosis and Management of Acute Kidney Injury",
   "Algorithm for diagnosis and management of acute kidney injury: history, examination, investigations, staging, referral at stage 3, volume status, pre-renal/intrinsic/post-renal causes and investigations", ["0575"],
   "1. History of present illness: fluid intake and losses, oedema, severe systemic illness, shortness of breath, poor urine output or no urine output for more than 6 hours.\n"
   "2. Physical signs: tachycardia, JVP, oedema, encephalopathy, dry mucous membranes, weak pulses, decreased level of consciousness.\n"
   "3. Investigations: renal function, electrolytes, urine sediment, abdominal U/S, ECG if K is high.\n"
   "4. Classify the AKI stage (KDIGO/AKIN): stage 1: creatinine x1.5 baseline, urine output <0.5 ml/kg/hour for 6 hours; stage 2: creatinine x2 baseline, urine output <0.5 ml/kg/hour for 12 hours; stage 3: creatinine >3x, creatinine >356 mmol/l (as printed), urine output <0.5 ml/kg/hour for 24 hours.\n"
   "5. Confirm AKI.\n"
   "   - Stage 3: refer to a (paediatric) nephrologist in a centre that can perform RRT. All referrals in stage 3 who are stable need to be discussed with a physician and the receiving facility before referral.\n"
   "   - Stages 1 and 2: assess volume status, identify the causes, identify complications of AKI:\n"
   "     - Hypovolemia → pre-renal. Investigations: CBC, LFTs, CXR, ECG, UE, echocardiogram. Differential diagnosis: dehydration (inadequate fluid intake; GI losses - vomiting, diarrhoea; third spacing - sepsis, burns, pericarditis, nephrotic syndrome; salt wasting - renal/adrenal disease); blood loss; reduced cardiac output (congestive heart failure, cardiac tamponade, cardiogenic shock); sepsis; hepatorenal syndrome.\n"
   "     - Euvolemia → intrinsic renal. Investigations: serum CBC, LDH, albumin, hepatitis serology, UE; urine eosinophils; renal US + Doppler. Differential diagnosis: renal artery stenosis, venous thrombosis; vasculitis; HUS; glomerulonephritides; RPGN; TIN; acute tubular necrosis (nephrotoxic drugs, rhabdomyolysis, radiocontrast nephropathy, uric acid nephropathy, etc.).\n"
   "     - Third column (obstruction; labelled 'Hypovolemia / Pre-renal' as printed). Investigations: metabolic stone profile; abdominal US/CT. Differential diagnosis: posterior urethral valves; nephro/urolithiasis; blood clot; fungal ball; tumours; retroperitoneal process; fibrosis; haematoma. Needs urologist and nephrologist consult; relieve the obstruction.\n"
   "6. Drug administration & monitoring: treat underlying causes, avoid nephrotoxic drugs, IV antibiotics; monitor complications; monitor weight and urine output daily; if possible check UE, creatinine and plasma bicarbonate, Ca, PO4, FBC daily until stable.",
   ["The third branch is labelled 'Hypovolemia' and 'Pre-renal' but lists obstructive (post-renal) causes; it should presumably read post-renal.",
    "'pedestrian nephrologist' printed (paediatric). 'create' printed for creatinine; 'Fungal bail', 'Acute tubular recross', 'temponade' printed."]),
]
