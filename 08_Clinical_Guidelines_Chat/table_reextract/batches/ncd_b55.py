exec(open('batches/ncd_common.py').read())
CC = CH9 + " > Cervical Cancer"
def r(*v): return [C(x) for x in v]
ITEMS = [
 D("fig-cervical-screening-algorithm", 251, CC + " > Cervical Cancer Screening & Treatment Algorithm",
   "Cervical cancer screening and treatment algorithm: HIV-negative women vs women living with HIV (HPV DNA testing, VIA/VILI triage, screen-and-treat, stop age)", ["0720"],
   "A. General population (HIV-negative women):\n"
   "1. Age 25-50 years: HPV DNA testing; screen every 5 years.\n"
   "2. HPV negative: rescreen in 5 years. HPV positive: triage testing.\n"
   "3. VIA every 2 years (rescreen in 2 years):\n"
   "   - Negative: rescreen in 2 years.\n"
   "   - Positive: refer for LEEP/colposcopy.\n"
   "4. Stop screening after age 50 + two negative tests.\n\n"
   "B. Women living with HIV:\n"
   "1. HIV positive, age 25+ OR at diagnosis: HPV DNA testing; screen every 3 years.\n"
   "2. HPV negative: rescreen in 3 years. HPV positive: triage testing.\n"
   "3. VIA every year or VILI every year (return in 1 year):\n"
   "   - Negative: return in 1 year.\n"
   "   - Positive: refer for LEEP/oncology.\n"
   "4. Stop screening after age 50 + two negative tests.\n\n"
   "Single-visit screen-and-treat: SCREEN → TRIAGE → TREAT (same day) → FOLLOW-UP; same-day care when feasible.\n"
   "VIA: visual inspection with acetic acid. VILI: visual inspection with Lugol's iodine.",
   ["In both panels the chart draws VIA as a routine screen after a negative HPV test (as well as a triage test after a positive one), and the HIV panel has a second 'Negative' box reading 'Refer for LEEP / Year'. The intended pathway is unclear; summarised here. Clinician to confirm.",
    "Stopping screening at 50 in women living with HIV differs from usual WHO advice (continue screening); the age range for the general population is printed '25-50'."]),
 T("tbl-cervical-screening-summary", 252, CC + " > Cervical Cancer Screening & Management Summary Table",
   "Cervical cancer screening and management summary: HIV-negative women vs women living with HIV (start/stop age, test, intervals, triage, treatment, service model)", ["0722"],
   [[C("Component"), C("General Population (HIV-Negative Women)"), C("Women Living with HIV")]],
   [r("Start Age", "25 years", "25 years or at HIV diagnosis (whichever first)"),
    r("Stop Age", "After 50 years with 2 consecutive negative screens", "After 50 years with 2 consecutive negative screens"),
    r("Preferred Test", "HPV DNA testing", "HPV DNA testing"),
    r("HPV Screening Interval (if negative)", "Every 5 years", "Every 3 years"),
    r("If HPV Positive", "Triage (VIA / colposcopy / cytology)", "Triage (VIA / colposcopy / cytology)"),
    r("Alternative Method (if HPV unavailable)", "VIA", "VIA ± VILI"),
    r("VIA/VILI Interval", "Every 2 years", "Annually (every year)"),
    r("Screening Approach", "Screen-and-treat", "Screen-and-treat integrated into HIV care"),
    r("If VIA/VILI Negative", "Rescreen at interval", "Rescreen at interval"),
    r("If VIA/VILI Positive & eligible", "Same-day cryotherapy/thermal ablation", "Same-day cryotherapy/thermal ablation"),
    r("If not eligible for ablation", "Refer for LEEP/colposcopy", "Refer for LEEP/colposcopy/oncology"),
    r("Service Delivery Model", "Primary care, MCH/OPD clinics", "Routine HIV clinic visits (provider-initiated)")],
   context_before="Cervical cancer is the leading cause of cancer-related death among women in Eswatini (incidence 84.5 per 100,000 women, the highest in the world). Women living with HIV have a six-fold increased risk."),
 T("tbl-via-results-management", 252, CC + " > Management by VIA result",
   "Management by VIA screening result: negative, positive eligible for ablation, positive ineligible (LEEP), suspicious for cancer: eligibility, action and follow-up", ["0723"],
   [[C("VIA Screening Result"), C("Treatment Eligibility / Findings"), C("Clinical Action & Procedure"), C("Follow-Up Timeline")]],
   [r("VIA Negative", "No lesions or suspicious areas identified", "Discharge: return to routine screening (annual for HIV+; 2 years for HIV-)", "12 - 24 months (based on HIV status)"),
    r("VIA Positive (eligible for ablation)", "Lesion ≤75% of ectocervix; TZ fully visible (type 1); no endocervical extension; no suspicion of cancer", "Ablative treatment (same visit): thermal ablation or cryotherapy", "12 months (repeat VIA)"),
    r("VIA Positive (ineligible for ablation)", "Large lesion (≥75% coverage); high-grade lesion suspected; tissue diagnosis needed", "Refer for LEEP", "6 months (VIA or HPV)"),
    r("Suspicious for Cancer", "Visible mass/cauliflower growth; bleeds easily on contact; extension to vaginal walls", "Urgent referral to secondary/tertiary level for colposcopy and biopsy", "Immediate (per specialist)")],
   source_flags=["Ablation eligibility is '≤75%' and ineligibility '≥75%' (both include 75%); WHO uses <75% / ≥75%."]),
 T("tbl-cervical-special-populations", 253, CC + " > Special Populations",
   "Cervical cancer screening in special populations: women living with HIV (on ART/PrEP), pregnant women, HIV-negative women", ["0724", "0725"],
   [[C("Population"), C("Screening Rule"), C("Key Clinical Note")]],
   [r("HIV-positive women", "Annual VIA screening", "Integrate into ART initiation and routine follow-up."),
    r("On ART / PrEP", "Annual VIA screening", "Adherence reduces but does not eliminate risk."),
    r("Pregnant women", "Screen per HIV status", "VIA is safe. Defer treatment until post-delivery unless cancer is suspected."),
    r("HIV-negative", "Every 2 years", "Use community health workers and registries for recall.")],
   context_before="Because HIV significantly increases the risk of cervical cancer, screening must be integrated into routine care.",
   source_flags=["The PDF text layer for this page is overprinted with a second copy of the table; transcribed from the page image. 'On ART / PrEP' screening applies annual VIA screening to people on PrEP (HIV-negative), as printed."]),
]
