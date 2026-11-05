exec(open('batches/ncd_common.py').read())
CHD = CH3 + " > Congenital Heart Disease"
ITEMS = [
 D("fig-chd-pulse-oximetry-screening", 148, CHD + " > Screening and Diagnosis > Congenital Heart Diseases Screening",
   "Newborn pulse oximetry screening for congenital heart disease (flowchart: abnormal, indefinite, normal; repeat at 1 hour)", ["0404"],
   "Measure O2 saturation in the right hand and any foot of all newborns between 24-36 hours of age.\n"
   "- O2 sat <90% in the right hand or any foot = abnormal → screening failed: paediatric cardiologist consult.\n"
   "- O2 sat 90-94% in the right hand and any foot, or >3% difference between right hand and any foot = indefinite → repeat measurements in 1 hour.\n"
   "- O2 sat ≥95% in the right hand or any foot and ≤3% difference between right hand and any foot = normal → screening passed.\n"
   "Second measurement (1 hour later): same three outcomes; indefinite → repeat measurements in 1 more hour.\n"
   "Third measurement: O2 sat 90-94% or >3% difference = abnormal → screening failed (paediatric cardiologist consult); O2 sat ≥95% and ≤3% difference = normal → screening passed.",
   ["'Screening passed' is also followed by 'Pediatric cardiologist consult' in the PDF, probably copied from 'Screening failed'.",
    "The third-round box is garbled ('2 Sat between 90-94% in right any foot = Abnormal difference between right hand and any foot = Indefinite'); read as abnormal on the third reading, the usual protocol. Clinician to confirm."]),
]
ITEMS += [
 D("fig-chd-suspected-approach", 149, CHD + " > Approach to suspected congenital heart disease",
   "Approach to suspected congenital heart disease (decision tree: central cyanosis, hyperoxia test, acyanotic vs cyanotic CHD)", ["0405", "0406"],
   "Suspect congenital heart disease with: blue since birth or soon after birth and persistently blue, worsened by crying; poor or intermittent feeding, excessive sweating during feeding, crying and sleeping; precordial bulge, exercise intolerance; recurrent lower respiratory tract infection; recurrent episodes of heart failure; squatting, cyanotic spells, loss of consciousness; chest pain, shortness of breath and palpitations at rest and on exertion.\n\n"
   "Central cyanosis/hypoxia?\n"
   "- No: acyanotic CHD → chest X-ray, ECG, echocardiography.\n"
   "- Yes: cyanotic CHD or pulmonary disease; consider non-cardiac causes like sepsis. Do a hyperoxia test (formal or informal, 15 L of O2) and check O2 sat:\n"
   "  - O2 sat rises (Yes): pulmonary disease / non-cardiac causes. N.B. the hyperoxia test is not definitive; it does not completely exclude CHD.\n"
   "  - O2 sat does not rise (No): cyanotic CHD → chest X-ray, ECG, echocardiography.",
   ["'cynanosis', 'cynatic', 'Echocardior' printed."]),
]
CRIT = "If critical: ductal dependent; presents in the first days of life in shock."
ITEMS += [
 D("fig-chd-acyanotic-cyanotic", 150, CHD + " > Acyanotic and cyanotic congenital heart disease",
   "Acyanotic and cyanotic congenital heart disease: types, clinical features, imaging and management (pressure vs volume overload; decreased vs increased pulmonary blood flow)", ["0408", "0409"],
   "ACYANOTIC CHD\n"
   "A. Pressure overload (clinical manifestations depend on the severity of the obstruction):\n"
   f"- Pulmonary stenosis: {CRIT} If non-critical: tachypnoea, poor weight gain, poor feeding, ejection murmur over the pulmonary area.\n"
   f"- Aortic stenosis: {CRIT} If non-critical: tachypnoea, poor weight gain, poor feeding, ejection murmur over the pulmonary area.\n"
   f"- Coarctation of the aorta: {CRIT} If non-critical: HTN in the upper limbs, radial-to-femoral pulse delay, systolic murmur radiating to the back.\n"
   "B. Volume overload (clinical manifestations depend on the severity of the left-to-right shunt):\n"
   "- ASD: asymptomatic; can present with recurrent chest infections and poor weight gain. Physical findings: no respiratory distress, ejection murmur (most of the time absent) at the pulmonary area, fixed split S2.\n"
   "- VSD/AVSD: symptoms appear in the first weeks of life: diaphoresis, poor weight gain, poor feeding, tachypnoea, tachycardia. Physical findings: chest retraction, holosystolic murmur at the LLSB, hepatomegaly, Harrison sulcus.\n"
   "- PDA/AOW: symptoms appear in the first weeks of life: diaphoresis, poor weight gain, poor feeding, tachypnoea, tachycardia. Physical findings: chest retraction, continuous murmur at the left infraclavicular area, hepatomegaly.\n"
   "Management of acyanotic CHD: 1. General measures: nutritional support, prevention of URTI and infective endocarditis. 2. Medical treatment if in heart failure: Lasix (furosemide) 1-3 mg/kg/day; Aldactone (spironolactone) 1-3 mg/kg/day; captopril (with caution) 0.3-0.5 mg/kg/day. 3. Treat the underlying pathology surgically or by catheterization.\n\n"
   "CYANOTIC CHD\n"
   "A. Decreased pulmonary blood flow:\n"
   "- Tetralogy of Fallot (TOF): clinical features depend on the severity of the RVOTO; tet spells, squatting, poor weight gain; cyanosis, SEM at the ULSB, no hepatomegaly. Imaging: chest X-ray normal heart size with a boot shape, oligaemic lungs; ECG: RAD, RAE, RVH. Management of tet spells: knee-chest position, oxygen, IV fluids 10-20 ml/kg NS, propranolol 0.1 mg/kg/dose. Definitive management: paediatric cardiologist decides the indication and timing of cardiac surgery.\n"
   "- Tricuspid valve diseases: types: tricuspid atresia, tricuspid stenosis, Ebstein anomaly. Management: a paediatric cardiologist assesses the associated anomalies and recommends medical and surgical management.\n"
   "- Pulmonary valve atresia: severe form of TOF; ductal dependent and/or with MAPCAs; early presentation, marked central cyanosis, single loud S2, continuous murmur radiating to the back and axillae; very challenging surgical management and poor outcome.\n"
   "B. Increased pulmonary blood flow:\n"
   "- TGA: often associated with other cardiac anomalies; early presentation, absent or mild respiratory distress disproportionate to the high level of cyanosis, absent or systolic murmur. Imaging: chest X-ray 'egg on a string' appearance; ECG often normal. Management: PGE1, balloon atrial septostomy, arterial switch.\n"
   "- Truncus arteriosus: presentation in the first days of life, mild to moderate cyanosis, symptoms and signs of heart failure. Chest X-ray: cardiomegaly, increased pulmonary vascular markings. Treat as in the HF algorithm. Surgical repair before PAH becomes irreversible.\n"
   "- TAPVR: early presentation if obstructed, with severe respiratory distress, marked cyanosis and shock. If unobstructed: right HF symptoms and signs, fixed split S2, SEM at the ULSB, hepatomegaly. Treat as in the HF algorithm. Surgical repair when the patient is stable.\n"
   "C. Others: HLHS, interrupted aortic arch, complex CHD; variable associated cardiac anomalies; symptoms depend on the pulmonary blood flow. If in HF, treat as in the HF algorithm. A paediatric cardiologist decides the indication and timing of cardiac surgery.\n\n"
   "All suspected cases of CHD should be referred to a tertiary centre after proper counselling.",
   ["Aortic stenosis is described with an 'ejection murmur over the pulmonary area', copied from the pulmonary stenosis box.",
    "'IV Fluids: 10-20mV/kg', 'PGEI', 'asterial switch', 'mummer irradiating', 'Ebstein anomal' printed; read as ml/kg, PGE1, arterial switch, murmur radiating, Ebstein anomaly."]),
]
