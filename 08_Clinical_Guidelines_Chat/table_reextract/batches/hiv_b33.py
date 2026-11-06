exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.245-248 (Chapter 10: diabetes). From the page images.
C10 = "Chapter 10: Management of Non-Communicable Diseases"
DM = C10 + " > 10.3 Care and Management of Diabetes and HIV"
SU = ("Table 10.5 recommends metformin + sulphonylurea at Steps 4 and 5, but the text on p.246 says 'Do not use sulphonylureas (e.g., glibenclamide) because of drug "
      "interaction with protease inhibitors that may result in profound hypoglycaemia; efavirenz may also cause uncertain interactions with sulphonylureas'. "
      "Table 10.5 also brings in metformin only at Step 3, while Figure 10.1 starts metformin as soon as diabetes is confirmed.")
ITEMS = [
 B("box-dtg-metformin", 245, DM + " > DTG and metformin", "Dolutegravir and metformin (key message and dosing)", [],
   "Key message: Switching ART regimens should only be considered if a patient is on DTG, or LPV/r based regimen and their diabetes is out of control. Switching other ARV medications is of uncertain benefit.\n\n"
   "Key message: Special caution should be used when metformin is co-administered with DTG, as DTG significantly increases metformin concentration, leading to potential increased adverse events.\n"
   "1. If the patient is already on metformin and initiating dolutegravir, monitor closely for metformin adverse effects, glucose levels, and HbA1c, and adjust the dose as necessary.\n"
   "2. In patients taking dolutegravir who are starting metformin, begin with a low metformin dose (250mg twice daily or 500mg once daily) and titrate up carefully. It is recommended to limit the dose of metformin to 1000 mg daily i.e., 500mg twice daily."),
 D("fig-10.1-diabetes-evaluation", 246, DM + " > Figure 10.1", "Figure 10.1 Evaluation of clients with Diabetes and HIV infection", ["0676"],
   "Flow (top to bottom):\n1. HIV infection and diabetes diagnoses confirmed: conduct baseline physical assessment and laboratory investigation. Refer to practice guide for management of diabetes mellitus.\n"
   "↓\n2. Use Metformin 500 - 1000mg with or without additional insulin.\n"
   "↓\n3. Monitor blood sugar control and prevent end organ damage:\n- Blood glucose should be below 10mmol/L\n- HbA1c should be below 7%\n"
   "- Annual eye and foot examination is needed, and additional risk factors like dyslipidaemia and hypertension should be managed properly. Refer to national practice guide.",
   flags=["Figure 10.1 gives metformin 500-1000 mg without a frequency; with DTG the text limits metformin to 1000 mg daily (500 mg twice daily)."]),
 T("tbl-10.5-art-and-diabetes", 247, DM + " > Recommendations when initiating or switching to an INSTI (DTG) regimen > Table 10.5", "Table 10.5 Guidance on ART and Diabetes", ["0680", "0681"],
   [r("Step", "Blood sugar values", "Guidance for PLHIV newly initiating on/transitioning to DTG or PI-based regimens", "Guidance for HIV-positive clients already on DTG or PI-based regimens")],
   [[C("Step 1"), C("Pre-diabetes<br/>FBS 5.6-6.9 mmol/l<br/>RBS 7-11 mmol/l"),
     L("Check Blood Glucose at baseline", "Check Blood Glucose every 3 months", "Inform clients they may develop diabetes in future", "Advise lifestyle modifications", "The client can be on DTG or PI-based regimens"),
     L("Inform clients they may develop hyperglycaemia in future", "Advise lifestyle modifications", "Check blood glucose every 3 months if on ART regimen with risk of developing hyper-glycaemia", "The client can be on DTG or PI-based regimens")],
    [C("Step 2"), C("Diabetes<br/>FBS 7-10 mmol/l<br/>RBS ≥11.1-17 mmol/l"),
     L("The client can be on DTG or PI-based regimens provided blood glucose is controlled by adjusting antidiabetic medications", "Lifestyle modifications if the person is committed", "If not controlled after 1-3 months, go to Step 3", "If FBS >10 mmol/l or RBS >17 go to Step 3"),
     L("The client can be on DTG or PI-based regimens provided blood glucose is controlled by adjusting antidiabetic medications", "Lifestyle modifications if the person is committed", "If not controlled after 1-3 months, go to Step 3", "If FBS >10 mmol/l or RBS >17 go to Step 3")],
    [C("Step 3"), C("Failure at Step 2 OR<br/>FBS >10 mmol/l<br/>RBS >17mmol/l"),
     L("The client can be on DTG or PI-based regimens provided blood glucose is controlled by adjusting antidiabetic medications", "Lifestyle modification", "Metformin"),
     L("The client can be on DTG or PI-based regimens provided blood glucose is controlled by adjusting antidiabetic medications", "Lifestyle modification", "Metformin")],
    [C("Step 4"), C("Failure at Step 3<br/>RBS > 17mmol/l"),
     L("Consider starting the client on or maintaining EFV based regimen then transition to DTG once blood sugar is controlled", "Lifestyle modification", "Metformin + Sulphonylurea"),
     L("Consider substituting ARV that could contribute to elevated blood glucose", "Lifestyle modification", "Metformin + Sulphonylurea")],
    [C("Step 5"), C("Failure at Step 4<br/>RBS > 17mmol/l"),
     L("Consider starting the client on or maintaining EFV based regimen then transition to DTG once blood sugar is controlled", "Consider insulin", "Follow-up at hospital"),
     L("Consider substituting ARV that could contribute to elevated blood glucose", "Consider insulin", "Follow-up at hospital")]],
   pages=[247, 248],
   context_before="Recommendations when initiating or switching to an INSTI (DTG) regimen: measure and record baseline fasting and/or random blood sugar for any client starting or switching to DTG; record family history and/or current diabetes; ensure glucose in known diabetics is controlled (FBS<7mmol / RBS<10mmol); check blood glucose of newly DTG initiated/switched clients at baseline, at the 2nd and 6th-week visits and 6-monthly thereafter; educate on symptoms of diabetes; any client with new-onset random blood glucose >17mmol and signs of DKA or HHS should be treated as an emergency and referred. First header cell blank in the source; step cells are colour-graded from yellow (Step 1) to dark brown (Step 5).",
   source_flags=[SU,
     "Table 10.5 Step 1 says check blood glucose every 3 months for pre-diabetes, while the text above it says DTG clients should be checked at baseline, weeks 2 and 6 and 6-monthly thereafter.",
     "Table 10.5 treats FBS 7-10 mmol/l as acceptable on DTG/PI regimens (Step 2), while the text above defines controlled diabetes as FBS<7 / RBS<10 mmol; check against the national NCD guidelines and 2024 Amendment."]),
 B("box-diabetes-referral", 248, C10 + " > 10.4 Diabetes/Hypertension coinfection", "Who needs routine consultation with or referral to an experienced provider? (diabetes)", [],
   "Key message: Beta blockers are not recommended for initial management of hypertension in diabetic patients but can be used if thiazides or ACE inhibitors are unavailable or contraindicated.\n\n"
   "Who needs routine consultation with or referral to an experienced provider?\nConsultation with or referral to an experienced provider is recommended in the following circumstances:\n"
   "- FBS >14 mmol/l despite maximal doses of metformin and sulfonylurea\n- Individuals with newly diagnosed diabetes and urine ketones 2+\n- Severe infection and/or foot ulcers\n"
   "- Recent deterioration in vision\n- Gestational diabetes\n- Blood pressure ≥130/80 mmHg despite treatment with 2 blood pressure-lowering agents",
   flags=["The referral criteria refer to 'maximal doses of metformin and sulfonylurea', but p.246 says not to use sulphonylureas with PIs/EFV, and metformin is capped at 1000 mg/day with DTG."]),
]
