exec(open('batches/prep_common.py').read())
FU = CH3 + " > 3.3 PrEP Follow-up Visit"
ITEMS = [
 D("fig-followup-exposure-ahi", 49, FU + " > Component 2: Assessments > HIV Exposure and AHI Assessment", "Figure 12. PrEP follow-up flowchart: HIV test, exposure in past 72 hours and effective use (continue PrEP or start PEP), AHI symptoms in past 14 days, pause PrEP and retest", ["0122", "0123", "0124"],
   "1. Is the client's HIV test result negative?\n"
   "   - No: refer the client to confirmatory testing and HIV treatment.\n"
   "   - Yes: 2.\n"
   "2. Was the client potentially exposed to HIV in the past 72 hours? (⁰)\n"
   "   - Yes: did the client practise prevention-effective use of the chosen method during this potential exposure?\n"
   "     - Yes: continue PrEP standard of care (SOC).\n"
   "     - No: start PEP SOC. (²) If PEP is started, retest for HIV in 28 days; if seronegative on PEP completion, continue PrEP SOC.\n"
   "   - No: 3.\n"
   "3. Does the client have, or have they had, symptoms of AHI in the past 14 days? (¹)\n"
   "   - No: continue PrEP SOC; special effective-use counselling may be beneficial.\n"
   "   - Yes: did the client have a potential exposure to HIV in the 14 days before symptom onset?\n"
   "     - No: symptoms are unlikely due to AHI because the timing of exposure and symptom onset does not align. Continue PrEP SOC using best clinical judgement.\n"
   "     - Yes: did the client practise prevention-effective use of the chosen method around the potential exposure?\n"
   "       - Yes: symptoms are unlikely due to AHI because the method was used effectively at the time of exposure. Continue PrEP SOC using best clinical judgement.\n"
   "       - No: symptoms may be due to AHI. Provider and client should weigh the risks and benefits of pausing PrEP use and retesting per the national algorithm 28 days from potential exposure, or earlier if HIV testing that can reliably detect HIV given the timing of exposure is available. (²)\n"
   "Notes: ⁰ 'No' means no potential exposure at all, or exposure 72+ hours ago. ¹ Two-thirds of people have AHI symptoms within two to four weeks of acquiring HIV; similar symptoms (sore throat, fever, sweats, swollen glands, mouth ulcers, headache, rash, muscle aches) are commonly due to other illnesses, so use discretion. ² If HIV testing that can reliably detect HIV given the exposure and time frame is available, PrEP may be started earlier than 28 days if results are non-reactive."),
 T("tbl-creatinine-monitoring", 50, FU + " > Component 2: Assessments > Monitoring Kidney Function for Clients Using Oral PrEP", "Table 17. Creatinine (kidney function) monitoring for oral PrEP by age and risk group: under 30, 30-49, 50+, comorbidities, CrCl 60-89, nephrotoxic drugs; stop PrEP if CrCl <60", ["0126"],
   [[C("Population"), C("Frequency of creatinine monitoring")]],
   [[C("Age <30 years"), L("Optional (until age 30 or if kidney-related comorbidities develop).", "If done and CrCl <90 ml/min, conduct follow-up every six months.", "If <60 ml/min, stop PrEP and manage as per guidance (Section 4).")],
    [C("Age 30–49 years"), C("Conduct creatinine test once, at or within three months of initiation.<br/>- If CrCl ≥90 ml/min: optional (until age 50 or kidney-related comorbidities develop).<br/>- If CrCl <90 ml/min (60–89 ml/min): screening every 6–12 months.<br/>- If <60 ml/min: stop PrEP and manage as per guidance (Section 4).")],
    [C("Age 50+"), C("- Conduct creatinine test once, at or within three months of initiation.<br/>- Follow-up screening every 6–12 months.<br/>- If <60 ml/min, stop oral PrEP and manage as per guidance (Section 4).", rs=4)],
    [C("Individuals of any age with comorbidities")],
    [C("Individuals with CrCl <90 ml/min (60–89)")],
    [C("Individuals with concurrent nephrotoxic medication")]],
   context_before="Renal function testing is not a prerequisite at baseline before PrEP initiation. For certain age and population groups it should be monitored after one month of oral PrEP use and every six months thereafter.",
   table_note="For the management of clients with abnormal creatinine levels, see Section 4.",
   source_flags=["The text above the table says monitoring is after one month and every six months; the table says once within three months of initiation and then every 6–12 months (or six-monthly for under-30s with CrCl <90)."]),
 D("fig-oral-ring-dispensing-schedule", 51, FU + " > Component 4: PrEP Prescription Refill > Oral PrEP or PrEP Ring", "Figure 13. Oral PrEP and PrEP ring follow-up and dispensing schedule: 3 months at initiation, HIVST at month 1, then up to 6-month dispensing with HIVST every 3 months; 6-month refill criteria", ["0129"],
   "Figure 13 (timeline in months 0–13):\n"
   "- Month 0: initiate and dispense 3 months of PrEP product + HIVST.\n"
   "- Month 1: use HIVST at home.\n"
   "- Month 3: dispense a maximum of 6 months of PrEP + HIVST.\n"
   "- Month 6: use HIVST.\n"
   "- Month 9: dispense a maximum of 6 months of PrEP + HIVST.\n"
   "- Month 12: use HIVST.\n"
   "Six-month refill criteria (after the first follow-up visit; otherwise maximum three months): attends the follow-up appointment on time (not later than three days after the scheduled date); reports no side effects; wants to continue with the same method; not pregnant or breastfeeding and no co-morbidities; willing to do an HIVST after three months – if negative, continue with the remaining three months; if positive, stop the PrEP method and report to the facility for confirmation and linkage to ART.\n"
   "ED-PrEP users: dispense three months of PrEP minus the number of full bottles the client has at home (enough tablets should they use PrEP daily). Clients on 6-month dispensing get an HIVST to use after three months before continuing with the last three months of product."),
]
