exec(open('batches/ncd_common.py').read())
OS = CH2 + " > Management of Osteoporosis and Fragility Fractures"
ITEMS = [
 D("fig-osteoporosis-assessment", 70, OS + " > Algorithm for the assessment of patients with osteoporosis",
   "Algorithm for the management of osteoporosis in post-menopausal women and men aged 50 years and older", ["0192", "0193"],
   "Clinical risk factors (CRFs): advanced age; prior fracture; family history; excessive leanness (printed 'excessive learners'); diet/alcohol/smoking; fall propensity; secondary osteoporoses.\n\n"
   "Start: women and men with CRFs. Prior osteoporotic fracture?\n"
   "- Yes: consider specific treatment/prophylaxis.\n"
   "- No: measure BMD. By T-score:\n"
   "  - T-score ≤ -2.5: consider specific treatment/prophylaxis.\n"
   "  - T-score between -1.0 and -2.5 (printed '< -10 to > -2.5'; consider FRAX):\n"
   "      - > 75 years: consider specific treatment/prophylaxis.\n"
   "      - 65-75 years + ≥ 2 CRFs: yes: consider specific treatment/prophylaxis; no: individualised assessment of CRFs + BMD.\n"
   "      - > 60 years: individualised assessment of CRFs + BMD.\n"
   "    Individualised assessment outcome: yes: consider specific treatment/prophylaxis; uncertain (?): bone turnover markers (BTMs) or reassess in 24 months; no: lifestyle changes only.\n"
   "  - T-score ≥ -1.0: lifestyle changes only.",
   ["Superscripts a, b, c on 'prior osteoporotic fracture', 'Yes' and 'Measure BMD' have no footnotes printed.",
    "The middle T-score band is printed '< -10 to > -2.5'; read as -1.0 to -2.5.",
    "The '> 60 years' branch is drawn into the individualised assessment box; the age bands overlap (>60, 65-75, >75)."]),
 T("tbl-osteoporosis-pharmacological", 71, OS + " > Pharmacological management of osteoporosis",
   "Pharmacological management of osteoporosis: drug classes, typical dosage and common side effects", ["0195"],
   [[C("Drug class and name"), C("Typical dosage"), C("Common side effects")]],
   [{"section": "Bisphosphonates"},
    [C("Alendronate (Fosamax)"), C("70 mg once weekly or 10 mg daily"), C("Oesophageal irritation, musculoskeletal pain, nausea, abdominal pain")],
    [C("Risedronate (Actonel)"), C("35 mg once weekly or 150 mg once monthly"), C("Abdominal pain, musculoskeletal pain, nausea")],
    [C("Ibandronate (Boniva)"), C("150 mg once monthly"), C("Gastrointestinal irritation, musculoskeletal pain")],
    [C("Zoledronic acid (Reclast)"), C("5 mg once annually as an intravenous infusion"), C("Flu-like symptoms, renal impairment, hypocalcaemia")],
    {"section": "Selective estrogen receptor modulators (SERMs)"},
    [C("Raloxifene (Evista)"), C("60 mg daily"), C("Hot flashes, leg cramps, increased risk of blood clots")],
    {"section": "Hormone replacement therapy (HRT)"},
    [C("Conjugated estrogens (Premarin)"), C("Dosage varies"), C("Increased risk of breast cancer, blood clots, stroke, and other side effects")],
    [C("Calcitonin (Miacalcin)"), C("Typically 200 IU daily as nasal spray"), C("Nasal irritation, epistaxis (nosebleeds), flushing")],
    {"section": "Parathyroid hormone analogs"},
    [C("Teriparatide (Forteo)"), C("20 mcg once daily (subcutaneous)"), C("Dizziness, leg cramps, injection site reactions")],
    [C("Abaloparatide (Tymlos)"), C("80 mcg once daily (subcutaneous)"), C("Hypercalcaemia, dizziness, nausea, headache")],
    {"section": "Monoclonal antibodies"},
    [C("Denosumab (Prolia)"), C("60 mg once every six months (subcutaneous)"), C("Infections, back pain, dermatitis, hypocalcaemia")]],
   context_before="Non-pharmacological management: postmenopausal women and men aged ≥50 years with osteoporosis or at risk of fragility fracture are recommended: a healthy, nutrient-rich balanced diet; adequate calcium intake (minimum 700 mg daily), preferably from diet or otherwise by supplementation; vitamin D supplements of at least 800 IU/day if vitamin D insufficiency or risk factors for it are identified; regular weight-bearing and muscle-strengthening exercise tailored to the individual; advice on smoking and alcohol cessation; a falls assessment for all patients with osteoporosis and fragility fractures, with exercise programmes to improve balance for those at risk.",
   source_flags=["Calcitonin is listed under the HRT heading in the PDF (it has no class heading of its own)."]),
]
