exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.241-244 (Chapter 10: hypertension). From the page images; Table 10.4 colours/arrows read from a
# high-resolution render.
C10 = "Chapter 10: Management of Non-Communicable Diseases"
HT = C10 + " > 10.2 Care and Management of Hypertension and HIV for patients 18 years and older"
ITEMS = [
 T("tbl-10.1-bp-classification", 241, HT + " > Classification of hypertension > Table 10.1", "Table 10.1 The classification of BP for adults aged 18 years or older", ["0660"],
   [r("Category", "Systolic BP", "Diastolic BP")],
   [r("Normal", "< 120 mmHg", "<80mmHg"), r("Prehypertension", "120- 139 mmHg", "80 – 89 mmHg"), r("Stage 1", "140 – 159 mmHg", "90 – 99 mmHg"),
    r("Stage 2", "160 – 179 mmHg", "100 – 109 mmHg"), r("Stage 3", ">180 mmHg", ">110mmHg")],
   context_before="Hypertension is defined by the WHO as systolic blood pressure (SBP) ≥140 mmHg and/or diastolic blood pressure (DBP) ≥90 mmHg on two measurements. First header cell blank in the source.",
   source_flags=["Table 10.1 Stage 3 is printed as >180 / >110 mmHg, so readings of exactly 180 mmHg systolic or 110 mmHg diastolic fall in no category; usual practice is ≥180 / ≥110."]),
 T("tbl-10.2-non-pharmacological", 242, HT + " > Non-pharmacological management of hypertension > Table 10.2", "Table 10.2 Non-pharmacological management", ["0663"],
   [r("Behaviour", "Advice")],
   [[C("Physical activity"), L("Engage in regular physical activity (e.g., aerobics) for at least 30mins/days Daily", "Reduce and maintain BMI to 20-25kg/m²", "Reduce and maintain waist circumference to <94cm in men and <80cm in females")],
    [C("Tobacco"), L("Encourage smokers to stop tobacco use and encourage them in their efforts", "Encourage non-smokers not to start smoking")],
    [C("Harmful use of alcohol"), L("Limit alcohol to no more than 30ml of ethanol/day for men and 15ml/day for females and people of lighter weight", "Avoid binge drinking (≥5 drinks on a single occasion for men or ≥4 drinks on a single occasion for women, generally within about 2 hours)", "Avoid heavy drinking (≥15 drinks per week for men and ≥ 8 drinks or more per week for females)")],
    [C("Diet"), L("Eat a healthy diet low in saturated fats, Limit fatty meals,", "Reduce high-calorie food", "Reduce salt intake to not more than 5g of salt per day", "Maintain adequate dietary calcium and magnesium for general health", "Eat a diet high in fruits and vegetables")],
    [C("Adherence counselling"), L("Attend regular medical follow-up")]],
   context_before="The first step in managing uncomplicated hypertension is lifestyle modification.",
   footnotes=["When ≥2 of the above lifestyle modifications are maintained, BP is lowered, and cardiovascular disease risk is decreased."],
   source_flags=["The text above refers to 'Table 10.2 Non-pharmacological management' as showing high-risk features for patients with elevated BP; the high-risk features are in Table 10.3."]),
 T("tbl-low-risk-drinking-limits", 242, HT + " > Alcohol consumption > Low-risk drinking limits", "Low-risk drinking limits (untitled table)", ["0665"],
   [r("Low-risk drinking limits", "Males", "Females", "1 drink is approximately equivalent to:")],
   [[C("Maximum drinks per day"), C("4*"), C("3**"), C("- 350ml of beer,<br/>- 150ml of wine, or<br/>- 50ml of 40% alcohol content - distilled spirits or liquor (e.g., gin, rum, vodka, whiskey).", rs=3)],
    [C(""), C("AND", cs=2)],
    r("Maximum drinks per week", "14*", "7**")],
   context_before="There are no safe alcohol drinking limits, as even the drinking limits listed below may cause adverse health outcomes in certain individuals particularly if one consumes alcohol too quickly, if they have other health problems, if they are pregnant and if they are above the age of 65. Consumption of alcohol while pregnant is strongly condemned.",
   footnotes=["* A male who takes 3 drinks on a given day, must not consume more than 11 drinks for the remainder of the week (must not take more than 4 drinks on any given day).",
              "** A female who consumes 2 drinks on a given day, must not drink more than 5 drinks for the remainder of the week (must not take more than 3 drinks on any given day)."],
   source_flags=["Daily alcohol limits differ between the two tables: Table 10.2 says no more than 30 ml ethanol/day for men and 15 ml/day for women (roughly 2 and 1 standard drinks), while this table allows 4 and 3 drinks/day."]),
 T("tbl-10.3-hypertension-high-risk", 243, HT + " > Pharmacological management of hypertension > Table 10.3", "Table 10.3 High-risk features of hypertension", ["0668"],
   [r("High Risk", "Score", "Interpretation")],
   [[C("Diabetes"), C("2"), C("Patients with a score of 2 or more points are considered high risk and warrant more aggressive treatment", rs=5)],
    r("Renal Failure creatinine ≥ 100 μmol/L (1.1 mg/dL)", "2"), r("Age ≥ 65", "1"), r("BMI ≥25", "1"), r("Smoking", "1")]),
 B("box-aspirin", 243, HT + " > Recommended Drugs to Initiate in Special Cases > Aspirin", "Aspirin (box)", [],
   "Key message: Never combine angiotensin receptor blockers (ARBs) with ACE inhibitors. Use ARBs if clients develop side effects to ACE inhibitors (e.g., cough or angioedema). Do not give ACE inhibitors in clients with hyperkalaemia.\n\n"
   "Recommended drugs to initiate in special cases: refer to national NCD guidelines.\n\n"
   "Aspirin\n- Prescribe ASA to clients adults 40-70yrs old who are at risk of atherosclerotic cardiovascular disease:\n"
   "   - Clients aged > 40 years\n   - Clients with cardiovascular risk factors\n"
   "   - Clients with a history of a previous cardiovascular event e.g., type 2 diabetes, diabetic nephropathy, coronary artery disease, transient ischaemic attack or stroke, or peripheral vascular disease\n"
   "- Before prescribing aspirin, ensure BP is < 160/100mmHg to avoid intracerebral haemorrhage\n- Ensure there are no contra-indications to aspirin use",
   flags=["The aspirin box lists type 2 diabetes and diabetic nephropathy as examples of a 'previous cardiovascular event'; check current national NCD guidance on aspirin for primary prevention."]),
 T("tbl-10.4-antihypertensive-arv-interactions", 244, HT + " > Interactions between antihypertensives and ARVs > Table 10.4", "Table 10.4 Drug Interaction. Source: University of Liverpool, HIV-druginteractions.org", ["0672"],
   [r("Antihypertensive", "TDF/TAF", "AZT", "3TC", "FTC", "EFV", "NVP", "DTG", "LPV/r", "ATV/r", "DRV/r")],
   [r("Hydrochlorothiazide", "", "", "", "", "", "", "", "", "", ""),
    r("Amlodipine", "", "", "", "", "↓ (yellow)", "↓ (yellow)", "", "↑ (yellow)", "↑ (yellow)", "↑ (yellow)"),
    r("Enalapril", "", "", "", "", "", "", "", "", "", ""),
    r("Bisoprolol*", "", "", "", "", "↓ (yellow)", "↓ (yellow)", "", "↑ (orange)", "↑ (orange)", "↑ (orange)")],
   footnotes=["* WHO Essential Medicines list includes atenolol, metoprolol, and carvedilol as alternatives.",
              "Legend: green = no interaction; yellow = potential interaction with increased or decreased levels of antihypertensives which may require dose adjustment (drug levels of ARVs are not affected by calcium channel blockers or beta-blockers and no dose adjustment is required); orange = caution should also be exercised when administering B blockers and PIs due to the risk of QT prolongation — ECG monitoring is recommended. ↑ = increase in antihypertensive drug level; ↓ = decrease in antihypertensive drug level.",
              "Blank cells are uncoloured in the source (the green 'no interaction' colour is not used in any cell); read blank as no interaction listed."],
   context_before="Calcium channel blockers like nifedipine and amlodipine may interact with protease inhibitors, producing increased serum levels of CCBs; dose titration and ECG monitoring are required. Several protease inhibitors can cause ECG changes, especially PR interval prolongation: drugs for hypertension with similar effects (beta blockers, calcium channel blockers) should be used with caution with PIs, and ECG monitoring is recommended. Caution should also be exercised when combining diuretics with TDF; renal function could be impaired due to added risk for interstitial nephritis."),
]
