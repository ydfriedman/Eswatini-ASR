exec(open("batches/hiv_common.py").read())
# HIV 2022 part 1, pp.57-63 (Chapter 3: IPV screening, HIV screening tools, retesting, verification, pre-test information, test types).
# Transcribed from the page images (the text layer drops letters on pp.57-61), wording checked against the text layer.
C3 = "Chapter 3: HIV Testing Services"
O = lambda *xs: "<br/>".join("∞ " + x for x in xs)
ITEMS = [
 B("box-3.3-ipv-screening-tool", 57, C3 + " > 3.3 Intimate partner violence screening tool", "IPV screening tool: screen for probable index testing induced health risk", [],
   "IPV screening tool - SCREEN FOR PROBABLE INDEX TESTING INDUCED HEALTH RISK\n"
   "NB: Ask the question below for each of the partners listed: \"Do you anticipate any violence with partner (current or former) if/ when you disclose your HIV results?\" Yes / No\n"
   "If patient answers \"NO\":\n1. Record the patient as \"Not at risk\" in the index testing register\n2. DO NOT offer provider referral\n3. You can offer Client referral, Contract referral and Dual referral depending on the patient preference.\n"
   "If patient answers \"YES\": record the patient as \"at risk\" in the index testing register. The counsellor asks the patient to share his/her limitations about possible violence from the partner or partners (current/ former) using the prompts below, then, depending on the nature of the limitations, advises on the most appropriate disclosure strategy such as the use of Provider Referral.\n"
   "1. Do you think your partner (current/ former) will physically hurt you or force you to do something sexually that makes you feel uncomfortable if you disclose to him/her or he/she finds out your HIV status?\n"
   "2. Do you think your partner (current/ former) will emotionally hurt you if you disclose to him/her your HIV status or he/she finds out your HIV status?\n"
   "3. Do you fear your partner (current/ former) will abandon you or chase you from the place you live or stop paying/ contributing towards rent/ bond?\n"
   "4. Do you think your partner (current/ former) will stop financially supporting you or your children?\n"
   "NOTE: If client appears agitated, sweaty, restless, crying or irritable during the discussion, stop all questions and refer to Health Provider for further counseling management (debriefing / Psychological First Aid/ Cognitive Behavior Therapy/ Clinical Therapy)",
   flags=["The 'NO' branch says DO NOT offer provider referral, and the 'YES' branch suggests provider referral; this looks reversed. Section 3.2.3 says people at risk of IPV should NOT be offered provider referral, so provider referral belongs to the not-at-risk ('NO') branch."]),
 D("fig-3.5-hiv-eligibility-screening-adults", 58, C3 + " > 3.4 HIV Screening Tools > Figure 3.5", "Figure 3.5 HIV testing eligibility screening tool for adults", ["0128"],
   "1. Have you ever tested for HIV?\n   - No: offer routine HIV testing services.\n   - Yes: what is your HIV status?\n"
   "2. HIV status:\n   - Negative: refer to HTS counsellor for risk assessment.\n   - Positive: on ART?\n       - No: refer for ART initiation and LCM.\n       - Yes: patient may directly proceed to consultation room.\n"
   "Aims of the HIV screening tools: to ensure that testing reaches those most at risk for HIV infection; to reduce unnecessary HIV testing among low-risk clients by testing only those identified as eligible for testing; to identify individuals with the highest risk of HIV to receive HIV prevention interventions like PrEP or VMMC; to streamline testing/resources in settings with shortage of staff/kits and inform prioritization of resources.\n"
   "The screening tools should not be used for people with confirmed or presumptive TB, STI clients, index contacts, pregnant and lactating mothers or PrEP clients: HIV testing remains the standard of care for them.",
   flags=["The text before the figure refers to 'Figure 3.5 and Error! Reference source not found.' (a broken cross-reference, presumably Figure 3.6)."]),
 D("fig-3.6-hiv-risk-assessment-retesting", 59, C3 + " > 3.4 HIV Screening Tools > Figure 3.6 HIV risk assessment tool", "Figure 3.6 HIV risk assessment tool: risk assessment for HIV-negative adults and adolescents to assess need for retesting", ["0131"],
   "Not to be applied to TB patients, presumptive TB patients, pregnant and lactating women, STI clients, index contacts and PrEP clients.\n"
   "Patient previously tested HIV negative: conduct risk assessment to determine need for testing using the questions below (each YES leads to the action shown; NO moves to the next question).\n"
   "1. Do you have any of the following symptoms? (cough more than 2 weeks, fever, night sweats, noticeable weight loss, swollen lymph nodes, oral sores, recurrent skin rashes) - YES: test for HIV & TB\n"
   "2. Have you had sex while under the influence of alcohol or drugs since your last negative HIV test result? - YES: test for HIV\n"
   "3. Have you had more than 1 sexual partner since your last negative HIV test result? - YES: test for HIV\n"
   "4. Have you injected drugs and shared needles, syringes, and other drug equipment with other people since your last negative HIV test result? - YES: test for HIV\n"
   "5. Have you had a sexually transmitted infection since your last negative HIV test result? (abnormal penile or vaginal discharge, burning when urinating, sores in the genital area) - YES: test for HIV & treat STI\n"
   "6. Have you had condomless sex after your last negative HIV test result with a partner with either an HIV positive status or unknown HIV status? - YES: test for HIV\n"
   "Clients that answer YES to one or more of the above questions should be tested for HIV. Clients that answer NO to all questions should not be tested for HIV. Clients that answer YES to any of questions 2, 3, 4, 5, 6 and who test HIV negative should be offered PrEP and other prevention services e.g. VMMC.",
   flags=["The PDF text layer carries a second, different question numbering (e.g. question 2 numbered 4, question 6 numbered 2); the printed figure numbers 1-6 as above."]),
 T("tbl-3.4-retesting-frequencies", 60, C3 + " > 3.5 HIV retesting > Table 3.4 Optimal retesting frequencies for various population groups", "Table 3.4 Optimal retesting frequencies for various population groups", ["0133"],
   [r("Population", "When to Retest")],
   [r("General population", "Based on HIV testing and screening tool"),
    [C("Couples and Partners", rs=2), C("Sero-different couple: Based on the ongoing risk of exposure")],
    [C("Sero-different couple: retest every 2 months until/unless partner has evidence of undetectable Viral Load<br/>Once partner maintains undetectable V/L, retest based on HIV exposure or annually")],
    r("Pregnant and Lactating Women", "All HIV-negative pregnant women should be re-tested every 2 months (aligned with the ANC scheduled visits) with the most optimal time for retesting being during the third trimester visit (34 weeks gestation).<br/>At delivery: Test every woman with unknown HIV status; test all women who have not tested in the third trimester<br/>All HIV-negative lactating women should be re-tested at 6 weeks, 14 weeks, 6 months, 9 months, 12 months, 15 months and 18 months aligned with the MBP follow-up schedule.<br/>See Table 8.5"),
    r("Key Populations", "Retest every 8 weeks"),
    r("General population", "Based on HIV testing and screening tool"),
    [C("Couples and Partners", rs=2), C("Sero-different couple: Based on HIV testing and screening tool")],
    [C("Sero-different couple: retest every 2 months until/unless partner has evidence of undetectable Viral Load<br/>Once partner maintains undetectable V/L, retest based on HIV exposure or annually")]],
   source_flags=["The table repeats its 'General population' and 'Couples and Partners' rows at the end; the repeat says sero-different couples are retested 'based on HIV testing and screening tool' where the first says 'based on the ongoing risk of exposure'. The screening tools (Figures 3.5-3.6) are not meant for index contacts and partners.",
                 "Key populations: 'Retest every 8 weeks' is more frequent than WHO guidance (every 3-12 months by risk)."]),
 D("fig-3.7-verification-before-art", 61, C3 + " > 3.6 Verification of true new HIV tests and true new positive clients prior to ART initiation > Figure 3.7", "Figure 3.7 Verification of HIV status before registration (verification of true new HIV positive clients prior to HTS and ART initiation)", ["0136"],
   "HTS testing point:\n1. Client presents for HTS.\n2. Intensive data system search (surname, name, ID number, DOB, phone details).\n3. Verify client using CMIS or AMPR list of prior HTS.\n"
   "   - Client found: HTS not provided; link to ART department.\n   - Client not found: HTS provided.\n       - HIV+: linked to ART department.\n       - HIV-: follow-up per guidelines.\n"
   "ART unit:\n4. Linked to ART department: verify client in CMIS and AMPR list prior to ART initiation (intensive search: surname, name, ID number, DOB, phone details).\n"
   "   - Client found: no verification testing. Determine reason for retesting, offer disclosure and adherence counselling or facilitate care transfer as needed.\n"
   "   - Client not found: provide verification testing per guidelines.\n       - HIV+: initiate on ART.\n       - HIV-: follow re-testing guidance.\n"
   "Clients who are identified at ART points as not new will be removed from the HTS entry point as new, and reclassified accordingly on the same day."),
 T("tbl-3.5-pre-test-information", 62, C3 + " > 3.7 Pre-Test Information > Summary of Pre-Test Information > Table 3.5 Summary of pre-test information", "Table 3.5 Summary of pre-test information", ["0138", "0139"],
   [[C("Pre-test information included in both CIHTS and PIHTS", cs=3)]],
   [[C(O("The benefits of HIV testing (highlighting the positive benefits of knowledge of HIV status).", "The meaning of an HIV-positive and an HIV-negative diagnosis:") +
       "<br/>» The services available in the case of an HIV-positive diagnosis, including where ART is provided.<br/>» The potential for incorrect results if a person already on ART is tested.<br/>» A brief description of HIV prevention options and encouragement of partner testing.<br/>» The fact that the test result and any information shared by the client is confidential.", cs=3)],
    [C("Pre-test information included in both CIHTS and PIHTS", cs=3)],
    [C(O("The fact that the client has the right to opt out from testing and that declining testing will not affect the client’s access to HIV-related services or general medical care.",
         "Potential risks of testing to the client in settings where there are legal implications for those who test positive and/or for those whose sexual or other behaviour is stigmatized.",
         "An opportunity to ask the HTS provider questions.", "Clinical and HIV prevention benefits of HIV testing.",
         "Benefits of ART and the Test and Start approach (starting treatment today or within 2 weeks of diagnosis).",
         "Encourage voluntary notification of partners and disclosure of status and option of assisted notification under index testing services.",
         "Confidentiality of testing and results.", "An offer to answer any question the client may have.", "Clarify misconceptions and myths about HIV transmission and risks",
         "Condom use demonstrations (male and female condoms).", "HIV testing screening tool (Annex HIV Testing Screening Tool)",
         "Gender-based violence assessments for adolescent girls and young women using health risk assessment tool",
         "Offer index testing services to the client should they test positive and elicitation of contacts can be done at this stage."), cs=3)],
    r("CIHTS should also include:", "PIHTS should also include:", "HIVST should also include:"),
    r(O("Preparation for testing and receiving results", "Suicide assessment and coping skills", "Development of a risk reduction plan"),
      O("Information on shared confidentiality", "Reassurance that refusal to test will not result in the client being denied care for their current health problem"),
      O("An HIVST positive result should be confirmed by a trained HTS provider following the recommended algorithm", "Directly assisted demonstrations on how to perform the HIVST")),
    [C("Inform the client about HTS Hotline in case the client wants to ask questions.", cs=3)]],
   rhc=0, source_flags=["The heading 'Pre-test information included in both CIHTS and PIHTS' appears twice, over two separate lists (probably the second was meant to be a different heading)."],
   context_before="Obtain informed verbal consent in line with the 5 Cs of HTS."),
 T("tbl-3.6-hiv-test-types", 63, C3 + " > 3.8 HIV testing devices and procedure > Table 3.6 Types of laboratory tests for HIV screening and diagnosis", "Table 3.6 Types of laboratory tests for HIV screening and diagnosis", ["0140"],
   [[C(""), C("Antibody Test", cs=2), C("Virological Test")],
    r("Test name", "Rapid test: Determine HIV 1/2; Uni-gold HIV 1/2; Asante HIV-1", "HIVST: Oraquick HIV self-test", "NAT (RNA and/or DNA PCR)")],
   [r("Sample type", "Capillary/venous whole blood, plasma", "Saliva", "Capillary/venous whole blood"),
    r("Collection site", "Finger", "Mouth", "Heel/Toe/finger"),
    r("Window period", "8 weeks", "12 weeks", "2-6 weeks"),
    r("Indication", "-Diagnosis for clients 18 months and older<br/>-*Surveillance", "Self-Screening", "-Diagnosis for clients under 18 months<br/>-Diagnosis of clients with inconclusive HIV rapid test results"),
    r("Turnaround time (TAT)", "20mins", "20 mins", "2-6 weeks")],
   footnotes=["* The Eswatini HIV-1 recent infection surveillance (EHRIS) program tracks recent HIV infections by providing continuous epidemiological surveillance data on person, place, and time of HIV recent infections amongst adults 15 years and older to inform HIV prevention and epidemic control strategies", "From section 3.8.1: Eswatini has adopted the two-test strategy for the diagnosis of HIV with Determine HIV1/2 and UniGold HIV1/2; a three-test strategy should be considered if HIV positivity in HIV testing services falls below 5%. In ANC settings, the dual HIV/Syphilis rapid diagnostic tests may be considered the first test. The Asante HIV-1 Rapid Recency assay detects recent infection (within the past 12 months) among newly diagnosed individuals 15 years and above. The Ora-Quick HIV self-test is a triage test and does not provide a definitive HIV-positive diagnosis."],
   source_flags=["Product photographs in the 'Test name' row are not reproduced."]),
]
