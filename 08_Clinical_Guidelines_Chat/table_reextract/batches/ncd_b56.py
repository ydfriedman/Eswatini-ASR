exec(open('batches/ncd_common.py').read())
LY = CH9 + " > Adult Lymphomas"; BC = CH9 + " > Breast Cancer"
ITEMS = [
 T("tbl-lymphoma-investigations", 254, LY + " > Investigations",
   "Adult lymphoma investigations: biopsy, pathology, laboratory tests and radiology", ["0728"],
   [[C("Diagnostic Category"), C("Investigation")]],
   [[C("Biopsy"), L("A whole node excision biopsy by a medical officer", "Bone marrow aspirate trephine (BMAT)")],
    [C("Pathology"), L("A full pathology report with IHC and cell of origin defined", "Blood smear", "Immunohistochemistry (often CD45, CD20, CD3 etc.)")],
    [C("Laboratory Tests"), L("A full biochemistry report, including KFT, LFT, uric acid, LDH, CMP, blood glucose", "FBC and differential count", "Erythrocyte sedimentation rate (ESR)", "CD4 count and viral load for eligible patients", "Hepatitis B surface antigen (HBsAg), hepatitis C virus and HIV tests")],
    [C("Radiology"), L("Echocardiogram report", "Contrasted CT scan – must include neck, chest, abdomen, and pelvis", "PET/CT scan for Deauville scoring, if available")]],
   context_before="Lymphoma: no routine screening is available; patients are suspected from symptoms (enlarged lymph nodes, chills, weight loss, fatigue, swollen abdomen, early satiety, chest pain or pressure, shortness of breath or cough, severe or frequent infections, easy bruising or bleeding). High-risk groups: EBV infection, HTLV-1, Kaposi sarcoma, immunosuppression (HIV or non-HIV related), H. pylori infection, autoimmune disorders (Sjogren's syndrome, Hashimoto's thyroiditis), exposure to pesticides, radiation and chemotherapy.",
   table_note="REFER TO A HIGHER LEVEL FACILITY FOR FURTHER INVESTIGATION AND MANAGEMENT.",
   source_flags=["The lymphoma text on p.253 is overprinted with garbled characters in the PDF text layer."]),
 T("tbl-breast-cancer-risk", 255, BC + " > Risk Stratification for Breast Cancer",
   "Breast cancer risk stratification by family history and genetics: above average, moderately increased, high risk", ["0732"],
   [[C("Risk Level"), C("Criteria")]],
   [[C("Above Average Risk"), L("No family history", "One first-degree relative or 1–2 second-degree relatives diagnosed at age 50 or older")],
    [C("Moderately Increased Risk"), L("A first-degree relative diagnosed before age 50", "Two or more first-degree relatives on the same side of the family diagnosed at any age")],
    [C("High Risk"), L("Known to carry a breast cancer susceptibility gene mutation (e.g. BRCA1 or BRCA2)", "Strong family history with at least two first-degree relatives affected, plus other features")]],
   table_note="General population screening should begin at age 35 with clinical and self-exam. High-risk clients start 8-10 years earlier than the index case (e.g. those with BRCA mutations may start at age 25). High risk: radiation to the chest in childhood or adulthood; familial breast and ovarian cancer; male breast cancer in the family; presenting with a breast lump; breast cancer in a first-degree relative under 50.",
   source_flags=["'No family history' is listed under 'Above Average Risk'; presumably this level is average/near-population risk."]),
 T("tbl-breast-cancer-diagnostics", 256, BC + " > Recommended diagnostics for breast cancer",
   "Breast cancer diagnostics: biopsy techniques, pathology, laboratory tests and radiology for staging", ["0735", "0736", "0737", "0739", "0740"],
   [[C("Diagnostic Category"), C("Investigation")]],
   [[C("Biopsy"), L("Biopsy techniques: excision; lumpectomy; tru-cut biopsy", "Ultrasound guided biopsies are preferred")],
    [C("Pathology"), L("A full pathology report including immunohistochemistry (IHC)")],
    [C("Laboratory Tests"), L("A full biochemistry report, including KFT and LFT", "FBC and differential count")],
    [C("Radiology"), L("Echocardiogram report", "Contrasted CT scan to include chest, abdomen and pelvis to rule out metastasis", "Chest X-ray prior to surgery to rule out effusions", "Bone scan in locally advanced breast cancers on the radiologist's recommendation if CT does not show metastasis; diffusion-weighted imaging (DWI) with MRI to image the spine. Note: DWI is recommended in place of a bone scan if a bone scan is not available", "Bilateral mammogram required for every patient for staging: the mammogram should include bilateral and axillary ultrasound; lymph nodes: routine supraclavicular ultrasound")]],
   context_before="Screening modalities: breast self-examination (breast awareness); clinical breast examination by a trained health worker; breast ultrasound; mammography; FNA; tissue biopsy (incision, excision or tru-cut); MRI in selected cases.",
   source_flags=["The tick-mark sub-items in this table are missing from the PDF text layer; transcribed from the page image. 'Enchocardiogram' printed."]),
 B("box-breast-self-exam", 257, BC + " > How to Advise Client on Breast Self-Examination",
   "Breast self-examination: how to advise clients (looking, touching, lying down, lymph nodes)", ["0741", "0742"],
   "1. By looking: stand before a mirror and look at both breasts and nipples – once with both arms beside your body; once with both hands on your hips; once with both arms raised and arms behind your head.\n"
   "2. By touching: raise your left arm. Use the pads of 3 or 4 fingers of the right hand to examine your left breast; repeat on the right side. Examine once in lines up and down the breast from outside and inside; once in circles around the breast, making smaller circles towards the nipple; once in wedges starting from outside towards the nipple and back again.\n"
   "3. While lying down: lie on your back, left arm over your head and a pillow under your left shoulder. Examine your left breast with your right hand as described before; repeat for the right side. This position flattens the breast and makes it easier to examine.\n"
   "4. Lymph nodes: place your left hand on your waist. With your right hand try to find enlarged lymph nodes in the left underarm area and around your collar bone; repeat on your right side. An enlarged lymph node feels like a corn kernel or a bean."),
]
CC2 = CH9 + " > Childhood Cancers"
ITEMS += [
 B("box-cbe-what-to-look-for", 258, BC + " > Clinical Breast Examination > What to look out for and palpation sequence",
   "Clinical breast examination: what to look out for (lump, pulled-in nipple, dimpling, skin changes, redness/rash, discharge) and the palpation sequence", ["0745", "0746"],
   "What to look out for during CBE (illustration): lump; pulled-in nipple; dimpling; skin changes; redness/rash; dripping (nipple discharge).\n\n"
   "Sequence to follow when performing breast palpation: 1. upper outer quadrant; 2. upper inner quadrant; 3. lower inner quadrant; 4. lower outer quadrant; 5. nipple-areola area; 6. axillary (underarm) quadrant."),
 D("fig-breast-early-referral", 259, BC + " > Early Referral Flow Chart for Suspected Breast Cancer",
   "Early referral flowchart for suspected breast cancer: urgent referral to the specialised breast unit, booking, or surgical clinic, by likelihood of malignancy", ["0747"],
   "Suspected lump → provider-initiated clinical breast exam (PI-CBE) and direct referral to the specialised breast unit (SBU):\n"
   "- High likelihood of malignancy → URGENT REFERRAL TO SBU (call and inform the SBU): suspicious lump (fixed, hard, irregular); palpable axillary lymph node; ulceration; nodules on the skin; skin tethering; nipple retraction; nipple discharge (e.g. bloody).\n"
   "- Unsure → book SBU: palpable lump in women >25 years; non-lactational breast infection/abscess.\n"
   "- Unlikely to be malignant → book for surgical clinic: palpable lump in women <25 years; breast pain with normal PI-CBE; family history with normal PI-CBE; lactation-associated infection with non-resolution/recurrence."),
 T("tbl-childhood-cancer-warning-signs", 260, CC2 + " > Warning Signs of Childhood Cancers (St. Siluan's signs)",
   "Warning signs of childhood cancers (St. Siluan's signs): seek help, eye, lump, unexplained symptoms, aches, neurological signs, with likely cancers and actions", ["0752", "0753"],
   [[C("Letter"), C("Category"), C("Key Signs & Symptoms"), C("Actions/Considerations")]],
   [[C("S"), C("Seek"), C("Seek medical help early for ongoing symptoms: prolonged symptoms; symptoms persist after treatment; symptoms return after initially disappearing"), C("Seek medical help; return to the same clinic/doctor for follow-up")],
    [C("I (E)"), C("Eye"), C("White spot in the eye (leukocoria) → possible retinoblastoma; loss of red eye reflex; new squint or sudden blindness → possible brain tumour; bulging eyeball → possible eye cancer or retro-orbital tumour"), C("Urgent referral to an ophthalmologist or paediatrician")],
    [C("L"), C("Lump"), C("Lump in the abdomen, pelvis, head, arms, legs, testicle or glands; Wilms' tumour (age 3–4 years); consider neuroblastoma, lymphoma"), C("Refer every lump to a doctor. If treated for TB without confirmation and not improving after 2 weeks → re-evaluate, consider biopsy")],
    [C("U"), C("Unexplained"), C("Unexplained fever for over two weeks; weight or appetite loss; fatigue; pallor; easy bruising and bleeding"), C("Possible leukaemia or solid tumours; requires thorough clinical assessment")],
    [C("A"), C("Ache"), C("Aching bones, joints, back and easy fractures. Aches and pains in bones and back are not common in children and should raise suspicion"), C("Possible leukaemia or sarcoma; needs critical evaluation")],
    [C("N"), C("Neurological"), C("Change in walk, balance or speech; regression of milestones; slurred speech; continuous headaches (>1 week) with or without vomiting; early morning vomiting; cranial nerve palsy; enlarged head (hydrocephalus)"), C("Possible brain tumour; prompt referral and neuroimaging as needed")]],
   pages=[260, 261],
   context_before="Childhood cancers arise between birth and 19 years. The most common are leukaemias (about 28%), brain and spinal cord tumours (about 26%), neuroblastoma (about 6%), Wilms tumour (5%), lymphomas, rhabdomyosarcoma, retinoblastoma and bone cancers (osteosarcoma, Ewing sarcoma). A high index of suspicion and early detection are critical.",
   source_flags=["The summary box spells the mnemonic SILUAN (I = eye signs) while the detailed table on p.261 uses 'E' for Eye; combined here.", "The PDF prints a summary box (p.260) and a detailed table (p.261); merged."]),
]
