exec(open('batches/ncd_common.py').read())
SU = CH13 + " > Substance Use Disorder"
def r(*v): return [C(x) for x in v]
NALT_CI = "Absolute contraindication: acute hepatitis or liver failure; taking opioid analgesics; currently physically dependent on opioids, including those maintained on opioid agonists (e.g. methadone) or partial agonists (e.g. buprenorphine); acute opioid withdrawal"
ITEMS = [
 T("tbl-alcohol-withdrawal-sedative", 316, SU + " > Alcohol Withdrawal Syndrome",
   "Alcohol withdrawal syndrome: benzodiazepine (lorazepam) dosing, PAWSS and CIWA-Ar/SAWS assessment, outpatient vs inpatient", ["0910"],
   [[C("Class"), C("Drug"), C("Dosage and Frequency"), C("Contraindications")]],
   [r("Sedatives for insomnia: benzodiazepine", "Lorazepam PO", "1-2 mg nocte for 7 days", "Myasthenia gravis, sleep apnoea, bronchitis, and COPD")],
   context_before="Alcohol withdrawal starts 4-12 hours after the last drink (anxiety, agitation, tremor, sympathetic activation; severe: seizures and delirium tremens, potentially fatal); symptoms may last up to 5 days. Mild to moderate withdrawal can be managed as an outpatient in primary care with benzodiazepines; severe withdrawal or complicating conditions need inpatient management. Use the PAWSS to predict severe withdrawal (score <4 = low risk, suitable for outpatient care).",
   table_note="Where withdrawal symptoms are present, assess severity with a validated instrument: the Clinical Institute Withdrawal Assessment for Alcohol, Revised (CIWA-Ar), or the self-completed 10-item Short Alcohol Withdrawal Scale (SAWS).",
   source_flags=["The only benzodiazepine regimen given for alcohol withdrawal is the insomnia regimen 'lorazepam 1-2 mg nocte for 7 days', which is not a withdrawal regimen (usually symptom-triggered or fixed-schedule dosing, e.g. diazepam or chlordiazepoxide). Clinician to confirm."]),
 T("tbl-alcohol-dependence-drugs", 317, SU + " > Alcohol dependence: pharmacological management",
   "Medicines for alcohol dependence: acamprosate, naltrexone (oral and XR injectable), disulfiram, gabapentin, topiramate: doses and contraindications", ["0912", "0913", "0914"],
   [[C("Line"), C("Class"), C("Drug"), C("Dosage and Frequency"), C("Contraindications / Cautions")]],
   [r("1st line", "Organosulfonic acids", "Acamprosate", "Weight <60 kg: 666 mg once daily at breakfast and 333 mg twice daily at midday and night (maximum 1332 mg). Adults >60 kg: 666 mg TID. Start as soon as the patient has abstained from alcohol, within 7 days", "Do not prescribe if CrCl <30 mL/min or eGFR <30 mL/min/1.73 m2. Hypersensitivity to the active substance or excipients. Breast-feeding women"),
    [C("1st line", rs=2), C("Opiate antagonists (recommend XR naltrexone if adherence to oral is a concern; start naltrexone even if patients continue to use alcohol)", rs=2), C("Naltrexone oral"), C("Initial dose 25 mg OD; increase to 50 mg per day over about 1 week. Maintenance 50 mg once daily; if adverse events, consider 25 mg once daily. Maximum 100 mg daily"), C(NALT_CI, rs=2)],
    r("XR naltrexone, long-acting injectable", "Initial: oral naltrexone 50 mg once daily for at least 3 days. Maintenance: 380 mg intragluteal injection every 28 days"),
    r("2nd line", "Alcohol antagonists", "Disulfiram", "500 mg once daily for 1 to 2 weeks, then 250 mg once daily. Maintenance 250 mg once a day (range 125-500 mg). Maximum 500 mg once a day", "Absolute contraindication: recent or concomitant metronidazole, paraldehyde, alcohol or alcohol-containing preparations (e.g. cough syrups, tonics); coronary artery disease; recent myocardial infarction; psychoses; acute hepatitis or acute liver failure"),
    [C("3rd line", rs=2), C("Anticonvulsants (not FDA approved but found beneficial)", rs=2), C("Gabapentin"), C("Initial 300 mg once daily; increase by 300 mg every 1 to 2 days by response and tolerability. Maintenance individualised, generally in 3 divided doses, up to 2,400 mg or 3,600 mg per day"), C("Caution: gabapentin can be misused for its psychoactive effect, alone or with opioids, benzodiazepines and alcohol")],
    r("Topiramate", "Initial 25 mg once daily; increase by 50 mg each week to a maximum of 400 mg daily in 2 divided doses. Maintenance 200-400 mg daily in 2 doses. Moderate-to-severe renal impairment: 50% dose reduction", "Halve the dose in adults with CrCl ≤70 mL/min or eGFR ≤70 mL/min/1.73 m2")],
   pages=[317, 318],
   context_before="Alcohol dependence: three main classes of drugs are recommended: (i) organosulfonic acids, (ii) opiate antagonists, (iii) alcohol antagonists.",
   source_flags=["Table continues onto p.318 with the header repeated."]),
]
AX = CH13 + " > Anxiety Disorders"; SC = CH13 + " > Suicide"
ITEMS += [
 T("tbl-gad-drugs", 322, AX + " > Pharmacological Management of Generalized Anxiety Disorder",
   "Generalized anxiety disorder medicines: SSRIs (fluoxetine, sertraline) first line, plus lorazepam if insomnia", ["0922", "0923", "0924"],
   [[C("Line"), C("Class"), C("Drug"), C("Dosage and Frequency"), C("Contraindications")]],
   [[C("1st line", rs=2), C("Selective serotonin reuptake inhibitors", rs=2), C("Fluoxetine"), C("Initial dose 10-20 mg PO nocte. Maximum dose 60-80 mg/24 hours"), C("Use with caution: bipolar disorder in a manic phase (may be useful for depressive phases); bleeding disorders such as haemophilia; type 1 or type 2 diabetes", rs=2)],
    r("Sertraline", "Initial dose 25 mg PO nocte. Maximum dose 200 mg/24 hours"),
    {"section": "PLUS a sedative with anxiolytic effect if insomnia is a presenting symptom (GAD with insomnia)"},
    r("Sedative for insomnia", "Benzodiazepine", "Lorazepam PO", "1-2 mg nocte for 7 days", "Myasthenia gravis, sleep apnoea, bronchitis, and COPD")],
   context_before="Generalized anxiety disorder responds better to psychotherapy and low-dose SSRIs. Prescribing rules: one antidepressant at a time; do not prescribe anti-muscarinics routinely, manage side effects.",
   source_flags=["Fluoxetine and sertraline are given 'nocte'; SSRIs are usually given in the morning (fluoxetine is 'mane' on p.309)."]),
 B("box-suicide-warning-signs", 323, SC + " > Warning Signs of Suicidal Behaviour",
   "Warning signs of suicidal behaviour", ["0927"],
   "Warning signs to look out for: feeling like a burden; being isolated; increased anxiety; talking about feeling trapped or in unbearable pain; increased substance use; looking for a way to access lethal means; increased anger or rage; extreme mood swings; expressing hopelessness and having no reason to live; sleeping too little or too much; talking or posting about wanting to die or to kill oneself; making plans for suicide; giving away prized possessions; showing rage or talking about seeking revenge; suddenly coming out of being hopeless; not wanting to complete projects one has started.",
   context_before="Suicidal behaviour is any thought, action or behaviour indicating intent or desire to end one's life: suicidal ideation, suicide plan, suicide attempt, completed suicide. It emerges from individual, interpersonal, communal and societal factors."),
 B("box-suicidal-behaviour-diagnostic-features", 324, SC + " > Diagnostic Features of Suicidal Behaviour",
   "Diagnostic features of suicidal behaviour disorder (DSM-5)", ["0929"],
   "a. The act: 1. has been attempted within the last 24 months; 2. does not meet criteria for non-suicidal self-injury (self-injury to produce a positive mood); 3. is not applied to suicidal ideation or preparatory acts; 4. was not initiated during a state of delirium or confusion; 5. was not undertaken solely for a political or religious objective.\n"
   "b. The behaviour or its consequences cause clinically significant distress or interference in interpersonal, academic, or other important areas of functioning.\n"
   "c. The behaviour does not occur exclusively during psychotic episodes, delirium, substance intoxication, or substance withdrawal."),
]
