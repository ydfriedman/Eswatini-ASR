exec(open('batches/ncd_common.py').read())
MD = CH13 + " > Major Depressive Disorder"
def r(*v): return [C(x) for x in v]
ITEMS = [
 B("box-mdd-assessment", 308, MD + " > Screening and Diagnosis of Major Depressive Disorder",
   "Major depressive disorder: 8-step assessment, DSM-5/ICD-11 criteria (5 of 9 for 2+ weeks), severity classification and when to refer urgently", ["0883", "0884", "0885", "0886"],
   "Assessment steps:\n"
   "1. Screen: 'Have you felt sad/depressed most of the time for the past 2 weeks?' AND 'Have you lost interest in activities you usually enjoy?'\n"
   "2. Assess core symptoms: 5 or more of 9 criteria present for 2+ weeks.\n"
   "3. Assess functional impairment: work, relationships, self-care, daily activities.\n"
   "4. RULE OUT: bipolar disorder (past mania?), psychosis, medical causes (hypothyroidism, anaemia, HIV, stroke, diabetes).\n"
   "5. Screen for suicide/self-harm: 'Do you have thoughts of harming yourself or not wanting to live?'\n"
   "6. Assess alcohol and substance use (may co-occur or cause symptoms).\n"
   "7. Determine severity: mild / moderate / severe (any psychotic features?).\n"
   "8. DIAGNOSIS confirmed if 5+ criteria are met, at least 1 being depressed mood or anhedonia.\n\n"
   "DSM-5 / ICD-11 criteria (5 of 9, lasting 2+ weeks): depressed mood most of the day (or irritability in children/adolescents); markedly diminished interest or pleasure (anhedonia); significant weight loss/gain or appetite change; insomnia or hypersomnia nearly every day; psychomotor agitation or retardation (observable by others); fatigue or loss of energy nearly every day; feelings of worthlessness or excessive/inappropriate guilt; difficulty concentrating or making decisions; recurrent thoughts of death or suicidal ideation.\n\n"
   "Severity: mild – few symptoms beyond the minimum, mild functional impairment; moderate – between mild and severe, moderate impairment; severe – most symptoms, marked impairment, may have psychotic features.\n\n"
   "When to refer urgently: active suicidal ideation with plan or intent; psychotic features (hallucinations, delusions); severe self-neglect or inability to care for self; no response after 2 adequate medication trials; suspected bipolar disorder.",
   context_before="Screen all clients accessing services for major depressive disorder with the PHQ-9 (self-administered or by a provider)."),
 T("tbl-antidepressants-summary", 309, MD + " > Depression Management – Pharmacological Treatment",
   "Antidepressants for moderate-severe depression: fluoxetine, amitriptyline, imipramine, sertraline, escitalopram: starting and usual doses and notes; psychoeducation and cautions", ["0887", "0888", "0889", "0890"],
   [[C("Drug"), C("Starting Dose"), C("Usual Dose"), C("Notes")]],
   [r("Fluoxetine (SSRI)", "10-20 mg mane", "20-60 mg/day", "First-line; only SSRI recommended for adolescents ≥12 yrs; avoid with MAOIs"),
    r("Amitriptyline (TCA)", "25-50 mg nocte", "75-150 mg/day", "Effective; caution in cardiac disease, elderly, overdose risk"),
    r("Imipramine (TCA)", "25-50 mg nocte", "75-200 mg/day", "Alternative TCA; monitor ECG if cardiac risk present"),
    r("Sertraline (SSRI)", "25-50 mg/day", "50-200 mg/day", "Good tolerability; preferred in elderly and cardiac disease"),
    r("Escitalopram (SSRI)", "5-10 mg/day", "10-20 mg/day", "Well tolerated; fewer drug interactions; good for elderly")],
   context_before="Consider antidepressants for moderate-severe depression. Discuss with the person: not addictive; takes 2-4 weeks for effect; must be taken for 9-12 months minimum after remission.",
   table_note="Psychoeducation & psychosocial interventions: depression is very common and NOT a sign of weakness or laziness; negative thoughts about self, world and future are symptoms, not reality; encourage regular activity, social engagement and pleasurable activities, regular sleep/wake times and meals; Problem Management Plus (PM+, WHO behavioural activation + problem solving); group interpersonal therapy (IPT); Thinking Healthy (CBT approach for perinatal depression); medications are NOT addictive (9-12 month course); never stop antidepressants abruptly – taper gradually. Cautions & special populations: if a manic episode occurs STOP the antidepressant immediately (may be bipolar disorder); do not combine antidepressants (serotonin syndrome); SSRIs may increase suicidal ideation in adolescents/young adults – weekly monitoring for the first 4 weeks; pregnancy: avoid if possible, if severe use the lowest effective dose with specialist input; breastfeeding: fluoxetine and sertraline generally safer; elderly: start low, go slow, monitor for falls and hyponatraemia (SSRIs); epilepsy: avoid tricyclics (lower seizure threshold).",
   source_flags=["This table makes fluoxetine first line; the MDD table on p.310 lists amitriptyline as '1st line' alongside SSRIs. Sertraline is 'preferred in elderly' here."]),
 B("box-suicide-risk-depression-follow-up", 310, MD + " > Suicide Risk Assessment and Follow-up",
   "Depression: suicide risk assessment (mandatory), risk-level actions, follow-up schedule and PHQ-9 rescreening", ["0891", "0892", "0893"],
   "SUICIDE RISK ASSESSMENT – mandatory in all depression cases. Ask directly: 'Are you having thoughts of harming yourself or ending your life?' If YES, assess: plan? method? intent? previous attempts? access to means (medications, weapons)?\n"
   "- HIGH RISK: hospitalise / urgent referral; remove access to lethal means immediately.\n"
   "- MEDIUM RISK: safety plan; close follow-up within 2-3 days; involve a trusted person/carer.\n"
   "- ALL risk levels: do not leave alone; mobilise social support; document the safety plan.\n\n"
   "FOLLOW-UP – depression (2 weeks initially, then monthly, then every 3 months):\n"
   "- Weeks 2-4: assess side effects and suicidal ideation (especially adolescents on SSRIs).\n"
   "- Weeks 4-6: has mood/interest improved? If no response, increase the dose or switch medication.\n"
   "- Weeks 8-12: full remission expected; reinforce adherence for the full course (9-12 months minimum).\n"
   "- After 9-12 months symptom-free: discuss gradual tapering over weeks to months.\n"
   "- 3+ recurrent episodes: consider long-term maintenance therapy.\n"
   "- Screen for re-emergence of symptoms at every follow-up after stopping treatment.\n\n"
   "PHQ-9 can be used for screening and follow-up: clients scoring 0-9 are rescreened every 6 months; those scoring 10 and above are reassessed 2 weeks after the initial visit and then at every follow-up visit.",
   ["'Week 4-6: if no response increase dose or switch' conflicts with the prescribing rule on the same page ('consider second line after maximum dose for at least 8 weeks')."]),
 T("tbl-mdd-pharmacological", 310, MD + " > Pharmacological Management of Major Depressive Disorder",
   "Pharmacological management of major depressive disorder by line: TCA and SSRIs (1st), duloxetine (2nd), valproate and flunarizine (3rd), lorazepam for insomnia, antipsychotics (haloperidol, sulpiride, aripiprazole; risperidone, olanzapine 2nd line) for psychotic depression", ["0894", "0895", "0896", "0897", "0898", "0899"],
   [[C("Line"), C("Class"), C("Drug"), C("Dosage and frequency"), C("Contraindications")]],
   [[C("1st line", rs=3), C("Tricyclic antidepressants"), C("Amitriptyline"), C("Initial dose 25 mg PO nocte for 3 days then 50 mg PO nocte. Maximum dose 200 mg/24 hrs"), C("Urine retention, constipation, arrhythmia")],
    [C("Selective serotonin reuptake inhibitors", rs=2), C("Fluoxetine"), C("Initial dose 10-20 mg PO nocte. Maximum dose 60-80 mg/24 hours"), C("Use with caution: bipolar disorder in a manic phase (may be useful for depressive phases); bleeding disorders such as haemophilia; type 1 or type 2 diabetes", rs=2)],
    r("Sertraline", "Initial dose 25-50 mg PO nocte. Maximum dose 200 mg/24 hours"),
    r("2nd line", "Serotonin norepinephrine reuptake inhibitor", "Duloxetine", "Initial dose 30 mg PO nocte", "Urolithiasis, AGE (as printed), cognitive dysfunction"),
    [C("3rd line", rs=2), C("Anticonvulsant"), C("Sodium valproate"), C("200 mg twice a day"), C("Pregnancy, hepatic impairment")],
    r("Calcium-channel blocker", "Flunarizine", "5 mg nocte", "Depression; constipation"),
    {"section": "PLUS sedatives if insomnia (MDD with insomnia)"},
    r("Sedative for insomnia", "Benzodiazepine", "Lorazepam PO", "1-2 mg nocte for 7 days", "Myasthenia gravis, sleep apnoea, bronchitis, and COPD"),
    {"section": "PLUS antipsychotics if psychotic symptoms (MDD with psychosis)"},
    r("1st line", "Typical antipsychotic", "Haloperidol", "Initial dose 1.5-3 mg PO nocte. Maximum dose 20 mg/24 hours", "Previous acute stroke or coma; severe intoxication with alcohol or other CNS depressants; allergy to haloperidol or other butyrophenones; heart disease"),
    r("", "Selective D2 dopamine receptor antagonist", "Sulpiride", "Initial dose 50 mg PO nocte. Maximum dose 200 mg/24 hours", "Hypersensitivity to sulpiride; pre-existing breast cancer or other prolactin-dependent tumours; phaeochromocytoma; intoxication with other centrally-active drugs; concomitant levodopa; acute porphyria; comatose state or CNS depression; bone-marrow suppression"),
    r("", "Atypical antipsychotic", "Aripiprazole", "Initial dose 2-5 mg PO nocte. Maximum dose 30 mg/24 hours", "History of alcohol abuse; depression; diabetes mellitus or family history of DM; drug abuse or dependence; hyperglycaemia; neuroleptic malignant syndrome (NMS); neutropenia; history of seizures – use with caution"),
    [C("2nd line", rs=2), C("Atypical antipsychotic", rs=2), C("Risperidone"), C("Initial dose 1-2 mg PO nocte. Maximum dose 8-12 mg/24 hours"), C("Risperidone and olanzapine are absolutely contraindicated in patients with hypertension, diabetes mellitus, obesity, and elderly patients. Check BMI, FBS, BP and PR before prescribing olanzapine and risperidone", rs=2)],
    r("Olanzapine", "Initial dose 5-10 mg PO nocte. Maximum dose 25 mg/24 hours")],
   pages=[310, 311, 312],
   footnotes=["Avoid chlorpromazine for patients with major depressive disorder."],
   context_before="General prescribing rules: 1. prescribe one antidepressant or antipsychotic at a time; 2. consider second line after the maximum dose for at least 8 weeks without significant improvement; 3. do not prescribe anti-muscarinics routinely; manage side effects.",
   source_flags=["Flunarizine (a calcium-channel blocker used for migraine/vertigo) is listed as 3rd-line treatment for depression, while its own contraindication column lists 'Depression'; flunarizine can cause depression. Sodium valproate is also not an antidepressant. Clinician to confirm.",
                 "Fluoxetine is given 'nocte' here but 'mane' on p.309; amitriptyline is 1st line here but fluoxetine is first line on p.309.",
                 "Duloxetine contraindications 'Urolithiasis, AGE, cognitive dysfunction' are printed as is (AGE unexplained); sertraline/fluoxetine 'contraindications' list type 1 or 2 diabetes.",
                 "Aripiprazole 'contraindications' list depression, although it is listed here for depression with psychosis. 'Absolutely contraindicated' for risperidone/olanzapine in all elderly, hypertensive, diabetic or obese patients is stronger than usual guidance.", "'Amitryptyline', 'Sulpride', 'Norepinehrine' printed. Table continues onto pp.311-312."]),
]

ITEMS += [
 T("tbl-mdd-special-cases", 312, MD + " > Special cases",
   "Major depressive disorder special cases: children under 12, pregnancy and breastfeeding, psychotic depression, bipolar depression, emerging mania, PLHIV drug interactions", ["0900"],
   [[C("Special Case"), C("Intervention")]],
   [r("If younger than 12 years", "No antidepressants; provide counselling then refer"),
    r("Pregnant women and breastfeeding mothers", "Antidepressants should be avoided as far as possible, then refer"),
    r("Depression with psychotic symptoms", "Prescribe antidepressants + antipsychotics"),
    r("BAD (bipolar affective disorder), depressive phase", "Prescribe mood stabilizer + antidepressant + antipsychotic"),
    r("If symptoms of mania emerge during treatment of depression", "Immediately stop antidepressants and refer"),
    r("PLHIV", "Nevirapine may decrease the level of fluoxetine; ritonavir increases levels of amitriptyline and fluoxetine; darunavir decreases the level of sertraline; fluvoxamine increases levels of PIs and NNRTIs; carbamazepine is contraindicated as it increases levels of PIs and NNRTIs (as printed)")],
   source_flags=["Carbamazepine is a CYP3A4 inducer and usually DEcreases PI/NNRTI levels; 'increases' is printed. Pregnancy/breastfeeding advice here ('avoid') differs from p.309 (fluoxetine and sertraline safer in breastfeeding)."]),
]
