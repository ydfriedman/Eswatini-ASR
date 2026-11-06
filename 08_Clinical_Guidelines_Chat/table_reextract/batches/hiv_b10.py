exec(open("batches/hiv_common.py").read())
# HIV 2022 part 2, pp.86-92 (Chapter 5: clinical evaluation, baseline labs, co-trimoxazole). Text from the PDF grid / text layer,
# layout checked on the page images.
C5 = "Chapter 5: Basic Care Package for HIV-Positive Individuals"
B_ = lambda *xs: "<br/>".join("• " + x for x in xs)
ITEMS = [
 B("tbl-5.1-clinical-evaluation", 86, C5 + " > 5.1 Assessment of PLHIV at Initial Contact > Table 5.1", "Table 5.1 Elements of Clinical Evaluation for PLHIV", ["0205", "0208", "0210"],
   "HISTORY\nCurrent and past medical history:\n- Document current presenting complaints and symptoms.\n"
   "- Screen for opportunistic infections such as Covid-19, TB, cryptococcal meningitis, toxoplasmosis, Pneumocystis jiroveci pneumonia (PJP) and other bacterial infections.\n"
   "- Screen for STIs.\n- Document history of TB.\n- Document history of hepatitis B and hepatitis C.\n"
   "- Ask about any other past medical history (e.g., hypertension, diabetes, epilepsy, anaemia, Gastritis and Peptic ulcer disease).\n"
   "- Document previous or current ARV use (including for PMTCT), post-exposure prophylaxis (PEP), pre-exposure prophylaxis (PrEP), and ART.\n"
   "- Establish which current medications (prescription, non-prescription and herbal) are likely to adversely interact with ARVs.\n"
   "- Ask about drug allergies (especially sulphonamide drugs).\n- Family history of HIV testing\n"
   "Psychosocial history:\n- Establish and document social support structures.\n- Establish the possible presence of mental health concerns, depression, substance use, etc.\n"
   "- Encourage disclosure to trusted significant others and sexual partners.\n- Elicit and begin to address possible barriers to adherence to treatment.\n"
   "- Link to an additional facility and community support resources.\n- Employment status and place of employment\n- Family history of NCDs (see Annex 11.22)\n"
   "Sexual and reproductive history:\n- Discuss secondary prevention and avoidance of reinfection with STIs, including combined prevention approaches.\n- Ask about the HIV and ART status of the sexual partner(s).\n"
   "- Encourage HIV testing for all sexual partners of HIV-infected adults, all children of HIV-infected women, and all children whose mother’s HIV status is unknown (index testing).\n"
   "- Assess family planning intentions and contraceptive needs.\n- Screen females for cervical cancer annually and provide appropriate management.\n- Ask about current and past contraceptive use.\n- Assess condom use skills\n"
   "PHYSICAL EXAMINATION\nGeneral appearance of the clients:\n- The appearance of the client depends on the stage of the disease. The clients may look very healthy or be ill-looking and cachectic. Check for Jaundice, clubbing, oedema, nutritional status, lipodystrophy\n"
   "- Check vital signs (respiratory rate, temperature, heart rate, blood pressure, weight/Z score for children/growth chart)\n- Look for cyanosis, clubbing, jaundice, dehydration, pallor and oedema.\n"
   "- Calculate body mass index; use mid-upper arm circumference for pregnant women and children.\n- Temperature: Fever can be present.\n- Pulse: Tachycardia can be present.\n"
   "- Blood pressure: Hypotension, and hypertension can be present.\n- Respiratory rate: Tachypnoea can be seen during fever and respiratory tract infections\n- MUAC\n"
   "- Mental status examination and depression screening where indicated.\n- Look for signs of cryptococcal meningitis and TB as these illnesses will affect the timing of ART initiation; see Section 6.2.\n"
   "Skin:\n- Look out for folliculitis, Kaposi sarcoma, flat warts, secondary syphilis, psoriasis/eczema, seborrheic dermatitis, fungal infections of skin and nails, viral infections like flat warts, molluscum contagiosum and herpes zoster, thin sparse hair etc.\n"
   "Eyes:\n- Retinal haemorrhage, pallor, Kaposi sarcoma, squamous cell carcinoma of the eye, retinal infiltrates, herpes zoster, molluscum contagiosum.\n"
   "Ear, nose and throat:\n- Inflammation of the nasal turbinates may be present, tenderness over sinuses, suppurative otitis media, unilateral/bilateral hearing loss, Kaposi sarcoma, periodontal disease, dental caries in children, oral herpes simplex, oral hairy leucoplakia, oral thrush ± odynophagia, Non-Hodgkin’s lymphoma, orolabial warts.\n"
   "Lungs:\n- Oxygen saturation, cyanosis, dyspnoea, wheezes or stridor, Crackles and rhonchi, dullness to percussion, Increased tactile fremitus\n"
   "Cardiovascular system:\n- Look for signs of heart failure, A heart murmur, and muffled heart sounds can be found.\n"
   "Abdomen:\n- Central obesity, Abdominal distension or tenderness can be found, Hepatomegaly, Splenomegaly, pregnancy and rule out intrauterine growth retardation\n"
   "Genitourinary:\n- Vaginal or urethral discharge, genital ulcers/warts\nExtremities:\n- Muscle weakness, Joint swelling, Muscle wasting and fat redistribution\n"
   "Central nervous system:\n- Focal neurological deficits, confusion or altered mental status, peripheral neuropathy, and Gait disturbances may be present.\n"
   "DIAGNOSIS AND TREATMENT\n- Assign a provisional diagnosis and order confirmatory tests.\n- Document the initial WHO clinical stage and review laboratory tests to make a definitive diagnosis\n"
   "- Manage the presenting illnesses: prompt treatment of inter-current illness contributes to the success of ART and reduces early mortality.\n- Provide STI screening and management.\n"
   "- Refer client for further management if malnourished (e.g., Food by Prescription or Integrated Management of Children Illnesses Guidelines).\n"
   "- Provide or refer for COVID-19 vaccination and other pending immunisations\n- Identify and prioritize care for clients with advanced immunodeficiency to improve client outcomes.\n- Initiate ART and give review date.",
   pages=[86, 87, 88], flags=["'Cardiovascular system' is printed as a bullet under Lungs (a sub-heading); shown here as its own heading. '9index testing' read as '(index testing)'."]),
 T("tbl-5.2-baseline-labs", 89, C5 + " > 5.2 Baseline Laboratory Evaluation of PLHIV > Table 5.2", "Table 5.2 Baseline Laboratory Evaluation Differentiated by Client Category", ["0213", "0214"],
   [r("Population", "Baseline Test", "Comments")],
   [r("All PLHIV: Mild/ Moderate immunodeficiency", "Re-testing for verification<br/>CD4 count<br/>FBC", "Required; refer to Chapter 3 on HIV testing services (HTS)."),
    r("Advanced Immunodeficiency", "TBLAM, CrAg, X-pert MTB/RIF, Serum CrAg, CSF CrAg", "Refer to Section 6.2 for guidance<br/>If CD4 ≤100 cells/mm³, see Figure 6.3 for the CrAg screening algorithm<br/>" + B_("If positive and symptomatic for meningitis, refer the client to the hospital for further investigation", "If positive and asymptomatic, refer to Table 6.19 for fluconazole pre-emptive treatment.", "Reflexive test following CD4 result of ≤100 cells/mm³")),
    r("All TB presumptive clients", "Lateral flow urine lipoarabinomannan assay (LF TB-LAM)", B_("LF TB-LAM is an additional diagnostic tool.", "LF TB-LAM is now offered to all symptomatic PLHIV", "If LF TB-LAM is positive, start DS-TB treatment and follow-up sputum results.") + "<br/>See Figure 6.1 for the TB screening algorithm."),
    r("All PLHIV", "Alanine aminotransferase or aspartate aminotransferase (AST/ALT)", B_("Required to make management decisions for PLHIV with a positive HBsAg test", "If not available, look for signs of liver disease before ART initiation.")),
    [C("All PLHIV", rs=5), C("Creatinine"), C(B_("Recommended for clients being initiated on TDF.", "If not available, rule out renal dysfunction clinically before ART initiation, especially in clients with hypertension and diabetes, and run creatinine when later available. See Section 7.5 and Section 7.7.4"))],
    r("Haemoglobin/full blood count", B_("Full blood count with platelets and prothrombin time test can also be used in the absence of liver function tests.", "Recommended for clients being initiated on zidovudine (AZT). If not available, perform point-of-care haemoglobin using HemoCue® or clinically assess clients for the presence of anaemia.")),
    r("Hepatitis B surface antigen", B_("Can be done as a rapid point of care test.", "If positive, initiate the client on tenofovir (TDF)-based regimen.")),
    r("Pregnancy test", B_("Recommended for women of childbearing age including adolescent girls.")),
    r("Random blood sugar", B_("Recommended for patients at risk of developing diabetes mellitus and those initiating a DTG and PI-based ART regimen"))],
   context_before="Baseline laboratory samples should be collected on the same day as the HIV diagnosis although absence of results should not delay ART initiation."),
 T("tbl-5.3-ctx-dosing", 91, C5 + " > 5.4 Co-trimoxazole Preventive Therapy (CPT) > Cotrimoxazole Dosing > Table 5.3", "Table 5.3 Co-trimoxazole Prophylaxis Dosing for Adults, Adolescents and Children", ["0219"],
   [r("Age", "Weight", "Suspension 200mg sulfamethoxazole (SMZ) + 40 mg trimethoprim (TMP)/ 5 mL", "Paediatric Tablet 100mg SMZ + 20mg TMP Once daily", "Single Strength Adult Tablet 400mg SMZ + 80mg TMP Once Daily", "Double Strength 800mg SMZ + 100mg TMP Once Daily")],
   [r("6 weeks", "<5 kg", "2.5 mL", "1", "1/4", "--"), r("6 months to 5 years", "5–15 kg", "5.0 mL", "2", "1/2", "--"),
    r("≥ 6 years to 14 years", "15–30 kg", "10 mL", "4", "1", "--"), r(">14 years", ">30 kg", "--", "--", "2", "1")],
   rhc=2, context_before="Clients with a history of severe allergy to sulphur should not be given CPT. In such cases, dapsone is a safer alternative.",
   source_flags=["Double-strength tablet given as '800mg SMZ + 100mg TMP'; a double-strength co-trimoxazole tablet is 800 mg SMZ + 160 mg TMP (Table 5.5 also says 160 mg).",
                 "Age bands: '6 weeks' (presumably 6 weeks to <6 months) and '6 months to 5 years' leave no explicit band for 6 weeks-6 months; weight bands are continuous."]),
 T("tbl-5.4-ctx-toxicity-grading", 91, C5 + " > 5.4 Co-trimoxazole Preventive Therapy (CPT) > Cotrimoxazole adverse events > Table 5.4", "Table 5.4 Co-trimoxazole Prophylaxis Toxicity Grading Scale for Adults and Adolescents", ["0220"],
   [r("Toxicity Level", "Clinical Description", "Recommendation")],
   [[C("Grade 1"), C("Erythema"), C("Continue prophylaxis with careful and repeated observation and follow-up. Provide symptomatic treatment, such as antihistamines.", rs=2)],
    r("Grade 2", "Diffuse maculopapular rash, dry desquamation"),
    r("Grade 3", "Vesiculation, mucosal ulceration", "Discontinue Co-trimoxazole preventive therapy (CPT). Desensitization can be considered where a medical doctor is available (see Table 5.5 on CPT desensitization)."),
    r("Grade 4", "Exfoliative dermatitis, Stevens-Johnson syndrome or erythema multiforme, moist desquamation", "Permanently discontinue CPT. Refer client for hospital care.")],
   footnotes=["Document any allergic reactions clearly in the client’s file and appointment card, and report through available pharmacovigilance tools (see Annex 11.29)."]),
 T("tbl-5.5-ctx-desensitization", 92, C5 + " > 5.5 Co-trimoxazole desensitization in adults and adolescents > Table 5.5", "Table 5.5 Co-trimoxazole Prophylaxis Desensitization for Adults and Adolescents", ["0223"],
   [r("Step", "Dose", "Suspension*", "Tablet")],
   [r("Day 1", "80 mg SMZ + 16 mg TMP", "2 mL of oral suspension", "N/A"), r("Day 2", "160 mg SMZ + 32 mg TMP", "4 mL of oral suspension", "N/A"),
    r("Day 3", "240 mg SMZ + 48 mg TMP", "6 mL of oral suspension", "N/A"), r("Day 4", "320 mg SMZ + 64 mg TMP", "8 mL of oral suspension", "N/A"),
    r("Day 5", "400 mg SMZ + 80 mg TMP", "N/A", "1 single-strength SMZ–TMP tablet"), r("Day 6 and onward", "800 mg SMZ + 160 mg TMP", "N/A", "2 single-strength SMZ–TMP tablets or 1 double-strength tablet")],
   footnotes=["*The Co-trimoxazole oral suspension is (200 mg SMZ + 40 mg TMP) / 5 ml"],
   context_before="In instances of Grade 3 reactions to CPT, consider desensitization as described below. In clients with a Grade 4 reaction to CPT, do not attempt desensitization: immediately refer the client to a hospital for further management. Clients undergoing desensitization should be closely monitored.",
   source_flags=["The footnote prints 'TMZ' for TMP."]),
]
