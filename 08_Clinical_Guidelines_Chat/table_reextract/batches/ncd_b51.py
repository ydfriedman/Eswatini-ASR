exec(open('batches/ncd_common.py').read())
GN = CH7 + " > Glomerular Disease"
ITEMS = [
 T("tbl-gn-investigations-ddx", 225, GN + " > Screening and Diagnosis of Acute Glomerulonephritis",
   "Acute glomerulonephritis / nephrotic syndrome: investigations and differential diagnosis (primary, secondary, genetic, systemic, inflammatory and other causes)", ["0647", "0648"],
   [[C("Investigations"), C("Differential Diagnosis")]],
   [[L("Urine dipsticks", "Urinalysis with microscopy", "24-hour urine protein", "Blood urea nitrogen (BUN) and creatinine", "Full blood count", "Complement studies (C3, C4)", "Serum lipids", "Serum electrolytes",
       "Confirm the presence of nephrotic syndrome (albumin, cholesterol, urine dipstick & spot urine protein/creatinine ratio)",
       "Exclude an underlying systemic or exogenous cause of nephrotic syndrome that may require treatment (diabetes, HIV, VDRL, hepatitis B, lupus serology, ANA and anti-ds DNA antibody etc., underlying malignancy e.g. myeloma causing amyloidosis)",
       "Determine renal function (creatinine, GFR – note may be falsely low because of low muscle mass)",
       "Exclude complications of nephrotic syndrome (sepsis from urinary losses of immunoglobulins – e.g. ascitic tap; Doppler studies to exclude venous thrombosis)",
       "Determine the need for a kidney biopsy (e.g. in children: deteriorating kidney function, refractory proteinuria)"),
     C("1. Primary nephrotic syndromes: minimal change disease (MCD); focal segmental glomerulosclerosis (FSGS); membranous nephropathy; membranoproliferative glomerulonephritis (MPGN)<br/>2. Secondary causes: systemic lupus erythematosus (SLE); diabetes mellitus (diabetic nephropathy); amyloidosis; infections such as HIV, hepatitis B, hepatitis C and syphilis; drug-induced nephropathy<br/>3. Genetic and congenital disorders: Alport syndrome; congenital nephrotic syndrome<br/>4. Systemic diseases: multiple myeloma; systemic vasculitis; sarcoidosis<br/>5. Inflammatory and infectious causes: IgA nephropathy (Berger's disease); post-infectious glomerulonephritis<br/>6. Others: haematologic disorders – thrombotic microangiopathies like haemolytic-uraemic syndrome (HUS) and thrombotic thrombocytopenic purpura (TTP); malignancies – some cancers cause paraneoplastic glomerulopathies")]]),
 T("tbl-gn-investigations-by-level", 225, GN + " > Investigations by level of facility",
   "Glomerulonephritis/nephrotic syndrome: investigations by level of facility (clinic, health centre, regional and referral hospital); refer all suspected nephrotic syndrome", ["0649", "0650"],
   [[C("Clinic"), C("Health Centre"), C("Regional Hospital"), C("Referral Hospital")]],
   [[C("Patient history; urine dipstick; tuberculosis screen, HIV, hepatitis B, C, RPR"),
     C("Patient history; urine dipstick; RFTs, urinalysis, LFTs, CBC, lipid profile; abdominal USS; tuberculosis screen, HIV, hepatitis B, C, RPR"),
     C("Patient history; urine dipstick; RFTs, urinalysis, CBC, lipid profile, LFTs; tuberculosis screen, HIV, hepatitis B, C, RPR; abdominal USS; autoimmune screening, RF, anti-DNase, ASOT; cultures (blood, urine, swabs, shunt tip)"),
     C("Patient history; urine dipstick; RFTs, urinalysis, CBC, lipid profile, LFTs; tuberculosis screen, HIV, hepatitis B, C, RPR; abdominal USS; autoimmune screening, ASOT, RF, anti-DNase")]],
   table_note="REFER ALL SUSPECTED NEPHROTIC SYNDROMES TO A HIGHER LEVEL FACILITY AFTER PRIOR DISCUSSION WITH THE RECEIVING FACILITY.",
   source_flags=["The first column is headed 'Health' in the PDF (the second is 'Health Centre' implied); read as clinic and health centre."]),
 T("tbl-nephrotic-proteinuria-definitions", 226, GN + " > Nephrotic syndrome and nephrotic-range proteinuria",
   "Definitions of nephrotic syndrome, nephrotic-range proteinuria and non-nephrotic-range proteinuria (adults and children)", ["0651"],
   [[C("Nephrotic Syndrome"), C("Nephrotic-Range Proteinuria"), C("Non-Nephrotic-Range Proteinuria")]],
   [[C("Proteinuria (adults)*: >3.5 g per 24h; PCR >3000 mg/g (>300 mg/mmol)<br/>Proteinuria (children)*: >40 mg/m²/h; >300 mg/dl; 3+ on urine dipstick; PCR >2000 mg/g (>200 mg/mmol)<br/>Hypoalbuminemia†<br/>Edema‡<br/>Hyperlipidemia‡"),
     C("Proteinuria (adults): >3.5 g per 24h; PCR >3000 mg/g (>300 mg/mmol)<br/>Proteinuria (children)*: >40 mg/m²/h; >300 mg/dl; 3+ on urine dipstick; PCR >2000 mg/g (>200 mg/mmol)<br/>Serum albumin usually normal<br/>Edema is usually absent or minor<br/>Serum lipids usually normal or only mildly elevated"),
     C("Variable levels of proteinuria: 0.3-3.4 g per 24h; PCR <300 mg/g (<30 mg/mmol)<br/>Serum albumin normal<br/>No clinical symptoms")]],
   context_before="Nephrotic syndrome may present with the following ranges of proteinuria.",
   footnotes=["*Essential. †Laboratory-specific values: serum albumin should be measured by bromocresol purple (BCP; colorimetric), capillary electrophoresis (CE), or immunonephelometric (iMN) methods. Bromocresol green (BCG) methods can give erroneously high results; BCG values are about 5.5 g/l higher than BCP, CE or iMN values, so the degree of hypoalbuminemia that defines NS depends on the method. ‡Variable."]),
 T("tbl-nephrotic-key-terms", 226, GN + " > Pharmacological Management of Glomerulonephritis > Nephrotic Syndrome: definition of key terms",
   "Nephrotic syndrome definitions: remission, relapse, frequent relapse, steroid dependence; and general management of glomerulonephritis", ["0653", "0652"],
   [[C("Term"), C("Definition")]],
   [[C("Remission"), C("Urine albumin nil or trace (or proteinuria <4 mg/m2/h) for three consecutive days")],
    [C("Relapse"), C("Urine albumin 3+ or 4+ (or proteinuria >40 mg/m2/h) for three consecutive days, having been in remission previously")],
    [C("Frequent relapse"), C("Two or more relapses during 6 months, or more than three relapses during any 12-month period")],
    [C("Glucocorticoid steroid dependence (SDNS)"), C("Persistent proteinuria (>2 g/g creatinine) despite high-dose prednisone 60 mg/m² (2 mg/kg) daily for 4 weeks, in the absence of infection or nonadherence to medication")]],
   context_before="Management of acute glomerulonephritis: 1. low salt diet; 2. adequate but not excess protein; 3. ideally immunise before immunosuppressive therapy (pneumococcal vaccine repeated every 5 years, hepatitis B); 4. screen for infections before immunosuppressive therapy; 5. low sugar diet for those on glucocorticoids and calcineurin inhibitors.",
   footnotes=["GN, glomerulonephritis; SDNS, steroid dependent nephrotic syndrome; SSNS, steroid sensitive nephrotic syndrome."],
   source_flags=["The 'steroid dependence' definition describes steroid resistance (persistent proteinuria despite 4 weeks of high-dose prednisone); steroid dependence is usually relapse during or soon after tapering. Clinician to confirm."]),
 D("fig-nephrotic-syndrome-treatment", 227, GN + " > Pharmacological Management of Glomerulonephritis > Nephrotic syndrome treatment",
   "Nephrotic syndrome (children) treatment flowchart: initial prednisone, consolidation, and relapsing nephrotic syndrome (infrequent, frequent/steroid-dependent, steroid-resistant)", ["0655"],
   "Initial episode:\n"
   "1. Age 3-12 months or >12 years, gross haematuria, or low complement?\n"
   "   - Yes: consider kidney biopsy.\n"
   "   - No: intensive daily prednisone therapy 60 mg/m² (2 mg/kg).\n"
   "2. Remission within 4 [weeks]?\n"
   "   - No: consider kidney biopsy.\n"
   "   - Yes: consolidation therapy (alternate-day prednisone) for 8 weeks: 40 mg/m² (~1.5 mg/kg) every 48 h for 4 weeks, then 20 mg/m² (~0.75 mg/kg) every 48 h for 4 weeks, then stop.\n\n"
   "Relapsing idiopathic nephrotic syndrome:\n"
   "- Infrequent relapses: prednisone 60 mg/m² daily until remission, then 40 mg/m² on alternate days for 4 weeks.\n"
   "- Frequent relapses or glucocorticoid dependence:\n"
   "  - Option 1: assess the alternate-day prednisone threshold. Threshold <15 mg/m² (<0.5 mg/kg) → remission → alternate-day prednisone (0.1 to <0.5 mg/kg/dose). If glucocorticoid toxicity or no remission → option 2.\n"
   "  - Option 2: start a second-line agent if previous long-term glucocorticoid use with signs of toxicity.\n"
   "- Glucocorticoid resistance: kidney biopsy; therapy based on histological diagnosis.",
   ["'Remission within 4' has no unit (weeks). 'Gross hematuria, complement' presumably means low complement. '(-1.5mg/kg)' printed for ~1.5 mg/kg."]),
]
