exec(open('batches/tb_common.py').read())
SA = "Chapter 3: Tuberculosis Case Finding > 3.7 TB Screening Algorithms with CXR and CAD/AI Use"
ITEMS = [
 D("fig-screen-plhiv-cxr", 60, SA + " > Figure 11: PLHIV 15+ at Facilities with X-ray and CAD/AI", "Figure 11. TB screening algorithm for PLHIV aged 15+ at facilities with X-ray and CAD/AI: symptom screen, CXR in past 12 months, CAD result, sputum Xpert + urine LF-LAM, TPT", ["0128", "0129", "0130"],
   "Population: PLHIV adolescents >15 years and adults (old and new) attending health facilities.\n"
   "1. Symptom screen (multi-entry): current cough OR fever OR weight loss OR night sweats.\n"
   "   - Positive: collect two sputum samples and 1 urine sample**; perform microbiological assessment for active TB (Xpert and LF-LAM).\n"
   "   - Negative: check if CXR screening was done in the past 12 months.\n"
   "     - Yes: further clinical evaluation***; provide TPT if eligible.\n"
   "     - No: X-ray screen with CAD → positive: collect sputum ×2 + urine for Xpert and LF-LAM; negative: further clinical evaluation***, TPT if eligible; non-TB abnormalities*: further clinical evaluation***, TPT if eligible.\n"
   "2. Microbiological result: positive → initiate TB treatment; negative → further clinical evaluation***, provide TPT if eligible.\n"
   "* Abnormalities e.g. cardiomegaly, possible cancer, silicosis. ** A urine sample is collected from every client with advanced HIV disease (AHD) for LF-LAM regardless of symptoms or CAD result. *** Further clinical evaluation includes clinical assessment of resolution of TB symptoms, re-reading of the CXR by a trained clinician, and further management/specialist referral as required; if on re-reading the CXR is suggestive of TB, evaluate for TB.",
   ["The 'No' (no CXR in past 12 months) box has no arrow drawn to 'X-ray screen with CAD'; the link is implied."]),
 D("fig-screen-plhiv-cxr-crp", 61, SA + " > Figure 12: PLHIV 15+ at Facilities with X-ray, CAD/AI and CRP", "Figure 12. TB screening algorithm for PLHIV aged 15+ at ART clinics with X-ray, CAD/AI and CRP: symptom screen, CRP for those not on ART, CXR with CAD for those on ART, Xpert, TB-LAM for AHD, TPT", ["0131", "0132", "0133"],
   "Population: PLHIV (>15 years) attending ART clinics.\n"
   "1. Symptom screen: current cough OR fever OR weight loss OR night sweats (WSS)*.\n"
   "   - Yes: collect two sputum samples; perform Xpert for active TB diagnosis*.\n"
   "   - No: is the individual on ART?\n"
   "     - Not on ART: C-reactive protein screen → positive: collect two sputum samples for Xpert*; negative: evaluate for TPT eligibility and offer TPT if eligible.\n"
   "     - On ART: was CXR screening done in the past 12 months? Yes: (no next step drawn). No: X-ray screen with CAD → positive**: (no next step drawn); non-TB abnormal#: further clinical evaluation, TPT if eligible; negative: further clinical evaluation, TPT if eligible.\n"
   "2. Xpert result: positive → initiate TB treatment; negative → further clinical evaluation, TPT if eligible.\n"
   "* Perform TB-LAM for all with AHD (CD4 <200, WHO stage 3 or 4 regardless of symptoms; seriously ill regardless of CD4; all presumptive TB regardless of CD4). ** If CAD reports silicosis, refer for assessment and treatment of silicosis and provide TPT if eligible. # Abnormal (not TB): e.g. cardiomegaly, possible cancer, silicosis (if smoking history and possible cancer on CXR, highly suspicious of cancer).",
   ["A CAD-positive X-ray has no next step drawn – presumably sputum collection for Xpert, as in Figures 10 and 11. The earlier chunk wrongly sent it to 'further clinical evaluation'.", "'CXR screening done in the past 12 months: Yes' has no next step drawn (in Figure 11 it leads to further clinical evaluation and TPT)."]),
]
ITEMS.append(D("fig-plhiv-evaluation", 77, "Chapter 4: TB and Drug-Resistant TB Diagnosis > 4.3.4 Use of LF-LAM for TB Diagnosis in PLHIV > Figure 18: Algorithm to Evaluate for TB Among PLHIV", "Figure 18. Algorithm to evaluate for TB among PLHIV: TB symptoms/CXR/CRP, seriously ill, advanced HIV disease (AHD), urine LF-LAM and Xpert, start TB treatment, AHD package, TPT", ["0174", "0175"],
   "Assess: TB signs and symptoms†; whether seriously ill*; advanced HIV disease (AHD)**; perform CD4 testing (if eligible); perform CXR/CRP screening if eligible and available†.\n"
   "- Positive for TB symptoms and/or CXR/CRP positive for possible TB (regardless of CD4 / AHD status) → perform Xpert MTB/RIF Ultra and urine LAM (if not yet done).\n"
   "- AHD (regardless of TB symptoms) or seriously ill → perform urine LAM: LAM positive → perform Xpert and urine LAM (if not yet done); LAM negative → apply the AHD package of care.\n"
   "- No TB symptoms, CXR/CRP negative, CD4 >200 or unknown → clinical management; provide TPT if eligible.\n"
   "Results of Xpert and LAM: both negative → clinical management, provide TPT if eligible; Xpert AND/OR LAM positive → start TB treatment and perform work-up to exclude DR-TB (collect a specimen for phenotypic and genotypic DST).\n"
   "† Refer to the national TB guidelines and SOP for TB screening. * Seriously ill: at least one of respiratory rate >30/min, heart rate >120/min, temperature >39°C, or unable to walk unaided. ** AHD: CD4 <200 cells or WHO clinical stage 3 or 4; for children <5 years and have not been on treatment for at least 12 months (as printed). @ CRP >5 mg/L is defined as possible/presumptive TB.",
   ["AHD footnote for children is incomplete ('For children <5 years and have not been on treatment for at least 12 months'); WHO defines all children under 5 as having AHD, except those already stable on ART for over 12 months.", "CRP threshold printed as '>5m/L' (mg/L).", "'Seriously ill' uses >30/min, >120/min, >39°C here but ≥30, ≥120, ≥39°C in the Figure 16 footnote.", "For AHD with a negative LAM, the chart goes straight to the AHD package without Xpert, even though LAM sensitivity is limited; clinician to confirm intent (Xpert is done if symptomatic via the first branch)."]))
