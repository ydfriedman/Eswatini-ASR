exec(open('batches/ncd_common.py').read())
CC2 = CH9 + " > Childhood Cancers"; CR = CH9 + " > Colorectal Cancer"
def r(*v): return [C(x) for x in v]
ITEMS = [
 T("tbl-childhood-cancer-suspicious-features", 262, CC2 + " > Warning Signs of Childhood Cancer: suspicious clinical features",
   "Warning signs of childhood cancer: signs and symptoms with the clinical features that make them suspicious (pallor, fever, infections, lymphadenopathy, bleeding, headache, masses, bone pain and others)", ["0754", "0755", "0756", "0757"],
   [[C("Signs and Symptoms"), C("Suspicious Clinical Features")]],
   [r("Paleness, fatigue, and malaise", "Especially if persistent and associated with signs of bone marrow infiltration (unexplained fever, recurrent infections, bleeding diathesis) and/or lymphadenopathy"),
    r("Fever", "Prolonged (>2 weeks) without apparent cause, associated with weight loss, night sweats, paleness, petechiae, mass, bone pain and lymphadenopathy"),
    r("Recurrent or persistent infections", "Associated with paleness, petechiae, weight loss, bone pain, lymphadenopathy, hepatosplenomegaly or palpable mass"),
    r("Anorexia and weight loss", "Prolonged and unjustified, especially with other warning signs (recurrent infections, fever, paleness, lymphadenopathy, hepatosplenomegaly)"),
    r("Localized lymphadenopathy", "Persistent or progressive, not resolving in 4-6 weeks or unresponsive to antibiotics; size >2 cm, hard, painless, supraclavicular or epitrochlear"),
    r("Generalized or localized (lymphadenopathy)", "Associated with fever, night sweats, weight loss, malaise, paleness and hepatosplenomegaly"),
    r("Hemorrhagic manifestations (petechiae, ecchymosis, recurrent epistaxis, bleeding gums)", "Persistent or combined with other signs of bone marrow infiltration (paleness, fatigue, recurrent infections)"),
    r("Headache", "Recent onset, in the morning or waking the child at night, without a history of migraine, associated with vomiting or neurological symptoms (cranial palsy, motor or sensory signs), occipital location, worse when lying down"),
    r("Impaired school performance and mood changes", "Recent onset, progressive and not explained"),
    r("Palpable abdominal mass", "Any mass (except in the neonatal period) is suspicious for malignancy, especially with vomiting, abdominal pain, constipation, hematuria or hypertension"),
    r("Hepatomegaly", "Must always be investigated, even in asymptomatic cases"),
    r("Vomiting", "Persistent or recurring; associated with morning headache or abdominal mass"),
    r("Bone pain, arthralgia/arthritis, limp or refusal to walk", "Bone pain that wakes the child at night, duration >2 weeks, localized, associated with inflammation, no improvement with NSAIDs"),
    r("Back pain, kyphoscoliosis, lordosis and torticollis", "Back pain of sudden onset, age <4 years, worse at night, associated with fever or neurological symptoms, without trauma, not improving with NSAIDs"),
    r("Mass or lump in extremities, head, neck, or trunk", "Any palpable mass of recent appearance, deep to the fascia, not painful, hard, >2 cm in diameter and associated with regional lymphadenopathy"),
    r("Urinary retention/enuresis", "Recent; associated with neurological symptoms or abdominal mass"),
    r("Scrotal mass or swelling", "Recent; isolated right varicocele"),
    r("Swollen/bleeding gums", "Not explained"),
    r("Dermatological manifestations", "Eczema that does not respond to treatment; subcutaneous nodules")],
   footnotes=["NSAIDs: non-steroidal anti-inflammatory drugs."]),
 D("fig-childhood-cancer-referral", 263, CC2 + " > Childhood Cancer Referral Pathway",
   "Childhood cancer referral pathway: primary clinic identification, urgent referral, workup, MDT, confirmation, paediatric oncology", ["0758"],
   "1. Primary clinic (e.g. GP, school nurse): identify suspected cancer using the SILUAN signs (significant, unexplained, rapid onset, ongoing symptoms, night sweats).\n"
   "2. Urgent referral to a health centre/regional hospital.\n"
   "3. Initial workup and assessment: physical exam, blood tests, imaging as needed.\n"
   "4. Multidisciplinary team (MDT): paediatric oncologist, radiology, radiotherapy (as printed 'ratiology'), pathology, surgery.\n"
   "5. Confirmation of diagnosis.\n"
   "6. Referral to paediatric oncology for management (treatment planning, supportive care).",
   ["The chart expands SILUAN as 'Significant, Unexplained, Rapid onset, Ongoing, Night sweats', which does not match the SILUAN mnemonic on p.260. 'Night sweets', 'surgeology' printed."]),
 T("tbl-crc-risk-factors", 264, CR + " > Risk Factors for Colorectal Cancer",
   "Colorectal cancer risk factors: modifiable vs non-modifiable", ["0760"],
   [[C("Modifiable Risk Factors"), C("Non-modifiable Risk Factors")]],
   [r("Excess body fat", "Family history of colorectal cancer"), r("Sedentary lifestyle", "Advanced polyps"),
    r("Westernized diet including processed/pre-packed meats, fried foods, fast food etc.", "Polyposis syndrome (FAP, MAP)"),
    r("Processed meats", "Lynch syndrome (HNPCC)"), r("Red meats", "Black race"), r("Smoking", "Older age"), r("Alcohol", "Male gender")],
   footnotes=["CRC: colorectal cancer; FAP: familial adenomatous polyposis; HNPCC: hereditary non-polyposis colorectal cancer; MAP: MUTYH-associated polyposis."]),
]
