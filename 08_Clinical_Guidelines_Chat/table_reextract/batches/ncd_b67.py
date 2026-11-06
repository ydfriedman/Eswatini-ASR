exec(open('batches/ncd_common.py').read())
AS = CH14 + " > Bronchial Asthma"; AE = CH14 + " > Management of Acute Asthma Exacerbations"
def r(*v): return [C(x) for x in v]
ITEMS = [
 T("tbl-asthma-follow-up", 335, AS + " > Monitoring & Follow-Up Schedule",
   "Asthma monitoring and follow-up schedule by age: stable asthma and after an exacerbation", ["0963"],
   [[C("Population"), C("Stable Asthma"), C("After Exacerbation")]],
   [r("Children <5 yrs", "Every 3–6 months", "Within 2–4 weeks"), r("Children 6–11 yrs", "Every 3–6 months", "Within 2–4 weeks"),
    r("Adolescents ≥12 yrs", "Every 3–6 months", "Within 1–2 weeks"), r("Adults", "Every 3–12 months depending on control", "Within 1–2 weeks")],
   context_before="Asthma in pregnancy: uncontrolled asthma is more dangerous to the foetus than any asthma medication. Continue ICS at effective doses throughout pregnancy (do not step down); budesonide has the most safety data; SABA (salbutamol) is safe as reliever; montelukast may continue if essential; OCS may be used for exacerbations."),
 T("tbl-asthma-drug-classes", 335, AS + " > Management of Asthma > Pharmacological Treatment",
   "Asthma drug classes: SABA, ICS, LABA, LTRA, methylxanthines: examples, key points and precautions", ["0964"],
   [[C("Class"), C("Examples"), C("Key Points"), C("Notes/Precautions")]],
   [r("Short-Acting Beta Agonists (SABA)", "Salbutamol", "Mainstay of quick relief; used for acute symptom relief; frequent use suggests poor control", "Not for long-term control"),
    r("Inhaled Corticosteroids (ICS)", "Beclomethasone, budesonide, fluticasone", "Cornerstone of long-term treatment; safe and effective; use a spacer to improve delivery and reduce oral candidiasis", "Dose depends on severity, potency & response; increase ICS if SABA use is frequent"),
    r("Long-Acting Beta Agonists (LABA)", "Salmeterol, formoterol (in combination with ICS: fluticasone/salmeterol, budesonide/formoterol)", "Added to low/medium ICS to improve control; improve lung function", "Never use alone; always with ICS"),
    r("Leukotriene Receptor Antagonists (LTRA)", "Montelukast 10 mg", "Controls mild persistent asthma; useful in aspirin-induced, exercise-induced, and allergic rhinitis-associated asthma", "Less potent than ICS; stop if no benefit within 1 month"),
    r("Methylxanthines (second-line)", "Theophylline", "Mild bronchodilator; add-on for persistent asthma", "Narrow therapeutic window; requires serum level monitoring (5–15 μg/ml); starting dose 10 mg/kg/day")]),
 T("tbl-asthma-long-term-older-format", 336, AS + " > Long-term management by age (step table)",
   "Long-term asthma management step tables (children 6-11 and ages 12+): symptoms per step, preferred and alternative controllers, relievers", ["0965", "0967"],
   [[C("Age / option"), C("Step I"), C("Step II"), C("Step III"), C("Step IV"), C("Step V")]],
   [{"section": "Children 6–11 years (reliever: as-needed SABA, or ICS-formoterol reliever for MART)"},
    r("Symptoms", "Symptoms <twice a month", "Symptoms >twice a month", "Symptoms most days or waking with asthma once a week or more", "Symptoms most days or waking with asthma once a week or more and low lung function", "Short course OCS may also be needed for severely uncontrolled asthma"),
    r("Preferred controller", "Low dose ICS taken whenever SABA taken", "Daily low dose ICS", "Low dose ICS-LABA, or medium dose ICS, or very low dose ICS-formoterol MART", "Medium dose ICS-LABA, or low dose ICS-formoterol MART (refer for expert advice)", "Refer for phenotypic assessment ± higher dose ICS-LABA or add-on therapy, e.g. anti-IgE"),
    r("Alternative controller", "Consider daily low dose ICS", "Daily LTRA, or low dose ICS taken whenever SABA taken", "Low dose ICS + LTRA", "Add tiotropium or add LTRA", "Add-on anti-IL5, or add-on low dose OCS, but consider side effects"),
    {"section": "12 years onward, option A (reliever: as-needed low dose ICS-formoterol)"},
    r("Symptoms", "Symptoms less than 4–5 days a week", "Symptoms less than 4–5 days a week", "Symptoms most days or waking with asthma once a week or more", "Daily symptoms or waking with asthma once a week or more and low lung function", "Short course OCS may also be needed for severely uncontrolled asthma"),
    r("Controller and preferred reliever", "As-needed low dose ICS-formoterol", "As-needed low dose ICS-formoterol", "Low dose maintenance ICS-formoterol", "Medium dose maintenance ICS-formoterol", "High-dose maintenance ICS-formoterol. Refer for specialist review"),
    {"section": "12 years onward, option B (reliever: as-needed SABA)"},
    r("Symptoms", "Symptoms less than twice a month", "Symptoms twice a month or more but less than 4–5 days a week", "Symptoms most days or waking with asthma once a week or more", "Daily symptoms or waking with asthma once a week or more, and low lung function", "Short course OCS may also be needed for severely uncontrolled asthma"),
    r("Controller and alternative reliever", "Take ICS whenever SABA taken", "Low dose maintenance ICS", "Low dose maintenance ICS-LABA", "Medium/high dose maintenance ICS-LABA", "High-dose maintenance ICS-LABA. Refer for specialist review")],
   pages=[336, 337],
   source_flags=["These step tables (from the older GINA 2023 format) are printed after, and differ from, the treatment-step tables on pp.331-333 (e.g. children 6-11 step 1: 'low dose ICS taken whenever SABA taken' here vs 'no daily controller, as-needed SABA' there; step 4: medium ICS-LABA here vs medium-to-high ICS-LABA + LTRA there). Clinician to confirm which applies.",
                 "The 12+ option A step 1 and 2 symptom rows are identical ('less than 4–5 days a week'). Words run together throughout ('twicea', 'asthmaoncea'). The option B label is not printed."]),
 B("box-acute-asthma-immediate", 337, AE + " > All Age Groups – Immediate Actions and Admission Criteria",
   "Acute asthma exacerbation: immediate actions for all ages (oxygen, salbutamol, ipratropium, steroids, magnesium) and admission criteria", ["0968", "0969"],
   "All age groups – immediate actions:\n"
   "- Oxygen to achieve SpO2 94–98% (adults/adolescents) or 94–98% (children).\n"
   "- SABA: salbutamol 4–10 puffs via MDI + spacer every 20 min × 3 (first hour).\n"
   "- Severe: nebulised salbutamol 2.5 mg (children) / 5 mg (adults) every 20 min.\n"
   "- Ipratropium bromide: add 0.5 mg (adults) / 0.25 mg (children) to the nebuliser for moderate–severe exacerbations.\n"
   "- Systemic corticosteroids: prednisolone 1 mg/kg/day (max 40 mg, children) OR 40–50 mg/day (adults) × 5–7 days.\n"
   "- IV magnesium sulfate: 2 g IV over 20 min (adults/adolescents) or 25–75 mg/kg (children) for severe exacerbations, SpO2 <92%.\n\n"
   "Admission criteria – refer/admit if ANY: severe or life-threatening features; SpO2 <92% after initial treatment; no improvement after 1 hour of treatment; PEF remains <40% after initial treatment; unable to maintain oral intake (children); concern about home environment/adherence.",
   ["The oxygen target is printed '94–98% (adults/adolescents) or 94–98% (children)' (same range twice); the primary-care flowchart on p.338 targets 93–95% in adults. Children's magnesium '25–75 mg/kg' is printed (usually 25–50 mg/kg, max 2 g)."]),
 D("fig-acute-asthma-primary-care", 338, AE + " > Management of acute asthma in primary care",
   "Acute or sub-acute asthma exacerbation in primary care (flowchart): assessment, severity (mild/moderate, severe, life-threatening), treatment, transfer, discharge and follow-up", ["0970"],
   "1. Patient presents with an acute or sub-acute asthma exacerbation. Assess: is it asthma? Risk factors for asthma-related death? Severity of the exacerbation?\n"
   "2. Severity:\n"
   "   - Mild or moderate: talks in phrases; prefers sitting to lying; not agitated; respiratory rate increased; accessory muscles used; pulse 100-120 bpm; O2 saturation (on air) 90-95%; PEF >50% predicted or best (printed '50%').\n"
   "   - Severe: talks in words; sits hunched; agitated; respiratory rate >30/min; accessory muscles used; pulse >120/min; O2 saturation (on air) <90%; PEF <50% predicted or best.\n"
   "   - Life-threatening: drowsy; confused; silent chest.\n"
   "3. Mild/moderate: start treatment: SABA 4-10 puffs by pMDI + spacer, repeat every 20 min for 1 hour; prednisolone adults 40-50 mg, children 1-2 mg/kg (max 40 mg); controlled oxygen (if available), target saturation 93-95% (children 94-98%).\n"
   "   - Worsening → transfer to an acute care facility.\n"
   "   - Improving → continue SABA as needed; assess response at 1 hour (or earlier).\n"
   "4. Severe or life-threatening → transfer to an acute care facility; while waiting give SABA, ipratropium bromide, oxygen, systemic corticosteroids.\n"
   "5. Assess for discharge: symptoms improved, SABA not needed; PEF improving and >60-80% of personal best or predicted; oxygen saturation >94% on room air; adequate resources at home.\n"
   "6. Follow-up: review symptoms and signs (is the exacerbation resolving? should prednisolone be continued?). Reliever: reduce to as needed. Controller: continue a higher dose short term (1-2 weeks) or long term (3 months) depending on the background to the exacerbation. Risk factors: check and correct modifiable risk factors, including inhaler technique and adherence; refer if >1-2 exacerbations.",
   ["Severity thresholds here (SpO2 90-95% mild/moderate, <90% severe; PEF 50%) differ from the severity table on p.334 (SpO2 92-94% moderate, <92% severe; PEF 40-69% moderate, <40% severe). 'Life threating', 'Ipratroplum', 'on aur' printed."]),
]
