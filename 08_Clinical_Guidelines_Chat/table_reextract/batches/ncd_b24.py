exec(open('batches/ncd_common.py').read())
HT = CH3 + " > Hypertension"
ITEMS = [
 T("tbl-secondary-hypertension", 98, HT + " > Secondary Hypertension",
   "Secondary hypertension: clinical clues, basic biochemistry and further diagnostic tests by cause (renal, aldosteronism, renal artery stenosis, phaeochromocytoma, Cushing's, coarctation, sleep apnoea, thyroid)", ["0267", "0268"],
   [[C("Secondary Hypertension"), C("Clinical History and Physical Examination"), C("Basic Biochemistry and Urine Analysis"), C("Further Diagnostic Tests")]],
   [[C("Renal Parenchymal Disease"), C("- Personal/familial history of CKD"), C("- Proteinuria, hematuria, leukocyturia on dipstick urine analysis<br/>- Decreased estimated GFR"), C("- Kidney ultrasound")],
    [C("Primary Aldosteronism"), C("- Symptoms of hypokalemia (muscle weakness, muscle cramps, tetany)"),
     C("- Spontaneous hypokalemia or diuretic-induced hypokalemia on blood biochemistry (50% - 60% of patients are normokalemic)<br/>- Elevated plasma aldosterone-renin activity ratio"),
     C("- Confirmatory testing (eg, intravenous saline suppression test)<br/>- Imaging of adrenals (adrenal CT)<br/>- Adrenal vein sampling")],
    [C("Renal Artery Stenosis"), C("- Abdominal bruit<br/>- Bruits over other arteries (ie, carotid and femoral arteries)<br/>- Drop in estimated GFR >30% after exposure to ACE-inhibitors/ARBs<br/>- For suspected atherosclerotic RAS, history of flash pulmonary edema or history of atherosclerotic disease or presence of cardiovascular risk factors<br/>- For suspected fibromuscular dysplasia, young women with onset of hypertension <30 years"),
     C("- Decrease in estimated GFR"), C("- Imaging of renal arteries (duplex ultrasound, abdominal CT or MR angiograms depending on availability and patient's level of renal function)")],
    [C("Pheochromocytoma"), C("- Headaches<br/>- Palpitations<br/>- Perspiration<br/>- Pallor<br/>- History of labile hypertension"),
     C("- Increased plasma levels of metanephrines<br/>- Increased 24-hour urinary fractional excretion of metanephrines and catecholamines"), C("- Abdominal/pelvic CT or MRI")],
    [C("Cushing's Syndrome and Disease"), C("- Central obesity<br/>- Purple striae<br/>- Facial rubor<br/>- Signs of skin atrophy<br/>- Easy bruising<br/>- Dorsal and supraclavicular fat pad<br/>- Proximal muscle weakness"),
     C("- Hypokalemia<br/>- Increased late-night salivary cortisol"), C("- Dexamethasone suppression tests<br/>- 24-hour urinary free cortisol<br/>- Abdominal/pituitary imaging")],
    [C("Coarctation of the Aorta"), C("- Higher blood pressure in upper than lower extremities<br/>- Delayed or absent femoral pulses"), C(""), C("- Echocardiogram<br/>- CT angiogram<br/>- Magnetic resonance angiogram")],
    [C("Obstructive Sleep Apnea"), C("- Increased BMI<br/>- Snoring<br/>- Daytime sleepiness<br/>- Gasping or choking at night<br/>- Witnessed apneas during sleep<br/>- Nocturia"), C(""), C("- Home sleep apnea testing (e.g., level 3 sleep study)<br/>- Overnight polysomnography testing")],
    [C("Thyroid Disease"), C("- Symptoms of hyperthyroidism: heat intolerance, weight loss, tremor, palpitations<br/>- Symptoms of hypothyroidism: cold intolerance, weight gain, dry brittle hair"), C("- TSH, Free T4"), C("")]],
   pages=[98, 99],
   context_before="Consider screening for secondary hypertension in (1) patients with early onset hypertension (<30 years of age) especially in the absence of hypertension risk factors (obesity, metabolic syndrome, familial history etc.), (2) those with resistant hypertension, (3) individuals with sudden deterioration in BP control, (4) hypertensive urgency and emergency, (5) those presenting with high probability of secondary hypertension based on strong clinical clues.",
   table_note="REFER for further investigation and management of suspected secondary hypertension to a specialist centre with access to appropriate expertise and resources.",
   source_flags=["Table continues onto p.99 with the header repeated."]),
]
