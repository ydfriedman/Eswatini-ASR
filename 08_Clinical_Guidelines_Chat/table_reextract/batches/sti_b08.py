exec(open("batches/sti_common.py").read())
# STI/VH draft part 2, pp.86-93 (7.3 genital warts, PID treatment table, 7.5 survivors of sexual violence): Table 11, genital warts
# chart, PID table (printed over the warts chart), Table 12, Figure 11 (picture, read from a 260 dpi render).
CH7 = "7.0 Management of Other STI’s And Related Clinical Conditions"
GW = CH7 + " > 7.3 Genital Warts"
SV = CH7 + " > 7.5 Management of Survivors Of Sexual Violence"
ITEMS = [
 T("tbl-11-genital-warts", 86, GW + " > Recommended management of genital warts > Table 11", "Table 11: Treatment options for genital warts by site", ["0200", "0201"],
   [r("Site of warts", "First line treatment options", "Effective substitutes", "If woman is pregnant and Lactating")],
   [r("External penile, vulval and anal", "Podophyllin 25% tincture of benzoin, applied carefully to the warts while protecting the surrounding area with vaseline, once weekly. Wash off after 4 hours in adults and after 2 hours in children. Treatment should be repeated until lesions resolve completely, if there is no improvement after 6 weeks then refer for further management.",
      "Podophyllotoxin (Podofilox) 0.5% solution or gel applied BID for 3 days, followed by 4 days of no treatment, with the cycle repeated up to 4 times.<br/>OR<br/>Imiquimod 5% cream (it is user friendly but expensive), applied with a finger at bedtime, left overnight, 3 times a week for as long as 16 weeks<br/>OR<br/>Trichloroacetic acid (TCA) 80-90%, once a week. Wash off after 4 hours",
      "Podophyllin should not be applied in pregnant and lactating patients. Use other treatment options such cauterization, diatherm cryotherapy, imiquimoid 5% cream. guidelines Provide health education on personal hygiene"),
    [C("NB:<br/>- Not more than 5 ml of Podofilox and Podophyllin should be applied per day.<br/>- Podophyllin application should be done under medical supervision and patient should be warned against self-medication.<br/>- Cervical, meatal and urethral warts should be managed by expert<br/>- Sometimes warts never go away completely,<br/>- Treatment does not protect future infections of the syphilis. Although curable, any damage done by the syphilis bacteria cannot be reversed.", cs=4)]],
   pages=[86, 87], footnotes=["The header row is on p.86 and the body on p.87; 'after 4 hours' (TCA) is hidden by the cell border on the page and taken from the text layer."],
   source_flags=["Table 11 recommends imiquimod in pregnancy (not recommended: safety not established) and its NB about syphilis ('Treatment does not protect future infections of the syphilis...') belongs to another section; trichloroacetic acid is not washed off (it is applied and allowed to dry)."]),
 D("chart-genital-warts", 88, GW + " > Flowchart for management of Genital warts", "Flowchart for management of genital warts", ["0202", "0203"],
   "Patient complains of painless itchy growths in the genital, anal and or oral region → Take history and examine.\n"
   "→ Genital warts confirmed?\n   - NO → Any other STI syndrome or illness present? (NO → Reassure; counsel and educate; condom promoted and provided; refer to higher level. YES → Treat according to appropriate flow chart.)\n"
   "   - YES → Any of the following presentation/s? Intra-vaginal or cervical warts; peri-anal or ano-rectal warts; warts larger than 10 mm present.\n"
   "      - YES (as printed) → Rx: apply 20-25% Podophyllin, while carefully protecting the surrounding area with vaseline, to be washed off after 4 hours. Treatment should be repeated weekly until lesions resolve completely. Or podophyllotoxin 0.5% applied bid. Advise cervical cancer screening for female patients.\n"
   "      → Review after six weeks of application, if improved? (YES → Continue treatment until healed; reinforce health promotion package. NO → Refer for further management.)\n\n"
   "Health promotion package (partly hidden on the page by the overlapping table): educate, ensure compliance, and counsel on treatment; promote abstinence or condom use during treatment; promote correct and consistent condom use also provide condoms and lubricants; issue one notification slip for each sexual partner and emphasize the importance of partner treatment; offer HIV counselling and testing, as per Integrated HIV Guidelines; offer voluntary medical male circumcision; offer pre exposure prophylaxis as per guideline.",
   flags=["In the genital warts chart, intra-vaginal, cervical, ano-rectal or large (>10 mm) warts lead to podophyllin treatment, whereas Table 11 says cervical, meatal and urethral warts should be managed by an expert (podophyllin is not used on internal or cervical warts).",
          "On p.88 the 'Treatment options for pelvic inflammatory disease' heading and table are printed on top of the lower part of the genital warts chart and its health promotion box - a layout error in the draft."]),
 T("tbl-pid-treatment-options", 88, CH7 + " > Treatment options for pelvic inflammatory disease", "Treatment options for pelvic inflammatory disease (untitled table)", ["0204", "0205", "0206"],
   [[C("- Therapy for uncomplicated N. gonorrhea<br/>- Therapy for C. trachomatis<br/>- Therapy for anaerobic infections", cs=3)], r("Infections covered", "First-line options", "Effective substitutes")],
   [[C("In settings in which local antimicrobial resistance data are not available, the WHO STI guidelines suggest dual therapy for gonorrhoea.", cs=3)],
    r("N. gonorrhoeae", "Ceftriaxone 1 g, intramuscularly, single dose plus Azithromycin 1 gram, orally, single dose", "Cefixime 400 mg, orally, single dose plus Azithromycin 1 gram, orally, single dose"),
    r("C. trachomatis", "Doxycycline 100 mg, orally, twice daily for 14 days", "Erythromycin 500 mg, four times daily for 14 days (to be given only if gonorrhoea therapy did not include azithromycin)"),
    [C("In settings in which local antimicrobial resistance data reliably confirm the susceptibility of N. gonorrhoeae to the antimicrobial agent, singe therapy may be given as below.", cs=3)],
    r("N. gonorrhoeae", "Ceftriaxone 1 g, intramuscularly, single dose", "Cefixime 400 mg, orally, single dose"),
    [C("The treatment for anaerobes must be included in either treatment option above.", cs=3)],
    r("Anaerobes", "Metronidazole 400 mg or 500 mg, orally, twice daily for 14 days", "")],
   pages=[88, 89],
   footnotes=["Printed in the genital warts section, on top of the warts chart (p.88), continuing on p.89; it repeats the lower abdominal pain treatment (Table 8) with small differences (metronidazole 400 or 500 mg here)."]),
 T("tbl-12-sexual-assault-presumptive", 92, SV + " > Table 12", "Table 12: Presumptive STI treatment for survivors of sexual assault", ["0214", "0215", "0216"],
   [r("Treatment")],
   [r("Ceftriaxone 1g IMI STAT OR Cefixime 400mg STAT OR Spectinomycin 2g IM STAT"), r("PLUS"),
    r("Azithromycin 1g IMI STAT OR Doxycycline 100mg 12hrly x 7 days"), r("PLUS"),
    r("Metronidazole 2g PO STAT OR Metronidazole 400mg PO 12hrly x 7 days")],
   context_before="Include other measures: (the text after the table lists syphilis and HIV tests, pregnancy test and emergency contraception, HIV PEP and hepatitis B vaccine).",
   footnotes=["'7 days' for the metronidazole alternative is cut off by the cell border on the page."],
   source_flags=["Table 12 gives 'Azithromycin 1g IMI STAT' (azithromycin is oral) and ceftriaxone 1 g, while Figure 11 on the next page gives ceftriaxone 250 mg; the text's emergency contraception (4 combined pills, Yuzpe method) differs from Figure 11 (levonorgestrel 1.5 mg, ulipristal or copper IUD)."]),
 D("fig-11-sexual-violence", 93, SV + " > 7.5.1 Chart 11 (Figure 11)", "Figure 11: Syndromic treatment for management of survivors of sexual violence", ["0217", "0218", "0219", "0220", "0221", "0222"],
   "Suspected sexual violence → Take history and examine: HVS, microscopy, pregnancy test, HIV rapid test, hepatitis B status, syphilis RDT.\n\n"
   "Presenting within 72 hours:\n- Presumptive STI treatment [updated per WHO 2021]: ceftriaxone 250 mg IM stat PLUS azithromycin 1 g orally stat PLUS metronidazole 2 g orally stat.\n"
   "- HIV post-exposure prophylaxis [updated per WHO 2024]: initiate as soon as possible, ideally within 24 hours; preferred 3-drug regimen TDF + 3TC (or FTC) + DTG; full 28-day course prescribed at first visit; provide starter pack if full course not available, with rapid follow-up; if HIV positive: refer for chronic HIV care.\n"
   "- Hepatitis B [added]: initiate hepatitis B vaccination if unvaccinated; complete vaccination series at follow-up.\n"
   "- Emergency contraception [updated window]: if pregnancy test is negative: levonorgestrel 1.5 mg orally stat (up to 72 hours), OR ulipristal acetate 30 mg orally stat (up to 120 hours), OR copper IUD insertion (up to 120 hours, most effective method). If pregnancy test positive, refer to ANC. If negative, repeat test at 6 weeks.\n\n"
   "Presenting after 72 hours:\n- Presumptive STI treatment [updated per WHO 2021]: ceftriaxone 250 mg IM stat PLUS azithromycin 1 g orally stat PLUS metronidazole 2 g orally stat.\n"
   "- HIV status: HIV PEP is not recommended beyond 72 hours; if HIV negative: follow up per national guidelines; if HIV positive: refer for chronic HIV care.\n"
   "- Hepatitis B [added]: initiate hepatitis B vaccination if unvaccinated; complete vaccination series at follow-up.\n"
   "- Pregnancy status: if within 120 hours: emergency contraception still possible (ulipristal acetate or copper IUD); if pregnancy confirmed: refer to ANC and follow up; if no pregnancy: repeat test at 6 weeks.\n\n"
   "Follow-up schedule [added]: 2 weeks: assess PEP adherence and side effects, wound review. 6 weeks: repeat pregnancy test, repeat HIV test, syphilis serology. 3 months: repeat HIV test, repeat syphilis serology. 6 months: final HIV test, complete hepatitis B vaccination series.\n\n"
   "All survivors at every visit: advise on legal protection and support with medico-legal documentation; provide psychological first aid at time of crisis and ongoing mental health support (screen for PTSD, depression, anxiety); treat all physical injuries, including tetanus prophylaxis per wound status and immunisation history; if pregnancy resulted from the assault, therapeutic termination may be considered after consultation with relevant authorities per national law.\n\n"
   "Sources (printed): WHO Guidelines for HIV Post-Exposure Prophylaxis (2024); WHO Guidelines for the Management of Symptomatic STIs (2021); WHO Clinical Management of Rape and Intimate Partner Violence Survivors; CDC nPEP Guidelines (2025). Verify all regimens against Eswatini national formulary and guidelines before implementation.",
   flags=["Figure 11 still carries editing tags ('UPDATED PER WHO 2021', 'ADDED', 'UPDATED WINDOW') and the note 'Verify all regimens against Eswatini national formulary and guidelines before implementation' - draft review material left in the figure."]),
]
