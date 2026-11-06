exec(open("batches/sti_common.py").read())
# STI/VH draft guidelines part 1 (STI_1.pdf = pages 1-70; printed page = PDF page - 19 from p.20): front matter and Tables 1-2.
# From the page images; cell text from the ruled grid (grid_draft.py) with overflowing cell text restored from the text layer.
# NOTE: the old chunks came from a differently paginated version of this draft; replaces are matched by content, not page.
CH4 = "4.0 Laboratory Diagnosis of STIs and VH"
ITEMS = [
 B("box-writing-team", 6, "Acknowledgements > Writing team", "Writing team and Editorial and Validation team", [],
   "Writing team:\n"
   "- MoH - SRHU: Mngcineni Ndlangamandla, Nomkhosi Bhembe, Zandile Masangane, Wiseman Mngometulu, Diana Aebi - Nkambule\n"
   "- MoH - SNAP: Takhona Mkhabela, Mpumelelo J Mavimbela\n- MoH - ENLS: Oupa Dlamini, Gugu Tsabedze\n- MoH - NTDs: Nhlanhla Mhlanga\n- MoH - CMS: Pholile Maphalala\n"
   "- Sithobela Health Centre: Mr. Jabulani Nkuwa\n- PPGH: Lamile Tsabedze\n- FTM Clinic: Phumzile Myeza\n"
   "- World Health Organization: Dr. Nomthandazo Dlamini, Dr. Kisyeri Nicholus\n- UNFPA: Tamary Silindza\n- UNICEF: Nokuthula Mdluli\n"
   "- Médecins Sans Frontières (MSF): Dr. Hayk Karakozian\n- UNESWA: Dr. Colile Dlamini\n- ASPIRE: Dr. Kikanda Kindandi\n- ICAP: Sam Simelane\n"
   "- Baylor: Sr Thembela Mavuso\n- FLAS: Phindile Nkambule\n- CANGO: Sifiso Sigudla\n\n"
   "Editorial and Validation team:\n"
   "- MoH - SNAP: Mpumelelo J Mavimbela, Khanyisile Nyembe, Nomphilo Gwebu, Nhlanhla Magagula\n- MoH - SRHU: Nozipho Motsa - Nzunza\n- MoH - EPI: Xolisile Dlamini\n"
   "- MoH - M&E: Nompumelelo Mthunzi\n- ICAP: Dr Tesfay Abreha, Siphiwe Shongwe-Gama, Gugulethu Manyatsi\n"
   "- World Health Organization: Dr. WI Teodora (Geneva), Dr. Machekera, Shepherd\n- Médecins Sans Frontières (MSF): Dr. Pablo Valladares (Geneva), Dr. Djoki Joss\n"
   "- Baylor: Makhosazana Dlamini, Dr Jaime Petros\n- AHF: Dr. Nkululeko Dube\n- CANGO: Sifiso Sigudla\n- CHAI: Qhubekani Mphala, Celani Nkambule, Thandolwethu Hlatshwako, Nokuphila Ndzinisa",
   pages=[5, 6, 7]),
 T("tbl-1-abbreviations", 18, "Abbreviations", "Table 1: Abbreviations and acronyms used in these guidelines", [],
   [r("Abbreviation", "Meaning")],
   [r("AIDS", "Acquired immunodeficiency syndrome"),
    r("AMR", "Antimicrobial resistance"),
    r("ART", "Antiretroviral therapy"),
    r("BCC", "Behaviour change communication"),
    r("BID", "Twice a day"),
    r("BV", "Bacterial vaginosis"),
    r("CT", "Chlamydia trachomatis"),
    r("DAA", "Direct-acting antiviral"),
    r("FTA", "Fluorescent treponemal antibody"),
    r("GBV", "Gender-based violence"),
    r("GUD", "Genital ulcer disease"),
    r("HBV", "Hepatitis B virus"),
    r("HCV", "Hepatitis C virus"),
    r("HIV", "Human immunodeficiency virus"),
    r("HMIS", "Health management information system"),
    r("HPV", "Human papillomavirus"),
    r("HSV", "Herpes simplex virus"),
    r("HTS", "HIV testing services"),
    r("IM", "Intramuscular"),
    r("IU", "International unit"),
    r("IUD", "Intra-uterine device"),
    r("IV", "Intravenous"),
    r("LGV", "Lymphogranuloma venereum"),
    r("MoH", "Ministry of Health"),
    r("NAAT", "Nucleic acid amplification test"),
    r("NG", "Neisseria gonorrhoeae"),
    r("PEP", "Post-exposure prophylaxis"),
    r("PID", "Pelvic inflammatory disease"),
    r("PMTCT", "Prevention of mother-to-child transmission"),
    r("PO", "Orally"),
    r("POC", "Point of care"),
    r("PrEP", "Pre-exposure prophylaxis"),
    r("QID", "Four times a day"),
    r("RPR", "Rapid plasma reagin"),
    r("STAT", "Immediate dose"),
    r("STI", "Sexually transmitted infection"),
    r("TID/TDS", "Three times a day"),
    r("TPHA", "Treponema pallidum haemagglutination assay"),
    r("TV", "Trichomonas vaginalis"),
    r("UDS", "Urethral discharge syndrome"),
    r("VCT", "Voluntary counselling and testing"),
    r("VDS", "Vaginal discharge syndrome"),
    r("VH", "Viral hepatitis"),
    r("VIA", "Visual inspection of the cervix with acetic acid"),
    r("VMMC", "Voluntary medical male circumcision"),
    r("WHO", "World Health Organization")],
   footnotes=["Printed in two side-by-side column pairs; listed here alphabetically."]),
 T("tbl-2-diagnostic-tests", 32, CH4 + " > 4.1 Recommended diagnostic tests by infection", "Table 2: Recommended laboratory and point-of-care tests for the STIs and viral hepatitis covered by these guidelines", ["0064", "0065", "0066", "0067"],
   [r("Infection / pathogen", "Recommended test", "Specimen", "Notes")],
   [r("Neisseria gonorrhoeae (gonorrhoea)", "NAAT, laboratory or point of care (e.g. GeneXpert); culture where AMR surveillance is required", "First-void urine (male); vaginal or endocervical swab; rectal or pharyngeal swab per exposure", "Culture is the only method yielding an isolate for antimicrobial susceptibility testing. No quality-assured rapid test exists for NG alone."),
    r("Chlamydia trachomatis (chlamydia)", "NAAT, laboratory or point of care", "First-void urine (male); vaginal or endocervical swab (self-collected acceptable); rectal or pharyngeal swab", "Reference standard. Serology is not recommended for genital infection."),
    r("C. trachomatis serovars L1-L3 (LGV)", "NAAT with LGV genotyping at a reference laboratory", "Ulcer swab, bubo aspirate or rectal swab", "Refer specimen onward; genotyping is not available at facility level."),
    r("Trichomonas vaginalis", "NAAT preferred; POC antigen test or saline wet-mount microscopy where NAAT is unavailable", "Vaginal swab; first-void urine (male)", "Wet mount has low sensitivity - a negative result does not exclude infection."),
    r("Mycoplasma genitalium", "NAAT, with macrolide-resistance markers where available", "First-void urine; vaginal swab", "Test only in persistent or recurrent urethritis or cervicitis. Do not screen asymptomatic people."),
    r("Treponema pallidum (syphilis)", "Treponemal test (RDT, TPHA, TPPA or FTA) plus non-treponemal test (RPR or VDRL) with titre; dual HIV/syphilis RDT in antenatal care", "Whole blood by fingerprick for RDT; serum for laboratory tests", "WHO also recommends syphilis self-testing as an additional option. An RPR titre is required to monitor treatment response."),
    r("Herpes simplex virus types 1 and 2", "NAAT (PCR) on lesion material", "Swab from the base of an unroofed vesicle or ulcer", "Type-specific serology only in selected cases. Viral culture is insensitive."),
    r("Haemophilus ducreyi (chancroid)", "Multiplex genital ulcer NAAT where available; otherwise clinical diagnosis", "Ulcer swab", "Culture requires specialised media and is not routinely available."),
    r("Klebsiella granulomatis (donovanosis)", "Microscopy for Donovan bodies on a tissue crush preparation or biopsy", "Lesion tissue", "Culture is not routine."),
    r("Human papillomavirus (HPV)", "HPV DNA or mRNA testing as the primary cervical screening test; VIA where HPV testing is unavailable", "Cervical or vaginal sample (self-collection acceptable)", "Anogenital warts are diagnosed clinically - no laboratory test is required."),
    r("HIV", "Serial or parallel rapid diagnostic testing per the national algorithm; NAAT for infants", "Whole blood by fingerprick; plasma or serum", "Offer to every patient presenting with an STI, and retest per national guidelines."),
    r("Hepatitis B virus (HBV)", "HBsAg by RDT or laboratory immunoassay; HBV DNA viral load to assess treatment eligibility", "Whole blood by fingerprick for RDT; serum or plasma", "HBeAg and ALT support staging. Test all pregnant women at least once per pregnancy."),
    r("Hepatitis C virus (HCV)", "Anti-HCV antibody by RDT or laboratory assay; HCV RNA or core antigen to confirm viraemia", "Whole blood by fingerprick for RDT; serum or plasma", "Antibody alone cannot distinguish current from past infection."),
    r("Bacterial vaginosis", "Vaginal pH and microscopy using Nugent score or Amsel criteria", "Vaginal swab", "Not an STI in the strict sense. No NAAT required."),
    r("Vulvovaginal candidiasis", "Saline or KOH wet-mount microscopy; culture for recurrent disease", "Vaginal swab", "Clinical diagnosis is usually sufficient."),
    r("Scabies, pediculosis pubis and molluscum contagiosum", "Clinical diagnosis; dermoscopy or microscopy of the mite or louse if uncertain", "Not applicable", "No laboratory test is required.")],
   pages=[32, 33],
   footnotes=["In the source, the text of several cells overflows the cell and is cut off on the page ('NG alone', 'where NAAT is unavailable', 'asymptomatic people', 'HPV testing is unavailable', 'confirm viraemia', 'Amsel criteria'); the full text is taken from the text layer."]),
]
