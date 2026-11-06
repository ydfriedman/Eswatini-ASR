exec(open('batches/tb_common.py').read())
C8 = "Chapter 8: Childhood TB Screening, Diagnosis and Treatment > TB Screening Algorithms for Children"
ITEMS = [
 D("fig-screen-children", 156, C8 + " > Figure 23: Children <15 Years at Health Facilities", "Figure 23. TB screening algorithm for children <15 years at health facilities: symptom screen by age, risk factors (TB contact, MUAC, vulnerable children), CXR by human reader, sputum or stool Xpert, LF-LAM for children with HIV, TPT", ["0391", "0392"],
   "Population: children and adolescents <15 years attending health facilities.\n"
   "1. Symptom screen: for 10–15 years, current cough OR fever OR weight loss OR night sweats (W4SS); for <10 years, cough, fever, weight loss/poor weight gain of any duration, or history of TB contact.\n"
   "   - Positive: collect two specimens (if <5 years or cannot produce sputum, collect one stool sample) and perform microbiological assessment for active TB (including LF-LAM for children living with HIV*).\n"
   "   - Negative: assess risk factors – child TB contact, nutrition status (MUAC <12.5 cm for <5 years, <22.5 cm for >5 years), vulnerable children (e.g. orphans).\n"
   "     - No risk factors: exit.\n"
   "     - Risk factors: was CXR screening done in the past 12 months? Yes: further clinical evaluation, provide TPT if eligible. No: CXR read by a human reader → suggestive of TB: collect specimens as above; negative: further clinical evaluation, TPT if eligible; non-TB abnormalities: clinical assessment for active TB if symptoms persist or other morbidity, take CXR if not taken before, provide TPT if eligible.\n"
   "2. Microbiological result: positive → initiate TB treatment; negative → clinical assessment for active TB if symptoms persist or other morbidity, take CXR if not taken before, provide TPT if eligible.\n"
   "* Perform TB-LAM for all with AHD (CD4 <200, WHO stage 3 or 4) regardless of symptoms, seriously ill regardless of CD4, and all presumptive TB regardless of CD4.",
   ["The CXR result 'positive' is not drawn as a box; an arrow from 'CXR read by human reader' leads to specimen collection.", "MUAC <22.5 cm is given as the cut-off for all children >5 years; MUAC thresholds vary with age (5–9 vs 10–14 years), and BMI-for-age is usually used over 5.", "The symptom screen is defined for '>10-15 y.o' and '<10 y.o'; age 10 itself is not covered."]),
 D("fig-screen-children-plhiv", 157, C8 + " > Figure 24: Children <15 Years (With and Without HIV) at Facilities with X-ray, CAD/AI and CRP", "Figure 24. TB screening algorithm for children <15 years with and without HIV at facilities with X-ray, CAD/AI and CRP: symptom screen, risk factors, ART status, CRP (>10 years), CXR by human reader, sputum/stool Xpert, TB-LAM, TPT", ["0393", "0394", "0395"],
   "Population: children and adolescents <15 years attending health facilities (non-PLHIV and PLHIV).\n"
   "1. Symptom screen: current cough OR fever OR weight loss (poor weight gain, failure to thrive) OR night sweats.\n"
   "   - Positive (with or without HIV): collect two sputum samples (if <5 years or cannot produce sputum, one stool sample) and perform microbiological assessment for active TB (including TB-LAM for eligible PLHIV**).\n"
   "   - Negative, without HIV: assess risk factors* → none: exit; present: was CXR taken in the past 12 months? Yes: evaluate and provide TPT if eligible. No: CXR screen by human reader → negative: evaluate and provide TPT if eligible; positive: (no next step drawn).\n"
   "   - Negative, living with HIV: on ART? Yes: CXR pathway as above. No: CRP screen (for >10 years only) → positive: collect sputum/stool for microbiological assessment; negative: further clinical evaluation, provide TPT if eligible.\n"
   "2. Microbiological result: positive → initiate active TB treatment; negative → further clinical evaluation, provide TPT if eligible.\n"
   "* Risk factors: child TB contacts; nutrition status (MUAC <12.5 cm for <5 years, <22.5 cm for >5 years); vulnerable children (e.g. orphans). ** Perform TB-LAM for all with AHD (CD4 <200, WHO stage 3 or 4) regardless of symptoms, seriously ill regardless of CD4, and all presumptive TB regardless of CD4.",
   ["A positive CXR screen has no next step drawn (presumably specimen collection, as in Figure 23); the earlier chunk omitted the branch.", "Children with HIV, not on ART, symptom-negative and aged 10 or under have no screening step (CRP is 'for >10 years only').", "The figure title says 'PLHIV <15 years' but the chart covers children with and without HIV."]),
]
