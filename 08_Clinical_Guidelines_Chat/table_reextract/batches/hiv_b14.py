exec(open("batches/hiv_common.py").read())
# HIV 2022 part 2, pp.118-121 (Chapter 6: TB prevention, screening and diagnosis among PLHIV). From the page images (Figure 6.2 at 200 dpi),
# wording checked against the text layer.
C6 = "Chapter 6: TB/HIV Collaborative Activities & Advanced HIV Disease"
TB25 = "The 2025 National Integrated TB Management Guidelines update TB screening, diagnosis and TPT for PLHIV (e.g. CRP, CXR with CAD, LF-LAM indications, new TPT regimens); check the TB guidelines for current practice."
ITEMS = [
 B("tbl-6.1-tb-prevention-plhiv", 118, C6 + " > 6.1 Tuberculosis > 6.1.1 Introduction > TB/HIV collaborative activities > Table 6.1", "Table 6.1 Prevention of TB among PLHIV (prevention and treatment of TB among PLHIV)", ["0302"],
   "Intensified TB case-finding:\nI. Screen all clients for TB using the integrated TB/Covid-19 screening tool and refer them for either TB prophylaxis or TB treatment services.\nII. TB preventive treatment (TPT)/treatment of latent TB infection (LTBI)\nIII. To prevent the development of active TB, offer TPT to all clients who are eligible unless there are contraindications to TPT.\n"
   "Infection prevention and control of TB (IPC):\nI. Refer clients with active TB to a TB clinic if available; separate patients with presumed and demonstrated infectious TB patients from the rest in facility waiting areas and ensure adequate airflow.\nII. Triage and fast-track patients with positive symptom screen and early initiation of TB treatment rapid triage and provide a surgical mask for clients with cough in waiting areas.\nIII. Ensure that facilities have an up-to-date infection control plan with IPC focal points who implement and monitor IPC indicators\n"
   "Prevention and treatment of HIV infection in clients with active TB:\nI. Provide HTS to all clients with presumptive or diagnosed TB.\nII. Ensure HIV prevention interventions for HIV-negative TB clients and early ART initiation for TB clients living with HIV.\nIII. Provide TPT for TB/HIV coinfected clients who have completed their TB treatment.",
   flags=[TB25]),
 T("tbl-6.2-tb-screening-tests", 119, C6 + " > 6.1.2 TB Screening > TB screening tests > Table 6.2", "Table 6.2 TB screening tests", ["0305"],
   [r("Name of screening test", "Notes")],
   [r("C- Reactive Protein (CRP) with a cut-off point of >5mg/l", "• A general marker for inflammation can be performed as a point of care test<br/>• C-reactive protein should be used in patients, not on ART or presenting for ART initiation. A confirmatory diagnostic test for TB should be considered after a positive screen using CRP among PLHIV."),
    r("Chest X-ray (CXR)", "• CXR and W4SS combined to provide improved sensitivity and similar specificity to W4SS alone for all PLHIV subgroups<br/>• Most sensitive screening tool for PLHIV on ART")],
   footnotes=["Chest X-ray and C-reactive protein may be useful in improving the sensitivity of the four-symptom screen where feasible.", "Due to limited capacity and access to radiograph services currently, the chest x-ray recommendation for screening may not be implemented until further notice."],
   context_before="PLHIV should be systematically screened for TB disease using the WHO 4 symptoms screen (W4SS) tool at each clinical visit to a health facility.",
   source_flags=["CRP cut-off '>5mg/l': WHO recommends CRP >5 mg/L for TB screening in PLHIV, consistent; second column heading added.", TB25]),
 D("fig-6.1-tb-screening-plhiv", 119, C6 + " > 6.1.2 TB Screening > Figure 6.1", "Figure 6.1 TB screening algorithm for PLHIV", ["0307"],
   "PLHIV on ART:\n1. W4SS (cough, fever, night sweats, weight loss).\n   - W4SS positive: presumptive TB -> TB lab investigation.\n   - W4SS negative: CXR.\n       - CXR abnormal: presumptive TB -> TB lab investigation.\n       - CXR normal: not presumptive -> evaluate for TPT.\n"
   "PLHIV not on ART:\n1. W4SS (cough, fever, night sweats, weight loss).\n   - W4SS positive: presumptive TB -> TB lab investigation.\n   - W4SS negative: CRP.\n       - CRP positive: presumptive TB -> TB lab investigation.\n       - CRP negative: not presumptive -> evaluate for TPT.",
   flags=["The arrows from CXR/CRP to 'presumptive' and 'not presumptive' are unlabelled in the figure; read as abnormal/positive vs normal/negative. The figure does not show where a W4SS-positive client goes (shown here as presumptive TB).", TB25]),
 D("fig-6.2-tb-evaluation-plhiv", 121, C6 + " > 6.1.3 TB Diagnosis > Figure 6.2 Algorithm to evaluate for TB among PLHIV", "Figure 6.2 Algorithm to evaluate for TB among PLHIV", ["0311"],
   "Assess for TB signs and symptoms†; assess if seriously ill*; assess for advanced HIV disease (AHD)**; perform CD4 testing (if eligible, according to national guideline).\n"
   "A. Positive for TB signs and symptoms (regardless of CD4 count): perform Xpert MTB/RIF (Ultra) AND urine LAM if available.\n"
   "   - Xpert positive, LAM positive: TB treatment.\n   - Xpert positive, LAM negative: TB treatment.\n   - Xpert negative, LAM positive: treat for TB; perform work-up to exclude DR-TB.\n   - Xpert negative, LAM negative: clinical management; if CD4 <200, apply AHD package of care.\n"
   "B. No TB signs and symptoms with any of the following: seriously ill, or CD4 <200 (inpatients) OR CD4 <100 (outpatients): perform urine LAM.\n"
   "   - LAM negative: apply AHD package of care.\n   - LAM positive: perform Xpert if available.\n       - Xpert positive: TB treatment.\n       - Xpert negative or not available: treat for TB; perform work-up to exclude DR-TB.\n"
   "C. No TB signs and symptoms AND CD4 >200 or unknown: clinical management.\n"
   "† See National TB guidelines for the national TB symptoms screening tool.\n* 'Seriously ill' is defined as presence of at least one of the following danger signs: respiratory rate >30/min, temperature >39°C, heart rate >120/min and patient unable to walk unaided.\n"
   "** AHD: for adults, adolescents and children above 5 years, AHD is defined as CD4 count <200 cells/mm³ OR WHO stage 3 or 4 event. All children under 5 years old are considered as having advanced HIV disease.",
   flags=["The text before it (section 6.1.3) refers to this algorithm as 'Figure 6.1' (Figure 6.1 is the screening algorithm). Table 5.11 refers to 'Figure 6.2' for CrAg screening (the CrAg algorithm is Figure 6.3).", TB25]),
]
