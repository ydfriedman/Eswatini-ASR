exec(open('batches/mh_common.py').read())
# Repairs from the completeness audit (audit/REPAIR_WORKLIST.md): stepwise-management tables whose content the old
# parse had split into text chunks, written out from the page images. Loaded after mh_b03.
HPG = "Chapter 3: Overview of Different Psychiatric Conditions > Grief and Bereavement"
_bul = lambda *xs: "<br/>".join("• " + x for x in xs)
ITEMS = [
 T("tbl-p36-0068", 36, HPG + " > Table 8: Summary of classification of grief and bereavement",
   "Table 8: Summary of classification and classification of grief and bereavement", ["0068", "0069"],
   [r("SIGNS", "CLASSIFY AS:", "MANAGEMENT")],
   [r("If an individual experienced the death of someone with a close relationship<br/>PLUS at least one of the following symptoms to a clinically significant degree and has persisted for at least 12 moths;<br/>"
      + _bul("Persistent yearning/longing for the deceased", "Intense sorrow and emotional pain in response to the death", "Preoccupation with the deceased", "Preoccupation with the circumstances of the death")
      + "<br/>PLUS at least six of the following symptoms;<br/>"
      + _bul("Marked difficult in accepting death", "Experiencing disbelief or emotional numbness over the loss", "Difficulty with positive reminiscing about the deceased",
             "Bitterness or anger related to the loss", "Maladaptive appraisals about oneself in relation to the deceased or the death", "Excessive avoidance of reminders of the loss",
             "A desire to die in order to be with the deceased", "Difficulty trusting other individuals since the death", "Feeling alone or detached from others since the death.",
             "Feeling life is meaningless or empty without the deceased", "Confusion about one's role in life or a diminished sense of one's identity",
             "Difficulty or reluctance to pursue interests since the loss or plan for the future"),
      "PERSISTENT COMPLEX BEREAVEMENT DISORDER",
      _bul("Refer or provide the following interventions;", "Support and counselling", "Assess for symptoms of Major Depressive Disorder",
           "Refer to the Clinical Psychologist for psychotherapy if there is no improvement with counselling."))],
   source_flags=["'12 moths' (months). The first symptom list says 'at least one of the following' – DSM-5 persistent complex bereavement disorder requires at least one of these four and at least six of the twelve that follow, as the table states."]),
 T("tbl-37-stepwise-grief", 37, HPG + " > Table 9: Stepwise management of grief", "Table 9: Stepwise management of grief", ["0070"],
   [r("Entry point", "Management")],
   [[C("Step 1: Community Clinic Level", cs=2)],
    r(_bul("Persistent Complex Bereavement Disorder"),
      _bul("Take vital signs", "Conduct physical examination", "Conduct MSE", "Provide support and counseling", "Assess for MDD", "If there is no improvement after a month, go to step 2")),
    [C("Step 2: General Hospital or Health Centre", cs=2)],
    r(_bul("Failure at step1", "Persistent Complex Bereavement Disorder comorbid with mild or moderate symptoms of other psychiatric conditions such MDD, GAD, Bipolar Disorders"),
      _bul("Take vital signs", "Conduct physical examination", "Conduct MSE", "Provide support and counseling", "Prescribe medications", "If there is no improvement after a month, go to step 3")),
    [C("Step 3: National Psychiatric Referral Hospital", cs=2)],
    r(_bul("Failure at step 2", "Persistent Complex Bereavement Disorder comorbid with severe symptoms of other psychiatric conditions such MDD, GAD", "Children, adolescents and elderly"),
      _bul("Doctor and Clinical Psychologist led services"))],
   source_flags=["Step 2 says 'Prescribe medications' without naming which; no grief-specific medication guidance is given."]),
 # Table 17 continued (pp.53-55): the intoxication row's symptoms and whole management cell were in text chunk 0115; rows re-done from the images
 T("tbl-p53-0114", 53, "Chapter 3: Overview of Different Psychiatric Conditions > Substance-Related and Addictive Disorders > Table 17 (continued): alcohol intoxication, withdrawal and use disorder",
   "Table 17 (continued): Alcohol intoxication, alcohol withdrawal and alcohol use disorder", ["0114", "0115", "0116", "0118", "0119", "0121"],
   [r("SIGNS", "CLASSIFY AS:", "MANAGEMENT")],
   [r("If the patient has<br/>" + _bul("Recent use of alcohol", "Change of behavior that developed during or shortly after alcohol",
        "PLUS one or more of the following symptoms developing during or shortly after alcohol;") +
      "<br/>o Slurred speech<br/>o Incoordination<br/>o Unsteady gait<br/>o Nystagmus<br/>o Impairment in attention or memory<br/>o Stupor or coma",
      "ALCOHOL INTOXICATION",
      _bul("Initiate the following interventions or refer", "ABC", "Supplemental oxygen if in coma", "Random Blood Glucose testing and management",
           "Check Serum Creatinine and Urea, ALAT & ASAT, CBC, electrolytes and GGT and manage as indicated", "Urinary multi drug test to detect other substance use",
           "Check hydration status and manage.", "Prescribe thiamine (Refer page 79)", "Psycho-education", "Adherence counseling", "Counseling",
           "Long term rehabilitation as indicated", "Family involvement")),
    r("If the patient has;<br/>" + _bul("History of cessation or reduction of heavy alcohol use",
        "PLUS two or more of the following within several hours to few days after the cessation or reduction") +
      "<br/>o Autonomic hyperactivity e.g. sweating<br/>o Increased hand tremor<br/>o Insomnia<br/>o Nausea and vomiting<br/>o Transient visual, tactile or auditory hallucinations or illusions<br/>o Psychomotor agitation<br/>o Anxiety<br/>o Generalized tonic clonic seizures",
      "ALCOHOL WITHDRAW",
      _bul("Initiate the following interventions or refer", "Random Blood Glucose testing and management", "Check Serum Creatinine and Urea, ALAT & ASAT, CBC, electrolytes and GGT and manage",
           "Urinary multi drug test to detect other substance use", "Check hydration status and manage.", "Asses suicidal thoughts", "Manage seizures as indicted",
           "Prescribe medications", "Psycho-education", "Counseling")),
    r("If a client/ patient presents with the problematic pattern of alcohol or substance use leading to clinically significant impairment or distress, as manifested by at least two of the following, occurring within a 12-month period:<br/>"
      "1. Alcohol is often taken in larger amounts or over a longer period than was intended.<br/>"
      "2. There is a persistent desire or unsuccessful efforts to cut down or control alcohol use.<br/>"
      "3. A great deal of time is spent in activities necessary to obtain alcohol, use it or recover from its effects.<br/>"
      "4. Craving, or a strong desire or urge to use alcohol.<br/>"
      "5. Recurrent alcohol use resulting in a failure to fulfill major role obligations at work, school, or home.<br/>"
      "6. Continued alcohol use despite having persistent or recurrent social or interpersonal problems caused or exacerbated by the effects of alcohol.<br/>"
      "7. Important social, occupational, or recreational activities are given up or reduced because of alcohol use.<br/>"
      "8. Recurrent alcohol use in situations in which it is physically hazardous.<br/>"
      "9. Alcohol use is continued despite knowledge of having a persistent or recurrent physical or psychological problem that is likely to have been caused or exacerbated by alcohol.<br/>"
      "10. Tolerance<br/>11. Withdrawal symptoms",
      "ALCOHOL USE DISORDER",
      _bul("As a Initiate the following interventions or refer", "Check Serum Creatinine and Urea, ALAT & ASAT, and GGT and manage", "Urinary multi drug test to detect other substance use",
           "Psycho-education", "Counseling", "Family involvement", "Long term rehabilitation as indicated"))],
   pages=[53, 54, 55, 56],
   source_flags=["Alcohol withdrawal management lists investigations and 'Prescribe medications' but not thiamine; thiamine appears only under alcohol intoxication (p.53) and in the job aid. WHO mhGAP recommends thiamine for all patients with alcohol withdrawal.",
                 "Withdrawal management does not name the medication (benzodiazepine, e.g. the chlordiazepoxide regimen on p.91)."]),
 # Tables 13-14 (pp.45-48): Table 13's first row was cut after its first bullet (rest in text chunk 0090), the other Table 13 rows were
 # filed under Table 14, and Table 14's step cells were cut after their first line; both tables written out from the page images
 T("tbl-p45-0089", 45, "Chapter 3: Overview of Different Psychiatric Conditions > Schizophrenia and Other Psychosis > Table 13: Summary of Classification and Management of Schizophrenia & Other Psychosis",
   "Table 13: Summary of classification and management of schizophrenia & other psychosis", ["0089", "0090", "0091", "0092", "0093", "0095"],
   [r("SIGNS", "CLASSIFY AS:", "MANAGEMENT")],
   [r("If the patient has two or more of the following symptoms for not less than 6 months:<br/>" + _bul("Speech that is difficult to understand", "Delusions", "Hallucinations",
        "Marked unusual behaviour e.g. lack of self-care etc.", "Negative symptoms i.e. blunt affect, impairment in linguistic ability, decrease in motivation etc.") +
      "<br/>NB: If the above symptoms are present for a period of less than six months, diagnosis is Schizophreniform Disorder",
      "SCHIZOPHRENIA",
      "Initiate the following interventions or refer<br/>" + _bul("Anti-psychotics (Refer page 64)", "PLUS a sedative if the patient presents with insomnia",
        "Psycho-education (Refer page 89)", "Adherence counseling (Refer page 81)", "Family involvement (Refer page 81)", "Occupational therapy")),
    r("If the patient has one or more of the following symptoms for a duration of symptoms, at least one day but less than one month:<br/>1. Speech that is difficult to understand<br/>2. Delusions<br/>3. Hallucinations<br/>4. Marked unusual behaviour",
      "BRIEF PSYCHOTIC DISORDER", _bul("Consider the same interventions for managing schizophrenia")),
    r("If the patient has two or more of the following symptoms for a duration of one month but less than six months:<br/>1. Speech that is difficult to understand<br/>2. Delusions<br/>3. Hallucinations<br/>4. Marked unusual behavior",
      "SCHIZOPHRENIFORM DISORDER", _bul("Consider the same interventions for managing schizophrenia")),
    r("If the patient has symptoms of schizophrenia concurrent with a major mood episode (major depressive episode or manic episode)", "SCHIZOAFFECTIVE DISORDER",
      "Initiate the following interventions or refer<br/>" + _bul("Anti-psychotics (Refer page 64)", "PLUS a mood stabilizer (Refer page 69)", "PLUS a sedative if the patient presents with insomnia",
        "Psycho-education (Refer page 89)", "Adherence counseling (Refer page 81)", "Family involvement", "Assess for suicidal risk (Refer page 99)")),
    r("If the patient has<br/>" + _bul("Prominent delusions or hallucinations", "Evidence from history, physical examination or laboratory findings that the disturbance is the direct pathophysiological consequences of another medical condition.", "No presence of a mental condition"),
      "PSYCHOTIC DISORDER DUE TO A GENERAL MEDICAL CONDITION",
      "Provide first aid as applicable<br/>" + _bul("Manage the general Medical condition or refer (DO NOT REFER TO THE NPRH)", "Initiate low dose of an antipsychotic if there is no improvement after stabilizing the general Medical condition",
        "PLUS a sedative preferably Lorazepam 0.5 to 1mg nocte for seven days if presents with insomnia")),
    r("If the patient has:<br/>" + _bul("Either hallucinations or delusions or both", "Evidence from history, physical examination or laboratory findings of hallucinations and/or delusions developed during or soon after substance intoxication or withdrawal or after exposure to a medication.",
        "The involved substance or medication is capable of producing hallucinations and/or delusions.", "No presence of a mental condition"),
      "SUBSTANCE INDUCED PSYCHOTIC DISORDER", _bul("Consider the same interventions for managing schizophrenia", "PLUS substance use education and counseling", "Conduct multi drug test"))],
   pages=[45, 46, 47],
   source_flags=["The NB in the schizophrenia row says symptoms for less than six months mean schizophreniform disorder, but brief psychotic disorder (one day to under one month) is also under six months; the schizophreniform row correctly says one to six months."]),
 T("tbl-p45-0091", 48, "Chapter 3: Overview of Different Psychiatric Conditions > Schizophrenia and Other Psychosis > Table 14: Stepwise Management of Schizophrenia and Other Psychotic Disorders",
   "Table 14: Stepwise management of schizophrenia and other psychotic disorders", ["0097", "0099", "0101"],
   [r("Entry point", "Management")],
   [[C("Step 1: Community Clinic Level", cs=2)],
    r("The following conditions, stable on treatment<br/>" + _bul("Schizophrenia", "Schizophreniform disorder", "Schizoaffective disorder", "Brief Psychotic Disorder", "Substance Induced Psychotic Disorder", "Psychotic Disorder Due To A General Medical Condition"),
      _bul("Take vital signs", "Conduct MSE and physical examination", "Adherence counselling", "Family involvement", "Assess side effects of medications", "Refill medications as indicated", "Refer to Doctor led services every 6 months for review.")),
    [C("Step 2: General Hospital or Health Centre", cs=2)],
    r(_bul("Failure step 1", "Moderate psychotic symptoms of the following;") + "<br/>o Psychotic Disorder Due To A General Medical Condition<br/>o Schizophrenia<br/>o Schizophreniform disorder<br/>o Schizoaffective disorder<br/>o Brief Psychotic Disorder<br/>o Substance Induced Psychotic Disorder<br/>o Psychotic Disorder Due To A General Medical Condition",
      _bul("Take vital signs", "Conduct physical examination", "Conduct Mental Status Evaluation", "Review medications and prescribe as indicated", "Provide psychosocial support", "If not improved within 2 weeks refer to Doctor led services", "If no improvement go to step 3")),
    [C("Step 3: National Psychiatric Referral Hospital", cs=2)],
    r(_bul("Failure step 2", "Pregnant women, breastfeeding mothers, children and elderly with schizophrenia and other psychosis", "Severe acute psychotic symptoms") +
      "<br/>o Psychotic Disorder Due To A General Medical Condition<br/>o Schizophrenia<br/>o Schizophreniform disorder<br/>o Schizoaffective disorder<br/>o Brief Psychotic Disorder<br/>o Substance Induced Psychotic Disorder",
      "Doctor led services at NPRH")],
   source_flags=["Step 2 and Step 3 lists name 'Psychotic Disorder Due To A General Medical Condition' and 'Schizophrenia' run together, and Step 2 lists the general-medical-condition disorder twice; Table 13 says this disorder should not be referred to the NPRH, yet Step 3 includes it."]),
]
