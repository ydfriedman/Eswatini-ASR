# Where the work paused

## Done and committed
- HIV Amendment 2024: all tables, boxes and flowcharts re-extracted (`hiv-amendment-2024_*`).
- NCDIMH part 1 (pp.1-89): 74 tables, boxes and flowcharts re-extracted (`ncdimh_*`, `batches/ncd_b01-b21.py`).
- Both are merged into `../chunks_v3` by `apply_reextraction.py`.

## In progress: NCDIMH text-chunk fixes for pp.1-89
1. **Labels.** `pdf_headings.py` proposes labels from the PDF's heading fonts; the proposals are in `ncdimh_text_label_proposals_p11-89.txt`. Use NEW unless corrected below (chapter prefix = "Chapter 1: Prevention, Health Education and Routine Health Examinations" for pp.11-30, "Chapter 2: Endocrinology" for pp.31-89):
   - 0013 Introduction · 0016 Screening for and Identifying Modifiable Risk Factors > Target Population for Screening
   - 0023/0025/0026 Referral Criteria and Follow-Up > Referral to Specialist Care / Documentation / Patient Education Priorities
   - 0030 Physical Inactivity > Screening for Physical Inactivity > Simple Screening Questions · 0031 Physical Inactivity > Health Consequences of Physical Inactivity · 0033 Physical Inactivity > Practical Recommendations: Low-Cost, Accessible Activities · 0034 Physical Inactivity > Special Considerations
   - 0039 Alcohol Use > Health Harms of Alcohol Use · 0040 Alcohol Use > Other Major Health Consequences · 0041 Alcohol Use > Screening for Alcohol Use > Who to Screen · 0046/0047/0048/0049 Alcohol Use > Special Populations > (Pregnant Women and Women of Childbearing Age / Patients Living with HIV / Patients on TB Treatment / Older Adults (≥65 years)) · 0050 Alcohol Use > Practical Strategies for Patients > Managing Cravings and Triggers
   - 0056 Routine Health Examinations: What to Look for When Assessing for NCDs · 0057 Routine Health Examinations > Hypertension · 0065 Routine Health Examinations > Lipids Disorders
   - 0074 Testing and Diagnosis of Diabetes > Criteria for Testing · 0101/0102 Insulin Therapy for Type 1 Diabetes > Insulin Requirements / Initiating Therapy in a Child Not in DKA · 0112/0113 Insulin Injection Technique > How to Inject Insulin with a Syringe / Recommended Sites for Insulin Injection · 0140 Hypoglycaemia · 0150 Glycemic Control in Non-Critical Hospitalized Adult Patients Protocol > Correction/Sliding Scale: Selection of Low, Medium or High Insulin Dose
   - 0159/0160 Diabetes > Diet Education > Vegetables / Salad: Half Your Plate / Fats: Use Oils Sparingly · 0161 Diabetes > Follow-up (At Every Visit, 3-6 Monthly, Annually)
   - 0198 Thyroid Disorders > Hypothyroidism > Diagnosis · 0202 Management of Hypothyroidism > Complications & Emergencies (Myxoedema Coma) · 0203/0205/0206/0207 Congenital Hypothyroidism > Description / Investigations / Pharmacological Treatment / Referral · 0208/0210 Hypothyroidism in Older Children and Adolescents > Clinical Features / Referral
   - 0217 Management of Hyperthyroidism > Radioactive Iodine · 0219 Emergencies in Hyperthyroidism > Thyroid Storm/Thyrotoxic Crisis > Clinical Presentation · 0226-0229, 0232 Hyperthyroidism in Pregnancy > Introduction / Causes: Transient Gestational Hyperthyroidism / Causes: Graves' Disease / Diagnosis / Treatment and Monitoring
   - 0234/0235/0239 Cushing's Syndrome > Symptoms and Signs / Common Presenting Symptoms / Treatment: Medical Therapy
2. **Orphan fragments** (text chunks under 60 tokens on pp.1-89): attach each to its table or flowchart, or merge it into the neighbouring text chunk.
3. **Trailing headings:** move a heading at the end of a chunk to the start of the next chunk.
4. **Embedding noise:** strip escaped asterisks and "image:/icon:/photo:" lines from `embed_text` (keep them in `text`).
5. Then re-run `apply_reextraction.py`, check (unique ids, headers, neighbours, <512 tokens), and commit.

## Next after that
NCDIMH parts 2-5 (the user uploads them one at a time). Then the other guidelines. Keep a running "source issues" list from each item's `source_flags`.
