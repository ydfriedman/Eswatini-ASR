exec(open('batches/anc_common.py').read())
E = ""
COUNS = "Nutrition; diet; physical activity, rest, HIV test; avoid: caffeine intake, alcohol/tobacco/substance abuse; IPV, danger signs, emergency preparedness"
MAT = "Ask how mother is doing, clinical estimation of gestational age, physical examination, SFH/abdominal palpation, TB screening, IPV, ask about foetal movements, rule out PROM"
PREV = "IFA, calcium, combination prevention (PrEP, condom, VMMC for men)"
EGP = "Weight, BP, MUAC, male involvement, STI screening"
OTH = "Complete ANC card and give to woman; fill ANC register/CMIS"
FET = "FHR auscultation, ask about foetal movements"
def row(c, mat, fet, cou, poc, lab, rad, prev, egp, tm): return r(c, mat, fet, cou, poc, lab, rad, prev, egp, tm, OTH)
ITEMS = [
 T("tbl-mnch-indicators", 7, "1.0 Background > 1.2 Situation Analysis", "Table 1. Key MNCH indicators in Eswatini 2007-2018: ANC coverage, content of ANC, skilled birth attendance, institutional deliveries, caesarean section, postnatal care, stillbirths, maternal and neonatal mortality", ["0010", "0011", "0012"],
   [[C("Key indicator"), C("2007 ³"), C("2010 ⁴"), C("2012 ⁵"), C("2014 ⁶"), C("2017 ⁷"), C("2018")]],
   [r("Antenatal care coverage (%)", "97.1", "96.8", "97", "98.5", "95", "96"),
    r("Content of antenatal care (%)", E, "80.6", "80.6", "90", "90", "90"),
    r("Skilled attendant at delivery (%)", "74.3", "82", "82", "88.3", "88.3", "88.3"),
    r("Institutional deliveries (%)", "74.1", "80.4", "80.4", "87.7", "87.7", "87.7"),
    r("Caesarean section (%)", "7.9", "12.3", E, "11.6", "12", "14"),
    r("7–14 days post-partum (%)", E, E, "45", "59", "71", "75"),
    {"section": "Newborn deaths"},
    r("Macerated stillbirths", E, E, E, E, E, "239"), r("Fresh stillbirths", E, E, E, E, E, "168"), r("ENND", E, E, E, E, E, "226"),
    {"section": "Impact"},
    r("Maternal mortality ratio", E, E, "593", E, E, "117"), r("Neonatal mortality rate", "22", "23", E, "20", E, "20")],
   pages=[7, 8],
   footnotes=["³ Swaziland Demographic and Health Survey, 2017 (as printed for the 2007 column). ⁴ MICS, 2010. ⁵ Swaziland Demographic and Housing Survey, 2012. ⁶ MICS 2014. ⁷ SRH Report, 2017."],
   source_flags=["The 2007 column cites the 'Swaziland Demographic and Health survey, 2017'.", "Units are not given (percentages, counts, per 100,000 / per 1,000)."]),
 T("tbl-anc-contact-schedule", 13, "2.0 ANC Contact Schedule > 2.1 New Schedule of ANC Contacts", "Eight ANC contacts schedule: 1st contact 8-12 weeks, then 20, 26, 30, 34, 36, 38 and 40 weeks", ["0024"],
   [[C("Contact"), C("Recommended schedule")]],
   [r("1st contact", "As soon as the woman suspects she is pregnant; during the first trimester (preferably 8–12 weeks)"),
    r("2nd scheduled contact", "20 weeks"), r("3rd scheduled contact", "26 weeks"), r("4th scheduled contact", "30 weeks"),
    r("5th scheduled contact", "34 weeks"), r("6th scheduled contact", "36 weeks"), r("7th scheduled contact", "38 weeks"), r("8th scheduled contact", "40 weeks")],
   context_before="A new model with eight scheduled contacts is adopted (WHO 2016), replacing focused ANC (4 visits), to reduce perinatal mortality and improve women's experience of care."),
 T("tbl-anc-essential-package", 14, "2.0 ANC Contact Schedule > 2.2 Essential Package of ANC Interventions", "Essential package of ANC interventions at each of the 8 contacts: maternal and foetal assessment, counselling topics, point-of-care tests, lab investigations, ultrasound, preventive measures (IFA, calcium, deworming, PrEP), clinical practices, management, and cadres", ["0026", "0027", "0028", "0029", "0030", "0031", "0032", "0033", "0034", "0035", "0036", "0037", "0038", "0040", "0042", "0043"],
   [[C("Contact"), C("Maternal assessment"), C("Foetal assessment"), C("Counselling topics (information, education and counselling)"), C("Point-of-care tests"), C("Lab investigations"), C("Radiological tests"), C("Preventive measures"), C("Essential good clinical practices"), C("Treat / manage"), C("Others")]],
   [r("Contact 1 at 8–12 weeks", "Comprehensive history taking; clinical estimation of gestational age; examination head to toe; TB screening; screening for IPV", "—",
      "Nutrition; diet; physical activity, rest, HIV test and partner testing, adherence to medicines prescribed; danger signs, emergency preparedness, early stimulation of the baby, VMMC counselling, condom usage; avoid: caffeine intake, alcohol/tobacco/substance abuse",
      "HIV, syphilis, Hep B, urine dipstick, malaria, Hb", "Blood group and Rhesus; full blood count; check for ASB (Gram stain or culture); viral load, CD4 count; Hep B",
      "Ultrasound", "Iron and folic acid, calcium, TT/Td; combination prevention (PrEP, condom, VMMC for men); prophylaxis as needed", "Weight, height, BP, MUAC, male involvement, STI screening",
      "Common physiological disorders; STIs; complications of early pregnancy; ART; refer as per client's needs", OTH),
    row("Contact 2 at 20 weeks", "Assess general wellbeing, clinical estimation of gestational age, physical examination, SFH/abdominal palpation, TB screening, screening for IPV", "FHR auscultation in beats per minute; enquire about quickening",
        "Nutrition; diet; physical activity, rest, HIV test; avoid: caffeine intake, alcohol/tobacco/substance abuse; IPV, danger signs, emergency preparedness, early stimulation of the baby; condom usage re-enforcement, VMMC counselling",
        "Urine dipstick, HIV and syphilis re-test for those who were negative or not tested at the 1st contact, malaria test", "—", "Ultrasound if not yet done",
        "Anthelminthic (mebendazole); IFA, calcium, combination prevention (PrEP, condom, VMMC for men)", EGP, "Common physiological disorders; complications of early pregnancy; refills as indicated; refer as per client's needs"),
    row("Contact 3 at 26 weeks", MAT, FET, COUNS + ", IYCF, early stimulation of the baby", "Urine dipstick, malaria test", "Check Hb; check ASB", "Ultrasound if indicated", PREV, EGP, "Common physiological disorders; complications of pregnancy; refer as per client's needs"),
    row("Contact 4 at 30 weeks", MAT, FET, COUNS + ", IYCF, breastfeeding, breast care, FP/HTSP, birth planning, EIMC, early stimulation of the baby", "Urine dipstick, HIV and syphilis re-test for those who were negative, malaria test", "—", "Ultrasound if indicated", PREV, EGP, "Common physiological disorders; manage complications of pregnancy; refer as per client's needs"),
    row("Contact 5 at 34 weeks", MAT, FET, COUNS + ", IYCF, breastfeeding, FP/HTSP, breast care, birth planning, EIMC, early stimulation of the baby, signs of true labour, coping during labour, baby layette", "Urine dipstick, malaria test", "Check ASB", "Ultrasound if indicated", PREV, EGP, "Common physiological disorders; manage complications of pregnancy; refer as per client's needs"),
    row("Contact 6 at 36 weeks", MAT, FET, COUNS + ", IYCF, breastfeeding, FP/HTSP, EIMC, early stimulation of the baby, signs of true labour, coping during labour, baby layette", "Urine dipstick, malaria test", "Check Hb", "Ultrasound if indicated", PREV, EGP, "Common physiological disorders; manage complications; refer as per client's needs"),
    row("Contact 7 at 38 weeks", MAT, FET, COUNS + ", IYCF, breastfeeding, FP/HTSP, EIMC, early stimulation of the baby, signs of true labour, coping during labour, baby layette", "Urine dipstick, HIV and syphilis re-test for those who were negative, malaria test", "—", "Ultrasound if indicated", PREV, EGP, "Common physiological disorders; manage complications; refer as per client's needs"),
    row("Contact 8 at 40 weeks", MAT + ", ask about symptoms of labour", FET, COUNS + ", IYCF, breastfeeding, FP/HTSP, EIMC, early stimulation of the baby; counsel on admission if no signs of labour at 41 weeks", "Urine dipstick, malaria test", "—", "Ultrasound if indicated", PREV, EGP, "Common physiological disorders; manage complications; refer as per client's needs"),
    r("Cadres to provide the services", "Midwives, obstetricians, doctors", "Midwives, obstetricians, doctors", "Midwife, general nurse, nursing assistants, dieticians, nutritionist, health promotion, community health workers, doctors, obstetrician, sonographers", "Midwives, general nurses, doctors", "Lab technician", "Radiology, sonographers, obstetricians, midwives", "Nursing assistants; general nurse, midwives", "Midwives (BP), obstetricians (BP), doctors (BP); community health workers (weight, MUAC, height)", "Midwives, doctors, obstetricians", "Midwives, obstetricians, doctors")],
   pages=list(range(14, 23)), rhc=1,
   footnotes=["NB: 1. All cadres will be expected to provide IEC; depending on the roster, all midwives will be expected to provide individual counselling. 2. Health promotion will be done for community engagement. 3. Complete the ANC card, enter information into the register and give the card to the pregnant woman. 4. ANC services are offered at clinic, PHU and health centre. 5. Referral for complications to the next level.",
              "IPV – intimate partner violence; HTSP – healthy timing and spacing of pregnancy; IYCF – infant and young child feeding; EIMC – early infant male circumcision; ASB – asymptomatic bacteriuria; IFA – iron and folic acid; SFH – symphysis-fundal height; FHR – foetal heart rate."],
   source_flags=["The PDF prints each contact as a rotated landscape table with no text layer; cells were transcribed from the page images.", "Several cells are printed twice (contact 3, 4 and 5 preventive measures, clinical practices, management and 'Others'), and on contact 5 text from the maternal-assessment and counselling cells overflows into the preventive-measures and clinical-practices cells. Cleaned up here; the order of the overflow text was inferred.", "The 'Cadres' row on p.22 has six columns in the first block and five in the second; mapped to the 11 columns in printed order, so the mapping should be checked.", "Calcium and IFA are listed at every contact but doses are not given in this table."]),
]
