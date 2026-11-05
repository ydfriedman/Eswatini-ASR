exec(open('batches/ncd_common.py').read())
TH = CH2 + " > Thyroid Disorders > Hyperthyroidism"
ITEMS = [
 T("tbl-antithyroid-drugs", 79, TH + " > Management of hyperthyroidism > Antithyroid drug therapy",
   "Antithyroid drug therapy for hyperthyroidism and thyroid storm: medicines, dosing and comments", ["0216"],
   [[C("Medicine"), C("Dosing"), C("Comment")]],
   [[C("Propylthiouracil* (D)"), C("500-1000 mg load, then 250 mg 4-hourly"), C("Blocks new hormone synthesis; blocks T4-to-T3 conversion. Breastfeeding clients: propylthiouracil (up to a maximum dose of 450 mg/day).")],
    [C("Carbimazole (C)"), C("40-60 mg/day"), C("Blocks new hormone synthesis. Breastfeeding clients: carbimazole (up to maximum 15 mg/day).")],
    [C("Propranolol (A)"), C("60-80 mg every 4 hours"), C("Consider invasive monitoring in congestive heart failure patients. Blocks T4-to-T3 conversion in high doses. Alternative medicine: esmolol infusion.")],
    [C("Iodine (saturated solution of potassium iodide) (B)"), C("5 drops (0.25 mL or 250 mg) (PO) 6-hourly"), C("Do not start until 1 hour after antithyroid medicines. Blocks new hormone synthesis; blocks thyroid hormone release.")],
    [C("Hydrocortisone (A)"), C("300 mg intravenous load, then 100 mg 8-hourly"), C("May block T4-to-T3 conversion. Prophylaxis against relative adrenal insufficiency. Alternative medicine: dexamethasone.")]],
   table_note="Note: in thyroid storm, propylthiouracil is preferred to carbimazole.",
   footnotes=["Letters A-D after each medicine are the evidence/medicine codes as printed. *No footnote for the asterisk on propylthiouracil is printed."],
   source_flags=["Propranolol is 'every 4 hours' here but 'q6h' / '6-h' in the thyroid storm table and flowchart (pp.82-83). Clinician to confirm."]),
 D("fig-tsh-ft4-interpretation", 80, TH + " > Treatment targets of hyperthyroidism > TSH and FT4/FT3 diagnostic flowchart",
   "Interpreting TSH and FT4/FT3 results (thyroid function test flowchart)", ["0218"],
   "Start with TSH.\n\n"
   "TSH low:\n"
   "- FT4 and/or FT3 high (printed 'Nor FT4 and/or FT3 high'): primary hyperthyroidism. Perform test for TRAb/TSI; consider ordering thyroid scintigraphy. Repeat TFT in four weeks to determine course or impact of treatment. Specialist referral*.\n"
   "- FT4 and FT3 normal*: subclinical/mild hyperthyroidism. Repeat TSH, FT4 and FT3 in 1-3 months; may require further investigation.\n"
   "- FT4 and/or FT3 low: discordant: non-thyroidal illness; central hypothyroidism. Repeat TSH, FT4 and FT3 and follow to assess trend; if persistently abnormal, refer for further investigation.\n\n"
   "TSH normal: thyroid dysfunction excluded.\n\n"
   "TSH high:\n"
   "- FT4 low: primary hypothyroidism. Repeat TSH and FT4; check anti-TPO; treat with levothyroxine.\n"
   "- FT4 normal: subclinical/mild hypothyroidism. Repeat in 1-3 months; check anti-TPO antibody; monitor TFT annually if stable; consider treatment with levothyroxine*.\n"
   "- FT4 high: discordant: TSHoma; thyroid hormone resistance; assay interference. Repeat TSH and FT4 to assess trend; refer for further investigation.",
   ["Asterisks in the flowchart have no footnote printed.", "This flowchart covers hypo- and hyperthyroidism but sits under 'Treatment targets of hyperthyroidism' in the source."]),
 T("tbl-burch-wartofsky-score", 81, TH + " > Emergencies in hyperthyroidism > Thyroid storm diagnosis: Burch-Wartofsky Point Scale (BWPS)",
   "Burch-Wartofsky Point Scale (BWPS) for diagnosis of thyroid storm: criteria, points and interpretation", ["0220", "0221"],
   [[C("Category"), C("Feature"), C("Criteria (points)"), C("Score range")]],
   [[C("Thermoregulatory dysfunction"), C("Temperature (°C)"), C("37.2-37.7: 5; 37.8-38.3: 10; 38.4-38.8: 15; 38.9-39.4: 20; 39.5-39.9: 25; ≥40.0: 30"), C("5-30")],
    [C("Central nervous system effects"), C("Manifestations"), C("Mild (agitation): 10; moderate (delirium, psychosis, extreme lethargy): 20; severe (seizure, coma): 30"), C("0-30")],
    [C("Gastrointestinal-hepatic dysfunction"), C("Symptoms"), C("Moderate (diarrhoea, nausea/vomiting, abdominal pain): 10; severe (jaundice): 20"), C("0-20")],
    [C("Cardiovascular dysfunction"), C("Tachycardia (bpm)"), C("90-109: 5; 110-119: 10; 120-129: 15; 130-139: 20; ≥140: 25"), C("5-25")],
    [C("Cardiovascular dysfunction"), C("Atrial fibrillation"), C("Present: 10"), C("0-10")],
    [C("Cardiovascular dysfunction"), C("Congestive heart failure"), C("Mild (pedal oedema): 5; moderate (bibasilar rales): 10; severe (pulmonary oedema): 15"), C("0-15")],
    [C("Precipitating event"), C("Trigger (e.g., infection, surgery, trauma, withdrawal of antithyroid drugs)"), C("Present: 10"), C("0-10")]],
   context_before="Thyroid storm/thyrotoxic crisis is a rare but potentially life-threatening syndrome of exaggerated hyperthyroidism: hyperthermia, severe tachycardia with or without cardiac failure, severe agitation, possible jaundice, and mental disorientation, culminating in stupor and coma.",
   table_note="Interpretation of total score: ≥45: thyroid storm highly likely; 25-44: impending storm; <25: thyroid storm unlikely.",
   source_flags=["The temperature criteria are printed as one run-on line ('37.2–37.7 → 5 37.8–38.3 → 10 3 8.4–38.8 → 15 ...'); split into bands."]),
 D("fig-thyroid-storm-management", 82, TH + " > Management of thyroid storm > Recognition and management (flowchart)",
   "Thyroid storm: recognition and management (flowchart)", ["0222", "0223", "0224"],
   "1. Suspect thyroid storm (BWPS ≥45).\n"
   "2. Identify precipitant(s).\n"
   "3. Initial stabilization (ABC). Propylthiouracil (PTU) or methimazole.\n"
   "4. Block thyroid hormone synthesis (≥ 1 h after ATD): Lugol's iodine 8 drops PO q6-8h, or NaI IV 0.25-0.5 g q6h.\n"
   "5. Block peripheral effects: propranolol 60-80 mg OG 6-hourly, or 1 mg IV q10min (max 3); hydrocortisone 100 mg IV q8h.\n"
   "6. Continuous monitoring & support: ECG, vitals, fluid balance, electrolytes. Adjust therapy as needed.\n\n"
   "In addition to general supportive measures, therapy should be directed at the thyroid gland and the hypermetabolism and tachycardia. Patients should be monitored in an intensive or high care setting. The underlying precipitant should be actively treated and managed. Prevention is key: correct thyroid function before elective surgery.",
   ["Step 4 is titled 'Block thyroid hormone synthesis' but describes iodine, which the table on p.83 places under 'Block hormone release'.", "'Identity precipitants' and 'Continuos' printed; corrected."]),
 T("tbl-thyroid-storm-treatment", 82, TH + " > Management of thyroid storm > Treatment steps and doses",
   "Thyroid storm treatment steps: therapeutic targets, drugs and doses", ["0225"],
   [[C("Step"), C("Therapeutic target"), C("Drug / intervention"), C("Dose / notes")]],
   [[C("Block thyroid hormone synthesis"), C("Antithyroid drugs (ATDs)"), C("Propylthiouracil (PTU): 500-1000 mg loading, then 250 mg q4h; preferred early as it inhibits T4-to-T3 conversion. Methimazole: 60-80 mg/day if PTU unavailable."), C("Start immediately on diagnosis")],
    [C("Block hormone release (give ≥1 hr after ATD)"), C("Iodine therapy"), C("Lugol's iodine: 8 drops q6-8h. Sodium iodide IV: 0.25-0.5 g q6h. Administer ≥1 hr after ATD to avoid iodine-fuelled synthesis."), C("Reduces preformed hormone release")],
    [C("Block peripheral effects"), C("Beta-blockade; corticosteroid therapy"), C("Propranolol: 60-80 mg PO q6h or 1 mg IV q10min (max 3 doses); esmolol IV infusion is an alternative in heart failure. Hydrocortisone: 100 mg IV q8h (reduces T4-to-T3 conversion and prevents adrenal crisis)."), C("Controls adrenergic effects; protects against adrenal failure")]],
   pages=[82, 83], source_flags=["Table continues onto p.83."]),
]
