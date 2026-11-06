exec(open('batches/ncd_common.py').read())
GN = CH7 + " > Glomerular Disease"
ITEMS = [
 D("fig-ns-new-child-algorithm", 228, GN + " > Pharmacological Management of Glomerulonephritis > Treatment algorithm for NS in a newly nephrotic child",
   "Treatment algorithm for nephrotic syndrome in a newly nephrotic child: by age and syndromic features; steroid response; frequent relapser, infrequent relapser, steroid-dependent, non-responder", ["0657", "0658"],
   "New nephrotic syndrome in a child:\n"
   "- ≥12 years of age, syndromic features or family history (as printed; see flag): biopsy and/or genetic testing + referral to a specialty centre.\n"
   "- ≤12 years of age, no syndromic features or family history: glucocorticoids* (oral prednisone or prednisolone).\n"
   "  - No response after 4 or 6 weeks: genetic testing; kidney biopsy; calcineurin inhibitor; renin-angiotensin-aldosterone system blockade.\n"
   "  - Complete responder: glucocorticoids* for 8 or 12 weeks, then by course:\n"
   "    - Frequent relapser: cyclophosphamide; levamisole; mycophenolate mofetil; rituximab; calcineurin inhibitor.\n"
   "    - Infrequent relapser: glucocorticoids*.\n"
   "    - Steroid-dependent: mycophenolate mofetil; rituximab; calcineurin inhibitor; cyclophosphamide.\n\n"
   "Refer to a clinical trial where appropriate. NS, nephrotic syndrome. The management of glomerular disease depends on the type/cause and is individualised by a specialist according to the kidney biopsy histology.",
   ["The PDF draws the 'glucocorticoids' arrow from the '≥12 years, syndromic features' box and the 'biopsy/genetic testing' arrow from the '≤12 years, no syndromic features' box; the source algorithm (KDIGO 2021) has these the other way round, as written here. Clinician to confirm."]),
 B("box-kidney-biopsy-decision", 228, GN + " > Kidney Biopsy",
   "When to do a kidney biopsy in patients with proteinuria and/or glomerular haematuria (decision tree)", ["0659", "0660"],
   "Decision tree for considering a kidney biopsy in patients with proteinuria and/or glomerular haematuria:\n"
   "- The kidney biopsy is the gold standard for diagnostic evaluation of glomerular diseases. Biopsy should be performed if the result is expected to modify treatment and/or if additional prognostic information is needed.\n"
   "- Patients classically treated without a kidney biopsy diagnosis (children): steroid-sensitive nephrotic syndrome ≤12 years old; post-streptococcal GN.\n"
   "- Examples of conditions for which treatment may be considered without diagnostic confirmation by kidney biopsy: PLA2Rab+ (membranous nephropathy); PR3+ ANCA vasculitis; anti-glomerular basement membrane disease; Alport disease; Fabry disease; familial focal and segmental glomerulosclerosis in families with well-characterised mutations; biopsy contraindicated as judged by history, physical exam and laboratory testing; systemic lupus erythematosus.\n\n"
   "ANCA, antineutrophil cytoplasmic antibody; MPO, myeloperoxidase; PLA2Rab+, M-type phospholipase A2 receptor antibody positive; PR3, proteinase 3. Referral to a nephrologist may include immunosuppressive treatment such as prednisolone, mycophenolate mofetil, cyclophosphamide, angiotensin blockade."),
 T("tbl-gn-histology-treatment", 229, GN + " > Histology based treatment of Glomerular Disease",
   "Histology-based treatment of glomerular disease: minimal change disease (children and adults), membranous nephropathy, membranoproliferative GN, IgA nephropathy, lupus nephritis, pauci-immune necrotising GN: regimens, doses and special considerations", ["0661", "0662", "0663", "0664", "0665", "0666"],
   [[C("Histological Pattern"), C("Treatment Regime"), C("Special Considerations")]],
   [[C("Minimal Change Disease: children", rs=4), C("Steroid sensitive. Initial: A: prednisolone 60 mg/m2/d or 2 mg/kg/d [max 60 mg/d] for 6 weeks (complete 6 weeks of initial treatment if remission is attained at 4 weeks). Continue: A: prednisolone 40 mg/m2 or 1.5 mg/kg (alternate days) for 6 weeks if remission was attained by 4 weeks of initial treatment; after 6 weeks of alternate-day therapy taper and stop within 6 weeks (taper by 5-10 mg a week)"),
     C("In children biopsy is indicated for: 1. steroid resistant NS; 2. late failure to respond following initial response; 3. decreasing kidney function", rs=2)],
    [C("Relapsing steroid sensitive: A: prednisolone 60 mg/m2 or 2 mg/kg [max 60 mg/d] until in complete remission for 3 days, THEN A: prednisolone single dose on alternate days (40 mg/m2 or 1.5 mg/kg per dose; maximum 40 mg on alternate days) for at least 4 weeks. S: levamisole (PO) 2.5 mg/kg on alternate days for 12 months")],
    [C("Frequent relapse/steroid dependent: S: cyclophosphamide 2 mg/kg/d for 10-12 weeks [max 168 mg/kg cumulative dose] OR S: cyclosporine 4-5 mg/kg/d (starting dose) OR S: tacrolimus 0.1 mg/kg/d (starting dose) OR S: everolimus 0.5-2 mg 12-hourly OR S: sirolimus 1-3 mg 12-hourly OR S: mycophenolate mofetil 1200 mg/m2/d in two divided doses; S: rituximab 375-1000 mg/m2"), C("Monitor calcineurin inhibitor toxicity/levels")],
    [C("Steroid resistant nephrotic syndrome: S: mycophenolate mofetil 1200 mg/m2/d in two divided doses OR S: mycophenolate sodium AND A: prednisolone high dose"), C("")],
    [C("Minimal Change Disease: adults", rs=2), C("D: prednisolone (PO) 1 mg/kg 24-hourly (maximum 80 mg) OR alternate-day single dose of 2 mg/kg (maximum 120 mg) – 4 weeks if remission; continue to 16 weeks if complete remission is not achieved"), C("Slow taper after remission over 6 months. Check HbA1c monthly. Screen for osteoporosis")],
    [C("Frequent relapse/steroid dependent/resistant (idiopathic only): D: prednisolone (PO) 1 mg/kg [max 80 mg] daily or alternate-day 2 mg/kg [max 120 mg] for 4-16 weeks. OR, if intolerant of steroids or steroid resistant: S: cyclosporine 3.5-5 mg/kg/d in 2 divided doses OR S: tacrolimus 0.1 mg/kg/day in 2 divided doses (then titrate)"), C("Exclude secondary causes. Slow taper after remission over 6 months. Monitor levels")],
    [C("Membranous nephropathy (idiopathic only)", rs=2), C("Children: alternating monthly treatment with methylprednisolone + prednisolone (months 1, 3 & 5) and oral cyclophosphamide (months 2, 4 & 6): D: methylprednisolone 10 mg/kg for 3 days, then prednisolone 0.5 mg/kg for 27 days; S: cyclophosphamide 2 mg/kg for 30 days. Alternative regimens: S: cyclosporine 3.5-5 mg/kg in two divided doses with prednisolone 0.15 mg/kg/day for 6 months; S: tacrolimus 0.2 mg/kg in two divided doses without prednisolone"),
     C("Exclude secondary causes. Monitor for 6 months before starting unless life-threatening symptoms OR rising creatinine. Do not use if serum creatinine >309 micromol/l [CKD patient]. Kidney biopsy might be repeated", rs=2)],
    [C("Adults: S: cyclophosphamide; A: prednisolone 1 mg/kg/day; D: methylprednisolone IV monthly. Alternative regimens: S: tacrolimus 0.1 mg/kg/day in 2 divided doses for 6 months OR S: cyclosporine 3.5-5 mg/kg/d in 2 divided doses. If albumin <25 g/l + thrombosis risk: C: warfarin 5 mg PO [refer to DVT anticoagulation]")],
    [C("Membranoproliferative GN"), C("S: cyclophosphamide OR S: mycophenolate mofetil 1200 mg/m2/d in two divided doses OR S: mycophenolate sodium AND A: prednisolone"), C("")],
    [C("IgA Nephropathy"), C("Initial supportive care for 3-6 months: C: enalapril (PO) 10-20 mg 24-hourly OR C: lisinopril (PO) 2.5-10 mg 24-hourly. For persistent proteinuria >1 g/d for 6 months (adults and children): A: prednisolone (PO) 1 mg/day for 6 months (as printed)"), C("Other registered ACEI or ARBs may be used as in the Hypertension section")],
    [C("Lupus nephritis (adult)", rs=3), C("All patients: S: hydroxychloroquine (PO) 6 mg/kg/day maintenance. Class II with proteinuria >3 g/day: treat as minimal change disease above"), C("")],
    [C("Class III and class IV, initial 6 months: D: methylprednisolone (IV slow) 250-1000 mg over 30 min for 3 days monthly AND S: cyclophosphamide (IV) 500-1000 mg/m2 monthly OR S: mycophenolate mofetil (PO) 0.5-1 g 12-hourly, titrating to 1.5 g 12-hourly if tolerated, OR S: mycophenolate sodium. Maintenance: S: azathioprine (PO) 1.5-2.5 mg/kg/d OR S: mycophenolate mofetil (PO) 0.5-1 g 12-hourly OR S: mycophenolate sodium OR S: cyclosporine 4-5 mg/kg/d (starting dose) for 6 months OR S: tacrolimus 0.1 mg/kg/d (starting dose)"),
     C("Oral prednisolone less effective; 60 mg/day may be given. A shorter, more frequent regimen (Euro-Lupus) may be used: cyclophosphamide 500 mg every two weeks x 6 doses")],
    [C("Class V + persistent nephrotic-range proteinuria: as class III and IV"), C("")],
    [C("Pauci-immune focal and segmental necrotizing glomerulonephritis"), C("Initial: S: cyclophosphamide (IV) 15 mg/kg every 2 weeks x 3 doses, then every three weeks for 3-6 months, OR S: cyclophosphamide oral 1.5-2 mg/kg daily for 3-6 months; AND D: methylprednisolone (IV) 250-1000 mg slowly over 30 min for 3 days as induction, then prednisolone 1 mg/kg, tapered to 30 mg in one week and then to 5 mg by 4-6 months. Severe disease: S: rituximab 1 g followed 14 days later by another 1 g, OR S: rituximab 375 mg/m2 per week for 4 weeks; AND D: methylprednisolone (IV) 250-1000 mg over 30 min for 3 days as induction, then A: prednisolone 1 mg/kg tapered as above. Maintenance: S: azathioprine (PO) 1-2 mg/kg/d for 18 months OR S: mycophenolate mofetil 1 g 12-hourly OR S: mycophenolate sodium"),
     C("S: haemodialysis. S: plasmapheresis in special indications")]],
   pages=[229, 230, 231],
   context_before="Letters before drugs (A, C, S, D) are the medicine level codes used in the guideline.",
   source_flags=["IgA nephropathy prednisolone is printed '1mg/day' (presumably 1 mg/kg/day); proteinuria threshold printed '1g/d' (presumably >1 g/d).",
                 "'0.9% sodium chloride' appears after 'Relapsing Steroid Sensitive' with no context.", "'Class V ... as clas II and IV' printed; read as class III and IV.",
                 "Membranous nephropathy 'Do not use serum creatinine >309' does not say what not to use (presumably cyclophosphamide/alkylating therapy).",
                 "'Membranous proliferative' printed; read as membranoproliferative. Table spans pp.229-231 with the header repeated."]),
]
ITEMS += [
 T("tbl-gn-pregnancy-care", 232, GN + " > Management in Special Populations > Glomerular disease in pregnancy",
   "Coordinated care of pregnant patients with glomerular disease: prepregnancy, antenatal, delivery and postnatal actions", ["0668", "0669", "0670"],
   [[C("Stage"), C("Actions")]],
   [[C("Prepregnancy"), L("Discuss timing of contraception; contraception advice if needed; fertility assessment if needed", "Assess disease activity, with repeat biopsy confirmation if necessary; optimize blood pressure control", "Change to non-teratogenic medications and provide reassurance about continuation of safe medications", "Explain the risk of pregnancy complications and the need for heightened surveillance")],
    [C("Antenatal"), L("Target BP <140/90 mmHg", "Oral glucose tolerance test (especially important in women taking glucocorticoids or calcineurin inhibitors)", "Start low dose aspirin; consider vitamin D and calcium supplements", "Frequent fetal monitoring if concerns about fetal well-being: up to twice weekly BPPs, up to placental Dopplers, 2-weekly growth scans", "Baseline and serial kidney function, proteinuria (albumin-creatinine or protein-creatinine ratios or 24h collections) and markers of disease activity", "Monitoring of calcineurin inhibitor levels if required", "Consider venous thromboembolism prophylaxis if risk factors, e.g. nephrotic syndrome, previous venous thromboembolic events, high body mass index")],
    [C("Delivery"), L("Delivery if fetal or maternal decompensation", "NOT at a pre-specified gestation", "Glucocorticoids for fetal lung maturation at least 24 h and up to 7 d before anticipated delivery if <34 weeks gestation")],
    [C("Postnatal"), L("Encourage breastfeeding", "Careful surveillance for active glomerulonephritis", "Calcineurin inhibitor level if dose changed in pregnancy", "Continue venous thromboembolism prophylaxis for at least 6 weeks if necessary", "Emotional support")]],
   context_before="Glomerular disease in pregnancy and women of child-bearing age (15-49 years): safer immunosuppression and adjuncts are azathioprine, calcineurin inhibitors (tacrolimus, cyclosporine), glucocorticoids, and hydroxychloroquine. Preferred contraception: products that do not contain estrogen.",
   footnotes=["Adapted from Blom K, Odutayo A, Bramham K, et al. Pregnancy and glomerular disease: a systematic review of the literature with management guidelines. Clin J Am Soc Nephrol. 2017;12:1862-1872. BP, blood pressure; BPP, biophysical profile; q2, every 2."],
   source_flags=["The PDF lays each stage out in four unlabeled columns; the bullets are listed per stage here. 'decomposition' and 'pre-specific gestation' printed (decompensation, pre-specified)."]),
 T("tbl-gn-contraception", 233, GN + " > Management in Special Populations > Contraception in women with glomerular disease",
   "Contraception in women with glomerular disease: unintended pregnancy rates (perfect and typical use), contraindications and other considerations by method", ["0671", "0672"],
   [[C("Contraceptive Method", rs=2), C("Unintended pregnancy rate within 1st year of use (%)", cs=2), C("Contraindications in glomerular disease", rs=2), C("Other considerations", rs=2)],
    [C("Perfect use"), C("Typical use")]],
   [[C("Estrogen-containing methods (pill, patch, ring)"), C("0.3"), C("9"), C("Lupus; venous thromboembolism; vascular disease"), C("Breast cancer risk; cervical cancer risk with immunosuppression; venous thromboembolism risk in nephrotic syndrome")],
    [C("Progesterone-only pill"), C("0.3"), C("9"), C("None"), C("Longest re-dosing interval with desogestrel (may improve typical use); possible breast cancer risk, especially >40 yr")],
    [C("Progesterone intrauterine device (Mirena)"), C("0.2"), C("0.2"), C("None"), C("Possible breast cancer risk, especially >40 yr; effective with immunosuppression, no evidence of increased infection")],
    [C("Progesterone implant (Nexplanon)"), C("0.05"), C("0.05"), C("None"), C("Possible breast cancer risk, especially >40 yr")],
    [C("Copper intrauterine device"), C("0.6"), C("0.8"), C("None"), C("No associated hormone risk")],
    [C("Male condom"), C("2"), C("18"), C("Ineffective for long-term use"), C("Protects against human immunodeficiency virus and sexually transmitted infection")],
    [C("Female condom"), C("5"), C("21"), C(""), C("")],
    [C("None"), C("85"), C("85"), C(""), C("")]],
   footnotes=["Reproduced from Kidney International Reports 3(2), Wiles K, Lightstone L. Glomerular diseases in women, pp.258-270, © 2018 International Society of Nephrology (CC BY-NC-ND). Rates from Trussell."]),
]
