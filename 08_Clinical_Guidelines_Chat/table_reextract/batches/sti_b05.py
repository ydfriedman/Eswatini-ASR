exec(open("batches/sti_common.py").read())
# STI/VH draft part 1, pp.64-70: syndromic charts for scrotal swelling, inguinal bubo and neonatal conjunctivitis. From the page images.
CH5 = "5.0 Management of STIs Associated Syndromes"
HPP = ("Health promotion package:\n- Educate, ensure compliance, and counsel on treatment.\n- Promote abstinence or condom use during treatment.\n"
       "- Promote correct and consistent condom use also provide condoms and lubricants.\n- Issue one notification slip for each sexual partner and emphasize the importance of partner treatment.\n"
       "- Offer HIV counselling and testing, as per Integrated HIV Guidelines.\n- Offer voluntary medical male circumcision.\n- Offer pre exposure prophylaxis as per guideline.")
ITEMS = [
 D("fig-sexual-history-steps", 27, "2.0 Essential Components > 2.1 History Taking and Assessing STI and HIV Risk > Steps to consider while taking a Sexual History", "Steps to consider while taking a Sexual History (flowchart)", ["0051", "0052"],
   "START BY → Within the last three (3) months, have you had sex with.... MALE / BOTH / FEMALE\n"
   "→ Consider exploring further whatever the choice. In your sexual encounters you had.... have you ever had? Anal sex / Vaginal/penile / Oral sex\n"
   "→ (each) Receptive / Both / Insertive:\n"
   "   - Receptive → Consider: oral, vaginal and anal STI. Ask about: pain, sores, ulcers, discharges, growths.\n"
   "   - Insertive → Consider: penile and oral STI. Ask about: pain, discharge, sores, ulcers and growths.\n"
   "   - Both → both of the above.\n"
   "→ Consider: the appropriate syndromic flow chart and treat accordingly.\n\n"
   "See annex 1 & 2: a table on guidance for clinical history taking of STI patients."),
 D("chart-scrotal-swelling", 64, CH5 + " > 5.5 Scrotal swelling (SSS) > 5.5.1 Chart (scrotal swelling)", "Syndromic treatment chart for scrotal swelling (section 5.5.1, 'chart 5')", ["0143", "0144", "0145"],
   "Patient complains of recent onset scrotal swelling or pain → Take history and examine.\n"
   "→ Decision box (as printed): 'Elevated torsion Or Recent history of Trauma or Incarcerated hernia. emergency referral (surgical). Unilateral testicular pain and swelling, often with tenderness'\n"
   "   - NO → Any other STI syndrome or illness present? (NO → Re-assure, counsel and educate; condom promoted and provided. YES → Treat according to appropriate flow chart.)\n"
   "   - YES → Ceftriaxone, 1 g IM stat PLUS Azithromycin, 1 g orally per week for 2 weeks PLUS combined with bed rest and scrotal support. Ask to come for the follow up after 7 days.\n"
   "      → Follow up at 7 days: improved? (YES → Finalise treatment; reinforce health promotion package. NO → Refer for further management.)\n\n"
   + HPP + "\n- Provide cervical cancer screening during follow-up visit.",
   pages=[63, 64],
   flags=["The scrotal swelling chart puts the emergency-referral conditions (torsion, trauma, incarcerated hernia) and the epididymitis signs in one decision box, so 'YES' leads to antibiotics; torsion needs immediate surgical referral, not treatment. The chart is labelled 'chart 5' (the same number as the lower abdominal pain chart), and its health promotion package includes cervical cancer screening for a male patient."]),
 D("chart-inguinal-bubo", 67, CH5 + " > 5.6. Inguinal bubo (IBS) > 5.6.1 Chart 6", "Syndromic treatment chart for inguinal bubo (chart 6)", ["0150", "0151", "0152"],
   "Client complains of swelling in the groin with or without pain → Take history and examine.\n"
   "→ Enlarged and/or painful inguinal/femoral bubo(s) present?\n"
   "   - NO → Any other STI syndrome or illness present? (NO → Reassure, counsel and educate; condom promoted and provided. YES → Treat according to appropriate flow chart.)\n"
   "   - YES → Azithromycin, 1g orally stat and then 1g orally per week for 2 weeks PLUS Ceftriaxone, 500mg IM stat. For a fluctuant bubo aspiration is vital. Follow up after 7 days.\n"
   "      → Follow-up at 7 days: improved?\n         - YES → Finalise treatment; reinforce health promotion package.\n"
   "         - NO → Poor compliance with oral therapy? (YES → Repeat treatment; reinforce health promotion package. NO → Refer for further management.)\n\n"
   + HPP + "\n- Provide cervical cancer screening during follow-up visit.",
   flags=["The inguinal bubo chart gives ceftriaxone 500 mg IM, while the treatment options on p.66 give ceftriaxone 1 g IM (chancroid) and, for LGV, doxycycline 100 mg twice daily for 14 days (the chart has no doxycycline). The text says to refer fluctuant buboes for aspiration; the chart says aspiration is vital."]),
 D("chart-neonatal-conjunctivitis", 70, CH5 + " > 5.7. Neonatal conjunctivitis > 5.7.1 Chart 7", "Syndromic treatment chart for neonatal conjunctivitis (chart 7)", ["0157", "0158", "0159"],
   "Neonate with eye(s) discharge → Take history and examine.\n"
   "→ Swollen eyelid(s) with purulent discharge present?\n   - NO → Reassure parent/guardian; advise to return if symptoms persist.\n"
   "   - YES → Ceftriaxone, 50mg/kg body weight (max. 125mg) IM single dose PLUS Erythromycin syrup, 50mg/kg body weight orally daily in 4 divided doses for 14 days. Provide health promotion package to parents; follow up after 2 days or earlier, if worsening.\n"
   "      → Follow up at 2 days: improved? (YES → Finalize treatment; reassure parent/guardian. NO → Reassure parent/guardian and refer for further management.)\n\n" + HPP,
   flags=["The neonatal conjunctivitis chart's health promotion package (for the parents) repeats the adult items, including voluntary medical male circumcision; it does not mention treating the mother and her partner(s)."]),
]
