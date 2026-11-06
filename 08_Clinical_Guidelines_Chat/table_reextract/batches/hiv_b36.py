exec(open("batches/hiv_common.py").read())
# HIV 2022 part 4, pp.259-262 (Chapter 10: palliative care and pain). From the page images; Table 10.16 bullets re-joined
# where the source wraps one bullet over several bullet glyphs.
C10 = "Chapter 10: Management of Non-Communicable Diseases"
PC = C10 + " > 10.9 Palliative Care and Management for PLHIV"
ITEMS = [
 T("tbl-10.14-pain-sources", 259, PC + " > Common Sources of Pain in PLHIV > Table 10.14", "Table 10.14 Common Sources of Pain in HIV and AIDS Clients", ["0720"],
   [r("Cutaneous/ Oral", "Visceral", "Somatic", "Neurological/ Headache")],
   [[L("Kaposi sarcoma", "Oral cavity pain", "Herpes zoster", "Oral/oesophageal candidiasis"), L("Tumours", "Gastritis", "Pancreatitis", "Infection", "Biliary tract disorders"),
     L("Rheumatological disease", "Back pain", "Myopathies"),
     L("HIV-related headaches: encephalitis, meningitis, etc.", "HIV-unrelated headaches: tension, migraine, etc.", "Iatrogenic (AZT) Peripheral neuropathy", "Herpes neuritis", "Alcohol, nutritional deficiencies")]]),
 D("fig-10.4-numeric-pain-scale", 259, PC + " > Pain Assessment > Figure 10.4", "Figure 10.4 Numeric Pain Rating Scale", [],
   "Scientifically validated pain scales: Numeric Pain Rating (adults); Wong-Baker FACES® Pain Rating Scale (children who can talk); Observation-FLACC Scale (children who cannot talk).\n\n"
   "Numeric pain rating scale 0-10 (colour bar from violet to red): 0 = no pain; 1-3 = mild pain; 4-6 = moderate pain; 7-10 = worst possible pain.",
   flags=["Figure 10.4 labels the whole 7-10 band 'worst possible pain'; the usual banding is 7-10 severe pain, with 10 the worst possible pain."]),
 D("fig-10.5-who-analgesic-ladder", 260, PC + " > World Health Organization Analgesic Step Ladder > Figure 10.5", "Figure 10.5 WHO analgesic step ladder", [],
   "Three steps with increasing pain:\n"
   "- STEP 1: Mild pain — Non-opioids (e.g., paracetamol, ibuprofen, diclofenac) ± adjuvant (e.g., antidepressant, anticonvulsant, antispasmodic, muscle relaxant, bisphosphonate, or corticosteroid). If pain is not controlled by Step 1 analgesics, move to Step 2 by adding a weak opioid.\n"
   "- STEP 2: Moderate pain — Weak opioids e.g., codeine, tramadol, or low dose of morphine ± non-opioid ± adjuvant. If a weak opioid has been used to a maximum dose for moderate pain and the client still has pain, then move to Step 3 by changing to a strong opioid.\n"
   "- STEP 3: Severe pain — Strong opioid (e.g., morphine, fentanyl, methadone) ± non-opioid ± adjuvant."),
 T("tbl-10.15-pain-children", 261, PC + " > Specific Considerations for Pain in Children > Table 10.15", "Table 10.15 Specific Considerations for Pain in Children", ["0725"],
   [r("Condition", "Consideration")],
   [r("Peripheral neuropathy", "Peripheral neuropathy is more common in adults than children, but it does occur in children and is often underdiagnosed. When treating it, add adjuvant: carbamazepine for young children and amitriptyline for older children. It is best not to use carbamazepine and EFV together; if necessary, switch EFV to lopinavir/ritonavir (LPV/r)."),
    r("Muscle spasm in HIV", "Children with basal ganglia disease and abnormal movements may also experience considerable pain from muscle spasms."),
    r("Treatment-related problems with HIV and AIDS and cancer", "For management of mucositis, use mouthwash as appropriate (e.g., in children, 10 mL lignocaine [1%], 30 mL Nystatin suspension and 15–30 mg morphine). Gargle and spit out.")],
   source_flags=["Table 10.15 recommends carbamazepine for neuropathic pain in young children without mentioning that carbamazepine lowers DTG levels (most children are on DTG); the text on p.263 notes the DTG/EFV interaction for adults.",
                 "The mucositis mouthwash for children includes '15–30 mg morphine' with no volume or concentration; verify before use."]),
 T("tbl-10.16-pain-syndromes", 261, PC + " > Pain Management Strategy > Table 10.16", "Table 10.16 Specific Pain-Related Syndromes in HIV", ["0727", "0728", "0729"],
   [r("Clinical Presentation", "Causes", "Treatment")],
   [{"section": "Peripheral neuropathy"},
    [L("Burning pain in hands and feet", "Pins and needles", "Allodynia (the experience of pain from a stimulus that would not usually cause pain in a normal individual)", "Pain relieved by local pressure"),
     L("HIV itself (distal sensory neuropathy)", "Cytomegalovirus", "Nerve entrapments, carpal tunnel syndrome", "Post-herpetic neuralgia", "ARVs, especially didanosine and stavudine", "Other treatments: chemotherapy, Isoniazid, Metronidazole"),
     L("Remove offending agents if possible: change stavudine or didanosine to TDF", "Treat herpes zoster early with acyclovir to limit post-herpetic neuralgia", "Use WHO analgesic ladder—NSAIDs and opioids", "Gabapentin in resistant cases", "Try topical analgesics", "For localized neuropathies-nerve block")],
    {"section": "Abdominal pain in HIV"},
    [C("Abdominal pain in HIV"),
     L("TB abdomen", "Mycobacterium avium complex (MAC)", "Pancreatitis", "Peptic ulcer disease", "Gastro-oesophageal reflux disease", "Gall bladder and biliary tract disease", "Malabsorption syndromes", "Drug side effects", "Neuropathic abdominal pain (diagnosis of exclusion)"),
     L("Diagnose and treat the underlying cause if possible", "Start ARVs if indicated", "Treat pain according to the WHO analgesic ladder", "Beware of ileus/constipation caused by opioids: can make the pain worse", "Remember morphine causes contraction of sphincter of Oddi, so pethidine is a better choice in pancreatitis", "For IRIS, try low-dose steroids", "Beware of NSAIDs and gastritis")],
    {"section": "Muscle spasm"},
    [C("Muscle spasm"),
     L("Caused by HIV itself in the form of HIV encephalopathy with increased tone", "Secondary to cerebral insults from bacterial or tuberculosis meningitis"),
     L("ARVs", "Levodopa (extrapyramidal dysfunction)", "Analgesics (Step 2: non-opioid + weak opioid)", "NSAIDs may help with musculoskeletal pain", "Baclofen (for muscle spasm, can cause seizures)", "Adjuvants, especially Clonazepam")],
    {"section": "Headache"},
    [L("Headache with focal neurological deficits"), L("Cryptococcal meningitis", "Toxoplasmosis"),
     L("Treat pain according to the WHO analgesic ladder", "Morphine and pethidine are contraindicated for raised intracranial pressure", "Lumbar puncture is essential to control intracranial pressure from cryptococcal meningitis")]],
   pages=[261, 262],
   footnotes=["In the source several bullets are split across lines that each carry a bullet glyph (e.g. 'Cytomegalovirus Nerve / entrapments'); they are re-joined here."],
   source_flags=["Table 10.16 still advises changing stavudine or didanosine to TDF; neither drug is in current Eswatini regimens."]),
 B("box-palliative-symptom-control", 262, PC + " > General Principles of Treatment", "General principles of treatment, nausea and neuropathic pain dosing (palliative care)", [],
   "Key message: Give palliative care medication by the mouth, by the clock, by the ladder.\n\n"
   "Dosing for nausea: prescribe an anti-emetic for 7–10 days, after which nausea should subside.\n- Haloperidol: 1.5 – 5 mg, every night, for 5–7 days OR\n- Metoclopramide: 10 mg, 3 times daily, for 5–7 days\n\n"
   "Management of neuropathic pain:\n- Amitriptyline: Adults: 10–75 mg or 0.5–2 mg/kg at night (then increase slowly as needed).\n- Sodium valproate: Adults: 200 mg – 1.2 g once a day\n"
   "- Gabapentin: Adults: 300–400 mg in divided doses, increase gradually according to the response. Maximum 2400 mg/ day.\n"
   "If sodium valproate and gabapentin are not available, carbamazepine can be used, but it should be noted that carbamazepine can interact with DTG and EFV. Carbamazepine: Adults: start at 100 mg twice a day and can be increased up to 800 mg twice a day.",
   pages=[262, 263],
   flags=["Anti-emetic duration is inconsistent: 'for 7–10 days' in the lead sentence, '5–7 days' for each drug.",
          "Amitriptyline for adults is given as '10–75 mg or 0.5–2 mg/kg at night'; 0.5–2 mg/kg is a paediatric-style dose (35–140 mg for a 70 kg adult)."]),
]
