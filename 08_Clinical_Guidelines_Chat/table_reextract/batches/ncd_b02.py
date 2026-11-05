exec(open('batches/ncd_common.py').read())
OA = "Oral agents used in the management of type 2 diabetes: doses, frequency, side effects and contraindications"
ITEMS = [
 D("fig-t2dm-pharmacological-treatment", 34, CH2 + " > Management of Type 2 Diabetes in Outpatient > Type 2 diabetes pharmacological treatment",
   "Type 2 diabetes pharmacological treatment (flowchart, by HbA1c)", ["0079", "0080", "0081"],
   "Newly diagnosed type 2 DM patient: check HbA1c. Health promotion for all (disease, medication adherence, nutrition, behaviour), individual and group.\n\n"
   "By HbA1c at diagnosis:\n"
   "- HbA1c <7%: lifestyle modification; recheck HbA1c in 6 months.\n"
   "- HbA1c 7-8% (printed '<7%-8%'): start metformin [note 1]: 1. 500 mg OD; 2. recheck HbA1c in 3 months; 3. increase dose every 3 months until at goal or maximum tolerated dose.\n"
   "- HbA1c 8-9.9% (printed '<8%-9.9%'): consider dual therapy: 1. start metformin 500 mg OD and titrate every 2 weeks to a maximum of 2 g if tolerated; 2. add a second drug (sulfonylurea, DPP-4 inhibitor, pioglitazone, GLP-1 agonists or SGLT-2 inhibitors).\n"
   "- HbA1c >10%: consider insulin: consider starting the patient on insulin therapy alone or in combination with metformin (consult physician). Start at low-dose insulin and increase until target reached.\n\n"
   "Follow-up after lifestyle modification or metformin:\n"
   "- HbA1c <7%: 1. continue current medication; 2. recheck HbA1c in 6 months; 3. fasting blood glucose every 3 months.\n"
   "- HbA1c >7%: 1. add a second OGLA, e.g. sulfonylurea, DPP-4 inhibitor, pioglitazone, GLP-1 agonists or SGLT-2 inhibitors; 2. recheck HbA1c in 3 months; 3. increase the dose of the second agent until glycaemic target reached, or maximum dose. If HbA1c remains >8%, review with physician and consider referral to the diabetes clinic for insulin management.\n\n"
   "T2DM diagnosis criteria: 1. FPG > 7.0 mmol/L; 2. random glucose > 11.1 mmol/L; 3. need two positive tests, one must be FBG.\n"
   "For older patients, it is reasonable to set the HbA1c goal at < 8%.\n\n"
   "[note 1] Caution: metformin use in patients with reduced kidney function: 1. do not start new patients on metformin if CrCl < 45 ml/min; 2. continue metformin if already on it and CrCl is 30-45 ml/min, but repeat CrCl in 6 months; 3. stop metformin if CrCl < 30 ml/min.",
   ["HbA1c bands are printed '<7%', '<7%-8%', '<8%-9.9%', '>10%'; read as <7, 7-8, 8-9.9, >10 (10.0 itself is not covered).",
    "The diagnosis criteria here (FPG > 7.0, two positive tests) differ slightly from the diagnosis box on p.22 (FPG ≥ 7.0, HbA1c ≥ 6.5%)."]),
 T("tbl-oral-glucose-lowering-agents", 35, CH2 + " > Management of Type 2 Diabetes in Outpatient > Oral agents used in the management of type 2 diabetes",
   OA, ["0082", "0083", "0084", "0085", "0086", "0087"],
   [[C("Name of drug"), C("Minimum dose"), C("Max daily dose"), C("Frequency"), C("Major side effects"), C("Contraindications / use with caution")]],
   [{"section": "A. Sulphonylureas. Mechanism of action: stimulate the pancreas to release insulin (regardless of time and glucose levels)"},
    [C("Glibenclamide"), C("2.5 mg"), C("15 mg"), C("OD or BD"), C("Hypoglycemia, weight gain, skin rashes"), C("Caution in liver and renal disease")],
    [C("Gliclazide MR"), C("30 mg"), C("120 mg"), C("OD"), C("Hypoglycemia, weight gain, skin rashes"), C("Pregnancy; caution in liver disease")],
    [C("Glimepiride"), C("1 mg"), C("4 mg"), C("OD"), C("Hypoglycemia, weight gain, skin rashes"), C("Pregnancy; caution in liver and renal disease")],
    [C("Glipizide"), C("5 mg"), C("40 mg"), C("OD or BD"), C("Hypoglycemia, weight gain, skin rashes"), C("Pregnancy; caution in liver and renal disease")],
    {"section": "B. Biguanide. Mechanism of action: (i) reduce glucose production in liver; (ii) cause (mild) reduction in peripheral insulin resistance"},
    [C("Metformin"), C("500 mg"), C("2000 mg"), C("OD or BD"), C("Abdominal pain, nausea, loose bowel motions, lactic acidosis; vitamin B12 deficiency with prolonged use"), C("Renal failure, GFR <30 ml/min; heart failure stage 3 or 4; liver failure")],
    {"section": "C. Thiazolidinediones. Mechanism of action: (i) improved insulin sensitivity in muscle, adipose tissue and liver; (ii) reduce glucose output from liver; (iii) change fat distribution by decreasing visceral fat and increasing peripheral fat"},
    [C("Pioglitazone"), C("15 mg"), C("45 mg"), C("OD"), C("Liver impairment, fluid retention, weight gain, dilutional anemia, osteoporosis"), C("Heart failure and liver failure; pregnancy; bone fractures")],
    {"section": "D. Meglitinides. Mechanism of action: stimulate pancreas to release more insulin (possibly related to blood glucose level)"},
    [C("Repaglinide"), C("1.0 mg"), C("16 mg"), C("BD, TDS or QID (before meals)"), C("Liver impairment, fluid retention, weight gain, dilutional anemia"), C("")],
    {"section": "E. Alpha glucosidase inhibitors. Mechanism of action: slow digestion of complex sugars (sucrose and starch), delaying absorption and the post-meal rise in blood glucose"},
    [C("Acarbose"), C("25 mg"), C("300 mg"), C("TID (during meal)"), C("Dyspepsia, loose bowel motions, flatulence"), C("None")],
    {"section": "F. DPP-4 inhibitors (gliptins). Mechanism of action: improve pancreatic islet glucose sensing, increasing glucose-mediated insulin secretion and suppressing glucagon secretion"},
    [C("Vildagliptin"), C("50 mg"), C("100 mg"), C("OD or BD"), C("Urticaria, angioedema, and immune mediated dermatologic effects. Acute pancreatitis. Risk of hypoglycemia", rs=4), C("Pancreatitis; allergy, pregnancy, lactation; caution with heart failure (saxagliptin)", rs=4)],
    [C("Sitagliptin"), C(""), C("100 mg"), C("OD")],
    [C("Saxagliptin"), C("5 mg"), C("10 mg"), C("OD")],
    [C("Linagliptin"), C("5 mg"), C("5 mg"), C("OD")],
    {"section": "G. SGLT-2 inhibitors. Mechanism of action: suppress renal glucose reabsorption by blocking the sodium-glucose co-transporter 2 (SGLT-2), increasing urinary glucose excretion"},
    [C("Canagliflozin"), C("100 mg"), C("300 mg"), C("OD"), C("Polyurea, UTI, DKA, genital candidiasis, hypotension", rs=3), C("Renal failure (action dependent on normal GFR), or sensitivity to active ingredients or its excipients", rs=3)],
    [C("Dapagliflozin"), C("5 mg"), C("10 mg"), C("OD")],
    [C("Empagliflozin"), C("10 mg"), C("25 mg"), C("OD")]],
   pages=[35, 36], source_flags=["Table continues onto p.36 (sections F and G).",
     "Side effects and contraindications for DPP-4 inhibitors and for SGLT-2 inhibitors are single cells spanning all drugs in the class.",
     "Sitagliptin has no minimum dose printed."]),
 T("tbl-t2dm-pharmacotherapy-progression", 36, CH2 + " > Management of Type 2 Diabetes in Outpatient > Pharmacotherapy progression in type 2 diabetes",
   "Pharmacotherapy progression in type 2 diabetes (monotherapy to triple therapy and insulin)", [],
   [[C("Stage"), C("Regimen"), C("Guidance")]],
   [[C("Monotherapy"), C("Metformin is the drug of first choice at diagnosis."), C("Continue until contraindicated or not tolerated. If metformin is contraindicated or not tolerated, use gliclazide. For patients with established cardiovascular disease intolerant to metformin, consider SGLT2 inhibitor or GLP-1RA (under specialist care).")],
    [C("Initial dual therapy"), C("Metformin + gliclazide"), C("Consider if the patient has symptomatic hyperglycaemia and HbA1c >9% at diagnosis. Review gliclazide continuation once metformin dose and lifestyle interventions are optimized.")],
    [C("Dual therapy"), C("Add a second agent if target not achieved with monotherapy"), C("Options to add: gliclazide, DPP-4 inhibitor, pioglitazone, or SGLT2 inhibitor. Consider comorbidities, ability to access medicines, and properties of each drug. Fixed-dose combinations (e.g., DPP-4 inhibitor + metformin) may offer compliance and cost advantages.")],
    [C("Triple therapy"), C("Add a third oral agent or an injectable agent"), C("Consider if HbA1c is above individualized target (typically <7% for most) with two oral agents. Injectable options: GLP-1RA or basal insulin. Do NOT combine: GLP-1RA with DPP-4 inhibitor; GLP-1RA with SGLT2 inhibitor; pioglitazone with insulin.")],
    [C("Triple therapy (insulin)"), C("Add a third oral agent or an injectable agent."), C("For patients on three oral agents who are still not at target. Other oral agents can be stopped upon initiation of premix insulin.")]],
   source_flags=["The last row is printed 'Triple Therapy' a second time; its guidance is about starting premix insulin.",
                 "The old chunks for this page repeated the DPP-4/SGLT-2 rows instead of this table; this table was missing from the chunk set."]),
 T("tbl-insulin-indications-t2dm", 37, CH2 + " > Insulin Therapy in Type 2 Diabetes > Indications and timing for insulin",
   "Insulin therapy in type 2 diabetes: indications, when to initiate, and good practice", ["0089", "0090"],
   [[C("Indications for insulin"), C("When should insulin be initiated?"), C("Good practice")]],
   [[C("Poor glycaemic control: HbA1c still [above target] despite previous attempts to improve with lifestyle modification and maximum oral therapy. Patient is symptomatic (weight loss, polyuria, polydipsia, recurrent infections). Steroid-induced diabetes. Patient unable to tolerate or has contraindication to OGLAs. Gestational diabetes or diabetes in pregnancy not controlled on OGLAs. Painful neuropathy. Foot ulceration and infection."),
     C("As soon as there is evidence of sub-optimal glycaemic control. After reviewing the patient's ability to change their lifestyle and medication concordance. Following a full discussion with the patient that includes identifying barriers to insulin initiation, e.g. occupational issues, fear of weight gain, fear of hypoglycaemia and fear of injections."),
     C("Insulin initiation should be part of a structured educational programme for the patient, and competent health care staff should have sufficient time for initiation and follow-up until glycaemic control is optimized. The decision to start insulin should be made in partnership with the person, and the choice of regimen should cater for individual needs. The person initiating insulin should be trained and competent to do so in line with the national guidelines, and should consult with the physician/diabetologist. Ensure educational materials and support literature are available for the patient starting insulin. Patients requiring insulin prior to pregnancy should be referred to the gynaecologist.")]],
   context_before="Diabetes is a progressive condition, and many patients with type 2 diabetes eventually require and benefit from insulin therapy.",
   source_flags=["The PDF prints 'HbA1c still despite previous attempts'; a word is missing ('[above target]' added)."]),
]
