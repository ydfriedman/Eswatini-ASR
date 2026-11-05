exec(open('batches/ncd_common.py').read())
AD = CH4 + " > Atopic Dermatitis (Eczema)"
E = C("")
ITEMS = [
 T("tbl-ad-stages", 151, AD + " > Classification and Characteristics of AD",
   "Atopic dermatitis (eczema) stages and key characteristics: acute, subacute, chronic", ["0411"],
   [[C("Stage"), C("Key Characteristics")]],
   [[C("Acute Eczema"), C("- Intensely pruritic (itchy)<br/>- Erythematous papules and vesicles<br/>- Exudation and crusting")],
    [C("Subacute Eczema"), C("- Features overlap between acute and chronic stages<br/>- Lesions are slightly elevated, red, brownish, or purplish<br/>- Variable scaling")],
    [C("Chronic Eczema"), C("- Dry, scaly, or excoriated papules/plaques<br/>- Skin thickening from chronic scratching<br/>- May lead to fissuring and lichenification")]],
   context_before="Atopic dermatitis is a chronic, pruritic inflammatory skin condition that occurs most frequently in children but may also affect adults, with a relapsing course. Dry skin and severe pruritus are cardinal signs of AD."),
 T("tbl-ad-age-groups", 151, AD + " > Symptoms in the different Age Groups",
   "Atopic dermatitis symptoms and sites by age group (infants, older children and adolescents, adults)", ["0412"],
   [[C("Age Group"), C("Typical Symptoms"), C("Common Sites / Distribution"), C("Additional Notes")]],
   [[C("Infants & Young Children (0–2 years)"), C("Pruritic, red, scaly, crusted lesions"), C("Extensor surfaces, cheeks, scalp; may be diffuse"), C("Diaper area usually spared")],
    [C("Older Children & Adolescents"), C("Lichenified plaques"), C("Flexural areas: antecubital & popliteal fossae, volar wrist, ankles, neck"), C("Chronic scratching can lead to thickened skin")],
    [C("Adults"), C("Localized, lichenified lesions"), C("Mainly skin flexures"), C("Lesions more persistent; may be less widespread")]],
   pages=[151, 152], source_flags=["Table continues onto p.152 with the header repeated."]),
 T("tbl-ad-patient-assessment", 152, AD + " > Patient Assessment",
   "Atopic dermatitis patient assessment: history, examination, laboratory and other investigations at the initial visit, 3-6 monthly and annually", ["0414", "0415", "0416", "0417"],
   [[C("Component"), C("Initial visit"), C("3-6 monthly visit"), C("Annually")]],
   [{"section": "Patient History"},
    [C("History"), C("Pruritus, dry skin, dermatitis affecting specific areas which are age dependent (as above). Chronic and relapsing history. Personal or family history of atopy. History of triggers e.g. emotional factors and environmental factors, food, and skin irritants"), C("Skin assessment and follow up"), C("Skin assessment and follow up")],
    [C("Risk factor assessment"), C("Assess for triggers through history taking"), E, E],
    [C("Other relevant medical history"), C("History of atopy and food allergies"), E, E],
    [C("Symptoms/signs of drugs"), C("Current medication being used and their effects"), E, E],
    [C("Lifestyle"), C("Skin care. Avoidance of triggers"), E, E],
    [C("Psychosocial"), C("Psychotherapy recommendation"), E, E],
    {"section": "Physical Examination"},
    [C("Integument and appendages"), C("Complete skin exam"), C("Complete skin exam"), C("Complete skin exam")],
    {"section": "Laboratory Investigations"},
    [C("Serum"), C("IgE"), E, E],
    [C("Further testing for secondary dermatological conditions if suspected"), C("Skin biopsy, skin scrapings for KOH"), E, E],
    {"section": "Radiological & Other Investigations"},
    [C("Dermatoscopy (initial visit, thereafter as needed)"), C("X"), E, E],
    [C("Other Tests"), C("MC&S if secondary infection is suspected"), E, E],
    {"section": "Other Assessments"},
    [C("Lifestyle management"), C("Patient literacy on how to avoid triggers and exacerbators"), E, E],
    [C("Preconception counselling and family planning"), C("N/A"), E, E],
    [C("Medication review and adjustment"), C("Review of medications the patient is currently on"), C("Review of medications the patient is currently on"), C("Review of medications the patient is currently on")]],
   pages=[152, 153, 154], source_flags=["Table continues onto pp.153-154 with the header repeated for each section."]),
]

ITEMS += [
 D("fig-ad-management-summary", 155, AD + " > Summary of Patient Management",
   "Atopic dermatitis (eczema): summary of patient management by severity (flowchart: mild vs moderate/severe, flare treatment, follow-up, hospitalisation)", ["0421"],
   "1. Assess disease history, extent and severity, and the impact on the patient's and family's quality of life.\n"
   "2. Educate the patient and carer about eczema care, trigger avoidance, and recognising and responding to eczema flares and infections.\n"
   "3. Mild eczema: follow the eczema management plan: 1. daily bathing; 2. moisturiser applied top to toe at least twice per day; 3. trigger avoidance advice. Follow up within two weeks.\n"
   "   - Improved: support optimal care at home, e.g. consider referral to community-based services.\n"
   "   - Not improved: manage as moderate or severe eczema (step 4).\n"
   "4. Moderate or severe eczema: assess for skin infections and compliance with correct eczema treatments.\n"
   "   - Unwell or febrile: consider hospitalisation and/or IV antimicrobials.\n"
   "   - Well: commence eczema flare treatment: increase moisturiser use to at least four times daily; eczema baths; topical steroids; wet dressings and compresses; commence oral antimicrobials if appropriate. Follow up within one week.\n"
   "     - Improved: support optimal care at home.\n"
   "     - Not improved: consider hospitalisation and/or IV antimicrobials.",
   ["The branch to flare treatment is labelled 'Well or febrile' in the PDF, while the other branch is 'Unwell or febrile'; read as 'Well'. 'Moisturisese', 'atleast' printed."]),
]
