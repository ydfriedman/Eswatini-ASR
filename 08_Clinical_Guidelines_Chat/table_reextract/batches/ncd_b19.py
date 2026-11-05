exec(open('batches/ncd_common.py').read())
ITEMS = [
 T("tbl-who-physical-activity", 16, CH1 + " > Physical Inactivity > WHO physical activity recommendations",
   "WHO physical activity recommendations by age group (children, adults, older adults, pregnant and postpartum women)", ["0028", "0029"],
   [[C("Age group"), C("Recommendations")]],
   [[C("Children & adolescents (5-17 years)"), C("At least 60 minutes of moderate-to-vigorous intensity PA daily. Include vigorous-intensity aerobic activities at least 3 days/week. Include muscle- and bone-strengthening activities at least 3 days/week.")],
    [C("Adults (18-64 years)"), C("At least 150-300 minutes of moderate-intensity PA per week, OR at least 75-150 minutes of vigorous-intensity PA per week, OR an equivalent combination of moderate and vigorous activity. Muscle-strengthening activities involving major muscle groups on 2 or more days per week.")],
    [C("Older adults (≥65 years)"), C("Same as adults (150-300 min moderate or 75-150 min vigorous). Muscle-strengthening activities 2 or more days per week. Multicomponent PA emphasizing functional balance and strength training 3 or more days/week to prevent falls.")],
    [C("Pregnant & postpartum women"), C("At least 150 minutes of moderate-intensity PA per week. Incorporate a variety of aerobic and muscle-strengthening activities. Add gentle stretching; may be beneficial to add pelvic floor muscle training.")]],
   context_before="Physical inactivity: not meeting the WHO recommendation of at least 150 minutes of moderate-intensity physical activity per week. Sedentary behaviour: any waking behaviour with low energy expenditure (≤1.5 METs) while sitting, reclining, or lying down.",
   table_note="Note: some activity is better than none. Inactive individuals should start with small amounts and gradually increase frequency, intensity, and duration. Screening for physical inactivity: who to screen: all patients attending primary care facilities, particularly those with risk factors (obesity, hypertension, diabetes, cardiovascular disease, depression); routine screening at annual check-ups or chronic disease reviews."),
 T("tbl-physical-activity-5as", 17, CH1 + " > Physical Inactivity > Brief counselling intervention (5 A's framework)",
   "Brief counselling intervention for physical inactivity: the 5 A's (ask, advise, assess, assist, arrange)", ["0032"],
   [[C("Step"), C("Action")]],
   [[C("ASK"), C("Ask about current physical activity levels using screening questions.")],
    [C("ADVISE"), C("Provide clear, personalized advice on benefits of physical activity for their specific health condition.")],
    [C("ASSESS"), C("Assess willingness and readiness to change. Identify barriers (time, safety, cost, cultural factors).")],
    [C("ASSIST"), C("Help develop a realistic action plan. Start small and build gradually. Provide written guidance.")],
    [C("ARRANGE"), C("Arrange follow-up to monitor progress and provide ongoing support.")]],
   context_before="Screening: if <150 minutes of moderate activity per week, the patient is physically inactive."),
 D("fig-smoking-cessation", 19, CH1 + " > Nicotine Use > Smoking cessation approach",
   "Smoking cessation approach in clinical practice (flowchart, with nicotine dependence table)", ["0035", "0036", "0038"],
   "All smokers should be identified and their readiness to quit evaluated. If resistance to quitting exists, information and suitable follow-up should be provided. If the person is ready to make a quit attempt, evaluation of nicotine dependence, co-morbid and psychosocial factors should guide the choice of effective interventions.\n\n"
   "1. Ask: do you smoke? do you know the risks? have you thought of quitting?\n"
   "2. Alert: do you know the benefits of quitting? do you know that we can help you?\n"
   "3. Assess: are you ready to quit?\n"
   "4. Assist/arrange:\n"
   "   - No or maybe: give a motivational pamphlet and encourage follow-up; return to Ask at the next visit.\n"
   "   - Yes: arrange for cessation intervention.\n"
   "5. Specific nicotine dependence review: Fagerstrom/CO levels; current smoking and history of quit attempts; social stressors/household smokers.\n"
   "   Dependence level (already attempted to quit / cigarettes per day / time to first cigarette after waking):\n"
   "   - Very high: yes / >30 / >5 min (printed)\n   - High: yes / 20-30 / 5-30 min\n   - Medium: yes / 10-20 / 30-60 min\n   - Low: no / <10 / >60 min\n"
   "6. By dependence:\n"
   "   - Motivated, low dependence: could manage with counselling/support alone or NRT; support group, text/internet/smartphone-based support.\n"
   "   - Motivated, high dependence: probably will need added pharmacological support; assess medical/psychiatric history; evaluate capacity to purchase medicine; review availability of medication. Medication options: nicotine replacement therapy (patch/gum/spray), varenicline, bupropion.\n"
   "7. Set quit date: arrange appropriate support and medication if needed.\n"
   "8. Follow-up: assess withdrawal symptoms and drug side-effects; evaluate mood and psychosocial stressors; identify potential for relapse.\n\n"
   "CO = carbon monoxide; NRT = nicotine replacement therapy.",
   ["The 'very high' dependence row prints '>5 min' to first cigarette; it presumably means <5 min (shorter time = higher dependence). Clinician to confirm.",
    "'cassation', 'quite date', 'theraphy' printed; corrected."]),
 T("tbl-audit-c", 21, CH1 + " > Alcohol Use > Screening tools > AUDIT-C",
   "AUDIT-C alcohol screening questionnaire: questions, scoring and interpretation", ["0043", "0044"],
   [[C("Question"), C("Answer scoring"), C("Points")]],
   [[C("1. How often do you have a drink containing alcohol?"), C("Never (0); monthly or less (1); 2-4 times/month (2); 2-3 times/week (3); 4+ times/week (4)"), C("0-4")],
    [C("2. How many drinks containing alcohol do you have on a typical day when drinking?"), C("1 or 2 (0); 3 or 4 (1); 5 or 6 (2); 7-9 (3); 10+ (4)"), C("0-4")],
    [C("3. How often do you have 5 or more drinks on one occasion?"), C("Never (0); less than monthly (1); monthly (2); weekly (3); daily/almost daily (4)"), C("0-4")]],
   table_note="AUDIT-C interpretation: men: score ≥4 = unhealthy alcohol use: provide brief intervention. Women: score ≥3 = unhealthy alcohol use: provide brief intervention. Score ≥8: possible alcohol use disorder: consider full AUDIT and referral."),
 T("tbl-alcohol-5as", 21, CH1 + " > Alcohol Use > Brief intervention: the 5 A's",
   "Brief intervention for alcohol use: the 5 A's (ask, advise, assess, assist, arrange)", ["0045"],
   [[C("Step"), C("Action")]],
   [[C("ASK"), C("Ask about alcohol use using AUDIT-C: 'How often do you drink alcohol?' 'How much do you typically drink?'")],
    [C("ADVISE"), C("Provide clear, personalized advice: 'The safest choice is to not drink alcohol at all. There is no safe level of drinking.' Link to their health concerns: 'Alcohol is making your blood pressure worse' or 'Drinking increases your cancer risk.'")],
    [C("ASSESS"), C("Assess readiness to change: 'How do you feel about quitting or cutting down?' 'What makes it difficult for you to stop?'")],
    [C("ASSIST"), C("Help develop a quit/reduction plan: set a quit date or reduction goal; identify triggers and develop coping strategies; provide written educational materials; consider referral to counselling or support groups.")],
    [C("ARRANGE"), C("Schedule follow-up in 2-4 weeks to monitor progress, provide support, and address challenges.")]]),
]
