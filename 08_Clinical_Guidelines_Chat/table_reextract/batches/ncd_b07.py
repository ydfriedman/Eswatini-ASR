exec(open('batches/ncd_common.py').read())
ITEMS = [
 D("fig-dka-algorithm", 50, CH2 + " > Diabetic Emergencies > Algorithm for DKA",
   "Algorithm for DKA (flowchart: assessment, resuscitation, IV therapy, insulin, monitoring, cerebral oedema)", ["0138", "0139"],
   "Immediate assessment:\n"
   "- Clinical history: polyuria, polydipsia, nocturia, enuresis, weight loss, nausea, vomiting, abdominal pain, weakness, fatigue, confusion, level of consciousness.\n"
   "- Clinical signs: dehydration; deep sighing respiration (Kussmaul); smell of ketones; lethargy/drowsiness.\n"
   "- Biochemical features & investigations: ketones in urine; blood glucose; acidaemia (vpH < 7.3, HCO3 <15 mmol/L); urea, electrolytes; other investigations as indicated.\n"
   "Diagnosis confirmed: diabetic ketoacidosis. Contact senior staff.\n\n"
   "Then by clinical state:\n"
   "A. Shock (reduced peripheral pulses), reduced conscious level/coma: resuscitation: airway ± NG tube; breathing (100% oxygen); circulation: 0.9% saline 10-20 ml/kg over 1-2 h, repeat until circulation is restored (see CE management). Then IV therapy (as B).\n"
   "B. Dehydration >5%, not in shock, acidotic (hyperventilation), vomiting: IV therapy: saline 0.9% 10 ml/kg over 1 h, may repeat; calculate fluid requirements; correct fluid deficit over 24-48 hours; ECG for abnormal T-waves; add KCl 40 mmol per litre of fluid.\n"
   "C. Minimal dehydration, tolerating oral fluid: therapy: start with SC insulin; continue oral hydration. If no improvement: IV therapy (as B).\n\n"
   "After IV therapy: continuous insulin infusion at 0.05-0.1 unit/kg/hour, starting 1 hour after fluids initiated.\n\n"
   "Critical observations: hourly blood glucose; hourly fluid input & output; neurological status at least hourly; electrolytes 2-hourly after starting IV fluid therapy; monitor ECG for T-wave changes.\n\n"
   "Then:\n"
   "- Acidosis not improving: re-evaluate IV fluid calculations, insulin delivery system & dose, need for additional resuscitation; consider sepsis.\n"
   "- Blood glucose ≤17 mmol/L (300 mg/dL) or blood glucose falls >5 mmol/L/hour (90 mg/dL): IV therapy: change to 0.45% or 0.9% saline; add glucose to fluids (5%-12.5%) to prevent hypoglycaemia; adjust sodium infusion to promote an increase in measured serum sodium. When improved (clinically well, ketoacidosis resolved, tolerating oral fluids): transition to SC insulin: start SC insulin, then stop IV insulin after an appropriate interval.\n"
   "- Neurological deterioration: warning signs: severe or progressive headache, slowing heart rate, irritability, confusion, decreased consciousness, incontinence, specific neurological signs. Exclude hypoglycaemia; is it cerebral oedema? CE (cerebral oedema) management: give mannitol 0.5-1 g/kg or 3% hypertonic saline; adjust IV fluids to maintain normal BP but avoid over-hydration; call senior staff; move to ICU; consider cranial imaging only after the patient is stabilized.",
   ["Fluid volumes here (10 ml/kg over 1 h; 10-20 ml/kg boluses) are weight-based, unlike the adult DKA fluid table on p.36 (1 L over 30-60 min). The algorithm does not say whether it is for children; clinician to confirm.",
    "Insulin infusion here is 0.05-0.1 unit/kg/hour starting 1 hour after fluids; the adult protocol on p.37 gives a 0.1 unit/kg bolus then 0.1 unit/kg/hr.",
    "Printed 'Kettones', 'Deep signing respiration', 'Consider sepsi'; corrected."]),
]
