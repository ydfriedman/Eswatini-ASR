exec(open('batches/ncd_common.py').read())
U = CH15
BP = CH15 + " > Benign Prostatic Uropathy"
ED = CH15 + " > Erectile Function Disorders"
def r(*v): return [C(x) for x in v]
ITEMS = [
 D("fig-male-luts-algorithm", 351, U + " > Adult Male LUTS / Haematuria / Retention - Clinical Algorithm",
   "Adult male with LUTS, haematuria or urinary retention: assessment pathway, red flags, medical treatment vs emergency care, refer to urologist", ["1002", "1003"],
   "Step 1–5: assessment pathway\n"
   "1. Adult male with LUTS ± haematuria / retention.\n"
   "2. History: LUTS, haematuria, retention; comorbidities, medications.\n"
   "3. IPSS ± IIEF.\n"
   "4. Examination: abdominal, neurological, DRE.\n"
   "5. Investigations: urine dipstick ± MCS; FBC, UECs, PSA; KUB ± prostate ultrasound.\n"
   "Decision: red flags present?\n"
   "- No red flags: medical treatment – alpha-blocker ± 5-ARI, monitor IPSS → refer if poor response.\n"
   "- Red flags present: emergency care – 3-way catheter 22–24 Fr, irrigation ± clot evacuation → stabilise.\n"
   "Both pathways: refer to urologist.\n"
   "Key: IPSS = International Prostate Symptom Score; IIEF = International Index of Erectile Function; DRE = digital rectal examination; FBC = full blood count; UECs = urea, electrolytes & creatinine; PSA = prostate-specific antigen; MCS = microscopy, culture & sensitivity; KUB = kidneys, ureters & bladder X-ray; 5-ARI = 5-alpha reductase inhibitor; USS = ultrasound scan; LUTS = lower urinary tract symptoms.",
   ["The red-flag criteria themselves are not listed on the algorithm."]),
 T("tbl-bph-terminology", 352, BP + " > Standard Classification of Benign Prostatic Uropathy",
   "Standard classification and terminology of benign prostatic uropathy: BOO, BPH, BPE, BPO definitions", ["1005"],
   [[C("Term"), C("Full name"), C("Definition"), C("Key characteristics")]],
   [r("BOO", "Bladder Outlet Obstruction", "A generic clinical term for a blockage that slows or stops urine flow during voiding.", "Diagnosed via urodynamics (shows high bladder pressure but low flow)."),
    r("BPH", "Benign Prostatic Hyperplasia", "A histological (microscopic) diagnosis referring to the overgrowth of prostate cells.", "It is a cellular diagnosis, typically confirmed through biopsy or pathology after surgery."),
    r("BPE", "Benign Prostatic Enlargement", "A clinical observation of an increased prostate volume (size), regardless of symptoms.", "Can be detected via physical exam (digital rectal exam) or imaging (ultrasound)."),
    r("BPO", "Benign Prostatic Obstruction", "A specific form of BOO where the blockage is proven to be caused by BPE.", "This links the physical size of the prostate to the actual obstruction of urine.")]),
 T("tbl-luts-etiology", 352, BP + " > Etiological Classification of LUTS",
   "Etiological classification of lower urinary tract symptoms (LUTS): anatomical, functional/neurological, inflammatory/infectious, systemic causes", ["1006"],
   [[C("Category"), C("Specific conditions")]],
   [r("Anatomical & structural", "Benign prostatic hyperplasia, urethral stricture, bladder tumour, stones (bladder or ureter)"),
    r("Functional & neurological", "Neurogenic bladder, overactive bladder / detrusor overactivity, detrusor underactivity"),
    r("Inflammatory & infectious", "Urinary tract infection & inflammation, chronic pelvic pain syndrome"),
    r("Systemic & miscellaneous", "Nocturnal polyuria (excessive night-time urination), others")]),
 T("tbl-bph-treatment", 352, BP + " > Benign Prostatic Obstructive Uropathy > Treatment",
   "Treatment of benign prostatic obstruction / BPH by line of therapy: watchful waiting, urotherapy and lifestyle, alpha-1 blockers tamsulosin and doxazosin, side effects, referral and follow-up", ["1007"],
   [[C("Line of therapy"), C("Indications"), C("Interventions"), C("Key notes / side effects")]],
   [[C("First-line therapy", rs=3), C("BPE without bothersome symptoms – mild IPSS score"), C("Watchful waiting (mild IPSS): reassure, reinforce healthy lifestyle"), C("Education and lifestyle modification are central", rs=3)],
    [C("Mild–moderate IPSS"), L("Urotherapy: double voiding", "Treat constipation", "Bladder training", "Urethral milking post-void", "Control fluid intake (storage LUTS)")],
    [C("Mild–moderate IPSS"), L("Avoid bladder irritants (coffee, alcohol, cola, spicy foods)", "Optimise DM/HTN control if concomitant", "Substitute LUTS-exacerbating drugs (diuretics, TCAs, antihistamines, flu medications)")],
    [C("Second-line therapy", rs=3), C("Moderate–severe LUTS – failed 1st-line therapy"), C("Alpha-1 blockers – relax internal sphincter & prostate smooth muscles"), C("")],
    [C("Preferred in normotensive patients"), C("Tamsulosin (Uromax) 0.4 mg OD (may double in selected cases) – uroselective"), L("Retrograde ejaculation → ↓ ejaculate volume", "Orthostatic hypotension (first few weeks) → ↑ fall risk", "Floppy iris syndrome in cataract surgery → avoid in cataract patients")],
    [C("Particularly useful in patients with hypertension"), C("Doxazosin (Cardura) 4 mg / 8 mg XL nocte"), L("Dizziness", "Asthenia", "Orthostatic hypotension", "Strong vasodilatory effect → avoid with nitrates or CCF")]],
   pages=[352, 353],
   table_note="Patients whose IPSS fails to improve despite the interventions above are candidates for referral to a urologist for further evaluation, with the possibility of combination therapy or surgical treatment. Patients doing well on therapy can be seen at 3–6-month intervals.",
   source_flags=["5-alpha reductase inhibitors are named in the algorithm (p.351) and investigations table (p.350) but have no dosing row in this treatment table."]),
 T("tbl-ed-classification", 353, ED + " > Classification",
   "Erectile dysfunction: classification (organic, psychogenic, mixed) and common contributing factors", ["1008"],
   [[C("Classification"), C("Description"), C("Common contributing factors")]],
   [r("Organic", "Caused by physical defects, vascular issues, or nerve damage.", "Cardiovascular disease, diabetes mellitus, hypertension, smoking, and chronic kidney disease"),
    r("Psychogenic", "Resulting from psychological factors or emotional stress.", "Anxiety, depression, relationship issues, and performance stress"),
    r("Mixed", "A combination of both physical and psychological factors.", "Primary organic issues that lead to secondary performance anxiety")],
   source_flags=["This table has no title and is printed between the BPH treatment table and the 'Erectile Function Disorders' heading; its content is the classification of erectile dysfunction."]),
 D("fig-ed-primary-care", 354, ED + " > Guidelines for Primary Care Management of Erectile Dysfunction",
   "Primary care management of erectile dysfunction (flowchart): initial assessment, psychogenic vs organic features, investigations, hypogonadism, PDE5 inhibitors, CHD, referral", ["1010", "1011"],
   "1. GP initial assessment: sexual history, relevant blood tests, blood pressure, genital examination. ALL young patients with a history of trauma and/or penile/testicular abnormalities on clinical examination SHOULD BE REFERRED TO UROLOGY IMMEDIATELY.\n"
   "2a. Suggests psychogenic: sudden onset; good or better early-morning / self-stimulated erections; relationship problems; variable depending on circumstances → first-line treatment with PDE5 inhibitors and monitor response; consider counselling.\n"
   "2b. Suggests organic: gradual onset; lack of tumescence; normal libido; relevant medical history; smoker; difficulty with penetration → further investigations: BMI, BP, abdominal circumference, HbA1c, lipogram; encourage weight loss.\n"
   "3. Clinical features suggestive of hypogonadism: testosterone (before 10 am) and thyroid function; if testosterone low, do FSH, LH, prolactin, SHBG.\n"
   "   - If abnormal: refer to urology / endocrinology as appropriate.\n"
   "   - If normal with no evidence of CHD: first-line treatment with PDE5 inhibitors.\n"
   "   - Normal but with CHD: guidance from cardiology/medicine; once the patient is low risk according to Princeton criteria, consider PDE5 inhibitors.\n"
   "PDE5 inhibitors: sildenafil (Viagra); tadalafil (Cialis) – consider daily dose if possible; vardenafil (Levitra).",
   ["Printed 'IF NORMAL WITH N EVIDENCE OF CHD' (read as 'no evidence'), 'Tadalifil', 'In hibitors', 'Princetown' (Princeton), 'SHOULD REFERRED'."]),
 T("tbl-pde5-comparison", 355, ED + " > PDE5 Inhibitors",
   "PDE5 inhibitors for erectile dysfunction: sildenafil (Viagra) vs tadalafil (Cialis) onset, half-life, food effect, doses, side effects, contraindications, pharmacological failure", ["1012", "1013"],
   [[C(""), C("Sildenafil / Viagra"), C("Tadalafil / Cialis")]],
   [r("Onset of action", "15 min – 1 hour", "15 min – 2 hours"),
    r("½ life", "3–5 hours", "17.5 hours"),
    r("Food effect", "Reduced absorption with fatty foods", "None"),
    r("Dosages", "25, 50, 100 mg", "5, 10, 20 mg"),
    [C("Side effects"), C("Headache, dyspepsia, facial flushing, blurred/blue vision (rare), myalgia, backache", cs=2)],
    r("Contraindications", "Nitrates", "Nitrates"),
    [C("Pharmacological failure"), C("Counsel the patient to take the medication at least 8 times at the maximum dose, 1 hour before sex, on an empty stomach, together with sexual stimulation, before it is deemed medication failure. Then refer to urology.", cs=2)]]),
 T("tbl-pde5-princeton-risk", 355, ED + " > PDE5 Inhibitor Eligibility (Princeton III)",
   "PDE5 inhibitor fitness/eligibility by cardiovascular risk (Princeton III Consensus 2010): low, intermediate, high risk and management", ["1014"],
   [[C("Risk level"), C("Examples / criteria"), C("Next steps / management")]],
   [[C("Low risk"), L("Controlled hypertension", "Successfully revascularised (e.g. bypass surgery)"), C("Lifestyle changes, PDE5 inhibitors")],
    [C("Intermediate risk"), L("Mild or moderate stable angina", "Past myocardial infarction (2–8 weeks)"), C("Cardiovascular evaluation & management → if improves: low-risk management; if fails: high-risk management (refer to cardiologist / internal medicine)")],
    [C("High risk"), L("Unstable angina", "CCF NYHA IV", "Recent MI (<2 weeks)"), C("Refer to cardiologist / internal medicine")]],
   context_before="PDE5 inhibitors' fitness/eligibility criteria – based on the Princeton III Consensus Conference 2010."),
 T("tbl-premature-ejaculation-types", 355, ED + " > Premature Ejaculation",
   "Premature ejaculation: types (lifelong/primary vs acquired/secondary), description and aetiology", ["1015"],
   [[C("Type"), C("Description"), C("Etiology")]],
   [r("Lifelong / primary", "Cluster of core symptoms including early ejaculation at nearly every intercourse: within 30–60 seconds in ~80% of cases; between 1–2 minutes in ~20% of cases", "Present from first sexual experiences"),
    r("Acquired / secondary", "Early ejaculation at some point in life in men who previously had normal ejaculatory experiences", "Situational: partner conflicts; psychological: stressors")]),
]
