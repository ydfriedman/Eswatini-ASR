exec(open('batches/ncd_common.py').read())
ITEMS = [
 D("fig-insulin-initiation-t2dm", 38, CH2 + " > Insulin Therapy in Type 2 Diabetes > Stepwise approach to insulin initiation in type 2 DM",
   "Stepwise approach to insulin initiation in type 2 DM (flowchart)", ["0091", "0092", "0093"],
   "Steps run from 1 injection (more flexible, lower patient complexity) to 3+ injections (less flexible, high complexity).\n\n"
   "Step 1 - Basal insulin (usually with metformin), 1 injection:\n"
   "  Start: 10 units per day, or 0.1 to 0.2 units per kg per day.\n"
   "  Adjust: 10% to 15%, or 2 to 4 units, once or twice weekly to reach fasting BG target.\n"
   "  For hypoglycaemia: determine and address cause; decrease dose by 4 units or 10% to 20%.\n\n"
   "If not controlled after fasting BG target is reached (or if dose > 0.5 units per kg per day), treat postprandial glucose excursions with mealtime insulin (consider an initial glucagon-like peptide 1 receptor agonist trial). Two options (2 injections, moderate complexity):\n\n"
   "Option A - Add 1 rapid-acting insulin injection before the largest meal:\n"
   "  Start: 4 units, 0.1 units per kg, or 10% of basal dose; if A1C <8%, consider decreasing basal insulin by the same amount.\n"
   "  Adjust: increase dose by 1 to 2 units or 10% to 15% once or twice weekly until SMBG target is reached.\n"
   "  For hypoglycaemia: determine and address cause; decrease dose by 2 to 4 units or 10% to 20%.\n"
   "  If not controlled: consider basal-bolus (Step 3).\n\n"
   "Option B - Change to premixed insulin twice daily:\n"
   "  Start: divide current basal dose into 2/3 a.m. and 1/3 p.m., or into 1/2 a.m. and 1/2 p.m.\n"
   "  Adjust: increase dose by 1 to 2 units or 10% to 15% once or twice weekly until SMBG target is reached.\n"
   "  For hypoglycaemia: determine and address cause; decrease dose by 2 to 4 units or 10% to 20%.\n"
   "  If not controlled: consider basal-bolus (Step 3).\n\n"
   "Step 3 - Add 2 or more rapid-acting insulin injections before the largest meals (basal-bolus, 3+ injections, high complexity):\n"
   "  Start: 4 units, 0.1 units per kg, or 10% of basal dose per meal; if A1C < 8%, consider decreasing basal dose by the same amount.\n"
   "  Adjust: increase dose by 1 to 2 units or 10% to 15% once or twice weekly until SMBG target is reached.\n"
   "  For hypoglycaemia: determine and address cause; decrease dose by 2 to 4 units or 10% to 20%.\n\n"
   "NB: for clients already on a single injectable agent, e.g. basal insulin, consider escalation to any of: 1. combination basal insulin and GLP-1RA therapy; 2. premix (twice daily) insulin; 3. basal-plus insulin therapy (adding one or more prandial doses of insulin to basal insulin). For all three options, metformin should be retained; consider stopping the other oral agents to reduce the cost and complexity of the regimen.",
   ["The PDF prints 'ubits' (units) and 'dese' (dose); corrected."]),
 T("tbl-premixed-insulin-adjustment", 39, CH2 + " > Insulin Therapy in Type 2 Diabetes > Adjusting dose of premixed insulin in type 2 DM",
   "Adjusting the dose of premixed insulin in type 2 DM by time-of-day glucose readings", ["0094", "0095", "0097"],
   [[C("Row"), C("Fasting glucose before breakfast (in the absence of nocturnal hypos)"), C("Lunch pre-meal value"), C("Evening pre-meal value"), C("Before-bed value")]],
   [[C("Which insulin dose this reading reflects"), C("[Breakfast] insulin: this dose will affect pre-lunch and pre-evening meal glucose levels"), C(""), C("[Evening] insulin: this will affect bedtime and morning fasting glucose levels"), C("")],
    [C("Target"), C("4 to 7 mmol/L"), C("4 to 7 mmol/L"), C("4 to 7 mmol/L"), C("6 to 8 mmol/L")],
    [C("If blood glucose is high"), C("Increase previous evening's insulin by 2 units or 10%, whichever is greater"), C("Increase breakfast insulin by 2 units or 10%, whichever is greater"), C("Increase previous evening's insulin by 2 units or 10%, whichever is greater"), C("Increase evening meal insulin, but not if blood tests at breakfast are 4-5 mmol/L")],
    [C("If blood glucose is low"), C("Decrease previous evening's insulin by 2 units or [text ends]"), C("Decrease breakfast insulin by 2"), C("Decrease breakfast insulin by 2"), C("Decrease evening meal insulin")]],
   source_flags=["The 'INSULIN' cells are printed under the fasting and evening columns without saying which dose; '[Breakfast]' and '[Evening]' are inferred from their text. Clinician to confirm.",
                 "The low-fasting cell ends at 'by 2 units or' in the PDF.",
                 "The high-evening cell says increase the previous evening's insulin, while the low-evening cell says decrease breakfast insulin. Possible inconsistency in the source."]),
 T("tbl-t1dm-signs-symptoms", 39, CH2 + " > Management of Type 1 Diabetes > Signs and symptoms of type 1 diabetes",
   "Type 1 diabetes: signs and symptoms by severity (early, severe without loss of consciousness, severe with coma)", ["0096", "0098"],
   [[C("Classification"), C("Sign / symptom"), C("Associated condition / severity")]],
   [[C("Early symptoms"), C("Polyuria; polydipsia; polyphagia; weight loss and/or poor weight gain; enuresis/nocturia; fatigue; blurred vision; perineal candidiasis (esp. prepubertal girls); inability and decreasing performance at school"),
     C("Hyperglycaemia (high blood sugar); dehydration due to fluid loss; cellular energy deficit; catabolism (breakdown of fat/muscle); polyuria (excessive night-time urination); lack of energy utilization; osmotic changes in the eye lens; localized fungal infection due to glucose in urine; general malaise/fatigue/frequent bathroom breaks")],
    [C("Severe symptoms (without loss of consciousness)"), C("Polyuria with severe dehydration; polydipsia; fast deep breathing (hyperventilation); presence of fruity (sweet) breath"),
     C("Uncontrolled hyperglycaemia and significant fluid loss; severe dehydration; compensatory mechanism for metabolic acidosis (Kussmaul breathing); diabetic ketoacidosis (DKA): presence of acetone/ketones")],
    [C("Severe symptoms (with coma)"), C("Severe hyperglycaemia which may progress to neurological compromise, seizures, and coma"), C("Diabetic ketoacidosis (DKA) or hyperosmolar hyperglycaemic state (HHS)")]],
   pages=[39, 40], context_before="All children and adolescents with type 1 diabetes require insulin. Poorly controlled type 1 diabetes increases the risk of stunted growth and diabetes complications, including diabetic ketoacidosis.",
   source_flags=["The old chunks repeated the premixed-insulin table here; the early and severe-without-coma rows were missing."]),
 D("fig-t1dm-diagnosis", 40, CH2 + " > Management of Type 1 Diabetes > Diagnosis of T1DM",
   "Diagnosis of type 1 diabetes (T1DM)", ["0099", "0100"],
   "Three stages, shown as three boxes:\n"
   "1. Symptoms (loss of weight, polyuria, polydipsia, ...): increased risk of diabetes. Suspect diabetes.\n"
   "2. Symptoms + glucose criteria: in case of abnormal plasma glucose values, experts suggest getting an HbA1c as a useful baseline. Diabetes is confirmed by: fasting plasma glucose ≥7.0 mmol/L (≥126 mg/dl); random plasma glucose ≥11.1 mmol/L (≥200 mg/dl); HbA1c ≥ 6.5%. Immune-mediated diabetes: presence of autoimmune markers.\n"
   "3. Immune-mediated diabetes (in tertiary care): presence of autoimmune markers: islet cell autoantibodies and autoantibodies to GAD (GAD65), insulin, the tyrosine phosphatases IA-2 and IA-2β, and ZnT8.",
   ["Boxes are side by side without arrows; read left to right as stages."]),
]
