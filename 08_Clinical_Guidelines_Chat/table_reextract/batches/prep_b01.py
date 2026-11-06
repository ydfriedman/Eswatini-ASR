exec(open('batches/prep_common.py').read())
OR = CH2 + " > 2.1 Oral PrEP"
RG = CH2 + " > 2.2 Dapivirine Vaginal Ring (PrEP Ring)"
ITEMS = [
 T("tbl-terminology", 8, "Terminology", "Terminology: adverse drug reaction, adverse event, assigned female/male at birth, cisgender, integration, non-binary, transgender", ["0010"],
   [[C("Term"), C("Definition")]],
   [r("Adverse Drug Reaction (ADR)", "A response to a drug which is noxious and unintended, and which occurs at doses normally used in humans for prophylaxis, diagnosis, or therapy of disease, or for the modification of physiological function. An adverse drug reaction, in contrast to an adverse event, is characterized by the fact that a causal relationship between a medical product and an occurrence is suspected."),
    r("Adverse Event (AE) / Adverse Experience", "Any untoward medical occurrence that may present during treatment with a pharmaceutical product, but which does not necessarily have a causal relationship with this treatment."),
    r("Assigned female at birth", "People assigned female at birth may include cisgender women, transgender men, and some non-binary people."),
    r("Assigned male at birth", "People assigned male at birth may include cisgender men, transgender women, and some non-binary people."),
    r("Cisgender", "Describes a person whose gender identity corresponds to their sex assigned at birth."),
    r("Integration", "Joining operational programs to ensure effective outcomes through many modalities (multi-tasked providers, referral, one-stop-shop services under one roof, etc.)"),
    r("Non-binary", "A spectrum of gender identities that do not exclusively or neatly fit into the category male or female, man or woman, and are outside the gender binary."),
    r("Transgender", "A person who has a gender identity or gender expression that differs from the sex assigned at birth."),
    r("Transgender woman", "An individual assigned male sex at birth who identifies as a female."),
    r("Transgender man", "An individual assigned female sex at birth who identifies as a male.")]),
 T("tbl-oral-prep-drug-interactions", 12, OR + " > Oral PrEP and Other Drug Interactions", "Table 1. Oral PrEP (TDF/3TC) drug interactions: contraceptive hormones, gender-affirming hormones, estradiol-based exogenous hormones", ["0021"],
   [[C("Drug"), C("Interaction")]],
   [r("Contraceptive hormones", "No known interactions"),
    r("Gender-affirming hormones", "No known interactions: levels of gender-affirming hormones used by transgender individuals are not affected"),
    r("Estradiol-based exogenous hormones", "Estradiol-based exogenous hormones may reduce oral PrEP drug levels in people AMAB, which is why daily oral PrEP is recommended for these individuals, but ED-PrEP is not.")]),
 T("tbl-oral-prep-start-stop", 14, OR + " > Starting and Stopping Oral PrEP", "Table 2. Starting, using and stopping oral PrEP (daily and event-driven 2+1+1) by population: AMAB not on estradiol, AFAB, AMAB on estradiol hormones, people who inject drugs", ["0024", "0025"],
   [[C("Population(s)"), C("Often includes ᵃ"), C("Starting oral PrEP"), C("Using oral PrEP"), C("Stopping oral PrEP")]],
   [r("People assigned male at birth who are NOT using estradiol-based exogenous hormones and are using oral PrEP to prevent HIV acquisition during sex", "Cisgender men and transgender women who are not using estradiol-based exogenous hormones; non-binary people assigned male at birth who are not using estradiol-based exogenous hormones", "Daily or ED: take a double dose 2 to 24 hours before potential sexual exposure. Ideally, this loading dose should be taken closer to 24 hours before potential exposure.", "Take one dose per day.", "Daily or ED: after a single dose is taken daily for two days after the last potential exposure, PrEP can be stopped."),
    [C("People assigned female at birth who are using oral PrEP to prevent HIV acquisition during sex"), C("Cisgender women, transgender men, non-binary people assigned female at birth"),
     C("Daily: take a single dose daily for seven days before potential exposure.<br/>ED-PrEP is not recommended for these populations.", rs=3), C("Take one dose per day.", rs=3), C("After a single dose is taken daily for seven days after the last potential exposure, PrEP can be stopped.", rs=3)],
    r("People assigned male at birth who are using estradiol-based exogenous hormones who are using oral PrEP to prevent HIV acquisition during sex", "Transgender women who are using estradiol-based exogenous hormones; non-binary people assigned male at birth who are using estradiol-based exogenous hormones"),
    r("People using oral PrEP to prevent HIV acquisition from nonsexual exposures", "Anyone who shares injection-related materials ᵇ")],
   footnotes=["ᵃ This list is provided to support interpretation of this guidance and is not inclusive of all gender identities or terms that may be used by people with diverse gender identities to describe themselves and/or their communities. Starting and stopping oral PrEP should be based on the factors in the first column.",
              "ᵇ Injection drug use is mentioned in this guidance; however, first-line prevention strategies for people who inject drugs are needle exchange and/or drug use harm reduction and treatment. Daily oral PrEP has some preventative effects for this population and should be offered as part of a larger prevention package."]),
 D("fig-ed-prep-examples", 15, OR + " > Additional Guidance for ED-PrEP Use", "Figures 1-6. Event-driven (ED, 2+1+1) oral PrEP dosing examples: sex once, on consecutive days, on non-consecutive days, sex does not occur; switching between ED-PrEP and daily PrEP", ["0028", "0030"],
   "Examples for clients AMAB not using estradiol-based hormones (pill = one tablet; all doses at 9 AM in the examples).\n"
   "Figure 1 – sex one time / in one day: double dose (2 tablets) Friday 9 AM; sex Friday 11 PM; then 1 tablet Saturday 9 AM and 1 tablet Sunday 9 AM (two days after sex), then stop.\n"
   "Figure 2 – sex on multiple consecutive days: double dose Friday 9 AM; sex Friday 11 PM, Saturday 10 PM, Sunday 4 AM; 1 tablet daily Saturday to Tuesday 9 AM (continued daily through the days of sex and for two days after the last sex), then stop.\n"
   "Figure 3 – sex on multiple non-consecutive days: double dose Friday 9 AM; sex Friday 11 PM and Sunday 1 PM; 1 tablet daily Saturday to Tuesday 9 AM (two days after the last sex), then stop.\n"
   "Figure 4 – sex does not occur: double dose Friday 9 AM; no sex; no further tablets are shown.\n"
   "Figure 5 – transitioning from ED-PrEP to daily PrEP: ED course (double dose Saturday 9 AM, sex Saturday 7 PM, 1 tablet Sunday and Monday); later, when sex becomes frequent, double dose Sunday 9 AM then 1 tablet daily while having sex almost every day (Sunday 3 PM to Saturday 8 PM), continuing daily dosing; to stop, continue for two days after the last sex.\n"
   "Figure 6 – transitioning from daily PrEP to ED-PrEP: daily dosing (double dose Sunday 9 AM, then 1 tablet daily) while sex occurs Monday to Saturday; daily tablets continue for two days after the last sex (to Monday) and then stop; for the next sex (Thursday 2 PM), a double dose Thursday 9 AM, then 1 tablet Friday and Saturday 9 AM.",
   ["Figures 1-6 are pictures (day strips with pill and sex icons); described here in words. In Figure 4 the Saturday and Sunday 9 AM labels are printed without tablets; whether to continue after a loading dose when sex does not happen is not stated in the text."], pages=[15, 16, 17]),
 T("tbl-ring-pbfw-contraindications", 18, RG + " > Contraindications for PrEP Ring Use", "Table 3. Additional contraindications for the dapivirine PrEP ring in pregnant and breastfeeding women (during pregnancy and postnatal period)", ["0034"],
   [[C("Additional contraindication for the ring for PBFW", cs=2)], [C("During pregnancy"), C("During the postnatal period")]],
   [[L("Active labour at any gestation", "Vaginal bleeding", "Suspected or confirmed rupture of the amniotic membranes", "Cervical cerclage", "Suspected or confirmed intrauterine infection"),
     L("Unresolved postnatal vaginal bleeding", "Uterus not yet returned to near pre-pregnancy size through normal involution", "Following spontaneous or therapeutic abortion")]],
   rhc=0,
   context_before="In addition to the general contraindications for PrEP, the ring should not be provided to: individuals assigned male at birth; individuals exposed to HIV through anal sex or needle sharing; allergy or hypersensitivity to the active substances; women using contraceptive vaginal rings or diaphragm. For PBFW there are additional contraindications (Table 3)."),
 T("tbl-ring-drug-interactions", 19, RG + " > PrEP Ring and Other Drug Interactions", "Table 4. Dapivirine PrEP ring drug interactions: vaginal antimicrobials, miconazole, clotrimazole, metronidazole, clindamycin, other vaginal rings, hormones", ["0038"],
   [[C("Drug"), C("Interaction")]],
   [[C("Vaginally administered antimicrobial products"), L("No data available on concurrent use with the ring", "Concomitant use is not recommended")],
    r("Miconazole", "Evaluations of co-administered use of miconazole and the ring are not fully resolved; clients should be advised to use additional preventative measures for HIV when co-treated with vaginal miconazole."),
    r("Clotrimazole vaginal cream", "Co-administered clotrimazole as a water-based vaginal cream with the ring was well tolerated, but given methodological issues that limited the reliability of the pharmacokinetic results of both clotrimazole and dapivirine, concurrent use should be undertaken with caution."),
    [C("Metronidazole; clindamycin"), C("There is no data on concomitant use of the ring and metronidazole or clindamycin, so concomitant use is not recommended.")],
    r("Other vaginal rings, e.g. contraceptive rings or diaphragms", "No current data on concomitant use of the ring and other vaginal rings, so concomitant use is not recommended."),
    r("Contraceptive hormones; gender-affirming hormone therapy", "No known interactions")]),
 B("box-ring-insertion", 20, RG + " > Starting and Stopping the PrEP Ring > Inserting the PrEP Ring", "Box 3. Dapivirine PrEP ring insertion steps for clients", ["0041"],
   "Box 3. Ring insertion steps for clients:\n"
   "1. Get into a position that is comfortable for inserting the ring, such as squatting, one leg lifted, or lying down. If a health care provider is assisting you, you should be in a reclining position.\n"
   "2. With clean hands, squeeze the ring between the thumb and forefinger, pressing both sides together so that the ring forms a 'figure 8' shape.\n"
   "3. Use the other hand to open the folds of skin around the vagina.\n"
   "4. Place the tip of the ring into the vaginal opening and use your fingers to push the folded ring gently up into the vagina.\n"
   "5. Push the ring as far toward the lower back as possible. If the ring feels uncomfortable, it is probably not inserted far enough; use a finger to push it as far up into the vagina as is comfortable.\n"
   "*Ring insertion should be painless. If you have any bleeding or discomfort upon insertion, contact your health care provider.", pages=[20, 21]),
 T("tbl-ring-start-stop", 22, RG + " > Starting and Stopping the PrEP Ring", "Table 5. Starting, using and stopping the dapivirine PrEP ring (24 hours to effectiveness, 28-day ring, no protection after removal)", ["0044"],
   [[C("Starting PrEP ring"), C("Using PrEP ring"), C("Stopping PrEP ring")]],
   [r("The ring must be in place for at least 24 hours before it is maximally effective.", "The ring must be left in place for 28 days. After 28 days, the ring can be removed and replaced immediately with a new ring.", "When the ring is removed, dapivirine levels drop quickly and there will be no protection from acquiring HIV.")], rhc=0),
]
