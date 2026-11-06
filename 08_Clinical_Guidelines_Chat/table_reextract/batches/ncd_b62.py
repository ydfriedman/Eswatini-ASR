exec(open('batches/ncd_common.py').read())
DF = CH12 + " > Diabetic Foot"; PN = CH12 + " > Peripheral Neuropathy"
def r(*v): return [C(x) for x in v]
SNRI_N = "Side effects: nausea, vomiting, dry mouth, constipation, decreased appetite, insomnia, dizziness, somnolence, blurred vision, increased sweating and fatigue. Advise taking with food to reduce nausea"
ITEMS = [
 T("tbl-peripheral-neuropathy-types", 304, PN + " > Guide to Clinical diagnosis of Peripheral Neuropathies",
   "Peripheral neuropathy types: distal symmetric polyneuropathy, mononeuropathy, mononeuropathy multiplex, hereditary neuropathies: clinical features and common causes", ["0874"],
   [[C("Type"), C("Clinical Features"), C("Common causes")]],
   [r("Distal Symmetric Polyneuropathy", "Length-dependent: diffuse involvement affects distal segments first; symptoms occur below the knees before affecting the fingertips", "Most common cause: diabetes. Chronic idiopathic axonal polyneuropathy, alcohol, chemotherapy induced"),
    r("Mononeuropathy", "Symptoms restricted to the distribution of a single nerve, myotome, or dermatome; asymmetric reflexes", "Entrapment neuropathies, e.g. carpal tunnel, peroneal nerve entrapment; post-traumatic neuropathies; diabetes"),
    r("Mononeuropathy multiplex", "Occurrence of several concurrent mononeuropathies", "Autoimmune vasculitis etiologies"),
    r("Hereditary neuropathies", "Distal calf atrophy, hammertoes, pes cavus; motor deficits ≥ sensory deficits; diffuse areflexia", "Genetic diseases")],
   context_before="Peripheral neuropathies are disorders of peripheral nerve cells and fibres affecting motor, sensory and autonomic fibres; classified as mononeuropathies, multifocal neuropathies and polyneuropathies, and as axonal, demyelinating or mixed."),
 D("fig-painful-diabetic-neuropathy", 305, PN + " > Treatment of Neuropathic Pain in Diabetic Foot",
   "Treatment of painful diabetic neuropathy (flowchart): first-line anticonvulsants or antidepressants, second-line SNRIs, opioid-like drugs, topicals, third-line SSRIs and opioids", ["0876", "0877"],
   "Patient presenting with painful neuropathy → rule out other causes of neuropathy → establish treatment goals → optimise glycaemic control.\n"
   "- First-line therapy: anticonvulsants (pregabalin, gabapentin) or antidepressants (TCAs and SNRIs: amitriptyline, duloxetine).\n"
   "- Second-line therapy: SNRIs (venlafaxine or desvenlafaxine); opioid-like drugs (tramadol or tapentadol ER); topical treatments (lidocaine 5% patch or capsaicin 0.075% cream).\n"
   "- Third-line therapy: SSRIs (citalopram or paroxetine or escitalopram); opioids (oxycodone controlled release).\n"
   "ER = extended release; SNRI = serotonin-norepinephrine reuptake inhibitor; SSRI = selective serotonin reuptake inhibitor; TCA = tricyclic antidepressant. Adapted from Snyder MJ, Gibbs LM, Lindsay TJ. Treating Painful Diabetic Peripheral Neuropathy: An Update. Am Fam Physician. 2016;94(3):227-34.",
   ["'Capsaisin' printed. 'or Escitalopram' is printed under the opioids column; read as a third SSRI option."]),
 T("tbl-neuropathic-pain-drugs", 306, PN + " > Medicines for painful diabetic neuropathy: doses",
   "Medicines for painful diabetic neuropathy: SNRIs, opioid-like drugs, topicals, anticonvulsants, amitriptyline: doses, maximum doses and cautions", ["0878", "0879"],
   [[C("Medicine"), C("Usual dose"), C("Maximum dose"), C("Notes")]],
   [{"section": "Serotonin-norepinephrine reuptake inhibitors"},
    [C("Duloxetine"), C("60 mg daily or divided twice daily"), C("120 mg daily or divided twice daily"), C(SNRI_N, rs=3)],
    r("Venlafaxine", "150 mg daily", "225 mg daily"), r("Desvenlafaxine", "200 mg daily", "400 mg daily"),
    {"section": "Opioid-like medications"},
    [C("Tramadol"), C("50 mg every 4 to 6 hours"), C("100 mg every 6 hours; maximum 400 mg daily"), C("Lowers seizure threshold; avoid in epilepsy or at risk of seizures", rs=2)],
    r("Tapentadol ER", "100 mg twice daily", "250 mg twice daily"),
    {"section": "Topical medications"},
    r("Lidocaine 5% patch", "1 patch daily", "3 patches daily", ""), r("Capsaicin 0.075% cream", "Four times daily", "NA", ""),
    r("Isosorbide dinitrate spray", "30 mg at bedtime applied to the bottom of the feet", "NA", ""),
    {"section": "Anticonvulsants"},
    r("Pregabalin", "300 mg divided twice daily", "600 mg divided twice daily", "Side effects: dizziness, sedation, GI symptoms and mild peripheral oedema. Use cautiously in heart failure and with thiazolidinediones (cases of decompensated heart failure reported); renal insufficiency (creatinine clearance ≤30 ml/min/1.73 m2) requires dose adjustment"),
    r("Gabapentin", "1,200 mg divided three times daily", "3,600 mg divided three times daily", "Side effects: dizziness, sedation, GI symptoms and mild peripheral oedema. Dose adjustment recommended in renal impairment"),
    {"section": "Tricyclic antidepressant"},
    r("Amitriptyline", "25 mg daily at bedtime", "150 mg daily at bedtime or divided twice daily", "Side effects: dry mouth, sedation, disturbed vision, arrhythmia, palpitations, postural hypotension, urinary retention and constipation. Contraindicated in cardiovascular disease (unstable angina, recent MI, heart failure, abnormal cardiac conduction) and glaucoma. Caution in elderly patients")],
   source_flags=["The table has no column headers in the PDF; the dose columns are read as usual and maximum dose.", "Amitriptyline is listed under a second 'Anticonvulsants' heading in the PDF; it is a tricyclic antidepressant.",
                 "Gabapentin 'usual' 1,200 mg/day and amitriptyline max 150 mg differ from the palliative adjuvant table on p.293 (gabapentin max 2,400 mg/day; amitriptyline 10-75 mg)."]),
]
