exec(open("batches/hiv_common.py").read())
# HIV 2022 part 1, pp.65-70 (Chapter 3: testing algorithms and counselling). Figures from the page images (Figure 3.8 read at 250 dpi;
# its text layer is unreadable), tables from the images with wording checked against the text layer.
C3 = "Chapter 3: HIV Testing Services"
O = lambda *xs: "<br/>".join("∞ " + x for x in xs)
ITEMS = [
 D("fig-3.8-infant-testing-algorithm", 65, C3 + " > 3.9 HIV Testing Algorithm > 3.9.1 HIV testing in Infants and Children Less Than 18 Months > Figure 3.8", "Figure 3.8 HIV testing algorithm for Infants and Children Less Than 18 Months", ["0146"],
   "HIV-exposed newborn (0-3 days): conduct NAT (RNA and/or DNA PCR).\n"
   "- Positive: infant is infected. Immediately start ART; repeat NAT (RNA and/or DNA PCR) using a new sample to confirm infection.\n"
   "- Indeterminate: repeat NAT.\n"
   "    - Indeterminate again: do not report as positive or initiate ART but maintain prophylaxis in accordance with national guidelines. Request a new sample and repeat NAT (RNA and/or DNA PCR) after 2 weeks. Further review by multidisciplinary team.\n"
   "- Negative: HIV infection not detected, but if infant/child is breastfed the risk of acquiring HIV remains high until cessation of breastfeeding. Regular clinical monitoring; conduct NAT at 6-8 weeks, at 9 months and at 12 months.\n"
   "    - Positive: infant is infected. Immediately start ART; repeat NAT (RNA and/or DNA PCR) using a new sample to confirm infection.\n"
   "    - Negative: HIV infection not detected, but if infant/child is breastfed the risk of acquiring HIV remains high until cessation of breastfeeding. Conduct antibody testing at 18 months of age OR at 2 months after cessation of breastfeeding, whichever comes first.",
   flags=["Final antibody test 'at 18 months of age OR at 2 months after cessation of breastfeeding, whichever comes first': a test before breastfeeding has stopped cannot exclude infection; WHO gives the final diagnosis at 18 months or 3 months after cessation of breastfeeding, whichever is LATER. Figure 3.9 says RDT 3 months after cessation of breastfeeding (not 2).",
          "The first box reads 'Infected is infected' (infant is infected)."]),
 T("tbl-3.7-eid-indeterminate-ct", 65, C3 + " > 3.9.1 HIV testing in Infants and Children Less Than 18 Months > Indeterminate Test Results > Table 3.7", "Table 3.7 Indeterminate range cycle threshold equivalents of current nucleic acid infant diagnosis assays", ["0148"],
   [r("Assay", "Estimated indeterminate range cycle threshold")],
   [r("Abbott m-PIMA™ HIV-1/2 Detect", "Not available"), r("Roche COBAS® Ampliprep/COBAS® TaqMan® HIV-1 Qualitative Test v2.0", "≥33"),
    r("Roche COBAS® HIV-1 Quantitative nucleic acid test for use on the COBAS® 6800/8800 Systems", "≥37")],
   context_before="An indeterminate range** of viral copy equivalents should be used to improve the accuracy of all nucleic acid-based early infant diagnosis assays. **Indeterminate range refers to a range of viral copy equivalents that would be too low to be accurately diagnosed as HIV-infected.",
   footnotes=["Repeat samples following an indeterminate result should be given priority in the laboratory.", "Infants/children with repeated indeterminate results need a multidisciplinary team of healthcare providers to support retention, tracking and status resolution.",
              "Clinical monitoring and further testing based on the national infant testing schedule need to be done until a definitive HIV status is established."]),
 D("fig-3.9-infant-confirmatory-testing", 66, C3 + " > 3.9.1 > Confirmatory testing of positive test results and managing discordant results > Figure 3.9", "Figure 3.9 Confirmatory HIV testing algorithm for Infants and Children Less Than 18 Months", ["0151"],
   "1. NAT (first EID test) positive: repeat NAT using a new sample to confirm infection. Do not delay ART initiation.\n"
   "2. Second NAT positive: continue ART.\n   Second NAT negative: stay on ART; repeat NAT (a third) using a new sample to confirm infection.\n"
   "3. Third NAT positive: continue ART.\n   Third NAT negative: stop ART, then follow-up testing after treatment interruption:\n"
   "   - If infant is breastfeeding: conduct NAT at 4 weeks, at 4 months and at 8 months after treatment interruption. Conduct RDT 3 months after cessation of breastfeeding.\n"
   "   - If infant is not breastfeeding or stops before completion of follow-up: conduct NAT at 4 weeks, at 4 months and at 8 months after treatment interruption.\n"
   "Before interrupting ART after discordant results (positive then negative) followed by a third negative test: the infant should have no clinical signs or symptoms suggesting HIV infection; a follow-up plan should be agreed with the family, caregiver(s) and healthcare staff; tracking information (phone, address, etc.) of the family and caregiver(s) should be collected and confirmed.",
   flags=["The branches in the figure are not labelled positive/negative; read from the layout and the text above the figure (second negative NAT -> third NAT before considering interruption)."]),
 B("tbl-3.8-serial-testing-steps", 67, C3 + " > 3.9.2 HIV testing in Adults, Adolescents and Children Older Than 18 Months > Table 3.8", "Table 3.8 Serial HIV Testing Steps for Rapid Testing in Adults and Children Above 18 Months", ["0153", "0154"],
   "Perform HIV testing as follows:\n"
   "1. Perform testing with Test 1 (Determine) through a finger-prick.\n2. If non-reactive, the result is interpreted and communicated as HIV-negative.\n3. If reactive, a second test is done using Test 2 (UniGold).\n"
   "4. If Test 2 (UniGold) is reactive, the result is interpreted and communicated as HIV-positive.\n"
   "5. If Test 2 (UniGold) is non-reactive (i.e., Determine and UniGold are inconclusive), repeat testing using Test 1 (Determine) and Test 2 (UniGold) in parallel. Collecting blood by venepuncture is recommended to minimize client discomfort from subsequent multiple finger pricks.\n"
   "6. If both repeat tests are non-reactive, the result is interpreted and communicated as HIV-negative.\n7. If both repeat tests are reactive, the result is interpreted and communicated as HIV-positive.\n"
   "8. If repeat tests remain Inconclusive (i.e., Determine test is reactive and UniGold test is non-reactive, or vice versa), appoint the client in two weeks and repeat parallel testing.\n"
   "9. If both repeat tests are non-reactive, the result is interpreted and communicated as HIV-negative.\n10. If both repeat tests are reactive, the result is interpreted and communicated as HIV-positive.\n"
   "11. If repeat tests remain Inconclusive (i.e., Determine test is reactive and UniGold test is non-reactive, or vice versa) collect samples for NAT (RNA and/or DNA PCR) and send a sample to the National Reference Laboratory for testing. All specimens referred to the National Reference Laboratory should be accompanied by a Laboratory Request Form. Then appoint clients in two weeks to receive results.\n"
   "12. If NAT (RNA and/or DNA PCR) results are Positive/ Detected, the result is interpreted and communicated as HIV-positive.\n13. If NAT (RNA and/or DNA PCR) results are Negative/ Undetected, the result is interpreted and communicated as HIV-negative.",
   flags=["The text refers to the algorithm as 'Table 3.8 and Table 3.9'; the algorithm is Figure 3.10 (Table 3.9 is the post-test counselling summary)."]),
 D("fig-3.10-serial-testing-algorithm", 68, C3 + " > 3.9.2 HIV testing in Adults, Adolescents and Children Older Than 18 Months > Figure 3.10", "Figure 3.10 Eswatini Serial HIV testing algorithm for Adults and Children above 18 Months", ["0156"],
   "1. Test 1: Determine.\n   - Determine non-reactive: report as HIV negative.\n   - Determine reactive: Test 2: Unigold.\n"
   "2. Unigold after reactive Determine:\n   - Determine reactive, Unigold reactive: report as HIV positive.\n   - Determine reactive, Unigold non-reactive: result inconclusive -> repeat Determine and Unigold (parallel testing).\n"
   "3. Parallel testing results:\n   - Both reactive: report as HIV positive.\n   - Both non-reactive: report as HIV negative.\n   - Determine reactive/Unigold non-reactive, or Determine non-reactive/Unigold reactive: result inconclusive -> appoint client in 2 weeks' time and repeat parallel testing.\n"
   "4. Repeat parallel testing after 2 weeks:\n   - Both reactive: report as HIV positive.\n   - Both non-reactive: report as HIV negative.\n   - Either discordant pattern: result inconclusive -> conduct NAT (RNA and/or DNA PCR) and re-appoint client in 2 weeks.\n"
   "5. NAT (RNA and/or DNA PCR) positive: report as HIV positive. NAT negative: report as HIV negative.\n"
   "Key: procedures (white), negative (green), positive (red), inconclusive (amber)."),
 D("fig-3.11-post-test-counselling-summary", 69, C3 + " > 3.10 Post-Test Counselling > General Post-Test Counselling Principles > Figure 3.11", "Figure 3.11 Summary of Post-Test Counselling", ["0159"],
   "Key messages that begin ART preparation for all PLHIV:\n- ART is available and is recommended for everyone confirmed as HIV-positive.\n"
   "- Starting treatment as soon as possible (preferably same day or within 7 days of testing HIV-positive) reduces the chance of worsening illness or transmitting HIV to others.\n"
   "- Encourage partner notification and disclosure.\n- If a client takes ART properly and does not miss pills, they can expect to live a long and productive life and significantly minimize the risk of passing HIV to sexual partners, unborn or breastfeeding children.",
   flags=["Timing of ART start differs within the chapter: 'same day or within 7 days' here, 'today or within 2 weeks of diagnosis' in Table 3.5."]),
 T("tbl-3.9-post-test-counselling", 69, C3 + " > 3.10 Post-Test Counselling > Table 3.9 Summary of post-test counselling", "Table 3.9 Summary of post-test counselling", ["0161", "0162"],
   [[C("Post-test counselling for both positive and negative results should include:", cs=2)]],
   [[C(O("Simple and clear communication of test results", "Check the client’s understanding of the result", "Opportunities for the client to ask questions", "Development of a coping strategy for the client",
         "Assessment of referral needs for other services", "Discussion of disclosure of test results", "Discussion of partner and family referral for HIV testing",
         "Clarify misconceptions and myths about HIV transmission and risks", "Referrals for relevant services"), cs=2)],
    r("Counselling for HIV-negative clients should also include:", "Counselling for HIV-positive clients should also include:"),
    r(O("Explanation of window period and recommendation of when to re-test based on their risk profile.", "Important to not encourage unnecessary re-testing.",
        "Discussion of partner testing, methods to prevent HIV such as VMMC, correct and consistent use of condoms, PrEP, PEP and reducing the number of sexual partners.",
        "Scheduling of ongoing supportive counselling sessions as per client need. Referral for prevention and other health services where indicated.",
        "Offer prevention services if eligible (VMMC, PrEP, Condoms, PEP)"),
      O("Supporting the emotions arising from the test result.", "Discussion of any immediate concerns.", "Informing the individual of available chronic HIV care and ART services.",
        "Informing client about benefits of Test and Start and active referral for treatment.", "Information on preventing HIV transmission.", "Discussion of “positive living.”",
        "Scheduling a follow-up counselling session if indicated.", "Referral to HIV care services and support groups.", "Assisted partner notification, disclosure and follow-up as needed",
        "Conduct elicitation of contacts (sexual partner, biological children (if female), family members and associates) and identify index referral options for each contact",
        "Assessment of other SRH needs, including FP"))],
   rhc=0),
 T("tbl-3.10-special-populations-counselling", 70, C3 + " > 3.10 Post-Test Counselling > Counselling for Special Populations > Table 3.10", "Table 3.10 Additional Key Counselling Messages for Special Populations", ["0163", "0164"],
   [r("Special Population", "Specific counselling messages to be included:")],
   [r("Couples and partners", "Counsel on the following points:<br/>" + O("Mutual support and disclosure.", "Male and female condom use.", "Contraception/ safer conception for future pregnancies.",
        "Partner and family testing and index testing services.", "Serodifference and how to stay negative, including offering PrEP for the negative partner in a serodifferent couple")),
    r("Pregnant and lactating women", "Counsel on the following points:<br/>" + O("Childbirth plans.", "Contraception/ safer conception for future pregnancies.", "Partner testing, notification and disclosure.",
        "Adequate nutrition for the mother, including iron and folic acid supplements.", "Infant feeding options.",
        "For HIV-positive pregnant and lactating women, Test and Start for the mother’s health and PMTCT should be promoted as well as the importance of HIV testing for the infant reviewed.")),
    r("Children", O("Younger children should be told their status incrementally to accommodate their cognitive skills and emotional maturity in preparation for full disclosure.")),
    r("Adolescents girls, Young women /men", O("Listen and address adolescents’ concerns.", "Focus on risky behaviour and develop risk reduction plans.", "If the test is positive, reassure them that they can live a long healthy life.",
        "Clarify misconceptions and myths.", "Provide condoms and refer to appropriate prevention, care and treatment services.")),
    r("Key populations", O("Remind clients of the modes of transmission of HIV.", "Provide and offer condoms, contraceptives and lubricants, and referrals for prevention, treatment and care, including the availability of PrEP, STI testing and treatment, and needle and syringe programmes.",
        "Offer options for Event led PrEP as per guidelines for MSM", "Discourage reuse of needles, razors and syringes.", "Encourage and support partner testing, notification and disclosure.", "Early treatment of STIs", "Encourage and emphasize VMMC"))]),
]
