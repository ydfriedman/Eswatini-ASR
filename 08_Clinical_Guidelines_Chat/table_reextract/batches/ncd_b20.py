exec(open('batches/ncd_common.py').read())
ITEMS = [
 B("box-alcohol-key-messages", 23, CH1 + " > Alcohol Use > Key messages for patients",
   "Key messages for patients about alcohol", ["0051"],
   "- NO amount of alcohol is safe for your health.\n- The safest choice is NOT to drink alcohol at all.\n- Alcohol increases your risk of cancer, heart disease, liver disease, and many other conditions.\n- Quitting alcohol improves your health at any age.\n- You don't have to quit alone: ask for help from healthcare providers, family, and support groups.\n- If you are pregnant or planning pregnancy, do NOT drink any alcohol."),
 T("tbl-healthy-eating-guidelines", 24, CH1 + " > Unhealthy Diet > Healthy eating guidelines",
   "Healthy eating guidelines: food groups, foods to limit, counselling tips and health benefits", ["0053", "0054", "0055"],
   [[C("Food group"), C("Advice"), C("Details / examples")]],
   [{"section": "Eat a variety of foods daily for good health"},
    [C("Vegetables & fruits"), C("Eat PLENTY daily"), C("At least 5 portions (400 g) per day. Examples: spinach, cabbage, tomatoes, carrots, pumpkin, oranges, bananas, mangoes")],
    [C("Starchy foods"), C("Part of MOST meals"), C("Choose WHOLE GRAINS. Examples: whole grain pap/maize meal, brown bread, rice, potatoes, sweet potatoes")],
    [C("Protein foods"), C("Eat DAILY"), C("Choose lean options. Examples: beans, lentils, peanuts, fish, chicken, lean meat, eggs")],
    [C("Milk & dairy"), C("Have EVERY DAY"), C("Good for bones & teeth. Examples: milk, maas, yoghurt, cheese")],
    [C("Clean water"), C("Drink LOTS daily"), C("6-8 glasses per day; best choice for hydration")],
    [C("Fats & oils"), C("Use SPARINGLY"), C("Choose vegetable oils; avoid hard fats & excessive frying")],
    {"section": "Foods to limit"},
    [C("Salt"), C("Less than 1 teaspoon (5 g) per day"), C("Reduces blood pressure & heart disease")],
    [C("Sugar"), C("Less than 6 teaspoons (25 g) per day"), C("Reduces blood pressure & heart disease")],
    [C("Processed foods"), C("Limit chips, soda, sweets, fast food"), C("High in salt, sugar & unhealthy fats")]],
   table_note="Counselling tips: fill half the plate with vegetables; eat locally available seasonal foods; choose whole grains over refined; eat beans/legumes regularly; remove visible fat from meat. Health benefits: prevents heart disease & stroke; reduces diabetes risk; helps maintain a healthy weight; prevents some cancers; improves overall wellbeing.",
   source_flags=["Infographic in the PDF; restructured as a table.", "The 'Clean water' panel is sub-headed 'Starchy foods' in the PDF (copy error); omitted."]),
 D("fig-hypertension-screening", 26, CH1 + " > Routine Health Examinations > Hypertension > Algorithm for hypertension screening",
   "Algorithm for hypertension screening in adults (18 years and above)", ["0058", "0059", "0060"],
   "Adults (18 years and above), by office blood pressure:\n"
   "- Optimal <120/80: repeat at least every 5 years.\n"
   "- Normal 120-129/80-84: repeat at least every 3 years.\n"
   "- High normal BP 130-139/85-89: consider masked hypertension; repeat annually. Consider out-of-office measurements (ABPM or HBPM).\n"
   "- Hypertension >140/90: repeated visits for office BP measurement, and consider out-of-office measurements (ABPM or HBPM).\n\n"
   "Adopted from ESC/ESH guidelines, 2023.\n"
   "N.B.: the Ministry of Health recommends measuring blood pressure yearly for adults ≥18 years of age.",
   ["These ESC/ESH categories differ from the blood pressure screening table on p.13 (ACC/AHA style: stage 1 from 130/80).",
    "'>140/90' printed; hypertension is ≥140/90 elsewhere in the guideline."]),
 T("tbl-anthropometric-bmi-waist", 27, CH1 + " > Routine Health Examinations > Obesity > Anthropometric measurements",
   "Anthropometric measurements in adults (≥18 years): BMI, obesity class and disease risk by waist circumference", ["0061", "0062"],
   [[C("Category", rs=2), C("BMI (kg/m2)", rs=2), C("Obesity class", rs=2), C("Disease risk* (relative to normal weight and waist circumference)", cs=2)],
    [C("Men ≤ 102 cm and women ≤ 88 cm"), C("Men ≥ 102 cm and women ≥ 88 cm")]],
   [[C("Underweight"), C("<18.5"), C(""), C("-"), C("")],
    [C("Normal*"), C("18.5-24.9"), C(""), C("-"), C("")],
    [C("Overweight"), C("25-29.9"), C(""), C("Increased"), C("High")],
    [C("Obesity", rs=3), C("30-34.9"), C("Class 1"), C("High"), C("Very high")],
    [C("35-39.9"), C("Class 2"), C("Very high"), C("Very high")],
    [C("≥ 40"), C("Class 3"), C("Extremely high"), C("Extremely high")]],
   context_before="Overweight and obesity are abnormal or excessive fat accumulation that presents a risk to health. In adults, a BMI over 25 is overweight and over 30 is obese. BMI = body mass (kg) divided by the square of body height (m).",
   footnotes=["*Disease risk for hypertension, type 2 diabetes, and cardiovascular diseases.", "*Increased waist circumference can also be a marker for increased risk even in persons of normal weight."],
   source_flags=["The left disease-risk sub-column has no heading in the PDF; 'Men ≤ 102 cm and women ≤ 88 cm' is inferred from the right one."]),
]
