exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.254-255 (Chapter 10: Kaposi sarcoma). From the page images.
C10 = "Chapter 10: Management of Non-Communicable Diseases"
KS = C10 + " > 10.8 Kaposi Sarcoma"
ITEMS = [
 T("tbl-10.10-ks-symptoms", 254, KS + " > Clinical features of KS > Table 10.10", "Table 10.10 Symptoms of Kaposi Sarcoma", ["0699"],
   [r("Mild or Moderate Kaposi Sarcoma Disease", "Severe Symptomatic Kaposi Sarcoma Disease")],
   [[C("Symptoms may include:<br/>- Confined to skin and/or lymph nodes<br/>- No symptoms of visceral disease<br/>- The oral disease does not interfere with chewing or swallowing<br/>- Oedema is not significant and does not affect normal function<br/>- Condition not functionally disabling or immediately life-threatening"),
     C("Symptoms may include:<br/>- Symptomatic visceral disease (pulmonary¹ or gastrointestinal)²<br/>- Extensive oral Kaposi sarcoma lesions which interfere with chewing or swallowing<br/>- Painful or disabling tumour-associated facial/genital/peripheral oedema or ulcerated tumours<br/>- Life-threatening or functionally disabling disease<br/>- Progressive³ or persistent Kaposi sarcoma despite ART")]],
   footnotes=["¹ Symptomatic pulmonary Kaposi sarcoma, suggested by shortness of breath, haemoptysis or moderate/severe cough which cannot be attributed to other pulmonary conditions.",
              "² Symptomatic gastrointestinal Kaposi sarcoma, suggested by bleeding from mouth or rectum which cannot be attributed to other gastrointestinal conditions.",
              "³ Progressive disease is defined as an increase of 25% or more in the size of previously existing lesions and/or the appearance of new lesions or new sites of disease and/or a change in the character of 25% or more of the skin or oral lesions from macular to plaque-like or nodular. The development of new or increasing symptomatic tumour-associated oedema or effusion is also considered to represent disease progression."]),
 T("tbl-10.11-ks-aids-staging", 254, KS + " > Tumour staging criteria > Table 10.11", "Table 10.11 Staging Criteria and Prognosis for AIDS-Related Kaposi Sarcoma", ["0701"],
   [r("Criterion", "Good Prognosis (All of the Following)", "Poor Prognosis (Any of the Following)")],
   [r("Tumour (T)", "(T₀) Tumour confined to the skin and/or lymph nodes and/or minimal oral disease¹", "(T₁) Tumour-associated oedema or ulceration, extensive oral Kaposi sarcoma, gastrointestinal Kaposi sarcoma, Kaposi sarcoma in other non-nodal viscera"),
    r("Immune system (I)", "(I₀) CD4 count ≥200 cells/mm³ CD4 ≥20%", "(I₁) CD4 count <200 cells/mm³ CD4 <20%"),
    r("Systemic illness (S)", "(S₀) No history of opportunistic infections and/or thrush; absence of “B” symptoms²; Karnofsky performance status score ≥70", "(S₁) History of opportunistic infections and/or thrush; the presence of “B” symptoms²; Karnofsky's performance status score is <70 (See Annex 11.25)")],
   footnotes=["Adapted from Krown and colleagues (1989 & 1997).", "¹ “Minimal oral disease” is defined as non-nodular Kaposi sarcoma confined to the palate.",
              "² “B” symptoms: unexplained fever, drenching night sweats, >10% involuntary weight loss, or diarrhoea persisting for more than 2 weeks."]),
 T("tbl-10.12-classic-ks-staging", 255, KS + " > Kaposi sarcoma staging criteria > Table 10.12", "Table 10.12 Staging Criteria for Classic Kaposi Sarcoma", ["0703"],
   [r("Stage", "Cutaneous Lesions", "Localization", "Behaviour")],
   [r("I—Maculonodular", "Macules or nodules or both", "Lower limbs", "Non-aggressive"), r("II—Infiltrative", "Plaques", "Lower limbs", "Locally aggressive"),
    r("III—Florid", "Angiomatous nodules and plaques", "Extremities, particularly the lower ones", "Locally aggressive"),
    r("IV—Disseminated", "Angiomatous nodules and plaques", "Extremities, trunk, head", "Disseminated, aggressive")]),
 D("fig-10.3-ks-treatment", 255, KS + " > Figure 10.3", "Figure 10.3 Treatment Guidelines for Kaposi Sarcoma", ["0705"],
   "Confirmed KS branches into two types:\n"
   "- Endemic or sporadic type:\n   - Local or early stage (Stage I/II) → Radiotherapy or topical bleomycin chemotherapy\n   - Extensive stage (visceral involvement) (Stage II/IV, as printed) → Systemic chemotherapy\n"
   "- Second branch (printed again as 'Endemic or sporadic type'; by its T/I/S staging this is AIDS-related (epidemic) KS):\n   - Low risk disease (T₀, I₀, S₀) → ART alone and observe\n   - High risk disease (T₁, I₁, S₁) → ART plus chemotherapy",
   flags=["Figure 10.3 labels both branches 'Endemic or sporadic type'; the second branch (staged by T/I/S, managed with ART) is AIDS-related KS.",
          "Figure 10.3 gives the extensive stage as 'Stage II/IV' (printed 'Stgae'), overlapping the early stage 'Stage I/II'; likely Stage III/IV."]),
 T("tbl-10.13-ks-treatment", 255, KS + " > Table 10.13", "Table 10.13 Treatment of Kaposi Sarcoma", ["0707"],
   [r("Indication", "Regimen")],
   [r("First-line regimen", "Bleomycin 15 IU/m² IV D1 Vincristine 2 mg IV D1 Every 3 weeks for 6 cycles"),
    r("Second-line regimen/recurrent Kaposi sarcoma", "Paclitaxel 100 mg/m² * Every 3 weeks for 6–8 cycles Radiotherapy"),
    r("First-line regimen among clients with pulmonary Kaposi sarcoma and poor PS", "Vincristine 1.4 mg/m² IV D1<br/>Repeat cycle every week for 6 weeks then transfer to a first-line regimen.")],
   footnotes=["Printed without a header row; 'IVD1' in the source = IV on day 1. The asterisk after paclitaxel has no footnote in the source."]),
]
