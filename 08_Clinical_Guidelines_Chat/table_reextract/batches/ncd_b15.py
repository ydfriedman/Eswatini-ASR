exec(open('batches/ncd_common.py').read())
TH = CH2 + " > Thyroid Disorders"
ITEMS = [
 T("tbl-hypothyroidism-symptoms", 72, TH + " > Hypothyroidism > Diagnostic criteria",
   "Hypothyroidism symptoms by system affected (diagnostic criteria)", ["0197"],
   [[C("System affected"), C("Common symptoms")]],
   [[C("General & metabolic"), C("Fatigue; weight gain; trouble tolerating cold; slowed heart rate; increased cholesterol levels")],
    [C("Skin, hair & nails"), C("Dry, rough skin; dry or thinning hair; hair loss")],
    [C("Musculoskeletal"), C("Joint pain; muscle pain or weakness")],
    [C("Reproductive (female)"), C("Heavy or irregular menstrual periods; fertility problems")],
    [C("Neurological & psychological"), C("Depression; memory loss")],
    [C("Gastrointestinal & voice"), C("Constipation; hoarse voice")]],
   context_before="The symptoms of hypothyroidism depend on the deficiency of thyroid hormone, but can include the following. Investigations: thyroid hormone profile. Diagnosis: may be primary or secondary hypothyroidism.",
   source_flags=["In chunks_v2 this table was labelled under Hyperthyroidism; it is the hypothyroidism symptom table."]),
 T("tbl-congenital-hypothyroidism-features", 75, TH + " > Congenital Hypothyroidism > Clinical features",
   "Congenital hypothyroidism: clinical features by category", ["0204"],
   [[C("Category"), C("Features")]],
   [[C("General"), C("Lethargy, somnolence, delayed physical and mental development, subnormal temperature")],
    [C("Skin/hair"), C("Dry skin, coarse and scanty hair")],
    [C("Facial/head"), C("Wide open fontanelles, enlarged tongue (macroglossia), periorbital oedema, coarse cry, hoarse voice, goitre")],
    [C("Growth/development"), C("Delayed dentition, short and thick neck, broad hands, hypotonia")],
    [C("Cardiovascular"), C("Bradycardia")], [C("Abdomen"), C("Abdominal distension, umbilical hernia, constipation")],
    [C("Extremities"), C("Oedema of extremities and genitals")], [C("Haematologic"), C("Anaemia")],
    [C("Respiratory"), C("Apnoeic episodes")], [C("Feeding"), C("Feeding difficulties")], [C("Other"), C("Prolonged unconjugated hyperbilirubinaemia")]]),
 T("tbl-levothyroxine-dose-children", 76, TH + " > Hypothyroidism in Older Children and Adolescents > Pharmacological treatment",
   "Levothyroxine dose by age for hypothyroidism in children and adolescents (oral, once daily on an empty stomach)", ["0209"],
   [[C("Age group"), C("Levothyroxine dose")]],
   [[C("1-6 months"), C("8-10 mcg/kg")], [C("6-12 months"), C("6-8 mcg/kg")], [C("1-5 years"), C("5-6 mcg/kg")], [C("6-12 years"), C("4-5 mcg/kg")], [C(">12 years"), C("2-3 mcg/kg")]],
   context_before="Hypothyroidism in older children and adolescents: low growth velocity or short stature with short limbs and a normal or elevated BMI; subtle features include cold intolerance, dry skin, brittle hair, pallor and myxoedema. Investigations: elevated TSH and low thyroxine. Levothyroxine, oral, once daily on an empty stomach. Refer all cases for investigation and initiation of therapy. (Neonates with congenital hypothyroidism: levothyroxine 10-15 mcg/kg once daily, started ideally within the first three weeks of life.)"),
 D("fig-primary-hyperthyroidism-diagnosis", 78, TH + " > Hyperthyroidism > Diagnostic algorithm for primary hyperthyroidism",
   "Diagnostic algorithm for primary hyperthyroidism (by radioactive iodine uptake)", ["0213", "0214"],
   "Primary hyperthyroidism: ↓ TSH, ↑ free T4, ↑ total T3. Next: radioactive iodine uptake (RAIU).\n"
   "- Diffuse uptake: homogeneous: Graves' disease; heterogeneous: toxic multinodular goitre.\n"
   "- Focal uptake: functioning adenoma.\n"
   "- No uptake: measure serum thyroglobulin: low (↓): thyrotoxicosis factitia; high (↑): thyroiditis, iodine load, or struma ovarii."),
]
