exec(open('batches/ncd_common.py').read())
CK = CH7 + " > Chronic Kidney Disease"
def act(*xs): return [C(x) for x in xs]
ITEMS = [
 T("tbl-ckd-complications", 218, CK + " > Complications of Chronic Kidney Disease",
   "Complications of CKD by body system: symptoms and pathophysiology (CNS, peripheral nerves, skin, musculoskeletal, GI, genitourinary, immune)", ["0624"],
   [[C("System"), C("Symptom"), C("Pathophysiology")]],
   [act("Central Nervous System", "1. Uraemic encephalopathy<br/>2. Seizures", "1. Uraemic toxins<br/>2. From uremic encephalopathy, or CKD-related hypoglycemia, hypocalcemia, or hypertensive emergency"),
    act("Peripheral Nervous System", "Peripheral neuropathy", "Uremic toxins"),
    act("Dermatology", "Pruritus; leukonychia; half and half nails; dry skin; pallor", "Uremic toxins stimulate histamine release with stimulation of prurigenic receptors in the skin, and transmission to the thalamus via the spinal cord"),
    act("Musculoskeletal", "Renal osteodystrophy", "Secondary and tertiary hyperparathyroidism"),
    act("Gastrointestinal", "Dyspepsia", "Hypergastrinemia from reduced renal excretion – with uremic gastritis"),
    act("Genitourinary", "Impotence; oligo-amenorrhea", "Hyperprolactinemia, raised luteinizing hormone"),
    act("Immune system", "Susceptibility to infection", "Uremia causes immune dysfunction")],
   pages=[218, 219], source_flags=["Table continues onto p.219 with the header repeated."]),
 T("tbl-ckd-glucose-lowering-agents", 220, CK + " > CKD and Diabetes > Glucose-lowering agents in CKD",
   "Glucose-lowering agents in CKD and type 2 diabetes compared: effect on CKD progression, ASCVD, heart failure, glucose-lowering efficacy, hypoglycaemia risk, weight and cost", ["0628", "0629", "0630"],
   [[C("Agent"), C("Progression of CKD"), C("ASCVD"), C("Heart Failure"), C("Glucose-lowering efficacy"), C("Hypoglycemia risk"), C("Weight effects"), C("Cost")]],
   [act("Metformin", "Neutral", "Potential benefit", "Potential benefit", "High", "Low", "Neutral", "Low"),
    act("SGLT2 inhibitors", "Benefits (a)", "Benefits (c)", "Benefits", "Intermediate", "Low", "Loss", "High"),
    act("GLP-1 receptor agonists", "Benefits (b)", "Benefits (c)", "Potential benefits", "High", "Low", "Loss", "High"),
    act("DPP-4 inhibitors", "Neutral", "Neutral", "Potential risk (c) (saxagliptin)", "Intermediate", "Low", "Neutral", "High (analogs)"),
    act("Insulin", "Neutral", "Neutral", "Neutral", "Highest", "High", "Gain", "Low (human)"),
    act("Sulfonylureas", "Neutral", "Neutral", "Neutral", "High", "High", "Gain", "Low"),
    act("Thiazolidinediones", "Neutral", "Potential benefit (pioglitazone)", "Increased risk", "High", "Low", "Gain", "Low"),
    act("α-Glucosidase inhibitors", "Neutral", "Neutral", "Neutral", "", "Low", "Neutral", "Low")],
   footnotes=["Colour key in the PDF: neutral; potential benefit or intermediate glucose-lowering efficacy; benefits (organ protection, high efficacy, low hypoglycemia risk, weight loss, or low cost); potential risk or high cost to patient; increased risk of adverse effects.",
              "(a) Benefit supported by primary and secondary outcome data. (b) Benefit supported by secondary outcome data. (c) Benefit or risk is agent specific.",
              "ASCVD, atherosclerotic cardiovascular disease; CKD, chronic kidney disease; DPP-4, dipeptidyl peptidase 4; GLP-1, glucagon-like peptide 1; SGLT2, sodium-glucose cotransporter-2; T2D, type 2 diabetes."],
   context_before="Glucose-lowering agents usable in CKD: metformin up to eGFR ≥30 ml/min/1.73 m2 (lactic acidosis reported with lower eGFR; reduces CV risk; check B12 after 4 years). SGLT2 inhibitors (dapagliflozin, empagliflozin) are recommended in diabetic and non-diabetic kidney disease to slow CKD progression; can be used in CKD4. GLP1-RAs are cardioprotective and reduce albuminuria and GFR decline in diabetic kidney disease; some can be used in CKD4. Non-renally cleared sulphonylureas such as gliclazide may be used cautiously (hypoglycaemia still possible). DPP4 inhibitors can be used in CKD1-5; thiazolidinediones (some agents) in CKD1-5; alpha glucosidase inhibitors up to CKD3b. Glucose may 'normalize' in advanced diabetic nephropathy.",
   source_flags=["The footnote markers in the table are letters (a-c) but the footnotes are numbered 1-3; matched in order.", "α-glucosidase inhibitors have no glucose-lowering efficacy printed."]),
 T("tbl-ckd-pregnancy-effects", 221, CK + " > Management in Special Populations > (h) CKD in pregnancy",
   "CKD in pregnancy: maternal effects and effects on the foetus; pre-eclampsia risk reduction (aspirin, calcium)", ["0633"],
   [[C("Maternal effects of CKD"), C("Effects of CKD on foetus")]],
   [[C("- Worsening of kidney function (higher risk if worse baseline kidney function, GFR <40 ml/min/1.73 m² and proteinuria >1 g/d; less if mild with little or no proteinuria and normal BP)<br/>- Proteinuria (which can worsen kidney disease)<br/>- Hypertension with risk of pre-eclampsia"),
     C("- Intra-uterine growth retardation (IUGR) = low nephron mass = future risk of kidney disease & hypertension in baby<br/>- Pre-term deliveries<br/>- Teratogenicity (RAAS inhibitors)")]],
   context_before="CKD in pregnancy requires co-management by an obstetrician and a nephrologist.",
   table_note="Pre-eclampsia risk reduction in CKD: aspirin 81-150 mg OD (increases vascular relaxant prostacyclin and reduces thrombogenic/vasoconstrictive thromboxane A2; trials suggest some benefit); calcium 1.5-2 g daily may help those with low calcium levels."),
]
GN = CH7 + " > Glomerular Disease"
ITEMS += [
 T("tbl-paeds-ckd", 222, CK + " > Management in Special Populations > (k) CKD in Paediatric Population",
   "CKD in children: definition, key points, and major causes under and over 5 years of age", ["0636", "0637"],
   [[C("In < 5 years of age"), C("In > 5 years of age")]],
   [[C("Congenital malformations: hypoplastic/dysplastic kidneys; reflux nephropathy; obstructive uropathy; posterior urethral valves"), C("Glomerular disease: focal segmental glomerulosclerosis; hemolytic uremic syndrome; chronic glomerulonephritis; Alport's syndrome")],
    [C("Metabolic/genetic disorders: oxalosis; polycystic kidney disease; congenital nephrotic syndrome; Wilms' tumor"), C("Tubulointerstitial disease: chronic tubulointerstitial nephritis; cystinosis; nephronophthisis; nephrotoxic drugs")]],
   context_before="Definition of CKD in children: (1) kidney damage for ≥3 months, shown by structural or functional abnormalities of the kidney, with or without decreased GFR, with one or more of: abnormalities in the composition of the blood or urine; abnormalities in imaging tests; abnormalities on kidney biopsy; or (2) GFR <60 mL/min/1.73 m² for ≥3 months, with or without other signs of kidney damage. Recognise children in the early stages of CKD; regular monitoring allows control of factors that aggravate progression. The main treatable causes of CKD in children in developing countries are urinary tract abnormalities, acute kidney injury and nephrotic syndrome. Identify the cause to plan management and prognosis. Major causes are congenital abnormalities of the kidney and urinary tract, reflux nephropathy, inherited disorders, glomerular diseases, renal stones, secondary to AKI, and haemolytic uraemic syndrome/thrombotic microangiopathy."),
 T("tbl-ckd-contrast-media", 223, CK + " > CKD and Contrast Media",
   "CKD and contrast media: effect on the kidneys and management for gadolinium (nephrogenic systemic fibrosis), iodinated contrast, and acute phosphate nephropathy", ["0638", "0639"],
   [[C(""), C("Gadolinium"), C("Radioiodine contrast media"), C("Acute phosphate nephropathy")]],
   [[C("Exposure"), C("Gadolinium-based contrast agents (MRI scans)"), C("Iodinated contrast"), C("Exposure to high phosphorus levels in the presence of renal insufficiency. Usually reported following bowel preparation (e.g. for colonoscopy) with sodium phosphate containing solutions")],
    [C("Effect on Kidneys"), C("Nephrogenic systemic fibrosis: a fibrosing disorder of the skin and viscera/systemic organs, secondary to gadolinium-based contrast agents in patients with acute and chronic renal insufficiency. First reported in patients with ESRD and AKI in 2006 (gadolinium is excreted unchanged by the kidneys)"),
     C("Direct toxic effect on renal tubules, disrupting mitochondrial function, with generation of free radicals, causing apoptosis. Vasoconstriction, reducing blood flow through the medulla, with resultant ischaemia"),
     C("Acute presentation with severely elevated serum phosphorus levels and AKI. Gradual worsening of renal function over weeks and months. Renal biopsy shows tubulointerstitial calcium and phosphorus deposition and damage")],
    [C("Management"), C("Avoid in CKD stage G5, but some risk in G4. If needed, counsel the patient and arrange dialysis immediately after the procedure and for up to 2 days after (based on gadolinium pharmacokinetics) to remove the gadolinium"),
     C("Hold exacerbating drugs on the day of use, e.g. metformin, diuretics. Pre- and post-hydrate with normal saline 1 ml/kg/hour or 100 ml/hour for 3-12 hours before and after contrast (lower rates if risk of pulmonary oedema). Use low-volume contrast that is not hyper-osmolar"),
     C("")]]),
 D("fig-gn-classification", 224, GN + " > Classification of Acute Glomerulonephritis",
   "Classification of glomerulonephritis: non-proliferative (minimal change, membranous, FSGS) vs proliferative (IgA, membranoproliferative, RPGN, post-infectious, vasculitic, Goodpasture's), features and treatment", ["0642", "0643"],
   "Glomerulonephritis is classified as non-proliferative (these tend to cause nephrotic syndrome) or proliferative.\n"
   "A. Non-proliferative:\n"
   "- Minimal change glomerulonephritis: abnormal podocytes seen on electron microscopy. Treat with supportive care + prednisolone; most respond well.\n"
   "- Membranous glomerulonephritis (MGN): thickened glomerular basement membrane; usually idiopathic. 1/3 have chronic MGN, 1/3 go into remission, 1/3 progress to renal failure.\n"
   "- Focal segmental glomerulosclerosis: segments of glomeruli develop sclerosis; presents with nephrotic syndrome; genetic causes identified; steroids often ineffective; 50% progress to renal failure.\n"
   "B. Proliferative:\n"
   "- IgA nephropathy: most common type of GN in adults; macroscopic haematuria appearing 24-48 hrs after URTI/GI infection; IgA deposits seen in the mesangial matrix.\n"
   "- Membranoproliferative glomerulonephritis: primary (immune mediated) or secondary (SLE, hepatitis); usually progresses to end-stage renal failure.\n"
   "- Post-infectious glomerulonephritis: occurs weeks after URTI, usually Strep pyogenes; supportive treatment; resolves over 2-4 weeks.\n"
   "- Rapidly progressive (crescentic) glomerulonephritis:\n"
   "  - Vasculitic disorders: Wegener's granulomatosis (vasculitis of lungs, kidney and other organs; c-ANCA positive; treat with steroids + cyclophosphamide); microscopic polyangiitis (small vessel vasculitis; p-ANCA positive; treat with long-term steroids +/- cytotoxic agents).\n"
   "  - Goodpasture's syndrome: autoimmune, anti-GBM antibody; glomerulus and lung affected; haematuria and haemoptysis; treat with steroids +/- steroid-sparing agents.",
   ["'Trear', 'Polyangitis', '+ye' printed."]),
 T("tbl-nephrotic-vs-nephritic", 224, GN + " > Comparison Table of Nephritic and Nephrotic Syndrome",
   "Nephrotic vs nephritic syndrome compared: characteristics, symptoms, proteinuria, haematuria, red cell casts, causes", ["0644"],
   [[C(""), C("Nephrotic Syndrome"), C("Nephritic Syndrome")]],
   [[C("Characteristics"), C("- Low serum albumin (<30 g/L)<br/>- Proteinuria (>3.5 g/day)<br/>- Oedema<br/>- Dyslipidemia<br/>- Hypercoagulability (loss of antithrombin III)<br/>- Reduced immunity (loss of immunoglobulins)"),
     C("- Hematuria: may have dysmorphic red cells (damaged during transit through the damaged glomerular filtration barrier), red cell casts, or granular casts (denatured cells stuck onto tubular proteins)<br/>- Hypertension<br/>- Mild proteinuria (<3.5 g/day)<br/>- Mild oedema<br/>- Temporary oliguria and uraemia")],
    [C("Symptoms"), C("Peripheral oedema (adults), facial oedema (children), frothy urine, fatigue, recurrent infections"), C("Haematuria (frank/microscopic), mild oedema, oliguria, signs of uraemia (fatigue, pruritus, nausea)")],
    [C("Proteinuria"), C("++++"), C("++")],
    [C("Haematuria"), C("May or may not be present"), C("+++")],
    [C("Red Blood Cell Casts"), C("Absent"), C("Present")],
    [C("Causes"), C("- Minimal change disease (most common in children)<br/>- Membranous nephropathy (most common in adults)<br/>- Focal segmental glomerulosclerosis"),
     C("- IgA nephropathy<br/>- Post-streptococcal glomerulonephritis (always check acute rheumatic fever patients)<br/>- Rapidly progressive glomerulonephritis (RPGN): anti-GBM; ANCA vasculitis")]],
   source_flags=["'Focal segmental glomerulonephritis' printed (glomerulosclerosis)."]),
]
