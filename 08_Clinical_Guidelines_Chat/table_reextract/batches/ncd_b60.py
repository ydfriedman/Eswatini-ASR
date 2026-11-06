exec(open('batches/ncd_common.py').read())
PM = CH11 + " > Pain Management"
def r(*v): return [C(x) for x in v]
ITEMS = [
 T("tbl-pain-types", 286, PM + " > Types and Characteristics of Pain",
   "Types of pain (nociceptive somatic, visceral, inflammatory; neurogenic; functional): characteristics, mechanisms and example drug treatments", ["0826"],
   [[C("Type of Pain"), C("Subtype"), C("Characteristics"), C("Mechanisms"), C("Examples of pharmacologic treatments")]],
   [[C("Nociceptive", rs=3), C("Somatic (tissue injury)"), C("Superficial (skin) or deep pain (muscle, fascia, tendon)"), C("Mechanical, thermal or chemical stimuli"), C("Acetaminophen, Na+ blockers, NSAIDs, steroids, opioids")],
    r("Visceral (irritable bowel, cystitis)", "Constant or cramping. Poor localization. Autonomic responses", "Visceral distension", "NSAIDs, antispasmodics, opioids"),
    r("Inflammatory (musculoskeletal)", "Localized or diffuse pain, hyperalgesia, allodynia", "Associated with localized inflammation", "NSAIDs, steroids"),
    [C("Neurogenic", rs=2), C("Neuralgia, radiculopathy, causalgia, CNS lesions"), C("Spontaneous, paroxysmal pain, allodynia, hyperalgesia"), C("Peripheral or CNS lesions"), C("Anticonvulsants, opioids, antidepressants")],
    r("Functional (FM, thalamic syndromes, irritable bowel syndrome)", "Diffuse deep pain, hyperalgesia, allodynia", "Dysregulation of excitatory or inhibitory mechanisms in CNS", "Antidepressants, anticonvulsants, opioids, cannabinoids")],
   pages=[286, 287],
   context_before="Pain is 'an unpleasant sensory and emotional experience associated with, or resembling that associated with, actual or potential tissue damage' (IASP).",
   source_flags=["Functional pain sits under 'Neurogenic' in the PDF's first column (row span), as printed. FM is not expanded (fibromyalgia)."]),
 D("fig-who-analgesic-ladder", 289, PM + " > Management of Pain > WHO Analgesic Ladder",
   "WHO analgesic ladder for adult pain: step 1 non-opioid (mild), step 2 weak opioid (moderate), step 3 strong opioid (severe), with drug categories", ["0831", "0832"],
   "Pain scores on the numerical rating scale: none 0; mild 1-3; moderate 4-6; severe 7-10.\n"
   "- Step 1, mild pain (0-3): non-opioid +/- adjuvant.\n"
   "- Step 2, moderate pain (4-6): weak opioid +/- non-opioid +/- adjuvant.\n"
   "- Step 3, severe pain: strong opioid +/- non-opioid +/- adjuvant.\n"
   "Step up if pain persists or increases; step down if pain decreases.\n\n"
   "Categories of drugs:\n"
   "- Non-opioids: ibuprofen or other NSAID, paracetamol (acetaminophen), or aspirin.\n"
   "- Weak opioids: codeine, tramadol, or low-dose morphine.\n"
   "- Strong opioids: morphine, fentanyl, oxycodone, hydromorphone, buprenorphine.\n"
   "- Adjuvants: antidepressant, anticonvulsant, antispasmodic, muscle relaxant, bisphosphonate, or corticosteroid.\n"
   "Combining an opioid and a non-opioid is effective, but do not combine drugs of the same class. Time doses by drug half-life ('dose by the clock'); do not wait for pain to recur."),
]
PA = CH11
ITEMS += [
 T("tbl-analgesic-doses", 290, PM + " > Analgesics: doses and cautions",
   "Analgesics for palliative pain management: non-opioids (paracetamol, ibuprofen, diclofenac), weak opioids (tramadol, codeine), strong opioid (morphine): doses, cautions and contraindications", ["0833", "0834"],
   [[C("Category"), C("Drug and Dosage"), C("Caution and Contraindications")]],
   [[C("Non-Opioid", rs=3), C("Paracetamol: 500 mg-1 g 6-8 hourly"), C("Hepatotoxicity. Maximum dose 4 g per day")],
    r("Ibuprofen: 400 mg 6-8 hourly", "Give with food. Maximum dose 1.2 g. Avoid in asthma and peptic ulcer. Lower dose if liver impairment"),
    r("Diclofenac: 50 mg 8-12 hourly", "Give with food; avoid in asthma and peptic ulcer. Maximum dose 150 mg"),
    [C("Weak Opioid", rs=2), C("Tramadol: 50-100 mg 4-6 hourly"), C("Caution in epileptic patients. Maximum dosage 240 mg daily (as printed). Give laxatives to avoid constipation unless the patient has diarrhoea", rs=2)],
    r("Codeine: 30-60 mg 4 hourly"),
    r("Strong Opioid", "Morphine: start with 2.5-20 mg q4h (immediate release); give 8-24 hourly for slow release. 5%-20% of the daily dose is used as the starting dose for breakthrough pain", "Low-dose morphine is given if the maximum weak-opioid dose does not work. No ceiling dose for morphine (increase gradually until pain is controlled). Pethidine can be used for acute pain (NOT for chronic pain)")],
   footnotes=["Less commonly used strong opioids in our settings: fentanyl, oxycodone, hydromorphone, methadone."],
   source_flags=["Tramadol maximum is printed '240mg daily'; the usual maximum is 400 mg/day. Clinician to confirm.", "'Ibuprofene', 'Qxycodone' printed."]),
 T("tbl-opioid-equianalgesic", 290, PA + " > Opioids Equi-analgesic Dose Ratios",
   "Opioid equi-analgesic doses: oral and subcutaneous/IV equivalents of codeine, tramadol, morphine, hydromorphone, oxycodone, fentanyl, methadone", ["0835"],
   [[C("Opioid"), C("Approximate oral equivalent dose"), C("Equivalent dose subcut (IV)")]],
   [r("Codeine", "100 mg", ""), r("Tramadol", "50 mg", ""), r("Morphine", "10 mg", "5 mg (3 mg)"),
    r("Hydromorphone", "2 mg", "1 mg (0.5 mg)"), r("Oxycodone", "5 mg-7.5 mg", ""), r("Fentanyl", "", "50 mcg"), r("Methadone", "About 1 mg", "")],
   source_flags=["Methadone 'about 1 mg' = 10 mg oral morphine is printed without noting that the ratio varies widely with dose; tramadol 50 mg ≈ morphine 10 mg is lower than usual (about 100 mg). Clinician to confirm."]),
 T("tbl-opioids-in-ckd", 291, PA + " > Opioids to use or to avoid with Chronic Kidney Disease",
   "Opioids in chronic kidney disease: which to use, reduce or avoid in mild-moderate vs advanced CKD", ["0836"],
   [[C("Opioid"), C("Mild to moderate CKD stages 1, 2, (3)"), C("Advanced CKD stages (3), 4, 5 (eGFR <30 mL/min)")]],
   [r("Codeine", "YES, reduced dose", "AVOID"), r("Tramadol", "YES, reduced dose", "Maybe (4), reduced dose"),
    r("Buprenorphine (3)", "YES", "YES, reduced dose"), r("Morphine", "YES, reduced dose", "AVOID"),
    r("Hydromorphone", "YES, reduced dose", "Use with caution, reduced dose"), r("Oxycodone", "YES, reduced dose", "AVOID (4)"),
    r("Fentanyl (1,2)", "YES (1)", "YES, reduced dose"), r("Methadone (1,2)", "YES (1,2)", "YES, with caution (1,2)")],
   footnotes=["(1) 2nd line. (2) Only to be used under palliative care or pain specialist supervision. (3) Not used much in palliative care settings. (4) Only very select cases."],
   source_flags=["The codeine row is split over two rows in the PDF ('Codeine' with empty cells, then 'YES, reduced dose | AVOID'); joined.",
                 "The mild-moderate column is headed '(eGFR >60 mL/min)' although it includes stage 3 (eGFR 30-59)."]),
 D("fig-palliative-care-trajectory-levels", 291, PA + " > Palliative Care in the Trajectory of the Patient's Illness",
   "Palliative care across the illness trajectory, and palliative care tasks by level (referral hospital, regional hospital, health centre/primary clinic, home)", ["0838", "0840", "0841"],
   "Trajectory (diagram): from presentation/diagnosis, therapies to modify disease (curative, restorative intent) decrease over time while therapies to relieve suffering and/or improve quality of life (palliative care) increase; palliative care continues through life closure and active dying to death, followed by bereavement care.\n\n"
   "Palliative care by level:\n"
   "- Referral hospitals: holistic assessment and reassessment; appropriate pain and symptom management; holistic care with specialised management (radiotherapy, chemotherapy, surgery).\n"
   "- Regional hospitals: holistic assessment and reassessment; appropriate pain and symptom management; initiate or adjust the PC regimen for mild, moderate or severe symptoms; plan continued PC after discharge to a lower level or home; refer to referral hospitals for specialised management.\n"
   "- Health centre/primary care clinic: visit the patient at home in the first week after discharge if possible; holistic pain assessment; pain and symptom management using the WHO ladder; emotional support; liaise with CHWs who visit patients at home; request oral morphine solution for PC patients in the HC catchment area; request advice from the regional hospital if needed; refer complicated cases to the regional hospital.\n"
   "- Home: recognise and report inadequately relieved pain or other physical, psychological or social distress, and improper use of morphine or other medicines; provide emotional support; educate the family on daily care (feeding, hygiene, mobility, medications)."),
 T("tbl-adjuvant-analgesics", 293, PM + " > Adjuvant Analgesics for Bone and Neuropathic Pain",
   "Adjuvant analgesics for bone and neuropathic pain: dexamethasone, amitriptyline, gabapentin, pregabalin: indications, doses and key notes", ["0844", "0845"],
   [[C("Class"), C("Indications"), C("Common Drugs & Doses"), C("Key Notes")]],
   [r("Steroids", "Pain caused by pressure (e.g. stretched liver capsule, raised ICP, Pancoast tumour)", "Dexamethasone: 8–16 mg once daily before noon; if effective, reduce by 2 mg/day after 3 days", "Stop after 5 days if no response"),
    r("Antidepressants", "Neuropathic pain", "Amitriptyline: 10–75 mg at night; start low, increase every 2–3 days until pain controlled or side effects limit use", "Sedating – useful at night; caution in elderly"),
    [C("Anticonvulsants", rs=2), C("Neuropathic pain", rs=2), C("Gabapentin: start 300 mg at night → increase by 300 mg every 2–3 days (night → BD → TDS → 600 mg BD); max 2400 mg/day; if no benefit after 900 mg/day, unlikely to be effective"), C("Titrate slowly to minimise dizziness & somnolence. Caution: renal impairment", rs=2)],
    r("Pregabalin: start 50 mg TDS or 75 mg BD; doses >300 mg/day rarely give extra benefit")],
   source_flags=["'&' is printed as 'C' (font substitution) in the title and cells."]),
]
