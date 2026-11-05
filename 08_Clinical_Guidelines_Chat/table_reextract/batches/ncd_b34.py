exec(open('batches/ncd_common.py').read())
ITEMS = [
 D("fig-arf-jones-criteria", 142, CH3 + " > Acute Rheumatic Fever > Diagnosis of Acute Rheumatic Fever (ARF)",
   "Diagnosis of acute rheumatic fever by the revised Jones criteria (2015): major and minor manifestations, evidence of preceding GAS infection, and diagnostic rules", ["0389", "0390"],
   "Diagnosis of acute rheumatic fever (ARF) by the revised Jones criteria (2015):\n"
   "- Major manifestations: carditis (clinical/subclinical); polyarthritis/migratory arthritis; Sydenham's chorea; erythema marginatum.\n"
   "- Minor manifestations: 1. fever (≥38°C); 2. monoarthralgia; 3. prolonged PR interval on ECG; 4. increased acute phase reactants (ESR ≥30 mm/hour or CRP ≥3.0 mg/dl).\n"
   "- Evidence of preceding GAS infection: 1. GAS on throat swab (positive culture); 2. raised ASO titre; 3. raised anti-DNase B; 4. positive quick strep test.\n\n"
   "The diagnosis of ARF is confirmed in any of these situations:\n"
   "1. Two major manifestations and any evidence of preceding GAS infection, OR\n"
   "2. One major and two minor manifestations and any evidence of preceding GAS infection, OR\n"
   "3. Presence of rheumatic chorea.",
   ["Subcutaneous nodules are a major manifestation in the text above (item 4) but are missing from the major list in this chart."]),
]
ITEMS += [
 T("tbl-rhd-cxr-ecg-findings", 144, CH3 + " > Rheumatic Heart Disease > Diagnostic findings according to diagnostic modality",
   "Rheumatic heart disease: chest X-ray and ECG findings by valvular lesion (mitral stenosis, mitral regurgitation, aortic stenosis, aortic regurgitation)", ["0394"],
   [[C("Valvular Lesion"), C("Chest X-ray Findings"), C("ECG Findings")]],
   [[C("Mitral Stenosis"), C("- Straightening of left heart border<br/>- Double right heart border<br/>- Splaying of carina<br/>- Pulmonary venous congestion (e.g., Kerley B lines, bat wings)"), C("- P mitrale (broad, notched P wave in lead II)<br/>- Atrial fibrillation (AF) common")],
    [C("Mitral Regurgitation"), C("- Enlarged left atrium (LA) and left ventricle (LV)<br/>- Pulmonary venous congestion"), C("- Features of LA and LV enlargement<br/>- Atrial fibrillation may be present")],
    [C("Aortic Stenosis"), C("Possible aortic valve calcification"), C("- Left ventricular hypertrophy (LVH)<br/>- ± T-wave inversion in V6")],
    [C("Aortic Regurgitation"), C("- LV-type cardiomegaly<br/>- Features of pulmonary venous hypertension"), C("- LV enlargement features")]],
   table_note="Echocardiogram is done to confirm the diagnosis and evaluate chamber size, valve morphology, valve stenosis or regurgitation, and ventricular function (details in the echocardiographic manual)."),
]
ITEMS += [
 D("fig-rhd-children-algorithm", 145, CH3 + " > Rheumatic Heart Disease > Algorithm with the Initial Evaluation and Management of RHD in Children",
   "Initial evaluation and management of acute rheumatic fever and rheumatic heart disease in children (algorithm: Jones criteria, primary and secondary penicillin prophylaxis by weight, valve involvement)", ["0396"],
   "Acute rheumatic fever (ARF):\n"
   "- 2-4 weeks after Group A Streptococcus. Diagnosis based on the revised Jones criteria:\n"
   "  - Major manifestations: pancarditis; subcutaneous nodules; Sydenham chorea; erythema marginatum; arthritis (usually migratory polyarthritis).\n"
   "  - Minor manifestations: fever 38°C; prolonged PR interval (on ECG); ESR 60 mm in the first hour and/or CRP 3.0 mg/dL; arthralgia.\n"
   "  - Diagnosis, initial ARF: 2 major OR 1 major plus 2 minor. Recurrent ARF: criteria for initial ARF OR 3 minor.\n"
   "- Management:\n"
   "  - Primary prevention: penicillin V. If <27 kg: 250 mg 2 to 3 times daily for 10 days. If >27 kg: 500 mg 2 to 3 times daily for 10 days.\n"
   "  - Secondary prevention: Extencilline (benzathine penicillin G), as printed: 'If >27 kg: 600,000 IU IM single dose every 28 days'; 'If >27 kg: 1.2M IU IM single dose every 28 days'.\n"
   "  - If allergic to penicillins: azithromycin 6 mg/kg/day, maximum dose 250 mg.\n"
   "  - Supportive treatment: arthritis, >2 years old: ibuprofen PO 10 to 20 mg/kg/day every 12 hours (maximum daily dose 1000 mg).\n\n"
   "Rheumatic heart disease (RHD): still prevalent in resource-limited settings; sequela of untreated ARF; definitive diagnosis by echocardiography. By valve:\n"
   "- Mitral valve involvement (most common): mitral regurgitation/mitral stenosis. Presentation: dyspnoea, paroxysmal nocturnal dyspnoea, systolic murmur at the apex, hepatomegaly, lower-limb oedema.\n"
   "- Aortic valve involvement (commonly with mitral valve): aortic regurgitation, aortic stenosis. Presentation: wide pulse pressure, syncope, thrill, diastolic/systolic (AR/AS) murmur, hepatomegaly, lower-limb oedema.\n"
   "- Tricuspid valve involvement (less common, very rarely isolated). Presentation: dyspnoea, orthopnoea, paroxysmal nocturnal dyspnoea, systolic murmur at the LLSB, hepatomegaly, lower-limb oedema.\n"
   "- For every valve: secondary prevention with Extencilline: if <27 kg 600,000 IU IM single dose every 28 days; if >27 kg 1.2M IU IM single dose every 28 days (the mitral column prints 'If <27 kg: 1.2M IU'). Treat heart failure as in the HF algorithm. A paediatric cardiologist decides the indication and timing of cardiac surgery.\n\n"
   "*To prevent pain from the Extencilline injection, mix the drug with low-dose lidocaine hydrochloride 1% (3.5-5 mls) solution.",
   ["Secondary prophylaxis weight bands are misprinted: the ARF box gives '>27 kg' for both 600,000 IU and 1.2M IU, and the mitral column gives 'If <27 kg: 1.2M IU'. The aortic and tricuspid columns give <27 kg = 600,000 IU, >27 kg = 1.2M IU. Clinician to confirm.",
    "Minor criteria here (ESR 60 mm, CRP 3.0 mg/dL; 'arthralgia') differ from the Jones chart on p.142 (ESR ≥30 mm/hour, CRP ≥3.0 mg/dl, monoarthralgia).",
    "The old chunk for this page lost the ARF box and the mitral column.", "'dysonea', 'postrul', 'Arthrisis', 'Arthrlgia', 'CRO' printed."]),
]
ITEMS += [
 D("fig-rhd-secondary-care", 147, CH3 + " > Rheumatic Heart Disease > Algorithm for Management of Rheumatic Heart Disease (RHD) at Secondary Care Level",
   "Management of rheumatic heart disease at secondary care level (algorithm by valve lesion: mitral stenosis, mitral regurgitation, aortic insufficiency, aortic stenosis)", ["0400", "0401"],
   "1. Suspect RHD at the health centre if a patient presents with new onset dyspnoea, fatigue or palpitations, plus: fast and irregular pulse; hyperactive precordium; loud murmur; distended jugular veins; ankle/leg oedema.\n"
   "2. Transfer to the district hospital: order CXR, FBC, RFTs, 12-lead ECG. Confirm the diagnosis with echocardiography.\n"
   "3. By lesion:\n"
   "   - Mitral stenosis (leaflet and sub-valvular thickening, commissural fusion, calcification and accelerated forward flow on colour Doppler; left atrium usually dilated): start PO atenolol 25 mg if HR >90 bpm and BP >90/60 mmHg; PO penicillin V 250 mg BID; check for AF to start warfarin 5 mg OD (therapeutic INR 2-3). If in pulmonary oedema, admit for IV furosemide. Early referral for balloon mitral valvotomy (BMV).\n"
   "   - Mitral regurgitation (leaflet and sub-valvular thickening, restricted leaflet motion, accelerated backward flow on colour Doppler; LV dilation +/- dysfunction): EF <60%: treat per HFrEF protocol, add penicillin V 250 mg BID, urgent referral to a cardiologist. EF >60%: low-dose PO furosemide, penicillin V 250 mg BID, non-urgent referral to a cardiologist.\n"
   "   - Aortic insufficiency (thickened cusps with rolled edges; accelerated backward flow on colour Doppler; usually with rheumatic mitral valve lesions; LV dilation +/- dysfunction): EF <60%: treat per HFrEF protocol, add penicillin V 250 mg BID, urgent referral to a cardiologist. EF >60%: low-dose PO furosemide, penicillin V 250 mg BID, non-urgent referral to a cardiologist.\n"
   "   - Aortic stenosis (thickened cusps with rolled edges; accelerated forward flow on colour Doppler; usually with rheumatic mitral valve lesions): aortic stenosis is a surgical condition. Refer to a cardiologist to quantify severity and plan surgery. Avoid afterload reduction unless AI or MR is associated.\n\n"
   "Please note: women should be educated and offered reproductive health services upon RHD diagnosis. Patients on warfarin should have their INR checked regularly and kept within the therapeutic range. Estimate RVSP by TR jet CW if it can inform management; check the tricuspid valve for rheumatic changes. Mixed mitral or aortic valve disease can be challenging for less experienced practitioners: consult for management. Secondary prophylaxis with penicillin is recommended until 40 years of age.",
   ["Secondary prophylaxis here is oral penicillin V 250 mg BID, while the children's algorithm (p.145) uses IM Extencilline every 28 days.",
    "An EF of exactly 60% is not covered (EF <60% / EF >60%).", "'Stenisis', 'quantity severity', 'Ballon' printed."]),
]
