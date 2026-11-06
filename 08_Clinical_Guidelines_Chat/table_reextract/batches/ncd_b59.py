exec(open('batches/ncd_common.py').read())
CA = CH10 + " > Cataract"; DR = CH10 + " > Diabetic Retinopathy"
def r(*v): return [C(x) for x in v]
ITEMS = [
 D("fig-cataract-workflow", 278, CA + " > Screening and Diagnosis of Cataract",
   "Cataract screening, diagnosis and management workflow: assessment, ruling out other causes, impact on daily life, referral, early vs significant cataract, surgery; referral rules", ["0796", "0797"],
   "1. Patient presents with visual complaints: gradual, painless vision loss; glare, haloes, blurred vision.\n"
   "2. Clinical assessment: visual acuity; lens exam (cloudiness); red reflex.\n"
   "3. Rule out other causes of vision loss: retinal disease; glaucoma; refractive errors.\n"
   "4. Confirm the cataract diagnosis.\n"
   "5. Assess the impact on daily life: daily activities; bilateral/unilateral; uncorrectable with glasses.\n"
   "6. Refer to an ophthalmologist: full evaluation; biometry.\n"
   "   - Mild/early cataract: monitor; improve lighting; adjust glasses.\n"
   "   - Affects daily life (significant cataract): surgery (phacoemulsification + IOL); post-operative care: eye drops, follow-up, patient education.\n\n"
   "REFER ALL SEVERE/SIGNIFICANT CATARACT CASES TO AN EYE SURGEON FOR CATARACT SURGERY. Refer clients with comorbidities such as HTN/DM, and pregnant women with cataract, to an ophthalmologist once a year from diagnosis for routine screening. Refer children immediately: a white pupil in a child may be an eye tumour, and late referral may lead to permanent loss of vision, squint, loss of the eye or loss of life."),
 T("tbl-dr-classification", 279, DR + " > Classification of DR",
   "Diabetic retinopathy classification by severity (no DR, mild/moderate/severe NPDR, PDR, DME): defining features, management and follow-up interval", ["0800", "0801"],
   [[C("DR Severity"), C("Defining Features"), C("Management"), C("Follow-up")]],
   [r("No DR", "No microvascular abnormalities", "Control blood glucose levels, serum lipid levels, and blood pressure", "1-2 yrs"),
    r("Mild NPDR", "Microaneurysms only", "Control blood glucose levels, serum lipid levels, and blood pressure", "6-12 mo"),
    r("Moderate NPDR", "Microaneurysms and other signs (dot and blot haemorrhages, hard exudates, cotton wool spots), but not severe NPDR", "Control blood glucose levels, serum lipid levels, and blood pressure", "3-6 mo"),
    r("Severe NPDR", "Intraretinal haemorrhages (>20 in each of 4 quadrants), definite venous beading (in at least 2 quadrants), or apparent IRMA (in at least 1 quadrant), but not PDR", "Consider PRP", "<3 mo"),
    r("PDR", "Neovascularization of the optic disc or elsewhere, preretinal haemorrhage, or vitreous haemorrhage", "Strongly consider PRP; consider vitrectomy for persistent vitreous haemorrhage or tractional retinal detachment", "<1 mo (variable)"),
    r("DME", "Retinal thickening in the macula", "Consider focal laser photocoagulation, anti-VEGF therapy, or corticosteroid therapy for centre-involving DME", "1-3 mo")],
   pages=[279, 280],
   footnotes=["No DR: no apparent retinopathy; NPDR: non-proliferative diabetic retinopathy; PDR: proliferative diabetic retinopathy; DME: diabetic macular oedema. Fundus photographs show normal fundus, moderate NPDR, severe NPDR and PDR (courtesy of Medscape Education)."],
   source_flags=["'Control blood levels' printed in the No DR row (blood glucose levels)."]),
 T("tbl-dr-screening-schedule", 281, DR + " > Screening and Diagnosis of Diabetic Retinopathy",
   "Diabetic retinopathy screening schedule: timing of first and subsequent retinal examination by risk factor (type 1, type 2, complications, poor control, other)", ["0802", "0803"],
   [[C("Risk Factors"), C("1st retinal examination"), C("Subsequent examination")]],
   [r("Type 1 DM", "Within 5 years of diagnosis and after onset of puberty", "Annually"),
    r("Type 2 DM", "At time of diagnosis", "Annually"),
    r("Evidence of other diabetic complications, e.g. CVD, renal disease (nephropathy), foot ulcers (neuropathy)", "Immediately", "As recommended by eye care provider"),
    r("Poor glycaemic control", "Immediately", "As recommended by eye care provider"),
    r("Other risk factors: hyperlipidemia, smoking, cataract surgery, obesity, anaemia, leukaemias etc.", "At time of diagnosis / immediately", "As recommended by eye care provider")],
   table_note="Screening by health care workers (medical officers and nursing staff): visual acuity with a Snellen or illiterate E chart; penlight torch to examine the external eye, pupillary reaction etc. Symptoms are absent early; later fluctuating or blurred vision, spots or floaters, dark or empty areas in vision, total loss of vision."),
 D("fig-dr-screening-flowchart", 281, DR + " > Screening flowchart for diabetic retinopathy",
   "Diabetic retinopathy screening flowchart: visual acuity and fundus findings → routine re-examination, non-urgent referral, or urgent referral", ["0804", "0805"],
   "1. Diabetes history, medical history, current medication, biochemical parameters.\n"
   "2. Uncorrected visual acuity (VA) with current spectacles, and ophthalmoscopy or fundus photography.\n"
   "   - VA better than 6/12 (20/40) and no DR → routine re-examination.\n"
   "   - VA 6/12 (20/40) or worse, or mild or moderate NPDR → non-urgent referral for refraction and assessment.\n"
   "   - Severe NPDR, DME, or PDR → urgent referral.\n"
   "*Need to optimise medical treatment: glycaemic control, hypertension, and lipids.\n"
   "DME = diabetic macular oedema; NPDR = non-proliferative diabetic retinopathy; PDR = proliferative diabetic retinopathy; VA = visual acuity.",
   ["Branch layout read from the chart; 'Current Medition' printed."]),
]
GL = CH10 + " > Glaucoma"
EY = "Instil 1 drop in the eyes"
ITEMS += [
 T("tbl-glaucoma-acute-vs-chronic", 283, GL + " > Screening and Diagnosis of Glaucoma",
   "Acute (angle-closure) vs chronic (open-angle) glaucoma: onset, pain, redness, vision, pupil, cornea, IOP, optic nerve, age, family history, urgency; who to screen", ["0810", "0811"],
   [[C("Feature"), C("Acute Glaucoma (Angle Closure)"), C("Chronic Glaucoma (Open Angle)")]],
   [r("Onset", "Sudden", "Gradual"), r("Pain", "Severe eye pain", "Usually painless"),
    r("Redness", "Present, typically unilateral", "Usually absent"),
    r("Vision Changes", "Sudden vision loss; haloes around lights", "Gradual peripheral vision loss (tunnel vision)"),
    r("Headache", "Unilateral, temporal", "Rare"), r("Nausea/Vomiting", "Common", "Rare"),
    r("Pupil", "Mid-dilated, fixed, non-reactive", "Usually normal"), r("Cornea", "Cloudy or hazy", "Clear"),
    r("Anterior Chamber", "Shallow", "Normal depth"),
    r("Intraocular Pressure (IOP)", "Markedly elevated; eye feels hard on palpation", "Elevated; eye may feel tense on palpation"),
    r("Optic Nerve", "May appear swollen in acute phase", "Shows cupping/damage on fundoscopy"),
    r("Age Group", "Usually >40 years", "Usually >40 years, earlier in Black individuals"),
    r("Family History", "Not prominent", "First-degree relatives at higher risk"),
    r("Urgency", "Ophthalmological emergency – urgent referral", "Chronic, but requires monitoring and long-term management")],
   context_before="Who must be screened (risk factors): adults ≥40 years; family history of glaucoma; high IOP; diabetes, hypertension, migraines, sickle cell anaemia; eye injuries or certain eye surgery; prolonged corticosteroid use, especially eye drops. Screening: all health workers take visual acuity with a Snellen chart and examine the external eye with a penlight torch.",
   footnotes=["Primary open-angle glaucoma has no symptoms in early stages, so routine intraocular pressure checks and fundus examination should be done in everyone aged 40 and above by qualified eye care personnel.", "All suspected cases of glaucoma should be referred to qualified eye care personnel for confirmation of diagnosis and a treatment plan."]),
 T("tbl-glaucoma-drugs", 284, GL + " > Pharmacological Management of Glaucoma",
   "Glaucoma medicines: acute glaucoma (acetazolamide, glycerol, timolol) and chronic glaucoma stepwise (timolol/betaxolol, latanoprost/bimatoprost, brimonidine, pilocarpine, acetazolamide): dose, frequency, duration", ["0814", "0815", "0816", "0817", "0818", "0819", "0821", "0822", "0823"],
   [[C("Step"), C("Medicine"), C("Dose"), C("Frequency"), C("Duration")]],
   [{"section": "Acute glaucoma (refer to ophthalmologist immediately)"},
    r("First", "Acetazolamide PO", "250-500 mg", "Once", ""),
    r("Or", "Glycerin as glycerol", "1 ml/kg", "Once", ""),
    r("Plus", "Timolol 0.25-0.5%", "Instil 1 drop", "Twice daily", "2 weeks"),
    {"section": "Chronic glaucoma"},
    r("First line", "Timolol 0.25 or 0.5% eye drops", EY, "Twice daily", "Long term"),
    r("Or", "Betaxolol 0.25 or 0.5% eye drops", EY, "Twice daily", "Long term"),
    r("If adherent with no good response, add (or first line if beta-blockers contraindicated)", "Latanoprost 0.005% eye drops", EY, "Twice daily (as printed)", "Long term"),
    r("Or", "Prostamide bimatoprost 0.03% eye drops", EY, "Twice daily (as printed)", "Long term"),
    r("If intolerant of or not responding to prostaglandin analogue", "Brimonidine 0.15-0.2% eye drops", EY, "Twice daily", "Long term"),
    r("Failure to respond (consult a specialist first)", "Pilocarpine hydrochloride 2% or 4% eye drops", EY, "Four times daily", "Review"),
    r("Severe cases or while waiting for surgery", "Acetazolamide PO", "250 mg", "Four times daily", "Review")],
   table_note="Acute glaucoma: also treat pain and nausea/vomiting. Acetazolamide contains sulphur: do not use in patients allergic to sulphur. Glycerol is a concentrated sugar solution: do not give to diabetic patients. Prostaglandin analogues may be first line when beta-blockers are contraindicated, or second line on beta-blockers if the target IOP reduction is not reached. Beta-blockers are contraindicated in overt asthma (may cause an acute asthma attack soon after instillation). Pilocarpine causes long-standing pupil constriction; use only when the patient is prepared for glaucoma surgery, or as an alternative when timolol is contraindicated.",
   pages=[284, 285],
   source_flags=["Latanoprost and bimatoprost are printed 'twice daily'; both are normally once daily (evening). Clinician to confirm.",
                 "The old chunks lost the first-line chronic glaucoma rows (timolol, betaxolol) and placed the acute glaucoma table under 'Chronic Glaucoma'."]),
]
