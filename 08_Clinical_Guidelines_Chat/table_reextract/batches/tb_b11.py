exec(open('batches/tb_common.py').read())
# Fixes from the user's review of the 50-item validation sample (Nov 2026). Load after tb_b10.
ITEMS = [
 D("fig-anaemia-thrombocytopenia", 190,
   "Chapter 9: Pharmacovigilance and Adverse Event Management > 9.9 Algorithms for Management of Adverse Events with Second-line Anti-TB Drugs > Figure 32: Management of Anaemia/ Thrombocytopenia",
   "Figure 32: Management of Anaemia/ Thrombocytopenia (linezolid, AZT, CTX): severity grades and linezolid action", ["0481"],
   "- Causative Medications: LZD, AZT, CTX -> Anaemia / Thrombocytopenia\n"
   "- Monitor elevated Anaemia / Thrombocytopenia checking baseline and monthly FBC and anytime if there are symptoms -> Anaemia / Thrombocytopenia\n"
   "- Anaemia / Thrombocytopenia: Anaemia: Signs and symptoms include bruising, pallor, SOB, Fatigue, palpitations, dizziness. Thrombocytopenia: Easy bruising, bleeding tendencies -> Assess for other causes\n"
   "- Assess for other causes. For anaemia, there multiple other causes, including TB itself, HIV, malignancy, iron deficiency, alcohol use, pregnancy, bleeding. For thrombocytopenia, some viruses may lead to prolonged or excessive bleeding -> Assess severity and manage\n"
   "- Assess severity and manage -> Mild/Grade 1: Hb: 9.5 - 10.5g/dl; Plt: 75,000 - 99,000/mm3. Continue linezolid. Monitor closely; 2 weekly FBC (If HB continues to decline reduce to 300 mg)\n"
   "- Assess severity and manage -> Moderate/Grade 2: Hb: 8.0 - 9.4g/dl; Plt: 50,000 - 74,999mm3. Reduce linezolid dose to 300 mg. 2 weekly FBC. Monitor closely\n"
   "- Assess severity and manage -> Severe/Grade 3: HB: 6.5-7.9g/dl; Plt: 20,000 - 49,999/mm3. Stop linezolid. Consider transfusion. Weekly FBC. Reinitiate 300mg/day if myelosuppression recovers within first 2 months of treatment\n"
   "- Assess severity and manage -> Life-threatening/Grade 4: Hb: < 6.5g/dl; Plt: < 20,000. Stop linezolid. Consider transfusion. Weekly FBC. Reinitiate 300mg/day if myelosuppression recovers within first 2 months of treatment\n"
   "Note (box below the chart): Patient with baseline anaemia of all grades can be treated with LZD. They should have more frequent FBC monitoring (i.e. every 2 weeks). This is true even of patients with Grade 3 or Grade 4 anemia, provided they are started on therapy as inpatients and that they have weekly FBC checked."),
]
