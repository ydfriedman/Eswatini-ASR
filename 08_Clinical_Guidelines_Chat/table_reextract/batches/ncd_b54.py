exec(open('batches/ncd_common.py').read())
EP = CH8 + " > Epilepsy"
def r(*v): return [C(x) for x in v]
ITEMS = [
 T("tbl-seizure-classification", 244, EP + " > Classification",
   "Classification of seizures: generalised (tonic-clonic, absence, myoclonic, epileptic spasms) and focal (aware, impaired awareness): consciousness, duration, features, typical age", ["0699"],
   [[C("Category"), C("Type"), C("Consciousness"), C("Duration"), C("Key Clinical Features"), C("Typical Age/Notes")]],
   [r("Generalized", "Tonic–clonic", "Lost", "2–5 min", "Fall, stiffening → jerking, frothing, tongue bite, incontinence, postictal sleep/confusion", "Most common"),
    r("Generalized", "Absence", "Briefly lost", "5–30 sec", "Blank stare, stops activity, eye rolling, no fall, no confusion after", "School-aged children, frequent, provoked by hyperventilation"),
    r("Generalized", "Myoclonic", "Usually preserved", "Seconds", "Sudden shock-like jerks of limbs/body", "Often in epileptic syndromes"),
    r("Generalized", "Epileptic spasms (infantile spasms)", "Variable", "Seconds (clusters)", "Head/trunk flexion, arm abduction, knee bending", "Infants <1 yr, developmental delay"),
    r("Focal", "Focal aware (simple partial)", "Preserved", "Seconds", "Local twitching, sensory changes, déjà vu, hallucinations", "Patient aware of event"),
    r("Focal", "Focal impaired awareness (complex partial)", "Impaired", "1–3 min", "Aura, staring, automatisms (lip smacking, picking clothes), confusion, amnesia", "Slow recovery, may appear aggressive")],
   pages=[244, 245],
   context_before="Epilepsy is a chronic noncommunicable brain disorder characterised by recurrent unprovoked seizures (two or more unprovoked seizures more than 24 hours apart). This module covers convulsive epilepsy. With proper treatment, most people can be seizure-free.",
   source_flags=["Table continues onto p.245 with the header repeated. The focal aware duration is printed 'Seconds (clusters)', copied from the row above."]),
 B("box-epilepsy-algorithm", 246, EP + " > Epilepsy Algorithm of Assessment and Management",
   "Epilepsy assessment and management algorithm: 8 assessment steps, emergency management of seizures >5 min, when to refer, first aid at home", ["0701", "0702", "0703", "0704"],
   "Assessment:\n"
   "1. Person presents with episodes of convulsions (fits, shaking, stiffening), witnessed or reported.\n"
   "2. Confirm 2+ unprovoked seizures (not febrile, not substance-related, not syncope). Onset, duration, frequency?\n"
   "3. Rule out other causes: hypoglycaemia, head injury, meningitis, stroke, eclampsia, substance withdrawal.\n"
   "4. Assess: postictal confusion? Tongue-biting? Urinary incontinence? Aura? Birth trauma history?\n"
   "5. Check current medications; assess for pregnancy in women of childbearing age.\n"
   "6. Assess functional impairment: school, work, driving, daily activities, social life.\n"
   "7. Screen for mental health comorbidities (depression, anxiety).\n"
   "8. Diagnosis: epilepsy confirmed → proceed to management.\n\n"
   "EMERGENCY MANAGEMENT (seizure > 5 min): call for emergency help immediately; diazepam 10-20 mg IV/PR or lorazepam 4 mg IV for status epilepticus; airway – place in recovery position, ensure breathing; DO NOT restrain; DO NOT put anything in the mouth; monitor blood glucose; give thiamine if alcohol-related.\n\n"
   "When to refer: first seizure (confirm diagnosis); seizures not controlled after 2 drug trials; pregnancy + epilepsy (specialist input needed); status epilepticus; suspected structural cause (tumour, stroke).\n\n"
   "First aid at home (advise carers): lay the person on their side, head turned to the side; ensure the airway is clear, loosen tight clothing; time the seizure and stay until fully conscious; no food/water until fully alert; seek help if the seizure lasts >5 min, there is no recovery, or injury; epilepsy is NOT contagious.",
   ["'First seizure' is a referral reason, while step 2 requires 2+ unprovoked seizures for diagnosis; both are printed."]),
 T("tbl-antiepileptic-drugs", 246, EP + " > Epilepsy Management — Pharmacological Treatment",
   "Antiepileptic medicines: sodium valproate, carbamazepine, phenytoin, phenobarbital, lamotrigine: adult and child doses, contraindications, side effects; principles of AED treatment", ["0705", "0706", "0707", "0708"],
   [[C("Class"), C("Drug"), C("Dosage and Frequency"), C("Contraindications"), C("Side Effects")]],
   [r("Anticonvulsant", "Sodium valproate", "Adults: 200 mg TDS PO; maintenance 400-1800 mg/day divided into 3 doses. Children: 10-15 mg/kg/day PO divided into 2 doses; maintenance <20 kg: 20-40 mg/kg/day; >20 kg: 20-30 mg/kg/day", "Hepatic impairment; von Willebrand disease", "Tremor, dizziness, weight gain, alopecia, diuresis, thrombocytopenia, impaired hepatic function"),
    r("Anticonvulsant", "Carbamazepine", "Adults: 200 mg BD PO; maintenance 800-1200 mg/day divided into 2 doses. Children: 10-20 mg/kg/day PO divided into 2 doses; maintenance 20-30 mg/kg/day", "Absence and myoclonic seizures; bone marrow suppression; hypersensitivity to tricyclic antidepressants", "Blurred/double vision, nystagmus, ataxia, drowsiness, hyponatremia, rash, cytopenia, liver dysfunction, Stevens-Johnson syndrome, toxic epidermal necrolysis"),
    r("Anticonvulsant", "Phenytoin", "Adults: 100 mg TDS PO; maintenance 300-900 mg/day divided into 3 doses. Children: 5-8 mg/kg/day divided into 2 doses", "Absence and myoclonic seizures; febrile convulsions", "Gingival hypertrophy, rash, confusion, fever, slurred speech, double vision, ataxia, bone marrow depression, hepatitis"),
    r("Barbiturate", "Phenobarbital", "Adults: 30 mg NOCTE PO; maintenance 30-120 mg/day divided into 2 doses. Children: 3-5 mg/kg/day divided into 2 doses", "Airway obstruction; dyspnea; marked hepatic impairment", "Nausea, rash, sedation, lethargy, dependence, alteration of sleep cycle, hyperactivity, ataxia, liver dysfunction"),
    r("Anticonvulsant", "Lamotrigine", "Adults: 25 mg every other day [with valproate], 25 mg OD [without valproate]; maintenance 100-200 mg/day [with valproate], 100-400 mg/day [without valproate]. Children: 0.15 mg/kg/day [with valproate], 0.3 mg/kg/day [without valproate]; maintenance 1-3 mg/kg/day [with valproate], 4.5-7.5 mg/kg/day [without valproate]", "Hypersensitivity to the drug or its ingredients. Be cautious and titrate slowly if used with sodium valproate", "Drowsiness, dizziness, diplopia, rash, cytopenia, liver injury, Stevens-Johnson syndrome, toxic epidermal necrolysis")],
   pages=[246, 247, 248],
   context_before="Antiepileptic medications: start one medication at the lowest dose and increase slowly until seizures are controlled. 1. Start low and go slow with a single AED as monotherapy, chosen by seizure type and epilepsy syndrome; titrate to the maximal dose. 2. If the first AED is ineffective at the maximum tolerated dose, introduce an alternative AED slowly without tapering the first. 3. If there is a good response to the second AED, consider withdrawing the original gradually. 4. If the first add-on AED is ineffective or has undesirable side effects, withdraw it slowly and replace it with another add-on AED. 5. If seizures are not controlled on two AEDs, some patients may benefit from a third. 6. Prefer an add-on AED with a different mode of action. 7. Review the diagnosis if seizures continue despite this approach and 2-3 years have elapsed.",
   source_flags=["The barbiturate row is printed 'Phenytoin'; the doses (30 mg nocte; 3-5 mg/kg/day) are phenobarbital doses. Clinician to confirm.",
                 "Lamotrigine children's dose without valproate is printed '0.3mg/kg' (no '/day'). Table spans pp.247-248."]),
 B("box-epilepsy-psychoeducation-cautions", 248, EP + " > Psychoeducation, cautions and follow-up",
   "Epilepsy psychoeducation and psychosocial interventions, cautions and special populations (drug interactions, pregnancy, children, PLHIV), and follow-up", ["0709", "0710", "0711"],
   "Psychoeducation & psychosocial interventions:\n"
   "- Epilepsy is caused by abnormal electrical brain activity, NOT spirits or witchcraft.\n"
   "- Chronic condition: medication controls seizures in most if taken daily.\n"
   "- People with epilepsy can marry, work, have children and lead normal lives.\n"
   "- Avoid open fires, swimming alone, heights, heavy machinery, alcohol excess.\n"
   "- Observe local driving laws; may qualify for disability benefits.\n"
   "- All AEMs: taper slowly; an abrupt stop causes breakthrough seizures.\n"
   "- Review every 3-6 months; check adherence and side effects.\n\n"
   "Cautions & special populations:\n"
   "- Check drug-drug interactions: AEMs reduce the efficacy of hormonal contraceptives and antiretrovirals.\n"
   "- Rare: severe bone marrow depression, Stevens-Johnson syndrome.\n"
   "- Pregnancy: consult a specialist; supplement folate; valproate contraindicated.\n"
   "- Children: weight-based dosing; monitor growth and development.\n"
   "- PLHIV: check interactions with antiretrovirals before prescribing.\n"
   "- (Printed in the same cell:) minimum 2 years seizure-free before [stopping AEMs].\n\n"
   "Follow-up (every 1-3 months initially, then 3-6 monthly): review seizure frequency (decreased or stopped?); check medication adherence and side effects; assess functional status (school, work, daily activities); screen for depression/anxiety comorbidity; if no seizures for 2+ years, discuss gradual tapering with a specialist; if seizures continue despite an adequate dose, increase the dose, check adherence, or refer to a specialist.",
   pages=[248, 249],
   flags=["'minimum 2 years seizure-free before' is printed at the end of the PLHIV bullet; it presumably refers to stopping AEMs.",
    "Valproate is 'contraindicated' in pregnancy here, while it is listed without a pregnancy warning in the drug table. The follow-up box continues on p.249."]),
]

ITEMS += [
 D("fig-epilepsy-long-term-treatment", 249, EP + " > Systematic approach to long-term pharmacological treatment",
   "Systematic approach to long-term pharmacological treatment of epilepsy: when to start AEDs, monotherapy, second AED, referral, re-evaluation, surgery and other options", ["0712", "0713", "0714"],
   "When to start AEDs: immediate AED therapy is usually not necessary after a single seizure; it is generally started after two or more unprovoked seizures.\n\n"
   "1. Initial AED monotherapy. Select the AED based on seizure type/syndrome, age, sex, childbearing potential, comorbidities, concomitant medications, adverse effects, interaction profile.\n"
   "2. If failure: second AED, as monotherapy or add-on.\n"
   "3. If failure: referral to a tertiary care centre (a).\n"
   "4. Diagnostic re-evaluation (epilepsy yes/no, seizure types, syndrome, adherence, dosing), then: resective surgery; additional drug trials; neurostimulatory and dietary approaches (b).\n"
   "Options at tertiary level: epilepsy surgery; ketogenic diet; vagus nerve stimulation; deep brain stimulation.",
   ["The footnotes (a) and (b) are not printed. 'sydrome' printed."]),
 D("fig-status-epilepticus", 250, CH8 + " > Epilepsy > Status Epilepticus > Treatment Algorithm for Status Epilepticus",
   "Management algorithm for status epilepticus in adults (ICU): stabilisation 0-5 min, first-line benzodiazepines 5-15 min, second-line valproate or phenytoin 15-30 min, third-line anaesthetic infusions after 30 min", ["0717"],
   "Epilepsy emergencies: (i) acute repetitive seizures; (ii) status epilepticus.\n\n"
   "0-5 minutes (stabilisation):\n"
   "1. Stabilise the patient: assess airway, breathing, circulation.\n"
   "2. Time the seizure onset; monitor vital signs (ECG, BP, HR, temperature).\n"
   "3. Finger-stick blood glucose. If glucose <60 mg/dl, give 50 ml of 50% dextrose IV.\n"
   "4. Laboratory investigations: electrolytes, CBC, liver and renal function tests.\n"
   "Does the seizure continue? No → routine medical care. Yes →\n\n"
   "5-15 minutes (first-line therapy): IV diazepam ('0.5 - 0.2 mg/kg/dose' as printed), max 10 mg, OR IV lorazepam 0.1 mg/kg (max not printed).\n"
   "Does the seizure continue? No → routine medical care. Yes →\n\n"
   "15-30 minutes, on ward (second-line therapy): valproate (VPA) 30 mg/kg loading dose and 4-8 mg/kg every 8 hr maintenance, OR phenytoin 20 mg/kg loading dose and '1.5 mg' every 8 hr maintenance (as printed).\n"
   "Does the seizure continue? No → routine medical care. Yes →\n\n"
   "After 30 minutes, on ward (third-line therapy):\n"
   "1. Ketamine 1-2 mg/kg bolus and 1-2 mg/kg/hr continuous infusion for a minimum of 24 hr.\n"
   "2. Propofol 1-3 mg/kg bolus and 5-10 mg/kg/hr continuous infusion for 24 hr.\n"
   "3. Thiopental 3-5 mg/kg bolus and '3-3 mg/kg/hr' continuous infusion for 24 hr (as printed).",
   ["Several doses are misprinted: diazepam '0.5 - 0.2 mg/kg/dose' (usually 0.15-0.2 mg/kg); phenytoin maintenance '1.5 mg every 8hr' (no per-kg unit); thiopental infusion '3-3 mg/kg/hr'; lorazepam has no maximum. Propofol 5-10 mg/kg/hr is high for a 24 h infusion. Clinician to confirm.",
    "Glucose threshold is in mg/dl (60 mg/dl ≈ 3.3 mmol/L) while the rest of the guideline uses mmol/L. 'Diazepan', 'bogus' (bolus), 'stablization' printed."]),
]
