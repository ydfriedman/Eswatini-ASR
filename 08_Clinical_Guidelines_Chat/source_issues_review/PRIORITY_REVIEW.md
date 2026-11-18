# Source issues: priority list for clinical review

The guideline documents behind the chat contain 825 issues found while checking every table, flowchart and text section against the PDFs (full list: `../SOURCE_ISSUES.md`). They are errors or inconsistencies **in the guidelines themselves**. Each was read and sorted by how much it could matter to a patient:

| Tier | Meaning | Issues |
|---|---|---|
| 1A | Could harm a patient if followed as printed | 66 |
| 1B | Guidelines disagree or are unclear on a clinical decision | 46 |
| 2 | Confusing or inconsistent; a clinician would probably read it correctly | 298 |
| 3 | Editorial: typos, captions, numbering, cross-references, layout | 269 |
| 0 | No clinical review needed: extraction notes, or 2022 HIV text replaced by the 2024 Amendment / 2025 PrEP guidelines | 146 |

**Suggested review:** Tier 1A first (66 issues), then Tier 1B (46). Tier 2 can be reviewed by programme leads as time allows; Tier 3 is for the guideline editors; Tier 0 needs no action. Some problems appear more than once (the same error in two places, or in two documents); these are cross-referenced under "See also".

Record decisions in `source_issues_tiered.csv` (one row per issue, Tier 1A first, with columns for the decision, the correct reading, and whether to send it to the guideline authors). Issue numbers follow the order of `SOURCE_ISSUES.md`.

## Tier 1A: could harm a patient if followed as printed

### NCDs, Injuries and Mental Health Guidelines 2025 (27)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 38 | 44 | Management of diabetic emergencies (DKA and HHS): diagnosis, evaluation, monitoring, resolution, transition to SC insulin, alternative SC insulin protocol and formulas | Several thresholds are garbled in the source: DKA 'low HCO3- :<10 ≤ 15 mEq/L', HHS 'BG:>600>1000 mg/dl 33.3mmol/L', and the HHS resolution 'BG <' has no value. Kept as printed. |  |
| 42 | 47 | 04 Potassium replacement protocol in DKA/HHS: action, KCl per litre and rate by serum K+ | The >5.5 row gives 'No KCl' but a rate of '10-20 mmol/hr', as printed. |  |
| 46 | 53 | Capillary blood glucose (CBG) insulin correction dose scale: units to add by CBG reading and insulin sensitivity | 'Bedtime correction doses should be REDUCED by 50%' appears alongside a bedtime column that already lists reduced doses; clinician to confirm whether a further 50% reduction applies. |  |
| 70 | 103 | IV drugs for hypertensive emergencies: onset, duration, dose, contraindications and adverse effects (esmolol, metoprolol, labetalol, nicardipine, nitroglycerine, nitroprusside, enalaprilat, urapidil, clonidine, phentolamine) | Labetalol bolus is printed '0-20 mg IV'; probably 10-20 mg. Clinician to confirm. |  |
| 78 | 120 | Acute decompensated heart failure with and without cardiogenic shock: signs, management and disposition; furosemide adjustment by volume status | Cardiogenic shock (SBP <80 mmHg) is described with 'warm extremities, not confused, good urine output' and managed 'as above' (including vasodilators if SBP >180) with ward admission; this looks copied from the row above. Inotropes are recommended for cardiogenic shock on p.117/119. Clinician to confirm. |  |
| 81 | 122 | Inotropes and vasodilators for acute decompensated heart failure: doses and comments (dobutamine, dopamine, epinephrine, nitroglycerin) | Dobutamine/dopamine are 5-10 mcg/kg/min here but 10-20 mcg/kg/min in the inotrope note on p.119. |  |
| 89 | 138 | Acute ischaemic stroke: acute management (alteplase, labetalol, thrombectomy, cerebral oedema), thrombolysis contraindications (absolute and relative), and secondary stroke prevention | Alteplase is said to be 'given if 3-4.5 hours from stroke symptom onset'; elsewhere the window is 0-4.5 h. |  |
| 95 | 145 | Initial evaluation and management of acute rheumatic fever and rheumatic heart disease in children (algorithm: Jones criteria, primary and secondary penicillin prophylaxis by weight, valve involvement) | Secondary prophylaxis weight bands are misprinted: the ARF box gives '>27 kg' for both 600,000 IU and 1.2M IU, and the mitral column gives 'If <27 kg: 1.2M IU'. The aortic and tricuspid columns give <27 kg = 600,000 IU, >27 kg = 1.2M IU. Clinician to confirm. |  |
| 110 | 182 | Snakebite management by venom type: supportive treatment, signs of severe envenomation, antivenom type, administration, starting and additional doses (mixed, cytotoxic, neurotoxic, haemotoxic) | Dosing instructions conflict: the chart gives starting doses of 20-200 ml diluted in 200 ml saline over 30 min, while the box below says first dose 10 ml IV at 1-2 ml/min, then no more than 20 ml per 500 ml bag. Clinician to confirm. | #125 |
| 113 | 188 | Drugs in traumatic brain injury: tranexamic acid, mannitol, hypertonic saline, propofol, enoxaparin, phenytoin, paracetamol, morphine: dose, contraindications, side effects | Head injury section (p.173) says 'Do not give narcotic analgesics to head injury patients. Use paracetamol', while this section says the analgesia of choice in TBI is morphine. | #808 |
| 119 | 196 | Poisoning management by exposure type: ingested poisons (activated charcoal doses), gastric decontamination, skin, eye and inhaled poisoning | Adrenaline for bronchospasm is printed 'SC/IM 25–50 mg or IV 5–25 mg'; doses in mg are about 1000 times too high (probably mcg, or 0.25–0.5 mg). Clinician to confirm. |  |
| 120 | 196 | Poisoning management by exposure type: ingested poisons (activated charcoal doses), gastric decontamination, skin, eye and inhaled poisoning | Inducing vomiting 'if charcoal not available' conflicts with current advice and with 'Do NOT induce vomiting' for some agents in the same cell. |  |
| 121 | 197 | Poisoning supportive care: toxic features (COPD signs, pulmonary oedema, PE, ARDS, MI, metabolic acidosis) with diagnosis, immediate stabilisation and definitive management | Pulmonary oedema is managed with 'bronchodilators, steroids', copied from the row above. |  |
| 124 | 198 | Antidotes and doses for common poisons: pesticides (organophosphates, carbamates, organochlorines, rodenticides), industrial chemicals (arsenic, methanol, ethylene glycol, cyanide, methaemoglobinaemia), drugs (paracetamol, iron, benzodiazepines, opioids, isoniazid, digoxin), envenomations and bites | Isoniazid antidote 'pyridoxine 10–25 mg PO q8hr' is a prophylaxis dose; isoniazid poisoning is usually treated with IV pyridoxine gram-for-gram (about 5 g). Similar low pyridoxine dosing is given for ethylene glycol. |  |
| 125 | 198 | Antidotes and doses for common poisons: pesticides (organophosphates, carbamates, organochlorines, rodenticides), industrial chemicals (arsenic, methanol, ethylene glycol, cyanide, methaemoglobinaemia), drugs (paracetamol, iron, benzodiazepines, opioids, isoniazid, digoxin), envenomations and bites | Snakebite antivenom volumes here differ from the venom-specific starting doses on p.182. | #110 |
| 126 | 198 | Antidotes and doses for common poisons: pesticides (organophosphates, carbamates, organochlorines, rodenticides), industrial chemicals (arsenic, methanol, ethylene glycol, cyanide, methaemoglobinaemia), drugs (paracetamol, iron, benzodiazepines, opioids, isoniazid, digoxin), envenomations and bites | The antidote cell for opioids is printed 'Naloxone 0.4–2mg PO depending on opioid amount; repeat in 2–3 min if needed' (p.189 of the guideline). Naloxone is given IV, IM or intranasally; oral naloxone is not effective for overdose, so 'PO' is probably an error in the guideline. |  |
| 130 | 203 | AKI management (algorithm, continued): fluid management, hypertension, electrolytes and acidosis (hyperkalaemia, hyponatraemia, hypocalcaemia, acidosis), nutrition, and indications for urgent dialysis | Several doses are misprinted: hyperkalaemia threshold '605mmol/L' (6.5); glucose '25-5 mls of D10W'; hypocalcaemia '0.1 mg/kg (0.5ml/kg)' (mg and ml do not match); protein '1.5-21 g/kg'; albumin 'over 30 to 60' with no unit. Clinician to confirm. |  |
| 134 | 207 | Hyperkalaemia (K ≥6 mmol/l) in AKI: adults vs children: calcium gluconate, insulin-dextrose, bicarbonate, salbutamol, potassium binder, furosemide, dialysis | Children: Kayexalate is contraindicated here ('DO NOT GIVE'), while the paediatric AKI chart on p.203 gives calcium resonium (kayexalate) 1 g/kg 4-hourly. Clinician to confirm. |  |
| 148 | 229 | Histology-based treatment of glomerular disease: minimal change disease (children and adults), membranous nephropathy, membranoproliferative GN, IgA nephropathy, lupus nephritis, pauci-immune necrotising GN: regimens, doses and special considerations | IgA nephropathy prednisolone is printed '1mg/day' (presumably 1 mg/kg/day); proteinuria threshold printed '1g/d' (presumably >1 g/d). |  |
| 154 | 246 | Antiepileptic medicines: sodium valproate, carbamazepine, phenytoin, phenobarbital, lamotrigine: adult and child doses, contraindications, side effects; principles of AED treatment | The barbiturate row is printed 'Phenytoin'; the doses (30 mg nocte; 3-5 mg/kg/day) are phenobarbital doses. Clinician to confirm. |  |
| 158 | 250 | Management algorithm for status epilepticus in adults (ICU): stabilisation 0-5 min, first-line benzodiazepines 5-15 min, second-line valproate or phenytoin 15-30 min, third-line anaesthetic infusions after 30 min | Several doses are misprinted: diazepam '0.5 - 0.2 mg/kg/dose' (usually 0.15-0.2 mg/kg); phenytoin maintenance '1.5 mg every 8hr' (no per-kg unit); thiopental infusion '3-3 mg/kg/hr'; lorazepam has no maximum. Propofol 5-10 mg/kg/hr is high for a 24 h infusion. Clinician to confirm. |  |
| 172 | 290 | Opioid equi-analgesic doses: oral and subcutaneous/IV equivalents of codeine, tramadol, morphine, hydromorphone, oxycodone, fentanyl, methadone | Methadone 'about 1 mg' = 10 mg oral morphine is printed without noting that the ratio varies widely with dose; tramadol 50 mg ≈ morphine 10 mg is lower than usual (about 100 mg). Clinician to confirm. |  |
| 185 | 316 | Alcohol withdrawal syndrome: benzodiazepine (lorazepam) dosing, PAWSS and CIWA-Ar/SAWS assessment, outpatient vs inpatient | The only benzodiazepine regimen given for alcohol withdrawal is the insomnia regimen 'lorazepam 1-2 mg nocte for 7 days', which is not a withdrawal regimen (usually symptom-triggered or fixed-schedule dosing, e.g. diazepam or chlordiazepoxide). Clinician to confirm. |  |
| 195 | 337 | Acute asthma exacerbation: immediate actions for all ages (oxygen, salbutamol, ipratropium, steroids, magnesium) and admission criteria | The oxygen target is printed '94–98% (adults/adolescents) or 94–98% (children)' (same range twice); the primary-care flowchart on p.338 targets 93–95% in adults. Children's magnesium '25–75 mg/kg' is printed (usually 25–50 mg/kg, max 2 g). |  |
| 799 | 113 | Paediatric hypertension | nifedipine 0.25-0.5 mg/kg sublingual is recommended, while the adult urgency section says 'AVOID NIFEDIPINE SUBLINGUAL' (unpredictable BP drops). |  |
| 808 | 173 | Head injury | 'Do not give narcotic analgesics to head injury patients. Use paracetamol', while the TBI section (p.190) says the analgesia of choice in TBI is morphine. | #113 |
| 819 | 292 | Morphine | the worked example converts oral 4-hourly morphine to 'morphine PR … 30mg twice daily' (PR = per rectum?) – presumably slow-release oral (MR) morphine. Paediatric morphine '0.2 to 0.3 mg/kg (10-15mg) initial dose' – the mg range is an adult dose. |  |

### STI and Viral Hepatitis Guidelines 2026 (draft) (10)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 749 | 37 | Table 3: Causative organisms with their signs and symptoms, treatment and options | Table 3 gives erythromycin as the pregnancy alternative for penicillin-allergic women with syphilis; erythromycin does not reliably treat the fetus (WHO recommends penicillin desensitisation or ceftriaxone, and treating the newborn). | #772, #773 |
| 763 | 57 | Treatment options for lower abdominal pain | The first treatment option reads 'Ceftriaxone, 1g I.M STAT, Gentamycin 240mg IM Stat and Spectinmycin 2 grams IM PLUS', which can be read as giving all three injectables together; they are alternatives. |  |
| 766 | 64 | Syndromic treatment chart for scrotal swelling (section 5.5.1, 'chart 5') | The scrotal swelling chart puts the emergency-referral conditions (torsion, trauma, incarcerated hernia) and the epididymitis signs in one decision box, so 'YES' leads to antibiotics; torsion needs immediate surgical referral, not treatment. The chart is labelled 'chart 5' (the same number as the lower abdominal pain chart), and its health promotion package includes cervical cancer screening for a male patient. |  |
| 772 | 79 | Treatment regimens for Syphilis in pregnancy | Syphilis in pregnancy: erythromycin for the mother does not prevent congenital syphilis (the newborn must be treated), and the neonatal procaine penicillin dose ('150 000 IU/kg IM, 12 hourly for 14 days') does not match standard dosing (procaine penicillin 50 000 IU/kg once daily for 10 days). Ceftriaxone 1 g daily for 8-10 days is listed without saying it is the penicillin-allergy alternative. | #749, #773 |
| 773 | 80 | Syndromic chart for syphilis in pregnancy (chart 8) | The syphilis-in-pregnancy chart treats every positive mother with benzathine penicillin weekly for 3 weeks (the regimen for late latent or unknown-duration syphilis; early syphilis needs a single dose), and gives the newborn 'Procaine Penicillin G 150 000 IU/kg IM, 12 hourly for 14 days' - procaine penicillin is 50 000 IU/kg once daily for 10 days (12-hourly dosing is for aqueous benzyl penicillin); erythromycin for 30 days does not treat congenital syphilis. | #749, #772 |
| 780 | 88 | Flowchart for management of genital warts | In the genital warts chart, intra-vaginal, cervical, ano-rectal or large (>10 mm) warts lead to podophyllin treatment, whereas Table 11 says cervical, meatal and urethral warts should be managed by an expert (podophyllin is not used on internal or cervical warts). |  |
| 788 | 140 | Table 17: Summary of common STI syndromes, their causes and treatment recommended in Eswatini | Annex 4 (Table 17) differs from the chapter 5 regimens: scrotal swelling 'Spectinomycin 250mg IM' (the dose elsewhere is 2 g) with doxycycline 7 days (chapter 5: azithromycin weekly x 2 or doxycycline 14 days); neonatal conjunctivitis uses spectinomycin 25 mg/kg for the neonate (chapter 5 chart: ceftriaxone 50 mg/kg, max 125 mg); vaginal discharge lists clotrimazole for six days and 'Cotrimazole' pessary 500 mg; the urethral discharge regimen includes metronidazole. |  |
| 789 | 142 | Annex 5: Precautions with penicillin administration | Annex 5 advises an intradermal penicillin test dose when the allergy history is unknown; intradermal testing with undiluted penicillin is not a validated allergy test and can itself cause anaphylaxis (WHO and national programmes advise giving benzathine penicillin with anaphylaxis preparedness rather than routine skin testing). |  |
| 790 | 143 | Table 18: Paediatric treatment dosages for the main STI pathogens | Annex 6 (Table 18) doses lack per-kg units ('Ceftriaxone 20-50mgs IM', 'Tinidazole 50-75mgs'; presumably mg/kg), gives azithromycin 12-hourly for 7 days (azithromycin is a once-daily or single-dose drug), recommends interferon for hepatitis B in children (tenofovir/entecavir are now first-line, see Figure 13) and 1% gamma benzene hexachloride (lindane) for children (neurotoxic; avoided in children). The Ureaplasma row is empty. | #791 |
| 791 | 146 | Table 19: Syndromic treatment table of paediatric dosages | Annex 6.1 (Table 19) lists ceftriaxone as the alternative for chlamydia (ceftriaxone does not treat chlamydia), gives ceftriaxone 250 mg for gonorrhoea in children over 45 kg (adults in this draft get 1 g), tinidazole '50-75 mg' (mg/kg intended) and trichloroacetic acid 50-70% for warts (Table 11: 80-90%); it disagrees with Table 18 on several doses (e.g. metronidazole 15 mg/kg TDS vs 7 mg/kg 8-hourly; fluconazole 200 vs 150 mg). | #790 |

### Integrated TB Management Guidelines 2025 (9)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 306 | 134 | Table 31: Weight-based dosing of medicines used in multidrug-resistant TB regimens, adults and children<sup>a</sup>: Table 31: Weight-based dosing of medicines used in multidrug-resistant TB regimens, adults and childrena (Group A Medicines, Formulation (tablets, diluted in 10 mL of water, as applicable), 3-4 kg, 5-6 kg, 7-9 kg, 10-15 kg, 16-24 kg, 25-29 kg, 30-35 kg, 36) | Meropenem adult dose printed '1 vials (1 g + 1 g) bd'; the WHO table gives meropenem 1 g three times daily (or 2 g twice daily) with clavulanate. |  |
| 307 | 150 | Table 36. Recommended treatment regimen and anti-TB drug dosages for paediatrics (Child friendly dispersible TB medicine for a baby <4 kg<br/>Number of Tablets, Child friendly dispersible TB medicine for a baby <4 kg<br/>Number of T) | Babies <4 kg: for 2.9 kg the intensive-phase dose is ½ tablet but the instruction says 'give 5 ml (1/2)' (half of the 20 ml solution is 10 ml); the continuation-phase cell says ¼ but the instruction gives 10 ml (1/2). | #308 |
| 308 | 150 | Table 36. Recommended treatment regimen and anti-TB drug dosages for paediatrics (Child friendly dispersible TB medicine for a baby <4 kg<br/>Number of Tablets, Child friendly dispersible TB medicine for a baby <4 kg<br/>Number of T) | Continuation phase for 2 kg and 2.9 kg tells the carer to dissolve an RHZ tablet; the continuation phase uses RH (as in the 3-3.9 kg row). | #307 |
| 320 | 162 | Table 40: When to stop anti-TB drugs (Reaction, Drug Responsible) | 'When to stop anti-TB drugs' lists only pyrazinamide for hepatitis; isoniazid and rifampicin are also hepatotoxic and Table 39 lists all three. |  |
| 322 | 178 | Table 43: Blood Potassium levels and recommended monitoring protocol (Potassium level mEq/L, Quantity of KCL 1mEq I. V=1mmol I.V 8mEq=600mg tablet, When to do the next control (sooner if the patient has vomiting or diarr) | K+ 2.4-2.6: '60 mmol IV and 6000 mg orally every 6 hours for 24 hours' would be 320 mEq oral plus IV per day if read literally; the 'every 6 hours' appears to belong to the monitoring column (as in the next row). The 'when to do the next control' cell is blank for this row. |  |
| 336 | 214 | Table 55: TPT regimen and drug dosing (TPT regimens and drug formulations, No. of tablets or quantity of solution by body weight band) | 1HP row lists 'Rifapentine 30 mg tab' (2 tablets); the 1HP rifapentine dose is 600 mg daily, i.e. 2 × 300 mg tablets. |  |
| 340 | 215 | Table 56: TPT dosing by body size (TPT regimens and drug formulations, No. of tablets or quantity of solution by body weight band) | Isoniazid 100 mg dt for 4-7.9 kg is printed '0.5 (0.5 mL)'; half a tablet in 10 mL is 5 mL. |  |
| 341 | 215 | Table 56: TPT dosing by body size (TPT regimens and drug formulations, No. of tablets or quantity of solution by body weight band) | ≥65 kg: isoniazid 300 mg × 1.25 tablets (375 mg) and rifampicin 300 mg × 2.5 capsules (750 mg) exceed the usual maximum daily doses (isoniazid 300 mg, rifampicin 600 mg for TPT); clinician to confirm. |  |
| 356 | 259 | Table 73: Treatment Regimens for MOTT Species (MOTT / NTM, Regimen (Adult Dose)) | M. kansasii: ethambutol is printed as 300 mg; the usual adult dose is 15 mg/kg (about 800-1,200 mg). 'Pyridoxide' is pyridoxine. |  |

### Integrated HIV Management Guidelines 2022 (9)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 535 | 136 | Table 6.19 Diagnostic Tests and management of Cryptococcal Meningitis (continued as 'Table 6.15') | Pregnancy is listed as a contraindication to fluconazole, while the footnote says the benefit of treating cryptococcal meningitis outweighs the risk; the contraindication should apply to pre-emptive/maintenance use, not to treatment of meningitis. |  |
| 538 | 140 | Table 6.20 The 5-FC (flucytosine) dose adjustment by creatinine clearance | Dose interval has no units (hours). The bullet '<50 ml/min: reduce subsequent doses by 50%' conflicts with the table, which keeps the full 25 mg/kg dose at CrCl >40 ml/min. |  |
| 541 | 146 | Table 7.1 Timing of ART initiation | Cryptococcal meningitis: '2-6 weeks' here, while Table 6.17 and the CrAg algorithm say ART is started 6 weeks after antifungal treatment (4 weeks for asymptomatic antigenaemia). | #622 |
| 603 | 189 | Table 8.10 Infant Dosing Regimens of NVP and AZT | NVP for 6-9 months and 9-24 months is given in mL only (3 mL = 30 mg, 5 mL = 50 mg of 10 mg/mL syrup); WHO infant NVP prophylaxis is 30 mg daily at 6-9 months and 40 mg daily from 9 months, so 50 mg is above the WHO dose. |  |
| 622 | 204 | Table 9.1 Timing of ART initiation (after HIV verification/confirmation and clinical assessment) | Cryptococcal meningitis: ART 4-6 weeks after antifungal treatment here, '6-8 weeks' in the STOP AIDS box (p.206), 6 weeks in Chapter 6 and 2-6 weeks in Chapter 7 (Table 7.1 notes). | #541 |
| 689 | 247 | Table 10.5 Guidance on ART and Diabetes | Table 10.5 recommends metformin + sulphonylurea at Steps 4 and 5, but the text on p.246 says 'Do not use sulphonylureas (e.g., glibenclamide) because of drug interaction with protease inhibitors that may result in profound hypoglycaemia; efavirenz may also cause uncertain interactions with sulphonylureas'. Table 10.5 also brings in metformin only at Step 3, while Figure 10.1 starts metformin as soon as diabetes is confirmed. |  |
| 695 | 250 | Table 10.6 Pharmacotherapy and Drug Information for Treatment of Hyperlipidaemia | Table 10.6 lists simvastatin (on the Essential Medicines List) and lovastatin without a warning, but the box above says simvastatin and lovastatin should not be used with protease inhibitors (rhabdomyolysis). |  |
| 713 | 265 | Annex 11.1 Overview of ARV Drugs | Annex 11.1 lists ABC/3TC 300 mg + 150 mg as '1 tablet every 24 hours' (half the adult daily dose) and omits the paediatric ABC/3TC 120/60 mg dispersible tablet that Chapter 9 makes the preferred formulation. |  |
| 728 | 285 | Annex 11.12 Hepatitis B Virus Treatment and Clinical Considerations | Annex 11.12 entecavir dose for 10–11 kg is printed as 2 (mL = 0.1 mg); the WHO weight-band dose is 3 mL (0.15 mg), and every other band rises by 1 mL. The dose column also has no units ('10 or 0.5 mg' for >30-35 kg mixes mL and mg). |  |

### Mental Health Desk Guide 2022 (7)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 379 | 49 | TABLE 15: SUMMARY OF CLASSIFICATION AND MANAGEMENT OF NEUROCOGNITIVE DISORDERS | Delirium: 'a sedative preferably lorazepam 0.5-1 mg nocte for seven days' – benzodiazepines can worsen delirium (except in alcohol or benzodiazepine withdrawal) and are generally avoided; low-dose antipsychotic only if distressing symptoms is the usual approach. | #380 |
| 380 | 49 | TABLE 15: SUMMARY OF CLASSIFICATION AND MANAGEMENT OF NEUROCOGNITIVE DISORDERS | Delirium: a benzodiazepine (lorazepam) is advised for insomnia; benzodiazepines can cause or worsen delirium and are generally avoided except in alcohol or sedative withdrawal. | #379 |
| 381 | 53 | Table 17 (continued): Alcohol intoxication, alcohol withdrawal and alcohol use disorder | Alcohol withdrawal management lists investigations and 'Prescribe medications' but not thiamine; thiamine appears only under alcohol intoxication (p.53) and in the job aid. WHO mhGAP recommends thiamine for all patients with alcohol withdrawal. |  |
| 385 | 71 | Tables 23-24. Major depressive disorder: lorazepam for insomnia; antipsychotics (haloperidol, risperidone, olanzapine, aripiprazole) for depression with psychosis – doses and titration; cautions for SSRIs and TCAs | Risperidone titration is printed 'by 50-200mg' (Table 24); risperidone is titrated in 0.5-1 mg steps (max 6 mg/day). The 50-200 mg figure appears copied from sulpiride/chlorpromazine. |  |
| 388 | 75 | Table 29. Rapid neuroleptization/tranquillization for acute psychosis: haloperidol IM, chlorpromazine IM, followed by diazepam IV or lorazepam IV – doses and maximums; cautions | Chlorpromazine 100-150 mg IM stat is a high intramuscular dose (usual 25-50 mg IM, risk of hypotension). |  |
| 394 | 81 | TABLE 38: SUMMARY OF MOOD STABILIZERS AS PER ESWATINI TREATMENT GUIDELINES AND ESSENTIAL MEDICINES LIST | Lamotrigine titration (25-50 mg daily for 7 days, then 50 mg 12-hourly, increasing every 7-14 days) is faster than the usual schedule (25 mg daily for 2 weeks, 50 mg daily for 2 weeks, then 100 mg); fast titration raises the risk of Stevens-Johnson syndrome, and doses must be halved with valproate. The maximum for bipolar disorder is usually 200-400 mg/day. | #395 |
| 395 | 81 | TABLE 38: SUMMARY OF MOOD STABILIZERS AS PER ESWATINI TREATMENT GUIDELINES AND ESSENTIAL MEDICINES LIST | Lamotrigine: '25-50 mg daily for the first 7 days then 50 mg 12-hourly' is faster than the recommended titration (25 mg daily for 2 weeks, then 50 mg daily for 2 weeks, then increase), which raises the risk of Stevens-Johnson syndrome. | #394 |

### Antenatal Care Guidelines (3)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 248 | 39 | Eclampsia: risk factors, symptoms and emergency management of convulsions (left lateral, airway, oxygen, magnesium sulphate, urgent referral) | Same magnesium sulphate '4 g IM' pre-referral dose as for severe pre-eclampsia (see above). | #250 |
| 250 | 39 | Pre-eclampsia: mild (BP ≥140/90 twice 4 hours apart) vs severe (BP ≥160/110, proteinuria, headache, blurred vision, epigastric pain, oliguria, thrombocytopenia) – referral and pre-referral magnesium sulphate | Pre-referral magnesium sulphate is given as '4 g IM'. The WHO IM regimen is 4 g IV plus 10 g IM (5 g in each buttock), or 10 g IM where IV is not possible; 4 g IM alone is below standard loading doses. Clinician to confirm. | #248 |
| 252 | 40 | Premature rupture of membranes (PROM) and preterm PROM (PPROM): assessment, clinic management (no digital vaginal exam, refer), hospital management by gestation (steroids betamethasone/dexamethasone, antibiotics erythromycin/amoxicillin, induction) | Betamethasone '12 mg every 12 hours for 24 hours' – the usual regimen is 12 mg IM every 24 hours for 2 doses; the dexamethasone dose is not given. |  |

### Family Planning Services Guidelines 2021 (1)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 359 | 38 | When a pill or more is missed (Number of Missed Pills, Action to be taken) | Missed progestin-only pills: the instructions ('take 2 pills as soon as she can and another 2 the next day'; for 3 missed pills 'do not attempt to replace') are combined-pill style. For POPs, WHO advises taking one pill as soon as possible whenever a pill is more than 3 hours late (27 hours for desogestrel), continuing daily, and using a backup method for the next 2 days. |  |

## Tier 1B: guidelines disagree or are unclear on a clinical decision

### NCDs, Injuries and Mental Health Guidelines 2025 (15)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 15 | 13 | Blood pressure screening algorithm: BP categories and actions | These categories follow the ACC/AHA scheme (stage 1 from 130/80); the hypertension section on p.25 defines hypertension as ≥140/90 (ESC/ESH). | #18 |
| 18 | 26 | Algorithm for hypertension screening in adults (18 years and above) | These ESC/ESH categories differ from the blood pressure screening table on p.13 (ACC/AHA style: stage 1 from 130/80). | #15 |
| 32 | 39 | Adjusting the dose of premixed insulin in type 2 DM by time-of-day glucose readings | The 'INSULIN' cells are printed under the fasting and evening columns without saying which dose. Clinician to confirm. | #33, #34 |
| 33 | 39 | Adjusting the dose of premixed insulin in type 2 DM by time-of-day glucose readings | The high-evening cell says increase the previous evening's insulin, while the low-evening cell says decrease breakfast insulin. Possible inconsistency in the source. | #32, #34 |
| 34 | 39 | Adjusting the dose of premixed insulin in type 2 DM by time-of-day glucose readings | The low-fasting cell ends at 'by 2 units or' in the PDF. | #32, #33 |
| 36 | 41 | Insulin dosage regimens for type 1 diabetes: share of total daily dose by meal (basal-bolus, split-mixed, three and two injections) | Option 2 rows: 'Lunch: short acting insulin (1/3 of evening dose)' is printed as is; with 2/3 of the total in the morning the remaining 1/3 is the evening dose. Clinician to confirm the intended timing. | #794 |
| 40 | 45 | 01 Diabetic ketoacidosis (DKA): diagnostic criteria (all 3 required) and severity | DKA glucose threshold is >11 mmol/L here but BG >13.9 mmol/L in the management box on p.34. |  |
| 43 | 48 | 08 Resolution criteria for DKA and HHS, and 3-step transition to subcutaneous insulin | Resolution criteria here (BG <14 mmol/L, pH >7.3, HCO3- >15, all required) differ from the management box on p.34 (BG <15 mmol/L + 2 or more criteria). Clinician to confirm which applies. |  |
| 44 | 50 | Algorithm for DKA (flowchart: assessment, resuscitation, IV therapy, insulin, monitoring, cerebral oedema) | Fluid volumes here (10 ml/kg over 1 h; 10-20 ml/kg boluses) are weight-based, unlike the adult DKA fluid table on p.36 (1 L over 30-60 min). The algorithm does not say whether it is for children; clinician to confirm. | #45 |
| 45 | 50 | Algorithm for DKA (flowchart: assessment, resuscitation, IV therapy, insulin, monitoring, cerebral oedema) | Insulin infusion here is 0.05-0.1 unit/kg/hour starting 1 hour after fluids; the adult protocol on p.37 gives a 0.1 unit/kg bolus then 0.1 unit/kg/hr. | #44 |
| 87 | 137 | rtPA (alteplase) eligibility criteria in acute ischaemic stroke: inclusion (all must be met) and exclusion (any = contraindicated) | 'NIHSS < 6 or > 25' as an exclusion conflicts with the tPA contraindications on p.133 (only NIHSS = 0 or rapidly improving) and with the DAPT advice for minor stroke (NIHSS ≤3). The age limit 18-80 is also not in the p.133 list. Clinician to confirm. |  |
| 143 | 217 | Interventions to slow CKD progression and reduce cardiovascular risk by GFR and albuminuria stage (lifestyle, smoking, RAS inhibition, BP, statins, glycaemia, SGLT2 inhibitors, GLP-1 RA, metabolic acidosis) | Note (b) is printed 'stains should be initiated for those beginning dialysis therapy'; the KDIGO source says statins should NOT be initiated in patients starting dialysis. Clinician to confirm. |  |
| 163 | 251-252 | Cervical screening algorithm (`ncdimh-fig-cervical-screening-algorithm`) vs summary table (`ncdimh-tbl-cervical-screening-summary`) and VIA management table | For both HIV-negative women and women living with HIV, the algorithm sends every positive VIA to LEEP/colposcopy (LEEP/oncology if HIV-positive), while both tables give same-day cryotherapy/thermal ablation when eligible and LEEP only when not. Clinician to confirm; probably needs correcting in the guideline. | #162 |
| 182 | 310 | Pharmacological management of major depressive disorder by line: TCA and SSRIs (1st), duloxetine (2nd), valproate and flunarizine (3rd), lorazepam for insomnia, antipsychotics (haloperidol, sulpiride, aripiprazole; risperidone, olanzapine 2nd line) for psychotic depression | Flunarizine (a calcium-channel blocker used for migraine/vertigo) is listed as 3rd-line treatment for depression, while its own contraindication column lists 'Depression'; flunarizine can cause depression. Sodium valproate is also not an antidepressant. Clinician to confirm. |  |
| 794 | 40 | Insulin therapy for type 1 diabetes: initiating therapy in a child not in DKA | The sentence starts "Breakfast and one-third before the evening meal"; the first part (presumably "two-thirds before breakfast") is missing. | #36 |

### Integrated HIV Management Guidelines 2022 (8)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 431 | 57 | IPV screening tool: screen for probable index testing induced health risk | The 'NO' branch says DO NOT offer provider referral, and the 'YES' branch suggests provider referral; this looks reversed. Section 3.2.3 says people at risk of IPV should NOT be offered provider referral, so provider referral belongs to the not-at-risk ('NO') branch. |  |
| 441 | 65 | Figure 3.8 HIV testing algorithm for Infants and Children Less Than 18 Months | Final antibody test 'at 18 months of age OR at 2 months after cessation of breastfeeding, whichever comes first': a test before breastfeeding has stopped cannot exclude infection; WHO gives the final diagnosis at 18 months or 3 months after cessation of breastfeeding, whichever is LATER. Figure 3.9 says RDT 3 months after cessation of breastfeeding (not 2). | #610, #614 |
| 520 | 131 | Table 6.16 TB Treatment Drug Interactions | 'DTG and all TB treatments' says the preference is to keep clients on TDF+3TC+EFV during TB treatment, which conflicts with Table 6.15 (TDF/3TC/DTG with an extra DTG 50 mg dose for clients on TB treatment) and with DTG as preferred first line. 'DTG and all TB treatments' is also inaccurate: the DTG interaction is with rifampicin. | #327 |
| 610 | 191 | Table 8.12 Infant Diagnostic Tests for Mothers of Varying HIV Statuses | Final infant test 'at 18 months' only; WHO also requires a test 3 months after cessation of breastfeeding (Table 8.13 uses 2 months). | #441, #614 |
| 614 | 192 | Table 8.13 Timing of HIV testing among exposed Infants and Young Children less than 18 months | Re-test '2 months after stopping breastfeeding' and 'whichever comes first' differ from WHO (final test at 18 months or 3 months after cessation of breastfeeding, whichever is later); see also the flag on Figure 3.8. | #441, #610 |
| 619 | 196 | Table 8.15 Special Considerations for Enhanced Infant Prophylaxis in Exposed Infants | The note says NVP 'may continue for longer until the mother has a detectable VL'; it should read until the mother has an UNDETECTABLE VL (section 8.11 and Table 8.9). |  |
| 707 | 261 | Table 10.15 Specific Considerations for Pain in Children | Table 10.15 recommends carbamazepine for neuropathic pain in young children without mentioning that carbamazepine lowers DTG levels (most children are on DTG); the text on p.263 notes the DTG/EFV interaction for adults. |  |
| 741 | 302 | Depression Assessment Score (English and Siswati) | The PHQ-9 score bands leave out 0-4 and a score of exactly 20 (5-9, 10-14, 15-19, >20), and nothing is said about a positive answer to item 9 (thoughts of death or self-harm), which needs same-day suicide risk assessment (see the 2024 Amendment Chapter 10 suicide screening). | #235 |

### Integrated TB Management Guidelines 2025 (6)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 291 | 111 | Table 19: Definition of TB treatment outcomes (Outcome, Definition) | Treatment failure is defined as 'sputum culture positive at 2 months, or smear positive at 5 months or later'. In the WHO definitions failure is a positive smear/culture at month 5 or later (or treatment change); a positive culture at month 2 is not treatment failure. |  |
| 302 | 133 | Table 30: Drug dosing for BPaLM and BPaL regimen (Drugs, Suggested, Remarks) | Linezolid alternative: '300 mg daily provided that 9 consecutive weeks of treatment is completed' is ambiguous; in the WHO BPaLM guidance linezolid 600 mg daily may be reduced to 300 mg daily after the first 9 weeks (or for toxicity); a three-times-weekly 600 mg schedule is not part of the WHO recommendation. |  |
| 311 | 152 | Table 38: Recommended dosing for 6RHZ+Ethionamide regimen for TB meningitis in children and adolescents (Drug, Dosage (mg/kg)) | The boxed 'Recommended TBM regimen for children: 2HRZE+Lfx/10RH' contradicts the sentence just above it (not yet recommended by WHO) and the WHO-recommended 6RHZEto shown in the table. |  |
| 327 | 196 | Table 47: TB treatment/ART Drug Interactions | The 'DTG and all TB treatments' row says the preference is to keep clients on TDF+3TC+EFV during TB treatment, which conflicts with Table 46 (increase DTG to 50 mg twice daily during rifampicin-based treatment, the current WHO approach). | #520 |
| 335 | 214 | Table 55: TPT regimen and drug dosing (TPT regimens and drug formulations, No. of tablets or quantity of solution by body weight band) | 1HP footnote reads 'for individuals aged < 13 years'; 1HP is recommended for people aged ≥13 years (Table 58 says ≥12 years). |  |
| 348 | 230 | Table 66: Interpretation of IGRA results (QuantiFERON GlodPlus) | The Negative and Indeterminate rows print '≥0.35 and ≥25% of Nil', which is the positive criterion. The manufacturer's (QuantiFERON-TB Gold Plus) criteria are: Negative = Mitogen minus Nil ≥0.5 and TB1 and TB2 minus Nil <0.35, or ≥0.35 and <25% of Nil; Indeterminate (Nil ≤8.0) = TB1 and TB2 negative with Mitogen minus Nil <0.5. As printed, a negative result also requires Mitogen <0.5, which is the indeterminate criterion. |  |

### HIV Management Amendment 2024 (4)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 4 | 28 | Chapter 7 adult ART: summary of changes in viral load thresholds and testing, 2022 vs 2024 guidance | Figure 7.1 on the same page gives low-level viraemia as VL 50 - 999 copies/mL, while this table gives 200 - 999 copies/mL for 2024. Inconsistency in the source: clinician to confirm. | #5 |
| 5 | 28 | Figure 7.1 Updated viral load thresholds | Low-level viraemia is 'VL 50-999' in this figure, '200-999' in the Chapter 7 summary table and footnote (a) of Figure 7.3, and '51-999' in the LLV section text. Inconsistent in the source; clinician to confirm. | #4 |
| 10 | 38 | TPT regimens and dosing by ART regimen, age and weight | The PDF prints the 3HP drug column as 'Isoniazid + Rifampicin x 3mo', but the dosing column (and the 3HP regimen) uses rifapentine. Possible error in the source: clinician to confirm. |  |
| 13 | 44 | Figure 10.3 Suicide screening using Suicide Risk Assessment Tool score chart | Score bands overlap at 20 ('11-20' and '20-30') as printed; clinician to confirm which band a score of 20 falls in. | #402 |

### Mental Health Desk Guide 2022 (4)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 374 | 39 | TABLE 10: STEPWISE MANAGEMENT OF SEXUAL ASSAULT IN PSYCHIATRY | Step 1 (sexual assault without psychiatric symptoms) lists only vital signs, examination, counselling and referral; time-critical post-assault care (HIV PEP within 72 hours, emergency contraception, STI prophylaxis, forensic documentation) is not mentioned in this table. |  |
| 376 | 41 | TABLE 11 (continued): Bipolar I hypomanic and major depressive episodes, and Bipolar II disorder | The carbamazepine note mentions only NNRTIs and PIs; carbamazepine also lowers dolutegravir levels (DTG is in first-line ART) and should be avoided or the DTG dose adjusted. |  |
| 396 | 81 | TABLE 38: SUMMARY OF MOOD STABILIZERS AS PER ESWATINI TREATMENT GUIDELINES AND ESSENTIAL MEDICINES LIST | Sodium valproate is recommended without a caution about women and girls of childbearing potential (teratogenicity); lithium is not listed. |  |
| 402 | 111 | SUICIDE RISK ASSESSMENT FORM (Adapted from Becks Suicidal Intent Scale) | The form has no item 4 (numbering goes from 3 to 5), so it has 14 items and a maximum score of 28, but the risk bands in the Recommendations table run to 30 (high risk 21-30). Beck's Suicidal Intent Scale has 15 items; the missing item is probably 'Acts to get help during/after the attempt'. | #13 |

### PrEP Implementation Guidelines 2025 (3)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 209 | 32 | Table 7. LEN (lenacapavir) drug interactions: TB rifamycins, anticonvulsants, ketamine contraindicated; supplemental LEN with rifampicin; erectile dysfunction drugs; hormones safe | Rifabutin is listed under 'LEN should not be co-administered', while the dose-adjustment row covers only rifampicin; supplemental dosing for rifabutin or rifapentine is not addressed. | #210 |
| 210 | 39 | Table 10. Product-specific PrEP eligibility criteria for oral PrEP, PrEP ring, CAB-LA and LEN: follow-up attendance, age ≥16, body weight, pregnancy/breastfeeding, contraindications | LEN's contraindications in this table omit the drug interactions listed in Table 7 (rifamycins, carbamazepine, phenobarbital, phenytoin, ketamine), while CAB-LA's include them. | #209 |
| 235 | 82 | Annex 5. PHQ-9 depression screening questionnaire (9 items scored 0-3) and score interpretation: 0-4 none, 5-9 mild, 10-14 moderate, 15-19 moderately severe, 20-27 severe, with proposed treatment actions | PHQ-9 item 9 (thoughts of death or self-harm) has no instruction for what to do with a positive answer regardless of total score. | #741 |

### Antenatal Care Guidelines (2)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 254 | 40 | Premature rupture of membranes (PROM) and preterm PROM (PPROM): assessment, clinic management (no digital vaginal exam, refer), hospital management by gestation (steroids betamethasone/dexamethasone, antibiotics erythromycin/amoxicillin, induction) | PPROM before 28 weeks: 'initiate process of evacuation by stimulation' – clinician to confirm intent. |  |
| 255 | 40 | Premature rupture of membranes (PROM) and preterm PROM (PPROM): assessment, clinic management (no digital vaginal exam, refer), hospital management by gestation (steroids betamethasone/dexamethasone, antibiotics erythromycin/amoxicillin, induction) | The >34-week row says 'give steroids before 37 weeks', which conflicts with steroids being limited to 28–33 weeks above. |  |

### STI and Viral Hepatitis Guidelines 2026 (draft) (2)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 756 | 46 | Flow chart for the syndromic management of anorectal discharge | The anorectal discharge chart gives ceftriaxone 250 mg IM (every other regimen in the draft uses 1 g) and doxycycline for 14 days (Table 5: 7 days, or 21 days for LGV). | #782, #785, #786 |
| 782 | 92 | Table 12: Presumptive STI treatment for survivors of sexual assault | Table 12 gives 'Azithromycin 1g IMI STAT' (azithromycin is oral) and ceftriaxone 1 g, while Figure 11 on the next page gives ceftriaxone 250 mg; the text's emergency contraception (4 combined pills, Yuzpe method) differs from Figure 11 (levonorgestrel 1.5 mg, ulipristal or copper IUD). | #756, #785, #786 |

### Enhanced Linkages Case Management SOP 2021 (1)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 264 | 55 | 12.20 Day 180 sixth clinical visit (6th ARV refill) – the last visit in the LCM | For clients still not on ART at Day 180: 'Inform client that there is no need to test again, should they decide that they want to be initiated on ART' – conflicts with retesting for verification before ART initiation required elsewhere in the SOP (sections 9.3-9.5, 12.24, Annexure 1). |  |

### Family Planning Services Guidelines 2021 (1)

| # | PDF page | Table or section | Issue | See also |
|---|---|---|---|---|
| 364 | 76 | Emergency Contraception: Who can use ECPs (MEC Category 1, MEC Category 2) | Clients on rifampicin, enzyme-inducing anticonvulsants or efavirenz are listed as suitable without a note that these reduce levonorgestrel ECP efficacy (WHO: double the LNG dose to 3 mg, or prefer a copper IUD). |  |

## Tiers 2, 3 and 0

Listed in `source_issues_tiered.csv` (and in full in `../SOURCE_ISSUES.md`). By document:

| Document | 1A | 1B | 2 | 3 | 0 |
|---|---|---|---|---|---|
| Antenatal Care Guidelines | 3 | 2 | 12 | 5 | 0 |
| Enhanced Linkages Case Management SOP 2021 | 0 | 1 | 8 | 6 | 0 |
| Family Planning Services Guidelines 2021 | 1 | 1 | 7 | 3 | 0 |
| HIV Management Amendment 2024 | 0 | 4 | 6 | 3 | 0 |
| Integrated HIV Management Guidelines 2022 | 9 | 8 | 82 | 96 | 146 |
| Integrated TB Management Guidelines 2025 | 9 | 6 | 40 | 29 | 0 |
| Mental Health Desk Guide 2022 | 7 | 4 | 19 | 4 | 0 |
| NCDs, Injuries and Mental Health Guidelines 2025 | 27 | 15 | 95 | 89 | 0 |
| PrEP Implementation Guidelines 2025 | 0 | 3 | 9 | 19 | 0 |
| STI and Viral Hepatitis Guidelines 2026 (draft) | 10 | 2 | 20 | 15 | 0 |
