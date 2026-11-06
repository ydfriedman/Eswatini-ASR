exec(open('batches/ncd_common.py').read())
DF = CH12 + " > Diabetic Foot"
def r(*v): return [C(x) for x in v]
INF = "With infection"; ISC = "With ischaemia"; BOTH = "With infection and ischaemia"
ITEMS = [
 T("tbl-wagner-classification", 294, DF + " > Classification > Wagner grades",
   "Diabetic foot ulcer classification (Wagner grades 0-5): description and category", ["0846"],
   [[C("Ulcer Grade"), C("Description"), C("Category")]],
   [r("0", "No ulcer but high-risk foot (e.g. deformity, callus, or ischaemia)", "Non-ulcer stage"),
    r("1", "Superficial ulcer involving only the skin", "Non-gangrenous ulcer"),
    r("2", "Deep ulcer, extending into tendon, bone, or joint capsule, but without bony involvement or abscess", "Non-gangrenous ulcer"),
    r("3", "Deep ulcer with abscess, osteomyelitis, or joint sepsis (confirmed clinically or by X-ray)", "Non-gangrenous ulcer"),
    r("4", "Localized gangrene (e.g. toe, heel, forefoot)", "Gangrenous ulcer"),
    r("5", "Extensive gangrene involving the whole foot", "Gangrenous ulcer")],
   context_before="Diabetic foot: infection, ulceration or destruction of tissues of the foot associated with neuropathy and/or peripheral arterial disease in people with diabetes. About 80% of non-traumatic lower limb amputations in diabetes are preceded by a foot ulcer.",
   source_flags=["Grade 2 is described as 'extending into tendon, bone, or joint capsule, but without bony involvement' (self-contradictory; Wagner grade 2 is a deep ulcer to tendon or capsule without abscess or osteomyelitis)."]),
 T("tbl-ut-classification", 294, DF + " > Classification > University of Texas classification",
   "University of Texas (UT) diabetic foot wound classification: grade 0-III by depth and stage A-D by infection and ischaemia", ["0847", "0848"],
   [[C("Stage"), C("Grade 0"), C("Grade I"), C("Grade II"), C("Grade III")]],
   [r("Stage A", "Pre- or post-ulcerative lesion, completely epithelialized", "Superficial wound, not involving tendon, capsule or bone", "Wound penetrating to tendon or capsule", "Wound penetrating to bone or joint"),
    r("Stage B", INF, INF, INF, INF), r("Stage C", ISC, ISC, ISC, ISC), r("Stage D", BOTH, BOTH, BOTH, BOTH)],
   table_note="All patients with diabetes should be assessed for diabetic foot at risk: screened, diagnosed, investigated, classified and risk-stratified."),
 D("fig-diabetic-foot-algorithm-a", 295, DF + " > Algorithm A: foot assessment and risk",
   "Diabetic foot algorithm A: foot assessment in all patients with diabetes, active foot problems, and risk stratification (high, moderate, low) with actions", ["0850", "0851"],
   "All patients with diabetes → foot assessment: skin; neurological; vascular; musculoskeletal.\n"
   "1. Active foot problem? (any of: ulceration; spreading infection; critical limb ischaemia; gangrene; suspicion of acute Charcot neuroarthropathy or an unexplained hot, red, swollen foot with or without pain)\n"
   "   - Yes → Algorithm B.\n"
   "   - No → 2.\n"
   "2. Previous history of ulceration, amputation, or on renal replacement therapy? Yes → HIGH RISK: early referral to podiatrist/surgical department for further care.\n"
   "3. Deformity/neuropathy/non-critical limb ischaemia → MODERATE RISK: refer to NCD clinic/podiatrist/surgical department for further review.\n"
   "4. Callus alone → LOW RISK: total contact insole; foot care education; yearly screening.\n"
   "5. Normal findings → foot care education; yearly screening.\n"
   "*Risk categories as in the diabetic foot risk stratification table."),
 D("fig-diabetic-foot-algorithm-b", 296, DF + " > Algorithm B: active foot problems",
   "Diabetic foot algorithm B: management of active foot problems by ulcer type, infection and ischaemia (outpatient, oral antibiotics, multidisciplinary foot care team)", ["0852"],
   "Active foot problems*:\n"
   "- Without ulcer (UT grade 0): manage as outpatient by foot protection services.\n"
   "- With ulcer:\n"
   "  - Superficial (UT IA): manage as outpatient by foot protection services.\n"
   "  - Infection:\n"
   "    - Superficial ulcer not requiring surgical intervention (UT IB): oral antibiotics (outpatient, foot protection services).\n"
   "    - Deep ulcer requiring surgical intervention (UT IIB/IIIB): refer to the multidisciplinary foot care team.\n"
   "  - Ischaemia (pulses not palpable) (UT IC/IIC/IIIC): refer to the multidisciplinary foot care team.\n"
   "  - Infection and ischaemia (UT ID/IID/IIID): refer to the multidisciplinary foot care team.\n"
   "*Refer urgently for admission if the patient presents with general illness (e.g. sepsis or diabetic [emergency]).",
   ["The footnote is cut off at 'sepsis or diabetic'; 'Without ulcer (UT' is also cut off."]),
 B("box-tuning-fork-test", 297, DF + " > Screening > Tuning Fork Examination",
   "How to perform the 128 Hz tuning fork test for diabetic neuropathy", ["0855"],
   "1. Ask the patient to close his/her eyes.\n2. Tap a 128 Hz tuning fork and place it on the patient's sternum to confirm vibration.\n3. Tap the tuning fork and place it on a bony prominence of the foot (distal phalanx of the great toe).\n4. Ask the patient to tell you when vibration is felt on the foot and when it stops.\n5. If sensation is impaired, continue to assess more proximally (e.g. mid-dorsal foot, medial malleolus, mid-fibula, patella).\n6. Repeat on the other leg.\nNote: any bony prominence of the foot can be tested, but the best point for the vibration test is the great toe."),
 T("tbl-diabetic-foot-risk", 297, DF + " > Diabetic Foot Risk Stratification",
   "Diabetic foot risk stratification: normal, low, moderate, high risk findings", ["0856"],
   [[C("Diabetic Foot Risk"), C("Findings")]],
   [r("Normal", "No abnormalities"), r("Low Risk", "Callus alone"),
    r("Moderate Risk", "Any of the following: deformity; neuropathy; non-critical limb ischaemia"),
    r("High Risk", "One of the following: previous ulceration; previous amputation; on renal replacement therapy; neuropathy and non-critical limb ischaemia; neuropathy with callus and/or deformity; non-critical limb ischaemia with callus and/or deformity"),
    r("Active Diabetic Foot Problem", "Any of the following: ulceration; infection; critical limb ischaemia; gangrene; suspicion of an acute Charcot neuroarthropathy, or an unexplained hot, red, swollen foot with or without pain")],
   pages=[297, 298],
   source_flags=["Table continues onto p.298 (active diabetic foot problem row). The PDF text layer for this page is overprinted with a second copy; transcribed from the page image."]),
]

ITEMS += [
 D("fig-dfu-key-steps", 299, DF + " > Key Steps in Diabetic Foot Ulcer (DFU) Management",
   "Key steps in diabetic foot ulcer management: risk stratification, MDT, assessment, debridement, infection, moist healing, advanced therapies, offloading, metabolic control, monitoring, referral", ["0860"],
   "1. Risk stratification (Wagner, UT, SINBAD).\n2. Multidisciplinary team (endocrinology, podiatry, surgery, nursing, dietitian).\n3. Comprehensive assessment (wound, vascular, neuropathy, labs).\n4. Debridement (sharp, enzymatic, autolytic, etc.).\n5. Infection management (antibiotics, osteomyelitis care).\n6. Moist wound healing (appropriate dressings).\n7. Advanced therapies (NPWT, skin substitutes, HBOT, PRP).\n8. Offloading (total contact cast is the gold standard; walkers; footwear).\n9. Glycaemic & metabolic control.\n10. Monitoring & documentation (weekly to biweekly, photos).\n11. Referral criteria (no healing, infection, ischaemia).",
   ["'Risk Stratification' is printed again as the last box (cycle back to the start)."]),
 T("tbl-dfu-offloading", 300, DF + " > Off-Loading Techniques for DFUs",
   "Off-loading techniques for diabetic foot ulcers: total contact cast, removable cast walkers, cushioned footwear, custom orthotics, wheelchair/bed rest: indications, advantages, disadvantages, care", ["0862", "0863"],
   [[C("Technique"), C("Description"), C("Indications"), C("Advantages"), C("Disadvantages"), C("Care Considerations")]],
   [r("Total Contact Cast (TCC)", "Cast that encompasses the foot & ankle, redistributing pressure", "Moderate–severe plantar DFUs; no infection or significant ischaemia", "Gold standard for off-loading; promotes wound healing; reduces recurrence & re-ulceration", "Hard to monitor wound; skin maceration risk; fall/ambulation difficulty", "Keep dry & intact; weekly reviews for skin breakdown or infection"),
    r("Removable Cast Walkers (RCWs) / Braces", "Custom-fitted, removable devices for off-loading", "Mild–moderate DFUs, or if TCC not feasible", "Allows wound inspection & hygiene; more comfortable & easier to use", "Less effective than TCC; compliance issues if removed too often", "Use with proper footwear; patient education on strict off-loading"),
    r("Cushioned Footwear", "Shoes with cushioned insoles, rocker soles, or extra depth", "Mild DFUs; patients needing frequent ambulation", "Comfortable & non-invasive; redistributes pressure, especially combined with other techniques", "Not effective for moderate–severe ulcers; requires consistent use", "Regular podiatry inspection & fitting"),
    r("Custom Orthotics", "Tailored insoles/orthotics to redistribute pressure", "DFUs on forefoot or heel", "Individualized to foot anatomy; less cumbersome than casts/walkers", "Requires precise fitting; wear out & need replacement", "Educate patients on maintenance; ensure proper shoe fit"),
    r("Wheelchair / Bed Rest", "Eliminates weight-bearing through immobilization", "Severe DFUs, or with major vascular/neuropathic issues", "Removes pressure completely; can combine with NPWT", "Reduces mobility & quality of life; risk of pressure sores from immobility", "Monitor skin, nutrition, and mental health closely")],
   context_before="Off-loading reduces chronic pressure on the ulcer (which prevents healing and can lead to tissue damage, infection and amputation), promotes healing (better blood flow, regulated inflammation, collagen formation), and lowers infection risk (less friction and moisture)."),
]
