exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.249-252 (Chapter 10: dyslipidaemia, depression, antipsychotics, mood stabilizers). From the page images.
C10 = "Chapter 10: Management of Non-Communicable Diseases"
LP = C10 + " > 10.5 Care and Management of Dyslipidaemia and HIV"
DP = C10 + " > 10.6 Care and Management of Depression and HIV"
ITEMS = [
 D("fig-10.2-dyslipidaemia-evaluation", 249, LP + " > Figure 10.2", "Figure 10.2 Evaluation of clients with dyslipidaemia and HIV infection", ["0685"],
   "Flow (top to bottom):\n1. Dyslipidaemia and HIV infection confirmed; LDL >160 mg/dL (4 mmol/L); TG >400 mg/dL. Refer to the practice guide for management of dyslipidaemia.\n"
   "↓\n2. Use pravastatin or atorvastatin until LDL is below 100 mg/dL (2 mmol/L). Counsel for lifestyle modification. Use gemfibrozil for isolated increase of TG.\n"
   "↓\n3. Monitor for blood sugar control and prevent end organ damage:\n- Blood glucose should be below 10 mmol/L\n- HbA1c should be below 7%\n"
   "- Annual eye examination is needed, and additional risk factors like dyslipidaemia and hypertension should be managed properly; refer to specific practice guides.\n\n"
   "Key message (box below the figure): Simvastatin and Lovastatin should not be used with protease inhibitors because of the risk for rhabdomyolysis. However, atorvastatin or pravastatin are safe to use concurrently with protease inhibitors.",
   flags=["The last box of Figure 10.2 repeats the diabetes monitoring targets of Figure 10.1 (blood glucose, HbA1c) rather than lipid monitoring.",
          "Figure 10.2 pairs LDL 100 mg/dL with 2 mmol/L; 100 mg/dL is about 2.6 mmol/L (2 mmol/L is about 77 mg/dL)."]),
 T("tbl-10.6-lipid-lowering-drugs", 250, LP + " > Table 10.6", "Table 10.6 Pharmacotherapy and Drug Information for Treatment of Hyperlipidaemia", ["0687"],
   [r("Drug Name and Class", "Starting Dose", "Maximal Dose")],
   [r("Atorvastatin*", "10 mg/day", "80 mg/day"), r("Simvastatin*", "20 mg/day", "40 mg/day"), r("Lovastatin", "20 mg/day", "80 mg/day"),
    r("Pravastatin", "40 mg/day", "80 mg/day"), r("Fluvastatin", "20 mg/day", "80 mg/day"), r("Rosuvastatin", "10 mg/day", "40 mg/day")],
   footnotes=["*Available in the Eswatini National Essential Medicines List as lipid-lowering agents."],
   context_before="HMG-CoA reductase inhibitors (statins) are indicated for patients with elevated LDL-C. Common side effects include joint and muscle pain with elevated transaminases.",
   source_flags=["Table 10.6 lists simvastatin (on the Essential Medicines List) and lovastatin without a warning, but the box above says simvastatin and lovastatin should not be used with protease inhibitors (rhabdomyolysis)."]),
 T("tbl-10.7-depression-management", 251, DP + " > Pharmacological Management of Depression > Table 10.7", "Table 10.7 Clinical Diagnosis and Recommendations for Management of Depression", ["0690"],
   [r("Clinical Diagnosis", "Recommendation")],
   [r("Depression only", "Use antidepressants (see Table 10.8 below)"),
    r("Depression with psychotic features", "Use antidepressants + antipsychotic drugs"),
    r("Bipolar affective disorder, (depressive phase)", "Use a mood stabilizer + antidepressants (add an antipsychotic drug if the client has psychotic features)."),
    [C("If the client presents with persistent insomnia, consider Lorazepam tablet (1 mg at night) or Promethazine (25–50 mg at night). Use of Lorazepam should not exceed 2 weeks; antidepressants with some sedation effect can be substituted. Avoid DTG at night; it is advisable to take it in the morning to avoid sleep deprivation.", cs=2)]]),
 T("tbl-10.8-antidepressants", 251, DP + " > Pharmacological Management of Depression > Table 10.8", "Table 10.8 Drugs used to treat depression", ["0691"],
   [r("Antidepressant Tablets", "Initial Dosage", "Max Dose/Day", "Indication")],
   [{"section": "Tricyclic Antidepressants (TCA)"},
    [C("Amitriptyline"), C("25 mg for 3/7, then 50 mg every night for 14 days then review"), C("200 mg/day (increase dose by 25 mg at a time)"), L("If sedation is desirable", "Pregnant women", "Breastfeeding mothers")],
    {"section": "Selective Serotonin Reuptake Inhibitors (SSRIs)"},
    [C("Fluoxetine"), C("20 mg/day preferably in the morning"), C("60–80mg /day (increase dose by 20 mg at a time)"),
     C(L("If sedation is not desirable", "Depression with suicide ideas/ attempt", "Elderly and children", "Physically ill clients; HIV with opportunistic infections, poorly controlled diabetes mellitus and hypertension, etc.")["t"], rs=2)],
    r("Sertraline", "50 mg/day", "200 mg/day (increase dose by 50 mg at a time)")],
   footnotes=["The indication cell is shared by fluoxetine and sertraline."]),
 B("box-antidepressant-arv-interactions", 251, DP + " > Drug Interactions: Antidepressants and ARVs", "Drug Interactions: Antidepressants and ARVs", [],
   "Drug interactions: antidepressants and ARVs\n- Most first-line ARVs, including DTG, do not interact with antidepressants.\n- Ritonavir increases levels of amitriptyline and fluoxetine.\n"
   "- Darunavir decreases levels of sertraline.\n- Fluvoxamine increases levels of protease inhibitors and non-nucleoside reverse-transcriptase inhibitors (NNRTIs).\n"
   "- Use of efavirenz (EFV) can be associated with suicidal thoughts and attempts; regular screening for depression is essential. EFV should be avoided in clients with overt psychiatric symptoms, including depression and psychosis.\n"
   "- The use of a high dose of amitriptyline with protease inhibitors can produce cardiac arrhythmia; electrocardiogram monitoring may be indicated when dose escalation is anticipated.\n"
   "- DTG can cause insomnia. DTG should be given in the morning to avoid insomnia."),
 T("tbl-10.9-antipsychotics", 252, DP + " > Table 10.9", "Table 10.9 Antipsychotic drugs", ["0693"],
   [r("Antipsychotic tablet", "Initial dose", "Maximum dose")],
   [r("Haloperidol", "3–5 mg 2 times daily", "20 mg/day (Increase dose by 1.5-5 mg at a time)"),
    r("Risperidone", "1–2 mg 2 times daily", "16 mg/day (Increase dose by 2 mg at a time)"),
    r("Olanzapine", "5 mg 2 times daily", "25 mg/day (Increase dose by 5 mg at a time)"),
    [C("Olanzapine and Risperidone can cause impressive weight gain and also risk for diabetes.", cs=3)]],
   source_flags=["Table 10.9 maximum doses are high: risperidone 16 mg/day (the absolute upper limit; usual maintenance is at most 6-8 mg/day) and olanzapine 25 mg/day (usual maximum 20 mg/day); check against the Eswatini Mental Health guidelines."]),
 B("box-mood-stabilizers", 252, DP + " > Mood Stabilizers", "Mood Stabilizers", ["0694"],
   "Mood stabilizers\n- Sodium valproate 50mg–600mg twice daily (mostly preferred in PLHIV):\n- Maximum therapeutic dose 2500mg/day in divided dose.\n- Increase dose by 200–500mg.\n"
   "- Check valproate levels yearly or every 6 months if the client is on the maximum dose.\n- Lamotrigine 25mg for the first 14 days then increase by 25-50mg, maximum 500mg/day in divided doses.\n"
   "- Carbamazepine is contraindicated as it increases levels of PIs and NNRTIs.",
   flags=["Carbamazepine is an enzyme inducer: it lowers (not increases) levels of PIs, NNRTIs and DTG; the stated reason for the contraindication is reversed.",
          "Valproate starting dose printed as '50mg–600mg twice daily'; check the intended starting dose (the Mental Health guidelines give the reference dosing)."]),
]
