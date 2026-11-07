exec(open("batches/sti_common.py").read())
# STI/VH draft part 2 (STI_2.pdf = document pages 71-151, offset 70), pp.71-85: Table 9, syphilis algorithms (Figures 7-9, pictures),
# syphilis-in-pregnancy chart, balanitis chart, Table 10, Figure 10. From the page images; Figure 10 read from a 230 dpi render.
CH6 = "6.0 Mixed STI Syndromes"
CH7 = "7.0 Management of Other STI’s And Related Clinical Conditions"
SY = CH7 + " > 7.1 Management of reactive syphilis test cases"
HPP = ("Health promotion package:\n- Educate, ensure compliance, and counsel on treatment.\n- Promote abstinence or condom use during treatment.\n"
       "- Promote correct and consistent condom use also provide condoms and lubricants.\n- Issue one notification slip for each sexual partner and emphasize the importance of partner treatment.\n"
       "- Offer HIV counselling and testing, as per Integrated HIV Guidelines.\n- Offer voluntary medical male circumcision.\n- Offer pre exposure prophylaxis as per guideline.")
ITEMS = [
 T("tbl-9-mixed-sti-syndromes", 71, CH6 + " > Table 9", "Table 9: Treatment of mixed STI syndromes", ["0160", "0161", "0162"],
   [r("Mixed Sexually Transmitted Infections", "Treatment (new episode)")],
   [r("UDS + SSS", "Ceftriaxone 1g IM STAT + Azithromycin, 1 g orally per week for 2 weeks + Metronidazole, 2g orally STAT + Supportive therapy: to reduce pain advice bed rest, scrotal elevation with a scrotal support (T-bandage) and analgesics."),
    r("UDS + Balanitis", "Ceftriaxone, 1 g IM STAT /Cefixime, 400mg orally STAT + Azithromycin 1 g orally STAT / Doxycycline, 100mg orally BID for 7 days + Metronidazole, 2g orally STAT + Clotrimazole cream, local application BID for 7 days."),
    r("UDS + GUS", "Ceftriaxone 1g IM STAT /Cefixime, 400mg orally STAT + Acyclovir, 400mg orally TDS for 7days + Benzathine Penicillin 2.4mu IM STAT + Azithromycin, 1g orally STAT /Doxycycline, 100mg orally BID for 7 days + Metronidazole, 2 g orally STAT."),
    r("VDS + LAP", "Ceftriaxone 1g IM STAT + Azithromycin, 1g orally per week for 2 weeks + Metronidazole, 400mg orally BID for 7-14 days. Clotrimazole pessary to be added, if vulval oedema, itching, excoriations or curd-like discharge present."),
    r("VDS + GUS (non-pregnant)", "Ceftriaxone 1g IM STAT/ Cefixime, 400mg STAT + Metronidazole, 2g orally STAT + Benzathine Penicillin, 2.4mu IM STAT Azithromycin, 1g orally STAT /Doxycycline, 100mg orally BID for 7 days + Acyclovir, 400mg orally TDS for 7 days. Clotrimazole pessary to be added, if vulval oedema, itching, excoriations or curd-like discharge"),
    r("VDS + GUS (pregnant, breastfeeding)", "Ceftriaxone 1g IM STAT /Cefixime, 400mg STAT / + Metronidazole, 2g orally STAT + Benzathine Penicillin, 2.4mu IM STAT + Azithromycin 1g orally STAT / Erythromycin, 500mg orally QID for 7 days + Acyclovir, 400mg orally TDS for 7 days. Clotrimazole pessary to be added, if vulval oedema, itching, excoriations or curd-like"),
    r("LAP + GUS", "Ceftriaxone 1g IM STAT + Metronidazole, 400 mg orally BID for 7-14 days + Benzathine Penicillin, 2.4mu IM STAT + Azithromycin, 1g orally per week for 2 weeks /Doxycycline, 100mg orally BID for 7-14 days + Acyclovir, 400 mg orally TDS for 7 days."),
    r("SSS + GUS", "Ceftriaxone, 1 g IM STAT + Benzathine Penicillin, 2.4mu IM STAT + Azithromycin, 1g orally per week for 2 weeks/Doxycycline, 100mg orally BID for 7-14 days +Acyclovir, 400mg orally TDS for 7 days<br/>*In Penicillin-allergic patients: Give Doxycycline (non-pregnant women) or Erythromycin (pregnant women) for 14 days")],
   pages=[71, 72], context_before="Definition: client presenting with more than one syndrome.",
   footnotes=["The VDS + GUS rows end mid-sentence ('...curd-like discharge' / '...curd-like') as printed. UDS urethral discharge syndrome; SSS scrotal swelling; GUS genital ulcer; VDS vaginal discharge; LAP lower abdominal pain."],
   source_flags=["Table 9 adds metronidazole 2 g to urethral discharge combinations (UDS + SSS, UDS + balanitis, UDS + GUS), as in chart 3, although the male urethral syndromic regimen in the text has no metronidazole; LAP combinations use metronidazole 400 mg BID for 7-14 days while Table 8 gives 500 mg BID for 14 days."]),
 D("fig-7-syphilis-option-1", 76, SY + " > 7.1.1 Syphilis testing and treatment algorithm > Figure 7", "Figure 7: Syphilis testing and treatment algorithm — Option 1: where RPR or VDRL testing is available", ["0170", "0171", "0172"],
   "Option 1: RPR/VDRL testing available.\nPatient with suspected syphilis → Perform RPR/VDRL test → Result?\n"
   "- Reactive → Stage syphilis (clinically assess stage) → Treat for syphilis (per stage of disease) → Monitor with RPR/VDRL at 3, 6, and 12 months.\n"
   "- Non-reactive → Clinical suspicion? (ulcer or rash present) → Yes → Treat presumptively; repeat RPR in 2-4 wks → Monitor with RPR/VDRL at 3, 6, and 12 months.\n"
   "→ Fourfold decline in titre = adequate treatment response."),
 D("fig-8-syphilis-option-2", 77, SY + " > 7.1.1 Syphilis testing and treatment algorithm > Figure 8", "Figure 8: Syphilis testing and treatment algorithm — Option 2: where RDT/Tp testing is available", ["0173", "0174"],
   "Patient with suspected syphilis → Perform treponemal RDT → Result?\n"
   "- Reactive → History of treatment? (documented prior Rx)\n   - No → Treat for syphilis → Treat partners, counsel, follow up.\n   - Yes → Assess for reinfection signs → Treat partners, counsel, follow up.\n"
   "- Non-reactive → Syphilis unlikely (consider other causes) → If high clinical suspicion: treat and repeat in 2-4 wks.\n"
   "Limitation: treponemal RDT stays reactive after treatment; cannot confirm active vs past infection without non-treponemal test.",
   context_before="The figure's own title line is cut off at the top of the picture."),
 D("fig-9-syphilis-option-3", 78, SY + " > 7.1.1 Syphilis testing and treatment algorithm > Figure 9", "Figure 9: Syphilis testing and treatment algorithm — Option 3: where RDT/Tp and non-treponemal testing are available", ["0175", "0176", "0177", "0178"],
   "Patient with suspected syphilis → Step 1: Perform treponemal RDT → RDT result?\n"
   "- Non-reactive → Syphilis unlikely; if clinical suspicion, repeat.\n"
   "- Reactive → Step 2: Perform RPR/VDRL → RPR/VDRL result?\n"
   "   - Reactive → Active syphilis: stage and treat → Record baseline titre; monitor at 3, 6, 12 months → Fourfold decline in RPR/VDRL titre = adequate treatment response.\n"
   "   - Non-reactive → Past treated syphilis or very early infection → History of prior treatment? (check records) → No → Treat for syphilis; Yes → No treatment.\n\n"
   "Below the figure an older chart is printed over the text of 7.1.2 (overlapping shapes): SERUM → RPR/VDRL → Positive results / Negative results; positive → RDT/Tp → Positive results / Negative results; positive → Confirmed syphilis: treat. Legend fragment: 'Tp = [treponemal test]; [RP]R = Non-trepo[nemal test]'.",
   flags=["On p.78 an older syphilis testing chart (serum → RPR/VDRL → RDT/Tp → confirmed syphilis, treat) is printed on top of the opening lines of section 7.1.2 Syphilis in pregnancy, hiding part of the text - a layout error in the draft."]),
 D("chart-syphilis-in-pregnancy", 80, SY + " > 7.1.2 Syphilis in pregnancy > Chart 8", "Syndromic chart for syphilis in pregnancy (chart 8)", ["0181", "0182", "0183"],
   "Pregnant woman at her first antenatal care (ANC) visit → Take history and examine; explain need for syphilis screening; provide HIV testing and counselling and do pre-test counselling for HIV. Then:\n"
   "- Any STI(s) present? YES → Treat according to appropriate flow chart.\n"
   "- Take blood for: RPR/RDT-Tp; HIV test, after counselling; other routine ANC tests.\n"
   "   - RPR/RDT-Tp (syphilis test) positive?\n      - NO → Provide health promotion package to pregnant woman and partner.\n"
   "      - YES → Mother: treat with Benzathine Penicillin, 2.4 million units IM weekly x 3 weeks. Offer examination and treatment to partner. Provide health promotion package to pregnant woman and partner. Repeat RPR/RDT-Tp testing after 3 months of treatment.\n"
   "        AND treat all newborns of mother with positive RPR/RDT-Tp: Rx: Benzathine Penicillin 50 000 IU/kg IM stat/ Procaine Penicillin G 150 000 IU/kg IM, 12 hourly for 14 days. If allergic Erythromycin 50mg/kg divided doses 6 hourly 30 days.\n"
   "   - HIV test positive? YES → Provide post-test counselling; refer to PMTCT, where available. NO → Repeat HIV test every 3 months if any STI present.\n\n" + HPP,
   flags=["The syphilis-in-pregnancy chart treats every positive mother with benzathine penicillin weekly for 3 weeks (the regimen for late latent or unknown-duration syphilis; early syphilis needs a single dose), and gives the newborn 'Procaine Penicillin G 150 000 IU/kg IM, 12 hourly for 14 days' - procaine penicillin is 50 000 IU/kg once daily for 10 days (12-hourly dosing is for aqueous benzyl penicillin); erythromycin for 30 days does not treat congenital syphilis."]),
 D("chart-balanitis", 83, CH7 + " > 7.2 Balanitis and balanoposthitis > Flowchart for syndromic treatment of balanitis", "Flowchart for syndromic treatment of balanitis and balanoposthitis", ["0188", "0189", "0190"],
   "Patient complains of soreness and or itching on penis → Take history and examine. Retract foreskin and clean with water.\n"
   "→ Erythema or erosions confirmed?\n   - NO → Counsel and educate; condom promoted and provided; offer HTC; refer accordingly.\n"
   "   - YES (as printed, one YES arrow goes to 'Treat according to appropriate flow chart') → Teach local hygiene PLUS Clotrimazole cream applied locally twice a day for 7 days. Cloxacillin and Metronidazole may be given if secondary bacterial infections present. Provide health promotion package and follow up after 7 days.\n"
   "      → Follow up at 7 days: improved? YES → Reinforce health promotion package. NO → Re-infection? Or poor compliance? Or no glycosuria on urinalysis? (YES → Repeat treatment; reinforce health promotion package. NO → Refer for further management.)\n\n" + HPP,
   flags=["The balanitis chart has two YES arrows from 'Erythema or erosions confirmed?' (one to 'Treat according to appropriate flow chart', one to the clotrimazole regimen), and asks 'No glycosuria on urinalysis?' where the intent is presumably to check for diabetes (glycosuria) in recurrent candidal balanitis. Its caption ('Figure 10: Flowchart for syndromic treatment of balanitis...') is printed two pages later under a different figure."]),
 T("tbl-10-upper-vaginal-infection", 84, CH7 + " > Treatment options for upper vaginal infection > Table 10", "Table 10: Treatment options for upper vaginal infection", ["0191", "0192", "0193"],
   [[C("- Therapy for uncomplicated N. gonorrhoeae (24)<br/>Plus<br/>- Therapy for C. trachomatis (25)", cs=4)],
    r("Infections covered", "First-line options", "Effective substitutes", "Options for pregnant women or during breastfeeding")],
   [[C("In settings in which local antimicrobial resistance data are not available, the WHO STI guidelines suggest dual therapy for gonorrhoea.", cs=4)],
    r("N. gonorrhoeae", "Ceftriaxone 1 g, intramuscularly, single dose plus Azithromycin 1 gram, orally, single dose", "Cefixime 400 mg, orally, single dose plus Azithromycin 1 gram, orally, single dose", "Ceftriaxone 250 mg, intramuscularly, single dose plus Azithromycin 1 gram, orally, single dose or Cefixime 400 mg, orally, single dose plus Azithromycin 1 gram, orally, single dose"),
    r("C. trachomatis", "Doxycycline 100 mg, orally, twice daily for 7 days (to be given only if gonorrhoea therapy did not include azithromycin)", "Azithromycin 1 gram, orally, single dose or Erythromycin 500 mg, orally, 4 times a day for 7 days or Ofloxacin 200-400 mg, orally, twice daily for 7 days (to be given only if gonorrhoea therapy did not include azithromycin)", "Erythromycin 500 mg, orally, 4 times a day for 7 days or Azithromycin 1 gram, orally, single dose (to be given only if gonorrhoea therapy did not include azithromycin)"),
    r("M. genitalium", "Azithromycin 500 gram, orally day 1, 250 mg daily, days 2-5 (absence of macrolide resistance)", "", "Azithromycin 500 gram, orally, day 1, 250 mg daily, days 2-5 (absence of macrolide resistance)")],
   footnotes=["'(24)', '(25)' are reference numbers left in the source. The end of the ofloxacin note is cut off by the cell border on the page."],
   source_flags=["Table 10 gives ceftriaxone 250 mg for pregnant women (1 g for everyone else) and azithromycin '500 gram' for M. genitalium; the section has no text explaining what an 'upper vaginal infection' is (it sits between balanitis and genital warts)."]),
 D("fig-10-buccal-problem", 85, CH7 + " > Figure 10 (assessment and management of a buccal problem)", "Figure 10 (picture): Assessment and management of a buccal problem in an STI context (printed caption: 'Flowchart for syndromic treatment of balanitis and balanoposthitis')", ["0194", "0195", "0196"],
   "Assessment and management of a buccal problem in an STI context. Always offer HIV test!\n"
   "- Small lesions ulcerated (or vesicular), grouped in clusters, painful? yes → Herpes possible: clean the area with mouthwashes; give paracetamol. Antiviral treatment: Acyclovir PO 400mg x3/day, for 5 or 7 days. This treatment reduces the duration of symptoms only if initiated within 5 days of a 1st episode (duration 7 days) or within 24 hours of a recurrence (duration 5 days).\n"
   "- Presence of mouth ulcer(s), unique or multiple? yes → Mouth ulceration. Treat: Syphilis*: Benzathine benzylpenicillin G IM 2.4 MUI (half dose in each buttock) single dose (SD). If it is painful or/and regional lymph nodes or/and not resolving with first treatment - suspect soft chancre: add Azithromycin PO 1g SD. Recommend: treatment of partners from the last 3 months with the same treatment (benzathine benzylpenicillin G IM 2.4 MUI SD for syphilis and/or azithromycin PO 1g SD for soft chancre). Give azithromycin PO 1g SD to everyone. Abstain from sexual practices with contact with the ulcer or use condoms until the ulcer resolves. Follow-up consultation after 7 days.\n"
   "- Presence of painless growths: wart(s) or condyloma? yes → Complicated warts: indication for surgical treatment, or with imiquimod. Refer to the hospital.\n"
   "- Presence of a whitish coating in the mouth? yes → Pain on swallowing and/or dysphagia and/or extensive lesions on the pharynx?\n"
   "   - yes → Oropharyngeal candidiasis: treatment fluconazole 400 mg/day, for 14 days. HIV-AIDS must be ruled out.\n"
   "   - no → Oral candidiasis: treatment miconazole muco-adhesive, 1 tablet/day, for 7 days; if severe or recurrent: fluconazole PO 200 mg/day, for 10 days. HIV-AIDS must be ruled out.\n"
   "- Presence of inflammation of the throat (in a context of fellatio)? yes → Pharyngitis: can be caused by Chlamydia trachomatis or Neisseria gonorrhoeae; however, the big majority of pharyngitis are viral. If risk factors of STI** AND oral sex → NG/CT pharyngeal swab for PCR and syphilis RDT.\n\n"
   "* The presence of the ulcers indicates an infection called 'early'. In this context, the treponemal test (SD Bioline, etc.) can still be negative in 30% of cases.\n"
   "** FDR of STI, MSM, urethral discharge in the partner, context of sexual violence or prostitution, new partner or more than one partner in the preceding 3 months.",
   flags=["Figure 10's caption says 'Flowchart for syndromic treatment of balanitis and balanoposthitis', but the picture is a slide on oral (buccal) STI problems with no section text around it; it appears to have been pasted from another document (slide number 5 is visible)."]),
]
