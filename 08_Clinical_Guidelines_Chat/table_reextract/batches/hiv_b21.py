exec(open("batches/hiv_common.py").read())
# HIV 2022 part 3, pp.169-175 (Chapter 7: treatment failure, second and third line, adherence, defaulter tracing). From the page images,
# wording checked against the text layer.
C7 = "Chapter 7: Adult Antiretroviral Therapy"
B_ = lambda *xs: "<br/>".join("• " + x for x in xs)
ITEMS = [
 T("tbl-7.11-second-line-sequence", 170, C7 + " > 7.12.1 Second-Line ART for Adults and Adolescents > Table 7.11", "Table 7.11 Recommended Sequence of Second-line NRTI Options", ["0453"],
   [r("Current 1st line Regimen", "Preferred 2nd Line Regimen", "Alternative 2nd Line Regimen", "Special Considerations")],
   [[C("AZT + 3TC + EFV"), C("TDF + 3TC + DTG"), C("TDF+3TC+boosted PI**"), C("Recycle the TDF/3TC backbone in chronic hepatitis B patients", rs=4)],
    r("ABC + 3TC + EFV", "AZT + 3TC + DTG", "AZT+3TC+boosted PI**<br/>TDF + 3TC + DTG***"),
    r("TDF +3TC + EFV", "TDF +3TC + DTG*", "AZT + 3TC + DTG<br/>AZT+3TC+boosted PI**"),
    [C("TDF + 3TC + DTG<br/>ABC + 3TC + DTG<br/>AZT + 3TC + DTG"), C("HIV resistance testing should be done for all clients failing on a DTG-based ART regimen. Only switch to 2nd line if the resistance test shows DTG resistance and the 2nd line regimen should be a boosted PI + 2 NRTIs determined by the genotype results", cs=2)]],
   footnotes=["*Studies have shown that for patients failing a TDF/3TC + NNRTI first-line regimen, recycling the TDF/3TC backbone in 2nd line was superior in viral suppression to switching to AZT/3TC",
              "** For clients weighing ≥ 40kg, ATV/r is preferred over LPV/r as it can be taken once daily.",
              "***There is a 10% risk of TDF resistance in clients failing ABC, only use this option if twice-daily dosing will be a barrier to treatment success",
              "Clients who cannot tolerate ATV/r or LPV/r in 2nd line may be considered for DRV/r after reviewing genotype results. As DRV/r doses depend on previous PI exposure and resistance mutation pattern, use of DRV/r as part of a second-line regimen has to be approved by the HIVDR clinical expert committee (snapthirdline@mohcoag.org).",
              "Second-line ART is two NRTIs plus DTG or a boosted PI depending on previous ART history. Alternative second-line regimens are for contraindications to the preferred regimen. ATV/r is preferred to LPV/r (one tablet once daily, better tolerability, lower cost) for clients weighing more than 40 kg, with adherence issues from twice-daily dosing or side effects from LPV/r."],
   context_before="Second-line ART and TB: see Table 6.15. Clients coinfected with HIV and HBV whose first line contained TDF + 3TC should continue TDF + 3TC in second line. If the failing regimen was TDF based, maintain TDF+3TC and add AZT to the NRTI backbone; if the failing regimen was AZT based, switch to TDF+3TC in the NRTI backbone.",
   source_flags=["Section 7.12.1 (p.169) says clients failing a DTG-based first line should have resistance testing before a switch, and the table says to switch to a boosted PI only if DTG resistance is shown; what to do when no DTG resistance is found (continue DTG with adherence support) is not stated."]),
 T("tbl-7.12-tb-second-line", 171, C7 + " > 7.12.1 > Second-Line ART and TB Infection > Table 7.12", "Table 7.12 Options for Managing TB Clients (on second-line ART)", ["0455"],
   [r("TB Client on Treatment", "Action")],
   [r("LPV/r", "Consult an experienced clinician or HIVDR expert committee (snapthirdline@mohcoag.org) before choosing the options below.<br/>" + B_("Super boost LPV/r to 400mg/400 mg by adding 300mg ritonavir to normal dose LPV/r and continue until 2 weeks after completion of TB treatment",
        "Double-dose of LPV/r to 800mg/200mg twice daily and continue until 2 weeks after completion of TB treatment. Double dosing is only for clients >10 years of age. See Annex 111.16 for dose adjustments in paeds",
        "If evidence of VL suppression in the past 3-6months, switch to a DTG-based regimen and continue twice daily DTG until 2 weeks after completion of TB treatment")),
    r("ATV/r and DRV/r", B_("Do not combine with RIF", "Change to twice daily DTG or to LPV/r with adjustments as stated above", "Use Bedaquiline with caution as there is a risk of QT prolongation")),
    r("DTG", B_("Increase DTG dosing to 50mg twice daily until 2 weeks after completion of TB treatment.", "Rifampicin is associated with hyperglycaemia so do monthly RBS"))],
   footnotes=["For all clients, maintain the same NRTI backbone provided there is no dose adjustment necessary, and clients are virally suppressed"],
   source_flags=["'Annex 111.16' (Annex 11.16).", "'Rifampicin is associated with hyperglycaemia' is placed under DTG; the monthly RBS advice is not explained."]),
 B("box-7.12.2-third-line-workup", 172, C7 + " > 7.12.2 Third-Line ART for Adults and Adolescents > Treatment-Experienced Clients", "Work-up of treatment-experienced clients before third-line ART", ["0461"],
   "Treatment-experienced clients are those with loss or lack of virological response to at least 2 ARV regimens, including at least one member of each of the three drug classes (NRTI, NNRTI and PIs). They are assessed and managed by a multidisciplinary team, with sequencing supported by HIV drug resistance testing (genotype) and the third-line committee (snapthirdline@mohcoag.org).\n"
   "- Ensure adequate adherence during SUAC before collecting sample for genotype. DOTS is advised.\n- Order genotypic resistance testing while the client is still taking the failing second-line regimen OR no later than 4 weeks after discontinuing the failing regimen.\n"
   "- Assess immune status (CD4 count) and need for: AHD package and prophylactic therapy.\n- Review and document a full medical, laboratory and ARV history. A full physical examination is advisable to exclude any opportunistic infections or comorbidities.\n"
   "- Ensure completion of SUAC.\n- Order appropriate laboratory tests (including haemoglobin, ALT, CD4, bilirubin, fasting blood sugar, lipid profile, HbsAg, Creatinine).\n"
   "Potential third-line regimens* (adults & adolescents 10-19 years, guided by genotype results):\n- DRV/r + DTG ± one or two NRTIs\n- DRV/r + two NRTIs ± NNRTI**\n"
   "*Construction of third-line ART regimens should be guided by HIV genotyping results; consult the HIVDR expert clinical committee on snapthirdline@mohcoag.org for guidance.\n**Caution: high-level NNRTI resistance in Eswatini limits the use of Etravirine (ETR) 200 mg 12 hourly.\nDRV/r should not be used in children less than 3 years of age.",
   pages=[171, 172]),
 B("box-7.15-adherence-formula", 174, C7 + " > 7.15 Adherence to care and treatment", "Pill count adherence calculation", ["0468"],
   "Pills remaining from last visit + pills dispensed last visit = pills given\n% Adherence = (# pills taken) / (# pills prescribed) x 100 = [(# pills given) - (# pills at hand)] / [(daily dose) x (# days since refill)] x 100\n"
   "The standard clinical definition of adherence has been taking >95% but <105% of medications the right way, at the right time, and includes following a care plan, attending scheduled clinic appointments, picking up medicines on time and getting scheduled laboratory tests."),
 D("fig-7.6-defaulter-tracing", 175, C7 + " > 7.15 Adherence to care and treatment > Figure 7.6 Defaulter tracing", "Figure 7.6 Defaulter tracing (timeline classifications)", ["0472"],
   "Timeline classifications (the probability of retention decreases with each day that passes after the appointment):\n"
   "- On time: came between 7 days before and less than 3 days after the appointment. Reminder system: pre-appointment reminders for clients particularly those at risk of missing appointment; post-appointment reminders for all clients as a proactive measure.\n"
   "- Honored appointment: client who came on the exact date of the appointment.\n- Pre-appointment reminder: efforts made to ensure clients come on time before the appointment.\n- Post-appointment reminder: efforts between 1 to less than 3 days after the appointment.\n"
   "- Missed appointment: 3-7 days after appointment. Facility follow-up: contact clients telephonically; at least 3 attempts must be made; daily and strategic contacts if phone not available or not picking; if not successful, contact treatment supporter; client is contacted using this method until defaulter or a conclusive outcome is ascertained; clients with unique challenges can be escalated as per escalation plan.\n"
   "- Defaulter: 7-28 days. Community follow-up: commences at defaulter stage; in-person community follow-up is conducted at community level; attempts depend on follow-up and are escalated based on the need of the client using the escalation plan; the client may be followed multiple times depending on follow-up outcome; frequency of follow-up may be reduced until a conclusive outcome is achieved; file may be closed after a home visit in resource-limited settings or if a conclusive outcome is attained and the escalation plan exhausted.\n"
   "- IIT (interruption in treatment): more than 28 days.\n"
   "For clients returning to care after being classified as having interrupted treatment, document reasons for interrupting treatment as outlined in the eLCM SOP.",
   flags=["Patient follow-up should begin on the same day an appointment is missed (section 7.15), while the figure starts facility follow-up at 3 days."]),
]
