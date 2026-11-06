exec(open('batches/ncd_common.py').read())
HM = CH15 + " > Hematuria"
def r(*v): return [C(x) for x in v]
ITEMS = [
 T("tbl-hematuria-definitions-classification", 347, HM + " > Definition and Standard Classification of Hematuria",
   "Haematuria: definitions (gross/visible, microscopic ≥3 RBC/HPF) and classification of causes (urological and non-urological)", ["0992", "0993"],
   [[C("Category"), C("Subcategory"), C("Definition / Examples")]],
   [{"section": "Definitions"},
    r("Gross Hematuria (GH) / Visible Hematuria (VH)", "", "Visible blood in urine"),
    r("Microscopic Hematuria", "", "Presence of ≥3 RBCs per HPF"),
    {"section": "Standard classification of hematuria (causes)"},
    [C("Urological causes", rs=6), C("Metabolic"), C("Stones")],
    r("Malignant", "Renal, ureter, bladder, prostate, urethral malignancies"), r("Congenital", "Congenital urological abnormalities"),
    r("Infective", "Tuberculosis (TB), bilharzia"), r("Inflammatory", "Cystitis"),
    r("Benign", "Benign prostatic hyperplasia (BPH), exercise-induced hematuria, post-sexual activity"),
    [C("Non-urological causes", rs=2), C("Medical (renal/systemic)"), C("Glomerulonephritis (GN), IgA nephropathy, pigmenturia, myoglobinuria, renal TB")],
    r("Hematological", "Bleeding disorders, blood dyscrasias, anticoagulant therapy")],
   context_before="Haematuria is the presence of blood in urine, grossly or microscopically. It is a sign rather than a condition, usually suggesting a condition of the genito-urinary tract that needs urgent attention."),
 T("tbl-gross-hematuria-pathways", 348, HM + " > Management of Gross Hematuria",
   "Management of gross haematuria by pathway: haemodynamically unstable, stable with clot retention, stable without clot retention", ["0996", "0997"],
   [[C("Element"), C("Pathway 1: Hemodynamically Unstable"), C("Pathway 2: Stable + Clot Retention"), C("Pathway 3: Stable, No Clot Retention")]],
   [r("Signs to look out for", "Hypotension, tachycardia, active bleeding", "Suprapubic pain, bladder distension, inability to void", "Visible hematuria, able to void"),
    r("Initial priority", "Resuscitation", "Relieve obstruction", "Investigate cause. Send urine for M/C/S. If terminal hematuria, send a specimen between 10am and 2pm to look for schistosomiasis and treat accordingly"),
    r("Immediate actions", "ATLS protocol; IV fluids ± blood", "3-way catheter; manual washout", "Basic investigations"),
    r("Bladder management", "3-way catheter + continuous irrigation", "3-way catheter + continuous irrigation", "Not routinely required"),
    r("Investigations", "After stabilisation", "After decompression", "UA, U&E, ultrasound"),
    r("Disposition", "Urgent urology referral", "Urology referral", "All gross hematuria → urology referral")],
   context_before="Initial management (clinic, health centre or hospital): ATLS approach; fluid therapy, blood transfusions; correct reversible derangements (infections, coagulopathies); indwelling 3-way catheter (22/24 Fr); clot evacuation and bladder irrigation with isotonic saline (60 cc catheter-tip syringes, 3 L saline bags/water for irrigation); once stabilised, refer to a urologist.",
   table_note="ALL CLIENTS PRESENTING WITH GROSS HEMATURIA SHOULD BE REFERRED TO THE UROLOGIST.",
   source_flags=["A heading 'Etiological Classification of Hematuria' is printed on p.348 with no content under it."]),
 D("fig-microhematuria", 349, HM + " > Management of Microhematuria",
   "Management of microscopic haematuria (flowchart): confirm, infection, glomerular cause, other causes, imaging, cytology, cystoscopy, follow-up", ["0998"],
   "1. Microscopic evaluation to confirm RBCs (>3 RBC/HPF) in 2 of 3 samples.\n"
   "2. Signs or symptoms of infection (dysuria, frequency, flank pain, leukocyte esterase, nitrites, white cells, bacteria)?\n"
   "   - Yes: treat the infection; confirm resolution of microscopic haematuria with a follow-up urinalysis 6 weeks after completing therapy.\n"
   "   - No: 3.\n"
   "3. Findings supporting a glomerular cause (proteinuria, elevated creatinine, red cell casts, dysmorphic RBCs, abnormal sediment, ≥5-10 WBC/HPF, or reduced renal function)? Yes: refer to a nephrologist. (Cytology is a poor screening test and is not recommended in the initial workup.)\n"
   "4. No: other aetiology probable (vigorous exercise, urethral trauma, menstruation, offending medication)? Yes: retest urine after the possible contributing factor is stopped.\n"
   "5. No: radiographic evaluation of the urinary tract (renal ultrasonography, CT, or IVP, considering availability and costs). If imaging is not available, refer to a urologist.\n"
   "   - If imaging is positive: refer to a urology subspecialist. If negative: urine cytology.\n"
   "   - Negative findings and low risk (age <40 and no risk factors): follow-up with urinalysis and blood pressure; if haematuria persists >3 months, consider specialist referral.\n"
   "   - Positive findings, or all patients >40, or younger patients with risk factors for urothelial tumours: refer to a urology subspecialist for cystoscopy.",
   ["Branch layout read from the chart; the caption fragment 'and costs.¹' is printed under renal ultrasonography."]),
 T("tbl-aua-microhematuria-risk", 350, HM + " > Diagnostic Stratification of Common Urological Conditions > AUA Microhematuria Risk Stratification",
   "Risk stratification of haematuria: AUA microhaematuria risk categories (low, intermediate, high) for urothelial malignancy and urgency of urology referral", ["0999", "1000"],
   [[C("Low Risk"), C("Intermediate Risk"), C("High Risk")]],
   [r("Women <50 yrs, men <40 yrs", "Women 50–59 yrs, men 40–59 yrs", "Women & men ≥60 yrs"),
    r("Never smoker or <10 pack-years", "10–30 pack-years", ">30 pack-years"),
    r("3–10 RBC/HPF", "11–25 [RBC/HPF]", "[>25] RBC/HPF"),
    r("3–10 RBC/HPF", "11–25 RBC/HPF on one urinalysis", "RBC >25/HPF on repeat urinalysis"),
    r("No other urothelial cancer risk factors", "1 or more additional urothelial cancer risk factors; previously low risk, no prior evaluation and RBC 3–25/HPF on repeat urinalysis", "History of gross hematuria; previously low risk, no prior evaluation")],
   table_note="Purpose: risk stratification helps the health practitioner decide which patients presenting with haematuria to refer as an emergency or urgently to a facility with urology services. The higher the category, the higher the malignancy risk and the greater the need for a full work-up and prompt referral to the urologist.",
   source_flags=["The RBC rows are garbled as printed: row 3 reads '3–10 RBC/HPF | 11–25 | RBC/HPF' (the high-risk value is missing; bracketed values inferred), and row 4 repeats '3–10 RBC/HPF'. In the AUA 2020 system, low risk is 3–10 RBC/HPF, intermediate 11–25 RBC/HPF, high >25 RBC/HPF; clinician to confirm and correct the table.", "'Starification' printed in the table title."]),
 T("tbl-hematuria-investigations", 350, HM + " > Diagnostic Stratification of Common Urological Conditions > Investigations",
   "Investigations and resources for haematuria and common urological conditions: laboratory, radiology, drugs, endoscopy", ["1001"],
   [[C("Category"), C("Items")]],
   [[C("Laboratory requirements"), L("Urine: MCS (microscopy, culture & sensitivity), cytology", "Bloods: full blood count (FBC), kidney function tests (KFTs), liver function tests (LFTs), coagulation profile", "Histological analysis")],
    [C("Radiology"), L("X-ray", "Ultrasound scan (USS)", "CT scan", "MRI")],
    [C("Drugs"), L("Intravesical aminocaproic acid / prostaglandin F2 / silver nitrate / aluminium ammonium sulphate", "Alpha blockers (see BPH protocol)", "5-alpha reductase inhibitors")],
    [C("Endoscope"), L("TURP set (transurethral resection of the prostate set)", "Cystoscope")]]),
]
