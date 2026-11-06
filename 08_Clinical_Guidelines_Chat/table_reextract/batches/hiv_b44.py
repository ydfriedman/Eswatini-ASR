exec(open("batches/hiv_common.py").read())
# HIV 2022 part 5, pp.282-286 (Annexes 11.10-11.15: hepatitis B algorithm, test interpretation and treatment, hypertension evaluation,
# infant LPV/r initiation). From the page images; the HBV algorithm read from a 190 dpi render.
AN = "Chapter 11: Annexes"
NEG, POS, EITHER = "-ve", "+ve", "+ or -ve"
ITEMS = [
 D("fig-11.10-hbv-treatment-algorithm", 282, AN + " > 11.10 Hepatitis B Virus Treatment Algorithm", "Annex 11.10 Hepatitis B Virusᵃ Treatment Algorithm", ["0765", "0766", "0767", "0768"],
   "Assessment for treatment. Start: HBsAg positive → Cirrhosis? (clinical criteriaᵇ; NITs: APRI score >2 in adults or FibroScan)\n"
   "- YES (cirrhosis) → Initiate NA therapy and monitor: tenofovir or entecavir; entecavir in children 2-11 years. Stopping treatment: cirrhosis → lifelong treatment.\n"
   "- NO (no cirrhosis):\n"
   "   - Ageᶜ >30 years (in particular) with ALTᵈ,ᵉ persistently abnormal:\n"
   "      - HBV DNA >20,000 IU/mL → Initiate NA therapy and monitor (tenofovir or entecavir; entecavir in children 2-11 years)\n"
   "      - HBV DNA 2,000-20,000 IU/mL → Defer treatment and monitor\n"
   "      - HBV DNA <2,000 IU/mL → Defer treatment and monitor\n"
   "   - ALTᵈ,ᵉ intermittently abnormal → Defer treatment and monitor\n"
   "   - ALTᵈ,ᵉ persistently normal → Defer treatment and monitor\n"
   "   - Age ≤30 years, ALTᵈ,ᵉ persistently normal, HBV DNA <2000 IU/mL → Defer treatment and monitor\n\n"
   "Monitoring (treated and deferred):\n- Every 6 months: detection of HCCᶠ (persons with cirrhosis or HCC family history)\n"
   "- Every 12 months: disease progression and/or treatment response in all: adherent at each visit, if on treatment; ALT, HBV DNA and HBeAg; clinical criteria and NITs (APRI in adults or FibroScan)\n"
   "- Baseline and every 12 months: toxicity monitoring in persons on treatment: renal function and risk factors for renal dysfunctionᵍ\n\n"
   "Stopping treatment:\n- Cirrhosis: lifelong treatment\n- No cirrhosis: may stop with HBeAg loss and seroconversion to anti-HBe after completion of at least one additional year of treatment, and persistently normal ALT, and persistently undetectable HBV DNA\n\n"
   "NITs: non-invasive tests; ALT: alanine aminotransferase; APRI: aspartate aminotransferase-to-platelet ratio index.\n"
   "ᵃ Defined as persistence of hepatitis B surface antigen (HBsAg) for six months or more. The algorithm does not capture all potential scenarios, but the main categories for treatment or monitoring. Recommendations for settings without access to HBV DNA testing are provided in the relevant chapters.\n"
   "ᵇ Clinical features of decompensated cirrhosis: portal hypertension (ascites, variceal haemorrhage and hepatic encephalopathy), coagulopathy, or liver insufficiency (jaundice). Other clinical features of advanced liver disease/cirrhosis may include hepatomegaly, splenomegaly, pruritus, fatigue, arthralgia, palmar erythema, and oedema.\n"
   "ᶜ The age cut-off of >30 years is not absolute, and some persons with CHB less than 30 years may also meet the criteria for antiviral treatment.\n"
   "ᵈ ALT levels fluctuate in persons with chronic hepatitis B and require longitudinal monitoring to determine the trend. Upper limits for normal ALT have been defined as below 30 U/L for men and 19 U/L for women, though local laboratory normal ranges should be applied. Persistently normal/abnormal may be defined as three ALT determinations below or above the upper limit of normal, made at unspecified intervals during a 6 to 12 month period or predefined intervals during a 12-month period.\n"
   "ᵉ Where HBV DNA testing is not available, treatment may be considered based on persistently abnormal ALT levels, but other common causes of persistently raised ALT levels such as impaired glucose tolerance, dyslipidaemia and fatty liver should be excluded.\n"
   "ᶠ All persons with CHB should be monitored regularly for disease activity/progression and detection of HCC, and after stopping treatment for evidence of reactivation. More frequent monitoring may be required in those with more advanced liver disease, during the first year of treatment or where adherence is a concern, and in those with abnormal ALT and HBV DNA levels >2000 IU/mL, not yet on treatment.\n"
   "ᵍ Before initiation, an assessment should be done of renal function (serum creatinine level, estimated glomerular filtration rate, urine dipsticks for proteinuria and glycosuria, and risk factors for renal dysfunction (decompensated cirrhosis, CrCl <50 mL/min, poorly controlled hypertension, proteinuria, uncontrolled diabetes, active glomerulonephritis, concomitant nephrotoxic drugs, solid organ transplantation, older age, BMI <18.5 kg/m2 (or body weight <50 kg), concomitant use of nephrotoxic drugs or a boosted protease inhibitor (PI) for HIV). Monitoring should be more frequent in those at higher risk of renal dysfunction.",
   pages=[282, 283]),
 T("tbl-11.11-hbv-test-interpretation", 283, AN + " > 11.11 Interpretation of HBV laboratory tests", "Annex 11.11 Interpretation of HBV laboratory tests", ["0769"],
   [r("HBsAg", "Total anti-HBc", "IgM anti HBc", "Anti-HBs", "HBeAg", "Anti-HBe", "Interpretation")],
   [r(NEG, NEG, "", NEG, "", "", "Never exposed"),
    r(NEG, POS, NEG, NEG, "", "", "Past natural infection, cleared, anti-HBs levels have waned over time"),
    r(POS, POS, POS, NEG, POS, NEG, "Acute Hepatitis B, ongoing infection"),
    r(POS, POS, NEG, NEG, POS, NEG, "Chronic Hepatitis B with active viral replication"),
    r(POS, "", "", NEG, NEG, POS, "Inactive HBV carrier state (low HBV DNA level) or HBeAg -ve chronic hepatitis B with active viral replication (high HBV DNA level)"),
    r(POS, "", "", POS, EITHER, EITHER, "Chronic hepatitis B with heterotypic anti-HBs (about 10% of cases)"),
    r(NEG, POS, POS, POS, "", "", "Recent infection, recovered, immunity achieved"),
    r(NEG, POS, NEG, POS, NEG, "+ve or -ve", "Immunity due to past infection"),
    r(NEG, NEG, NEG, POS, NEG, NEG, "Immunity due to vaccination"),
    r(NEG, "", "", NEG, NEG, NEG, "False positive; less commonly, infection in remote past")],
   footnotes=["Cells are colour-coded in the source: +ve red, -ve green, either orange; blank cells are not tested/not informative."],
   source_flags=["Annex 11.11 last row ('False positive; less commonly, infection in remote past') shows HBsAg -ve; the pattern usually described this way is isolated anti-HBc positive."]),
 D("fig-11.11-hbv-jaundice-diagnosis", 284, AN + " > 11.11 Interpretation of HBV laboratory tests > HBV diagnosis in jaundiced patients", "HBV diagnosis in jaundiced patients (flowchart)", ["0770", "0771"],
   "HBV diagnosis in jaundiced patients: test HBsAg (non-reactive / reactive) and IgM anti-HBc (non-reactive / reactive).\n"
   "- If HBsAg is reactive and IgM anti-HBc is non-reactive: HBV positive\n- If both HBsAg and IgM anti-HBc are positive: HBV positive\n"
   "- If IgM anti-HBc is reactive and HBsAg is non-reactive: HBV positive\n- If both IgM anti-HBc and HBsAg are negative: HBV negative\n\n"
   "Markers (text above the figure): IgM anti-HBc is a specific marker for acute HBV infection; it decreases and disappears after 32 weeks. Total anti-HBc: IgM and total anti-HBc increase after 2 weeks of infection; IgM indicates acute infection, IgG persists for life. Anti-HBs appears after acute infection, signalling cure. HBsAg increases within 2-10 weeks then decreases and disappears within 6 months with acute infection. HBeAg indicates HBV infectivity/replication. Total anti-HBc, mainly IgG, continues to be positive for life.",
   flags=["The figure label reads 'IgM anto HBc' (for IgM anti-HBc)."]),
 T("tbl-11.12-hbv-treatment", 285, AN + " > 11.12 Hepatitis B Virus Treatment and Clinical Considerations", "Annex 11.12 Hepatitis B Virus Treatment and Clinical Considerations", ["0772", "0773"],
   [r("", "Population", "Considerations")],
   [[C("Who to treat", rs=2), C("As a priority, all adults, adolescents and children with chronic hepatitis B infection (CHB) and clinical evidence of compensated or decompensated liver disease"), C("APRI score >2 in adults<br/>Start treatment regardless of alanine aminotransferase (ALT) level, HBeAg or hepatitis B virus DNA levels")],
    r("Adults with CHB who do not have clinical evidence of cirrhosis", "APRI score ≤2 and<br/>More than 30 years old and<br/>Has persistently abnormal ALT<br/>And if available, there is evidence of high-level HBV replication (HBV DNA >20,000 IU/mL)"),
    r("Who not to treat", "Treatment is not recommended in HIV-negative clients without clinical evidence of cirrhosis; however, clinical monitoring should continue", "APRI score ≤2 and<br/>Persistently normal ALT levels and<br/>Low level of HBV replication (HBV DNA <2,000 IU/mL)"),
    r("What to treat with", "Recommended agents and dosages (weight kg | dose | agent):<br/>≥35 | 1 OD | TDF (300mg) + 3TC (300mg)<br/>>30–35 | 10 or 0.5 mg | Entecavir (0.05 mg/mL)<br/>>26–30 | 9 | Entecavir (0.05 mg/mL)<br/>>23–26 | 8 | Entecavir (0.05 mg/mL)<br/>>20–23 | 7 | Entecavir (0.05 mg/mL)<br/>>17–20 | 6 | Entecavir (0.05 mg/mL)<br/>>14–17 | 5 | Entecavir (0.05 mg/mL)<br/>>11–14 | 4 | Entecavir (0.05 mg/mL)<br/>10–11 | 2 | Entecavir (0.05 mg/mL)", "Lamivudine (3TC) alone should not be used due to the rapid development of HBV resistance<br/>Provide pre-treatment counselling about indications for treatment, likely benefits and side effects, the need for follow-up both on and off therapy, and the importance of full adherence to treatment"),
    r("How to monitor", "The following should be monitored at least annually:<br/>- ALT (and aspartate aminotransferase [AST] for APRI)<br/>- HBsAg, HBeAg<br/>- HBV DNA levels<br/>- Adherence to treatment at each visit", "More frequent monitoring is required for the following:<br/>- Clients who do not meet the criteria for treatment<br/>- Clients with advanced disease on treatment<br/>- Clients who had their treatment discontinued"),
    r("When to stop treatment", "Discontinuation may be considered in the following:<br/>- Persons without clinical evidence of cirrhosis (APRI score ≤2) and also<br/>- Can be followed carefully and long-term for reactivation and also<br/>- Have persistently normal ALT levels and persistently undetectable HBV DNA levels", "- Lifelong treatment is required in all persons with cirrhosis based on clinical evidence (or APRI score >2 in adults)<br/>- Do not discontinue antiviral treatment due to the risk of reactivation<br/>- Relapse may occur after discontinuation, and re-treatment is recommended")],
   footnotes=["The dosing table is a sub-table inside the 'What to treat with' row; entecavir doses are in mL of the 0.05 mg/mL oral solution (units not printed)."],
   source_flags=["Annex 11.12 entecavir dose for 10–11 kg is printed as 2 (mL = 0.1 mg); the WHO weight-band dose is 3 mL (0.15 mg), and every other band rises by 1 mL. The dose column also has no units ('10 or 0.5 mg' for >30-35 kg mixes mL and mg)."]),
 B("box-11.13-hypertension-evaluation", 286, AN + " > 11.13 Clinical Evaluation of a Client with High Blood Pressure and HIV Infection", "Annex 11.13 Clinical Evaluation of a Client with High Blood Pressure and HIV Infection", ["0774"],
   "HIV and hypertension confirmed; assess risk factors for cardiovascular disease.\n"
   "Investigate for end-organ damage; ask for an echocardiogram (ECG), creatinine, haemoglobin, low-density lipoprotein cholesterol, TC renal sonography and urine albumin.\n"
   "Use conservative and/or pharmacologic treatment of hypertension:\n- Use diuretics and angiotensin-converting enzyme inhibitors as appropriate.\n- Avoid calcium channel blockers, or use them with caution.\n- Monitor closely for the occurrence of Ischemic heart disease.",
   flags=["Annex 11.13 expands ECG as 'echocardiogram'; ECG is an electrocardiogram (an echocardiogram is a different test)."]),
 T("tbl-11.15-infant-lpv-r-initiation", 286, AN + " > 11.15 Initiation of Infants Less Than 4 Weeks old on Lopinavir/Ritonavir", "Annex 11.15 Initiation of Infants Less Than 4 Weeks old on Lopinavir/Ritonavir", ["0776"],
   [r("Age", "AM", "PM")],
   [r("0–2 weeks", "AZT + 3TC + NVP", "AZT + 3TC + NVP"), r("2 weeks–3 months", "ABC + 3TC + LPV/r syrup", "ABC + 3TC + LPV/r syrup"),
    r("3–36 months", "ABC + 3TC + LPV/r syrup or pellets", "ABC + 3TC + LPV/r syrup or pellets")],
   source_flags=["Annex 11.15 keeps infants on ABC + 3TC + LPV/r up to 36 months; Chapter 9 and the 2024 Amendment move children to DTG (pDTG or pALD) from 4 weeks of age and 3 kg."]),
]
