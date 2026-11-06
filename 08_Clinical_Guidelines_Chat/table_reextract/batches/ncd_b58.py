exec(open('batches/ncd_common.py').read())
OM = CH9 + " > Oral & Maxillofacial Cancers"; PC = CH9 + " > Prostate Cancer"
def r(*v): return [C(x) for x in v]
ITEMS = [
 D("fig-oral-lesion-algorithm", 271, OM + " > Diagnostic Algorithm",
   "Oral lesion diagnostic algorithm: clinical diagnosis, follow-up vs biopsy, adjuvant diagnostic techniques and urgent referral", ["0776", "0777"],
   "Photographs show the steps of the oral examination.\n\n"
   "1. Oral lesion → previous clinical diagnosis based on clinical data.\n"
   "2. Lesion resolves with or without therapy → follow-up.\n"
   "3. Lesion changes, persists or progresses → perform a biopsy → identification of the histological entity, with or without malignancy → follow-up (or repeat biopsy).\n\n"
   "Adjuvant diagnostic techniques: 1. oral cytology; 2. salivary biomarkers; 3. light-based techniques (auto-fluorescence, spectroscopy, chemiluminescence); 4. tissue staining.\n\n"
   "Diagnostic workup: if there is any suspicion that a lesion may be oral cavity cancer, document the lesion site and size, take a clinical photograph if possible, and make an urgent referral to an oral & maxillofacial surgeon who is part of a head and neck oncology MDT. Any oral lesion (including a patch or ulcer) that fails to resolve in 2-3 weeks should raise suspicion.",
   ["The PDF text layer for this page is overprinted with garbled characters; transcribed from the page image."]),
 T("tbl-psa-risk-stratification", 272, PC + " > Screening and Diagnosis of Prostate Cancer > PSA levels",
   "PSA-based prostate cancer screening: risk stratification for PSA under 4 ng/ml by age (EAU 2022), and recommendations for PSA 4-10 and >10 ng/ml in men 50-75", ["0780", "0781", "0782"],
   [[C("Category / PSA level"), C("Definition"), C("Recommendation")]],
   [{"section": "PSA under 4 ng/ml: risk stratification (EAU 2022)"},
    r("Low Risk", "PSA <1 in those <40 years; PSA <2 in those 41-60 years", "Repeat screening after 5 - 8 years"),
    r("High Risk", "PSA >1 in those <40 years; PSA >2 in those 41-60 years", "Repeat screening after 2 years"),
    {"section": "PSA above 4 ng/ml in men 50-75 years"},
    r("4-10 ng/ml", "", "1. If DRE is normal, repeat after 4-6 weeks; if it increases, refer for urologist review. 2. If DRE abnormal, refer to urologist. 3. If available, determine the free to total PSA ratio and PSA density, and consult"),
    r("> 10 ng/ml", "", "Refer to urologist")],
   context_before="Prostate screening every two years for men above 50 with risk factors. Discuss screening at age 45 for men at high risk (African American, first-degree relative with prostate cancer at an early age) and at age 40 for very high risk (several first-degree relatives with early prostate cancer). DRE by a trained health worker, with annual PSA and rectal or pelvic ultrasound. Those with above-average risk start earlier at the clinician's discretion.",
   source_flags=["The age bands (<40 and 41-60) leave age 40 uncovered; the definitions 'PSA >1' / 'PSA >2' leave PSA exactly 1 or 2 uncovered.",
                 "Screening is said to be every two years from 50 'with any of the following risk factors' but the list that follows gives discussion ages, not risk factors; elsewhere PSA is annual."]),
 T("tbl-prostate-diagnostics", 273, PC + " > Diagnosis and Staging",
   "Prostate cancer diagnosis and staging investigations: biopsy, pathology, PSA tests, radiology, other", ["0784"],
   [[C("Diagnostic Category"), C("Investigation")]],
   [r("Biopsy", "Biopsy (trans-rectal ultrasound-guided biopsy is the current standard)"),
    r("Pathology", "A full histology report"),
    r("Laboratory Tests", "Prostate specific antigen (PSA) test and its isoforms: PSA doubling time; PSA density; PSA velocity; PSA ratio, free to bound"),
    r("Radiology", "Ultrasound pelvis and abdomen; chest X-ray; if PSA >20, bone scan, or MRI DWI (high risk) if bone scan unavailable; CT scan; MRI pelvis (prostate-specific sequences)"),
    r("Other", "Endoscopy and other specialized tests as indicated and available")],
   context_before="Signs and symptoms: may be asymptomatic; LUTS (urgency/frequency, dysuria, nocturia, poor stream, straining); haematuria, poor erectile function, bone pain, bladder outlet obstruction, urinary retention, chronic renal failure, rectal bleeding."),
]
ITEMS += [
 T("tbl-prostate-management-by-risk", 275, PC + " > Summary Guideline for Management by Risk Category",
   "Prostate cancer management by risk category (very low, low, high risk): observation, active surveillance, radiotherapy, radical prostatectomy, hormone therapy", ["0788"],
   [[C("Risk category"), C("Recommended Treatment")]],
   [r("Very Low Risk", "Life expectancy <10 yrs: observation. Life expectancy 10-20 yrs: active surveillance. Life expectancy >20 yrs: active surveillance, radiotherapy (EBRT or brachytherapy), or radical prostatectomy (RP) +/- pelvic lymph node dissection (LND) if >2% risk of LN involvement (Roach or Partin tables)"),
    r("Low Risk", "Life expectancy <10 yrs: observation. Life expectancy >10 yrs: RT alone, RP +/- pelvic LND, or active surveillance. If RP with positive margins → adjuvant RT (preferred) or expectant management"),
    r("High Risk", "Radiotherapy (3DCRT/IMRT with IGRT +/- brachytherapy boost) + long-term hormone therapy (2-3 yrs; neoadjuvant, concurrent and adjuvant). 4-6 months of androgen deprivation therapy (ADT) considered for select patients with a single adverse feature with Gleason score 6-7. Consider whole pelvis radiotherapy. Consider RP with pelvic LND only for selected patients with low-volume disease and no fixation. Adjuvant RT +/- short-term ADT for positive margins or pT3 disease")],
   context_before="Management depends on stage, risk category, age, comorbidities and life expectancy, performance status, resources, hormone sensitivity in metastatic disease, and the patient's wishes. Options: watchful waiting; active surveillance; surgery (radical prostatectomy, TURP etc.); radiotherapy (external beam, brachytherapy); hormonal therapy (medical or surgical castration, bilateral orchiectomy); chemotherapy; supportive care (pain management, bisphosphonates such as zoledronate). Localised disease: radical prostatectomy or radiotherapy with or without hormones. Metastatic hormone-sensitive: bilateral orchiectomy (cheaper than medical therapy) or hormonal therapy as ADT or combined androgen blockade (CAB). Castration-resistant: second-line hormonal agents (enzalutamide, abiraterone) and/or chemotherapy (docetaxel).",
   footnotes=["ADT: androgen deprivation therapy; CAB: combined androgen blockade; EBRT: external beam radiation therapy; IGRT: image-guided radiation therapy; IMRT: intensity-modulated radiation therapy; LN: lymph node; LND: lymph node dissection; RP: radical prostatectomy; RT: radiotherapy; 3DCRT: three-dimensional conformal radiation therapy."],
   source_flags=["The table has no intermediate-risk row (very low, low and high risk only). The first column is headed 'Stage' but lists risk categories."]),
]
