exec(open("batches/sti_common.py").read())
# STI/VH draft part 1, pp.50-60 (5.3 vaginal discharge, cervical infections, 5.4 lower abdominal pain): charts 4-5, Figure 6 and
# Tables 6-8. From the page images; text cut off by cell borders restored from the text layer.
CH5 = "5.0 Management of STIs Associated Syndromes"
VDS = CH5 + " > 5.3. Vaginal Discharge Syndrome (VDS)"
CERV = CH5 + " > Cervical Infections"
LAP = CH5 + " > 5.4 Lower abdominal pain (LAP)"
HPP = ("Health promotion package:\n- Educate, ensure compliance, and counsel on treatment.\n- Promote abstinence or condom use during treatment.\n"
       "- Promote correct and consistent condom use also provide condoms and lubricants.\n- Issue one notification slip for each sexual partner and emphasize the importance of partner treatment.\n"
       "- Offer HIV counselling and testing, as per Integrated HIV Guidelines.\n- Offer voluntary medical male circumcision.\n- Offer pre exposure prophylaxis as per guideline.\n"
       "- Provide cervical cancer screening during follow-up visit.")
ITEMS = [
 D("fig-4-chart-4-vaginal-discharge", 50, VDS + " > 5.3.1 Chart 4 (Figure 4)", "Figure 4 syndromic treatment for vaginal discharge syndrome (chart 4)", ["0110", "0111", "0112"],
   "Patient complains of vaginal discharge/burning micturition or vulval itchiness\n→ Take history and do risk assessment. Perform bi-manual examination and examine including speculum.\n"
   "→ Abnormal discharge or vulval itchiness confirmed?\n"
   "   - NO → Any other STI syndrome or illness present?\n      - NO → Reassure, counsel and educate. Condom promoted and [provided].\n      - YES → Treat according to appropriate flow chart.\n"
   "   - YES → Ceftriaxone, 1 g IM stat PLUS Azithromycin, 1g orally stat PLUS Metronidazole, 2g orally stat. If candida is evident give clotrimazole 500mg pessaries intra-vaginally stat and follow up after 7 days.\n"
   "      → Follow up at 7 days: improved?\n         - YES → Reinforce health promotion.\n         - NO → Re-infection? Or poor compliance?\n            - YES → Repeat treatment and reinforce health promotion package.\n            - NO → Refer for further management.\n\n" + HPP,
   flags=["Chart 4 treats every confirmed vaginal discharge with ceftriaxone + azithromycin + metronidazole, while the text (p.48) says to do a risk assessment first and, if negative, cover only bacterial vaginosis and candidiasis (metronidazole + clotrimazole). The 'Condom promoted and' box text is cut off in the source."]),
 T("tbl-6-vaginal-infections", 51, VDS + " > Table 6", "Table 6: Syndromic treatment options for vaginal infections", ["0113", "0114", "0115", "0116", "0117", "0118", "0119"],
   [r("Infections covered", "First-line options", "Effective substitutes")],
   [[C("- Therapy for bacterial vaginosis and trichomoniasis<br/>Plus<br/>- Therapy for yeast infection if curd-like white discharge, vulvovaginal redness and itching are present", cs=3)],
    r("Bacterial vaginosis", "Metronidazole 2 grams, orally, single dose", "Clindamycin 300 mg, orally, twice daily for 7 days or<br/>Metronidazole 400 mg or 500 mg, orally, twice daily for 7 days"),
    r("T. vaginalis", "Metronidazole 2 grams, orally, in a single dose or", "Tinidazole 2 grams orally, single dose or<br/>Tinidazole 500 mg orally, twice daily for 5 days<br/>Metronidazole 400 mg or 500 mg, orally, twice daily for 7 days"),
    r("C. albicans (yeast infection)", "Clotrimazole vaginal tablet, 500 mg, as a single dose or<br/>Miconazole vaginal pessaries, 200 mg inserted at night for 3 nights or", "Clotrimazole vaginal tablet, 100 mg, at night for 6 days<br/>or<br/>Fluconazole 150 mg (or 200mg), orally, single dose<br/>OR<br/>Nystatin, 200,000-unit vaginal tablet, inserted at night for 7 nights<br/>or"),
    r("N. gonorrhoeae", "Ceftriaxone 1 g, intramuscularly, single dose", "Cefixime 400 mg, orally, single dose"),
    r("C. trachomatis", "Doxycycline 100 mg, orally, twice daily for 7 days<br/>(to be given only if gonorrhoea therapy did not include azithromycin)", "Azithromycin 1 gram, orally, single dose<br/>or<br/>Erythromycin 500 mg, orally, 4 times a day for 7 days<br/>or<br/>Ofloxacin 200-400 mg, orally, twice daily for 7 days<br/>(to be given only if gonorrhoea therapy did not include azithromycin)"),
    r("M. genitalium", "Azithromycin 500 gram, orally day 1, 250 mg daily, days 2-5 (absence of macrolide resistance)", "")],
   pages=[51, 52, 53],
   footnotes=["NB: People taking metronidazole should be cautioned to avoid alcohol.", "The header row is on p.51; the body rows are on pp.52-53. Several cells end with a dangling 'or' as printed."],
   source_flags=["Table 6 gives M. genitalium azithromycin as '500 gram' on day 1 (should be 500 mg).",
                 "Table 6 makes doxycycline first-line and azithromycin a substitute for chlamydia, the reverse of Table 4 (male urethral syndrome)."]),
 T("tbl-7-cervical-infections", 55, CERV + " > Management of cervical infections > Table 7", "Table 7: Treatment for cervical infections", ["0123", "0124"],
   [[C("- Therapy for uncomplicated N. gonorrhoeae plus<br/>- Therapy for C. trachomatis", cs=4)],
    r("Infections covered", "First-line options (choose one from each cell below)", "Effective substitutes", "Options for pregnant women or during breastfeeding")],
   [r("N. gonorrhoeae", "Ceftriaxone 1 gram, intramuscularly, single dose", "Cefixime 800 mg, orally, single dose<br/>Plus test of cure OR<br/>Cefixime 800 mg plus Azithromycin 2 grams", "Ceftriaxone 1 gram, intramuscularly, single dose or<br/>Cefixime 800 mg, orally, single dose plus test of cure or<br/>Cefixime 800 mg, orally, single dose plus Azithromycin 2 gram, orally, single dose"),
    r("C. trachomatis", "Doxycycline 100 mg, orally, twice daily for 7 days<br/>(to be given only if gonorrhoea therapy did not include azithromycin)", "Azithromycin 1 gram, orally, single dose or<br/>Erythromycin 500 mg, orally, 4 times a day for 7 days or<br/>Ofloxacin 200-400 mg, orally, twice daily for 7 days<br/>(to be given only if gonorrhoea therapy did not include azithromycin)", "Erythromycin 500 mg, orally, 4 times a day for 7 days or<br/>Azithromycin 1 gram, orally, single dose<br/>(to be given only if gonorrhoea therapy did not include azithromycin)"),
    r("M. genitalium", "Doxycycline 100mg for 7 days followed by 1g azithromycin for 1 day then 500mg for 3 days)", "Moxifloxacin 500 mg x 7 days<br/>Pristinamycin or Minocycline or sitafloxacin", "Azithromycin 1 gram, orally, day 1, 500 mg daily, days 2-5 (absence of macrolide resistance)")],
   source_flags=["Table 7 gives cefixime 800 mg as the gonorrhoea substitute (Tables 4-6 and the text use cefixime 400 mg).",
                 "Table 7 gives moxifloxacin 500 mg for 7 days for M. genitalium (the usual dose is 400 mg once daily) and an azithromycin course of 1 g then 500 mg x 3 days (first-line) vs 1 g then 500 mg days 2-5 (pregnancy column) vs 500 mg then 250 mg days 2-5 (Tables 4 and 6)."]),
 D("fig-5-chart-5-lower-abdominal-pain", 58, LAP + " > 5.4.1 Chart 5 (Figure 5)", "Figure 5 syndromic treatment for lower abdominal pain (chart 5)", ["0129", "0130", "0131"],
   "Woman complains of LAP with or without vaginal discharge\n→ Take history including (gynaecological) and physical examination (abdominal and vaginal).\n"
   "→ Any of the following present? Missed/overdue period or recent delivery/abortion/miscarriage? Abdominal guarding and/or rebound tenderness? Or abnormal vaginal bleeding?\n"
   "   - YES → Do pregnancy test; set up an IV line; do resuscitation measures if necessary; refer for emergency medical care.\n"
   "   - NO → Pain on moving the cervix? Or lower abdominal tenderness with or without vaginal discharge?\n"
   "      - NO → Any other STI syndrome or illness present? (NO → Provide health promotion package and refer accordingly; YES → Treat according to appropriate flowchart.)\n"
   "      - YES → Ceftriaxone 1 g i.M. stat PLUS Azithromycin 1 g PO/week x 2 weeks PLUS Metronidazole 400 mg PO bid x 7-14 days and advise to come early within 3 days, or earlier if worsening.\n"
   "         → Follow up at 3 days: improved? (YES → Finalize treatment; re-inforce health promotion package. NO → Refer for further management.)\n\n" + HPP,
   flags=["Chart 5 gives azithromycin 1 g weekly for 2 weeks and metronidazole 400 mg twice daily for 7-14 days for lower abdominal pain, while Table 8 gives doxycycline 100 mg twice daily for 14 days and metronidazole 500 mg twice daily for 14 days."]),
 D("fig-6-poc-lower-abdominal-pain", 59, LAP + " > Figure 6", "Figure 6: Flow chart for management of lower abdominal pain", ["0132", "0133", "0134"],
   "Sexually active woman with symptom of lower abdominal pain → Take medical and sexual history and assess risk for exposure to STIs → Genital examination (including bi-manual palpation) and speculum examination (where feasible).\n"
   "→ Any of the following present? Missed/overdue period; recent delivery/abortion/miscarriage; abdominal guarding and/or rebound tenderness; abnormal vaginal bleeding; abdominal mass.\n"
   "   - Yes → Refer patient urgently for surgical or gynaecological opinion and assessment. Before referral set up an IV line and apply resuscitative measures if necessary.\n"
   "   - No → Is there lower abdominal tenderness or cervical motion tenderness?\n"
   "      - Yes → Manage for PID; test for NG/CT/MG if available*; see patient in 3 days → Patient has improved? (No → Refer patient; Yes → Offer HIV and syphilis testing and other preventive services.)\n"
   "      - No → Any other illness found? (Yes → Manage appropriately; No → Offer HIV and syphilis testing and other preventive services.)\n\n"
   "* to support partner notification. NG, N. gonorrhoeae; CT, C. trachomatis; MG, M. genitalium.",
   context_before="A picture adapted from the WHO STI guideline ('Fig. 6.' in its own heading)."),
 T("tbl-8-lower-abdominal-pain", 60, LAP + " > Table 8", "Table 8: Treatment options for lower abdominal pain (anaerobic infections)", ["0135", "0136"],
   [[C("Therapy for uncomplicated Neisseria gonorrhoeae PLUS<br/>Therapy for Chlamydia trachomatis<br/>PLUS<br/>Therapy for anaerobic infections", cs=3)], r("Infections covered", "First choice", "Effective substitutes")],
   [r("Neisseria gonorrhoeae", "Ceftriaxone 1 gram IM single dose", "- Cefixime 800 mg orally single dose PLUS<br/>- Azithromycin 2 gram orally single dose"),
    r("Chlamydia trachomatis", "Doxycycline 100 mg orally twice a day for 14 days", "- Erythromycin 500 mg four times daily for 14 days<br/>(NB. To be given only if gonorrhoea therapy did not include Azithromycin)"),
    [C("The treatment for anaerobes must be included in either treatment options above", cs=3)],
    r("Anaerobes", "Metronidazole 500 mg orally two times a day for 14 days", "")],
   footnotes=["'14 days' for metronidazole and the end of the erythromycin note are cut off by the cell border on the page; taken from the text layer."]),
]
