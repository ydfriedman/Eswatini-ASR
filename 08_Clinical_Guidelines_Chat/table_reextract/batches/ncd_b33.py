exec(open('batches/ncd_common.py').read())
ST = CH3 + " > Stroke Management > Emergency Management of Stroke"
def L(*xs): return C("<br/>".join("- " + x for x in xs))
ITEMS = [
 D("fig-stroke-facility-flowchart", 136, ST + " > Stroke management flowchart by facility level",
   "Stroke management by facility level (primary clinic, health centre, regional/referral hospital) with key time targets and CT decision (flowchart)", ["0373", "0374", "0375"],
   "Key time targets: door-to-CT < 25 minutes; door-to-needle (tPA) < 60 minutes; door-to-puncture (thrombectomy) < 60 min; tPA window ≤4.5 hours from last known well (LKW); thrombectomy window ≤24 hours (selected patients); CEA for TIA/minor stroke < 2 weeks.\n\n"
   "1. Primary clinic: identify signs and symptoms of stroke (SPOT A STROKE: F face drooping on one side; A arm or leg weakness; S speech difficulty; T time to call for ambulance immediately). Take vital signs, check glucose level, support ABCs and give oxygen if available.\n"
   "2. Health centre: take vital signs, support ABCs, and give oxygen if needed; establish time of symptom onset; check glucose level; transfer to hospital.\n"
   "3. Regional and referral hospital: take vital signs, support ABCs, give oxygen if needed; obtain IV access, do FBC, U&E, PT & PTT, lipid profile, HbA1c and glycemia; treat hypo- and hyperglycemia (according to protocol); obtain a 12-lead ECG; emergent brain CT/MRI; assess stroke severity scales (NIH Stroke Scale or Canadian Neurological Scale); see neurologist.\n"
   "4. Does CT/MRI show hemorrhage?\n"
   "   - Hemorrhage: consult neurologist & neurosurgeon.\n"
   "   - No hemorrhage: probable or confirmed acute ischemic stroke. Repeat brain CT/MRI if the first CT brain was negative:\n"
   "     - Ischemic changes: confirmed ischemic stroke.\n"
   "     - No ischemic changes: consider other plausible diagnoses.",
   ["'Ishchemic', 'Sroke', 'PPT' printed."]),
 T("tbl-rtpa-eligibility", 137, ST + " > Is the patient a candidate for thrombolytic therapy > rtPA eligibility criteria",
   "rtPA (alteplase) eligibility criteria in acute ischaemic stroke: inclusion (all must be met) and exclusion (any = contraindicated)", ["0376"],
   [[C("INCLUSION — All must be met"), C("EXCLUSION — Any = contraindicated")]],
   [[L("Ischemic stroke diagnosed", "Onset < 4.5 hours", "Age 18–80 years old"),
     L("Acute/severe head trauma within 3 months", "Ischemic stroke within 3 months", "Previous ICH", "Suspected SAH", "Intracerebral tumor", "Intracranial/intraspinal surgery within 3 months", "Active internal bleeding", "GI malignancy or serious GI bleed within 3 months", "Extensive hypoattenuation or hemorrhage on CT", "Known bleeding diathesis", "Aortic dissection", "Infective endocarditis", "Recent myocardial infarction", "Heparin within 48h (APTT prolonged) or LMWH within 24h", "Direct thrombin or factor Xa inhibitor within 48h", "NIHSS < 6 or > 25", "BP > 185/110 mmHg", "Platelets < 100,000/mm³", "Glucose > 22.2 mmol/L or < 2.7 mmol/L")]],
   source_flags=["'NIHSS < 6 or > 25' as an exclusion conflicts with the tPA contraindications on p.133 (only NIHSS = 0 or rapidly improving) and with the DAPT advice for minor stroke (NIHSS ≤3). The age limit 18-80 is also not in the p.133 list. Clinician to confirm."]),
 T("tbl-stroke-acute-contraindications-secondary", 138, ST + " > Is the patient a candidate for thrombolytic therapy > Acute management, contraindications and secondary prevention",
   "Acute ischaemic stroke: acute management (alteplase, labetalol, thrombectomy, cerebral oedema), thrombolysis contraindications (absolute and relative), and secondary stroke prevention", ["0377", "0378", "0379"],
   [[C("Acute Stroke Management", rs=2), C("Thrombolytic Contraindications", cs=2), C("Secondary Stroke Prevention", rs=2)],
    [C("Absolute"), C("Relative")]],
   [[C("1. IV Alteplase (0.9 mg/kg: 10% bolus in 1 min, rest over 1 hour) given if 3-4.5 hours from stroke symptom onset. No anticoagulation or antiplatelets within 24h of lysis.<br/>2. IV labetalol if SBP > 220 mmHg or DBP > 120 mmHg, or active ischemic coronary heart disease, heart failure, aortic dissection, hypertensive encephalopathy, pre-eclampsia/eclampsia: 15% lowering during the first 24 h; if lysis, keep BP < 180/105 mmHg.<br/>3. Endovascular thrombectomy.<br/>4. Cerebral edema: HOB > 30°, IV mannitol, or hemicraniectomy."),
     C("1. Any prior ICH<br/>2. Intracranial neoplasm, aneurysm, AVM<br/>3. Ischemic stroke within 3 months, 2 months' head/spine surgery<br/>4. Bleeding diathesis<br/>5. Suspected aortic dissection<br/>6. Severe uncontrolled HTN"),
     C("1. Severe HTN SBP > 180 or DBP > 110 mmHg<br/>2. Ischemic stroke > 3 months<br/>3. CPR > 10 min, trauma/major surgery within 3 weeks<br/>4. Internal bleed within 2-4 weeks, active PUD<br/>5. Pregnancy<br/>6. Non-compressible vascular punctures<br/>7. Platelets < 100k, INR [>] 1.7, PTT > 40, glycemia < 50 mg/dl"),
     C("1. Antiplatelets: ASA 100 mg OD<br/>2. Anticoagulants: consider in AF (CHA2DS2-VASc score), cardiac and paradoxical emboli (except endocarditis), hypercoagulable state; e.g. NOACs (rivaroxaban 20 mg OD) or warfarin (INR 2-3)<br/>3. Statin: atorvastatin 40-80 mg OD, or rosuvastatin 20 mg OD (for life)<br/>4. Blood pressure reduction (24-48 h after stroke onset; goal blood pressure '< 130/< 180' as printed; see Hypertension protocol)<br/>5. Carotid revascularization<br/>6. DVT prophylaxis: SC Lovenox (enoxaparin) 40 mg OD<br/>7. Lifestyle modification: smoking cessation, management of obesity, diabetes, and metabolic syndrome, alcohol moderation/cessation")]],
   source_flags=["Alteplase is said to be 'given if 3-4.5 hours from stroke symptom onset'; elsewhere the window is 0-4.5 h.",
                 "Absolute contraindication '2 months' head/spine surgery' differs from 3 months on pp.133 and 137.",
                 "The BP goal is printed '< 130/< 180'; probably <130/80.",
                 "'IV Alteplate (0.9m/kg)', 'AAS', 'Stain', 'DST prophylaxis', 'Puntures', 'Plates <100k, INR 1.7' and 'lysiskeen' printed; read as alteplase 0.9 mg/kg, ASA, statin, DVT prophylaxis, punctures, platelets, INR >1.7 and 'if lysis, keep'."]),
]
ASP_CI = C("Peptic ulcer; Active bleeding; Children: varicella/flu (Reye's syndrome)")
ASP_SE = C("Nausea / Dyspepsia; Heartburn / GI ulcer; Dizziness / Tinnitus")
CLO_SE = C("Purpura / Epistaxis; Edema; Headache")
ITEMS += [
 T("tbl-stroke-pharmacological", 139, CH3 + " > Stroke Management > Pharmacological Management of Stroke",
   "Pharmacological management of stroke by stroke type (TIA dual antiplatelet, ischaemic stroke, haemorrhagic stroke): drug, dose, contraindications and side effects", ["0380", "0381"],
   [[C("Stroke Type"), C("Drug Class"), C("Drug"), C("Dosage & Frequency"), C("Contraindications"), C("Side Effects")]],
   [[C("TIA (Dual Therapy × 3 weeks)", rs=2), C("Antiplatelet"), C("Aspirin"), C("Loading: 150 mg OD STAT. Maintenance: 150 mg OD po. If peptic ulcer: Ecotrin 81 mg OD po"), ASP_CI, ASP_SE],
    [C("Antiplatelet"), C("Clopidogrel"), C("Loading: 300 mg OD STAT. Maintenance: 75 mg OD po"), C("Active bleeding; ICH; Coagulation disorders"), CLO_SE],
    [C("Ischaemic Stroke (Monotherapy)", rs=3), C("Antiplatelet"), C("Aspirin"), C("Loading: 300 mg STAT po. Maintenance: 150 mg OD po. If peptic ulcer: Ecotrin 81 mg OD po"), ASP_CI, ASP_SE],
    [C("Antiplatelet"), C("Clopidogrel"), C("Loading: 300 mg OD po. Maintenance: 75 mg OD po"), C("Active bleeding; ICH; Coagulation disorders"), CLO_SE],
    [C("Anticoagulant (if AF + high CV risk)"), C("Warfarin"), C("5 mg OD po. Target INR: 2–3. Monitor INR regularly"), C("Active bleeding; Thrombocytopenia; Pregnancy; Malignant hypertension; Endocarditis / Coagulopathy"), C("Purpura / Epistaxis; Anaemia; Vasculitis; Rash / Hepatitis")],
    [C("Haemorrhagic Stroke: NO antiplatelets or anticoagulants"), C("Osmotic Diuretic (if raised ICP)"), C("Mannitol"), C("0.25–1 g/kg IV bolus every 6 hours"), C("Pulmonary congestion / oedema; Congestive Heart Failure; Severe dehydration"), C("Dehydration / Tachycardia; Pulmonary oedema; Chest pain / Diarrhoea")]],
   pages=[139, 140],
   footnotes=["General management (all stroke types): control BP — prefer CCB / ACEI / ARB (diuretics NOT first line). Hydration with isotonic solutions 0.5–1 L/day."],
   source_flags=["Antiplatelet doses differ across the stroke section: aspirin 150 mg maintenance here vs ASA 81 mg (p.134) and ASA 100 mg (p.138); aspirin loading 300 mg here vs 325 mg (p.133); TIA dual therapy '× 3 weeks' matches the 21 days on p.133.",
                 "Warfarin is given for AF here, while p.134 prefers DOACs over warfarin for AF-related stroke."]),
]
