exec(open("batches/hiv_common.py").read())
# HIV 2022 part 1, pp.32-39 (Chapter 2: Prevention). Tables: cell text from the PDF ruled grid (grid_extract.py),
# layout checked on the page images; figures written from the images (Figure 2.3 read at 220 dpi).
C2 = "Chapter 2: Prevention of HIV"
B_ = lambda *xs: "<br/>".join("• " + x for x in xs)
ITEMS = [
 D("fig-2.1-combination-prevention", 32, C2 + " > 2.1 HIV Combination Prevention Strategies > Figure 2.1", "Figure 2.1 HIV Combination Prevention Strategies", [],
   "Cycle of three intervention types that together make up combination HIV prevention:\n"
   "- Behavioural interventions: condom use, delaying sexual debut, reducing number of sexual partners\n"
   "- Biomedical interventions: VMMC, condoms, PrEP, PEP, STI screening & treatment, ART for all PLHIV\n"
   "- Structural interventions: decriminalisation laws protecting the rights of PLHIV, reducing stigma and discrimination"),
 T("tbl-2.1-condoms", 33, C2 + " > 2.2 Condoms > Table 2.1 Recommendations for Consistent and Correct Use of Condoms",
   "Table 2.1 Recommendations for Consistent and Correct Use of Condoms", ["0047"],
   [r("Priority Groups", "Key actions")],
   [[C("Heterosexuals who engage in anal sex"), C(B_("Counsel and demonstrate correct and consistent condom use", "Provide adequate condoms",
        "Provide condom-compatible lubricants to MSM and individuals practising anal sex.", "Provide information and counselling on HIV prevention for all, including adolescents"), rs=7)],
    [C("Men who have sex with men")], [C("Transgender people")], [C("Sex workers and clients of sex workers")],
    [C("Sero-different couples (Specific counselling for couples who are trying to conceive, please refer to Chapter 8, Section 8.2.1)")],
    [C("Adolescents (sexually active or not)")], [C("Pregnant and breastfeeding women")]],
   footnotes=["Key message: At every visit, assess knowledge and skill of condom use in all population (sexually active or not) to ensure correct and consistent condom use."]),
 T("tbl-2.5-prep-eligibility", 36, C2 + " > 2.5 Pre-exposure Prophylaxis > Eligibility criteria for PrEP", "Eligibility criteria for PrEP", ["0056"],
   [r("PrEP method", "Eligibility criteria")],
   [r("Any PrEP method", B_("HIV-negative test on the day of PrEP initiation as per national Guidelines.",
        "Absence of symptoms indicating acute HIV infection (AHI) in combination with exposure to HIV in the previous 14 days",
        "No recent exposure within 72 hours to HIV indicates the need for PEP", "Age ≥ 16 years, unless the client is a mature minor ≥ 12 years old",
        "Client willingness to attend scheduled PrEP visits")),
    r("Oral PrEP only", B_("No contra-indication for TDF + 3TC (oral PrEP users only)", "Bodyweight ≥ 30 kg")),
    r("Dapivirine ring only", B_("No contra-indication for Dapivirine"))],
   source_flags=["Column headings added (the PDF table has none). 'No recent exposure within 72 hours to HIV indicates the need for PEP' reads as a garbled criterion: the intended meaning is no exposure in the past 72 hours (an exposure within 72 hours indicates PEP)."]),
 D("fig-2.2-prep-initiation-ahi", 36, C2 + " > 2.5 Pre-exposure Prophylaxis > Figure 2.2 Flowchart for PrEP initiation", "Figure 2.2 Flowchart for PrEP (oral PrEP or the ring) initiation - HIV exposure and acute HIV infection (AHI) assessment", ["0058"],
   "1. HIV-negative?\n"
   "   - If NO: refer for HIV care and treatment.\n"
   "   - If YES: refer to HIV prevention, then ask: exposed to HIV in the past 72 hours?\n"
   "       - If YES: refer to PEP.\n"
   "       - If NO: screen for PrEP, then screen for AHI symptomatically.\n"
   "2. AHI symptoms?\n"
   "   - If NO: start PrEP (standard of care).\n"
   "   - If YES: high-risk sex in the past 14 days?\n"
   "       - If NO: start PrEP (standard of care).\n"
   "       - If YES: defer PrEP, retest for HIV in 28 days AND rescreen for PrEP if still HIV-negative.\n"
   "Key: PEP = post exposure prophylaxis; PrEP = pre-exposure prophylaxis; AHI = acute HIV infection.",
   flags=["The flowchart key defines PrEP as 'Post exposure prophylaxis' (should be pre-exposure prophylaxis).",
          "Deferral here is 'retest in 28 days'; Table 2.2 says defer PrEP for 4 weeks - consistent."]),
 T("tbl-2.2-prep-contraindications", 37, C2 + " > 2.5 Pre-exposure Prophylaxis > Table 2.2 Contraindications to oral pre-exposure prophylaxis",
   "Table 2.2 Contradictions to oral pre-exposure prophylaxis", ["0060"],
   [r("PrEP method", "Contraindications")],
   [r("Any PrEP method", B_("Individuals with an HIV-positive test result using the national HIV testing algorithm.", "Known exposure to HIV in the past 72 hours (offer PEP)",
        "Signs of acute HIV Infection (e.g., flu-like symptoms, sore throat, lymphadenopathy, fever, skin rash) AND a recent exposure in the past 14 days;") +
      "<br/>o if acute HIV infection is suspected, defer PrEP for 4 weeks and re-test the client.<br/>" +
      B_("Known creatinine clearance <60 mL/min.", "Inability to commit to adhere to PrEP and to attend scheduled PrEP visits for repeat HIV testing and medication pick up.")),
    r("Oral PrEP only", B_("Body weight <30 kg.", "Age <16 years except for mature minors (adolescents 12-16) that are already sexually active.")),
    r("Dapivirine ring only", B_("Allergy or hypersensitivity to the active substance or other substances listed in the product information sheet."))],
   source_flags=["Title reads 'Contradictions' (contraindications). Column headings added.",
                 "Creatinine clearance <60 mL/min is listed under 'Any PrEP method', but it is a contraindication to TDF (oral PrEP) only, not to the dapivirine ring."]),
 T("tbl-2.3-start-stop-oral-prep", 38, C2 + " > 2.5.1 Oral PrEP > Table 2.3 Starting and stopping oral PrEP", "Table 2.3 Starting and stopping oral PrEP", ["0066", "0067"],
   [[C("Population (s)", cs=2), C("Starting Oral PrEP"), C("Stopping¹ Oral PrEP")]],
   [r("People assigned males at birth using PrEP to prevent HIV acquisition during sex who are not using oestradiol-based exogenous hormones",
      "Often includes:<br/>-cisgender men<br/>-transgender women who are not using oestradiol-based exogenous hormones<br/>-non-binary people assigned male at birth who are not using oestradiol-based exogenous hormones",
      "Daily or ED: Take a double dose two to 24 hours before potential sexual exposure. Ideally, this loading dose should be taken closer to 24 hours before potential exposure.",
      "Daily or ED: Take a single dose daily for two days after the last potential exposure."),
    r("People using oral PrEP to prevent HIV acquisition from nonsexual exposures<br/>People assigned females at birth<br/>People assigned males at birth who are using oestradiol-based exogenous hormones",
      "Often includes:<br/>-anyone who shares injection-related materials²<br/>-cisgender women<br/>-transgender men<br/>-non-binary people assigned female at birth<br/>-transgender women who are using oestradiol-based exogenous hormones<br/>-non-binary people assigned male at birth who are using oestradiol-based exogenous hormones",
      "Take a single dose daily for seven days before potential exposure.", "Take a single dose daily for seven days after the last potential exposure")],
   footnotes=["¹Procedures for stopping oral PrEP are the same for clients who are discontinuing oral PrEP use indefinitely. Ideally, clients who are discontinuing PrEP use will alert their providers and receive support to use other HIV prevention practices if still needed.",
              "²Injection drug use is mentioned in this guidance; however, first-line prevention strategies for people who inject drugs (PWID) are needle exchange and/or drug use harm reduction and treatment. There are some preventative effects of daily oral PrEP for this population, and it should be offered as part of a larger prevention package."],
   pages=[38, 39], context_before="ED-PrEP regimen: TDF/3TC 300/300 mg or TDF/FTC 300/200 mg by mouth. Dose 1: 2 tablets 2 to 24 hours before sex. Dose 2: 1 tablet 24 hours after the first dose. Dose 3: 1 tablet 24 hours after the 2nd dose.",
   source_flags=["Footnote marker ² does not appear in the table body in the PDF; placed here on 'anyone who shares injection-related materials', which the footnote describes."]),
 D("fig-2.3-ed-prep-examples", 39, C2 + " > 2.5.1 Oral PrEP > Additional guidance for event-driven PrEP > Figure 2.3", "Figure 2.3 How to take Event-Driven PrEP", [],
   "Three examples of ED-PrEP (2+1+1) dosing:\n"
   "1. Sex one time or in one day: sex Friday 11 PM. Take 2 tablets Friday 9 AM, 1 tablet Saturday 9 AM, 1 tablet Sunday 9 AM.\n"
   "2. Sex on multiple consecutive days: sex Friday 11 PM, Saturday 10 PM and Sunday 4 AM. Take 2 tablets Friday 9 AM, then 1 tablet daily at 9 AM on Saturday, Sunday, Monday and Tuesday (continue daily until two days after the last sex).\n"
   "3. Sex on multiple non-consecutive days: sex Friday and Sunday. Take 2 tablets Friday 9 AM, then 1 tablet daily at 9 AM on Saturday, Sunday, Monday and Tuesday."),
]
