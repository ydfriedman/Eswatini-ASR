exec(open('batches/ncd_common.py').read())
ITEMS = [
 T("tbl-diabetes-microvascular-complications", 55, CH2 + " > Diabetes > Chronic microvascular complications",
   "Chronic microvascular complications of diabetes (nephropathy, eye disease, neuropathy): who to screen, how, management and referral criteria", ["0154", "0155", "0156"],
   [[C("Complication"), C("Who should be screened"), C("Screening/detection method"), C("Treatment/management principles"), C("Urgent referral/action criteria")]],
   [[C("Diabetes nephropathy"), C("Type 1 diabetes: duration > 5 years. Type 2 diabetes: at diagnosis."),
     C("Yearly check for proteinuria (reagent strips); if positive, exclude/treat UTIs, then refer if persistent. Yearly check for microalbuminuria (reagent strips or ACR). Measure serum creatinine bi-annually."),
     C("Optimize glycaemic control (with caution in advanced disease). Aggressive BP control (<125/75 mmHg). Use ACEI or ARBs as first-line (contraindicated in pregnancy). Stop tobacco use. Avoid nephrotoxic drugs (e.g., NSAIDs, aminoglycosides). Metformin should not be used if eGFR <30 mL/min/1.73 m2."),
     C("Persistent microalbuminuria. Inability to optimize blood pressure. Intolerance of ACEI/ARBs or >30% increase in creatinine within 3 months. Consider other causes if: extreme proteinuria (>6 g/day), persistent haematuria, rapidly falling eGFR, low eGFR with low/no proteinuria, diabetes <5 years.")],
    [C("Diabetes eye disease (retinopathy & cataracts)"), C("Type 2 diabetes: at presentation. Type 1 diabetes: >5 years duration (or at presentation if uncontrolled)."),
     C("Full eye examination including visual acuity and fundoscopy (preferably dilated) at initial contact; refer if no capacity. Repeat examinations annually, or more frequently if retinopathy is progressing. Women planning pregnancy and during the first trimester require a comprehensive exam. Type 1 pregnant women: fundoscopy every trimester."),
     C("Intensify management of blood pressure, glycaemia, and lipids. Stop smoking. Patients with proliferative diabetic retinopathy should avoid weight-bearing exercises and require guided exercises."),
     C("Sudden deterioration of vision. 'Floater' sensation reported by patient. Fundoscopy findings of dot or blot haemorrhages 1 disc-width away from the macula. Cataract present. Proliferative or exudative retinopathy.")],
    [C("Diabetes neuropathy (motor, sensory, autonomic)"), C("Not specified as a screening criterion, but assessment is part of clinical care."),
     C("Detailed history (numbness, tingling, pain). Examination of the feet: test sensation using 10 g monofilament, 128 Hz tuning fork, or cotton wool. Lying-and-standing BP and pulse rate to check for postural hypotension."),
     C("Improve glycaemic control. Exclude or treat other contributory factors (e.g., alcohol, B12 deficiency, smoking, HIV). Symptomatic treatment (see peripheral neuropathy guidelines)."),
     C("Referral to secondary and/or tertiary centre once symptomatic peripheral neuropathy is diagnosed.")]],
   pages=[55, 56], source_flags=["Table continues onto p.56 (neuropathy row)."]),
]
