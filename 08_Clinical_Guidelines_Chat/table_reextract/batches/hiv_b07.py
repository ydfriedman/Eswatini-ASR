exec(open("batches/hiv_common.py").read())
# HIV 2022 part 1, pp.72-75 (Chapter 3: recency testing, quality assurance). From the page images, wording checked against the text layer.
C3 = "Chapter 3: HIV Testing Services"
ITEMS = [
 D("fig-3.12-rtri-strip", 72, C3 + " > 3.11 Testing for Recent Infection > Laboratory Testing Methods > Figure 3.12", "Figure 3.12 Point of care recent infection test strip illustration", [],
   "Photograph of three Asante HIV-1 Rapid Recency test strips with the line positions marked C (control), V (verification) and LT (long-term):\n"
   "- C, V and LT lines present: RTRI long-term infection\n- C and V lines present: RTRI recent infection\n- Only the C line present: inconclusive recency status\n"
   "No control line: invalid result. A long-term line without a verification line is also an invalid recency result.\n"
   "The RTRI result does not change the client's HIV diagnosis or management (diagnosis follows the national two-test algorithm); it is used only to classify recency for surveillance. If Determine is reactive and UniGold non-reactive, the RTRI result is not reported until HIV infection is confirmed."),
 D("fig-3.13-rita-interpretation", 73, C3 + " > 3.11 Testing for Recent Infection > Recent Infection Testing Algorithm > Figure 3.13", "Figure 3.13 Interpretation of a Recent Infection Testing Algorithm Using a Rapid Test for Recent Infection and Viral Load Testing", ["0172"],
   "1. Routine HIV rapid testing (national algorithm: Determine/UniGold): HIV+.\n"
   "2. Rapid test for HIV recent infection (RTRI) classification: RTRI-recent, RTRI-long term, RTRI-inconclusive or RTRI-invalid.\n"
   "3. RTRI-recent: viral load test.\n   - VL ≥1000 copies/mL: RITA-recent.\n   - VL <1000 copies/mL: RITA-long term.\n"
   "Clients who test long-term on the RTRI need no additional testing and are classified as RTRI long-term infection.\n"
   "A recent infection is an infection occurring approximately within the past 12 months. Recency testing is for adults 15 years and older newly diagnosed with HIV at HTS who consent to all EHRIS procedures (RTRI and VL); results are for programmatic use only and are not disclosed to clients.",
   flags=["The text calls the recency algorithm 'Figure 2'; it is Figure 3.13.", "The second RITA box hangs from the RTRI-recent node only; the figure does not show what happens to RTRI-inconclusive or invalid results (the text records inconclusive as HIV positive with inconclusive recency status)."]),
 B("tbl-3.11-qa-responsibilities", 74, C3 + " > 3.11 Testing for Recent Infection > Quality assurance > Table 3.11 Responsibilities to ensure quality assurance", "Table 3.11 Responsibilities to ensure quality assurance", ["0175", "0176", "0178"],
   "HTS provider:\n"
   "- Run internal quality controls once weekly, for each new lot of test kits, for any new operator or when environmental conditions fall outside the range recommended by the manufacturer.\n"
   "- Participate in HIV proficiency panel testing, provide timely feedback and document corrective actions for unsatisfactory performance.\n"
   "- Store test kits in a temperature-controlled environment following the manufacturer’s recommendation (2-30 degrees Celsius). Document temperature and maintain a cold chain\n"
   "- Ensure samples are stored and transported appropriately\n"
   "- Ensure that standard operating procedures exist and are adhered to for all procedures, including specimen collection and processing, testing algorithms and all test procedures, with QC and final reporting (following a verified testing algorithm).\n"
   "- Administer counsellor reflection forms, client exit interviews\n- Document and dissemination of quality assurance report\n- Ensure information and testing aids are given to clients using the HIVST kits.\n"
   "- Ensure active linkages and a strong aftercare mechanism for clients\n"
   "- To identify non-conformance, routinely monitor indicators such as turnaround times for each assay, turnaround time for an overall testing report, rate of discrepant results, rate of invalid results, rate of specimen rejection, rate of test kit stock-outs, rate of supplies stock-outs and frequency of expiration of test kits.\n"
   "HIVST distributor:\n- Undergo training to distribute HIVST kits, including directly assisted HIVST\n"
   "- Store test kits in a temperature-controlled environment (temperature: 2-30 degrees Celsius), maintain a cold chain and ensure proper packaging, especially when going to the community or outreach\n"
   "- Ensure active linkage information for reactive and non-reactive results, and a strong after-care mechanism for clients\n- Manage HIVST inventory by adhering to stock monitoring, documentation and reporting procedures\n"
   "Supervisor:\n- Ensure HTS providers and HIVST distributors are trained and provided with refresher training every year\n- Ensure the facility (both fixed and mobile) has the capacity for cold chain management\n"
   "- Ensure samples are stored and transported appropriately\n- Ensure compliance with HIV testing/HIVST SOPs and national HIV testing algorithms.\n"
   "- Provide supportive supervision for HTS providers based on quality assurance tools (sit-ins, compliance to SOPs and guidelines, etc)\n- Monitor stock management of HIV testing commodities\n"
   "- Appoint HTS focal to monitor quality aspects of testing\n- Ensure active linkage of clients and after-care\n"
   "- Proactively identify opportunities for improvement and relay recommendations to a higher level of management for broader implementation.\n- Conduct competency assessments of testers at least once a year\n"
   "HTS Program:\n- Liaise with the lab on regular conduction of onsite supportive supervision for lab, point of testing sites, and individuals distributing HIVST\n"
   "- Conduct HTS training and refresher training sessions regularly\n- Ensure documentation and dissemination of quality assessment reports\n- Timely review of HIV testing registers, HIVST registers, SOPs and QA tools\n"
   "- Ensure samples are stored and transported appropriately\n- Regular update and disseminate information on HIV testing and monitoring compliance with recommended testing algorithm(s)\n"
   "- Engage all HIV testing points in an external quality assurance program of the Eswatini Health Laboratory services through participation in quarterly proficiency testing\n"
   "- Ensure all HTS points are conducting competency assessments of testers at least once a year\n- Conduct quarterly supportive supervisions at least once a year\n- Conduct site readiness assessments on all new testing sites",
   pages=[74, 75],
   flags=["'Conduct quarterly supportive supervisions at least once a year' is contradictory.", "Recency QA (p.73): monthly QC with HIV-positive and negative plasma and proficiency testing with dried tube specimens bi-annually; the HTS Program row says proficiency testing is quarterly."]),
]
