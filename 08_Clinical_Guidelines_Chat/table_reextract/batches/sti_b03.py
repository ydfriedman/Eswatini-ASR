exec(open("batches/sti_common.py").read())
# STI/VH draft part 1, pp.42-47 (5.2 male urethral syndrome, anorectal discharge): syndromic chart, point-of-care figures, Tables 4-5.
# From the page images (Figure 2, the anorectal chart and Figure 3 are pictures; the other chart is drawn with text boxes).
CH5 = "5.0 Management of STIs Associated Syndromes"
MUS = CH5 + " > 5.2 Male Urethral Syndrome (MUS)"
ANO = CH5 + " > Anorectal discharge"
HPP = ("Health promotion package:\n- Educate, ensure compliance, and counsel on treatment.\n- Promote abstinence or condom use during treatment.\n"
       "- Promote and demonstrate consistence condom use and provide condoms.\n- Issue one notification slip for each sexual partner and emphasize the importance of partner treatment.\n"
       "- Offer HIV counselling and testing, as per Integrated HIV Guidelines.\n- Offer male circumcision to the uncircumcised.\n- Offer pre exposure prophylaxis as per Guideline.\n"
       "- Provide cervical cancer screening during follow-up visit.")
ITEMS = [
 D("fig-1-chart-3-male-urethral-syndrome", 42, MUS + " > 5.2.1 Chart 3 (Figure 1)", "Figure 1 syndromic treatment chart for male urethral syndrome (chart 3)", ["0088"],
   "Patient complains of urethral discharge or burning on urination\n→ Take history and examine. Provide HIV testing and counselling (opt-out).\n"
   "→ Discharge seen or dysuria confirmed by clinical history?\n"
   "   - NO → Any other STIs syndrome or illness present?\n      - NO → Reassure, counsel and educate; condom promoted and provided.\n      - YES → Treat according to appropriate flow chart.\n"
   "   - YES → Ceftriaxone, 1 g I.M stat PLUS Azithromycin, 1 g orally stat PLUS Metronidazole, 2 g orally stat. Health promotion package and follow up after 7 days.\n"
   "      → Follow up at 7 days: discharge or dysuria present?\n         - NO → Reinforce health promotion package.\n"
   "         - YES → Re-infection? Or poor compliance?\n            - YES → Repeat treatment; reinforce health promotion package.\n"
   "            - NO → Reassure, condom promoted and provided. Refer for further management.\n\n" + HPP,
   flags=["Chart 3 adds metronidazole 2 g to ceftriaxone + azithromycin for male urethral syndrome, while the syndromic regimen in the text above (p.40) is ceftriaxone 1 g + azithromycin 1 g only (metronidazole is listed separately for trichomonas)."]),
 D("fig-2-poc-male-urethral", 43, MUS + " > Point of care management based on results (Figure 2)", "Figure 2 Point of care management of male urethral syndrome", ["0090", "0091"],
   "Person with symptom of urethral discharge from penis → Take medical and sexual history and assess risk for STIs → Physical and genital examination. Then:\n"
   "- Resources and capacity for molecular assays: Perform test → Are results available on same day?\n"
   "   - No* → (go to the limited-capacity pathway: urethral discharge present?)\n"
   "   - Yes → Is test positive for NG/CT?\n      - Yes → Treat based on test results → Offer HIV and syphilis testing and other preventive services.\n"
   "      - No → Offer HIV and syphilis testing and other preventive services.\n"
   "- Limited laboratory capacity: Urethral discharge present?\n   - Yes → TREAT for NG and CT → Offer HIV and syphilis testing and other preventive services.\n"
   "   - No → Offer HIV and syphilis testing and other preventive services.\n"
   "→ See patient in 1 week to see if symptoms persist or recur or contact sooner for treatment based on results of molecular assay.\n\n"
   "NG, N. gonorrhoeae; CT, C. trachomatis.\n* If molecular assay was performed and results were not available on same day, revise the syndromic treatment initially provided according to the test results when available.\n"
   "# If test is negative but urethral discharge is present, treat for non-gonococcal/non-chlamydial urethritis (such as M. genitalium, T. vaginalis or herpes simplex virus).",
   pages=[42, 43], context_before="Figure caption printed at the foot of p.42; the figure (a picture, adapted from the WHO STI guideline) is on p.43."),
 T("tbl-4-mus-treatment", 44, MUS + " > Table 4", "Table 4: First-line and effective treatment substitutes for male urethral syndrome", ["0093", "0094"],
   [r("Infections covered", "First-line options", "Effective substitutes")],
   [[C("In settings in which local antimicrobial resistance data are not available, the WHO STI guideline suggests dual therapy for gonorrhoea.", cs=3)],
    r("N. gonorrhoeae", "Ceftriaxone 1 gram intramuscularly, single dose", "Cefixime 400 mg, orally, single dose<br/>or<br/>Gentamycin 240mg IM Stat<br/>or<br/>Kanamycin 2grams Stat"),
    r("C. trachomatis", "Azithromycin 1 gram, orally, single dose", "Doxycycline 100mg bd x 7 days<br/>or<br/>Erythromycin 500 mg, orally, 4 times a day for 7 days<br/>or<br/>Ofloxacin 200-400 mg, orally, twice a day for 7 days.<br/>(to be given only if gonorrhoea therapy did not include azithromycin)"),
    [C("In settings in which local antimicrobial resistance data reliably confirm the susceptibility of N. gonorrhoeae to the antimicrobial agent, singe therapy may be given.", cs=3)],
    [C("Additional therapeutic options for recurrent or persistent infections", cs=3)],
    r("T. vaginalis", "Metronidazole 2 grams, orally, single doses", "Metronidazole 400 or 500 mg, twice daily for 7 days"),
    r("M. genitalium", "Azithromycin 500 mg, orally on day 1, 250 mg daily on days 2-5", "")],
   source_flags=["Table 4 makes azithromycin 1 g the first-line chlamydia treatment and doxycycline a substitute, while the text above says doxycycline is preferred for ano-rectal infection, and current WHO guidance (2021) prefers doxycycline 100 mg twice daily for 7 days for chlamydia.",
                 "Table 4 lists the gonorrhoea first-line substitutes as cefixime, gentamicin or kanamycin; the text above lists the second-line options as spectinomycin or gentamicin."]),
 D("fig-anorectal-discharge-chart", 46, ANO + " > Flow chart for the syndromic management of anorectal discharge", "Flow chart for the syndromic management of anorectal discharge", ["0097", "0098", "0099", "0100", "0101"],
   "Pain and itchiness → Take history; examine patient including ano-genital area. Then:\n"
   "- Ano-rectal ulcer present? YES → Benzathine Penicillin, 2.4 million units I.M stat PLUS Azithromycin, 1g, orally stat PLUS Acyclovir, 400mg orally TDS for 7 days. Health promotion package and follow up after 7 days.\n"
   "   → Follow-up at 7 days: ulcers and enlargement lymph nodes present?\n      - NO → Reinforce health promotion.\n      - YES → Re-infected or poor compliance → Repeat treatment and re-inforce health promotion package.\n"
   "- Anal discharge present? YES → Ceftriaxone, 250 mg IM stat PLUS Doxycycline 100mg bd 14day or Azithromycin 1gm stat.\n"
   "   → Follow-up at 7 days: improved?\n      - YES → Reinforce health promotion.\n      - NO → Re-infected or poor compliance → Repeat treatment and re-inforce health promotion package.\n\n"
   "Health promotion package:\n- Educate, ensure compliance, and counsel on treatment.\n- Promote abstinence or condom use during treatment.\n- Promote correct and consistent condom use also provide condoms and lubricants.\n"
   "- Issue one notification slip for each sexual partner and emphasize the importance of partner treatment.\n- Offer HIV counselling and testing, as per Integrated HIV Guidelines.\n"
   "- Offer voluntary medical male circumcision.\n- Offer pre exposure prophylaxis as per guideline.",
   flags=["The anorectal discharge chart gives ceftriaxone 250 mg IM (every other regimen in the draft uses 1 g) and doxycycline for 14 days (Table 5: 7 days, or 21 days for LGV)."]),
 D("fig-3-poc-anorectal", 47, ANO + " > Point of care based on results (Figure 3)", "Figure 3: Point-of-care workflow for anorectal discharge", ["0102", "0103"],
   "Person with symptom of anorectal discharge and reports receptive anal sex → Take medical and sexual history and assess risk for exposure to STIs → Perform genital and peri-anal inspection (and anoscopy if available or digital exam if acceptable) (→ Refer for other investigations if anorectal discharge not related to STIs). Then:\n"
   "- Resources and capacity for molecular assays: Perform test → Is test positive for NG/CT/MG?\n   - No → Offer HIV and syphilis testing and other preventive services.\n"
   "   - Yes → Treat based on results → Is there pain? (Yes → TREAT additionally for herpes simplex virus; No →) Offer HIV and syphilis testing and other preventive services.\n"
   "- Limited laboratory capacity: Anorectal discharge present?\n   - Yes → TREAT for NG and CT → Is there pain? (Yes → TREAT additionally for herpes simplex virus) → Offer HIV and syphilis testing and other preventive services.\n"
   "   - No → Offer HIV and syphilis testing and other preventive services.\n→ Review in 1 week if symptoms persist or recur.\n\n"
   "NG, N. gonorrhoeae; CT, C. trachomatis; MG, M. genitalium."),
 T("tbl-5-anorectal-treatment", 47, ANO + " > Treatment based on results > Table 5", "Table 5: Treatment based on results after testing - anorectal discharge", ["0104", "0105"],
   [r("Infections covered", "First-line options", "Effective substitutes")],
   [r("N. gonorrhoeae", "Ceftriaxone 1 g, intramuscularly, single dose", "Cefixime 400 mg, orally, single dose"),
    r("C. trachomatis (25)", "Doxycycline 100 mg orally, twice daily, for 7 days<br/>or<br/>Doxycycline for 21 days (to cover rectal lymphogranuloma venereum) if suspected or confirmed on NAAT<br/>(to be given only if dual therapy did not include azithromycin)", "Erythromycin 500 mg, orally, 4 times a day for 14 days (to be given only if dual therapy did not include azithromycin)")],
   footnotes=["'(25)' after C. trachomatis is a reference number left in the source."]),
]
