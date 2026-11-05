exec(open('batches/ncd_common.py').read())
LD = CH5 + " > Chronic Liver Disease"
ITEMS = [
 B("box-cirrhosis-symptoms-findings", 163, LD + " > Clinical Presentation > Symptoms and physical findings of liver cirrhosis",
   "Symptoms and physical findings of liver cirrhosis (with illustration of signs)", ["0442", "0443"],
   "Symptoms of liver cirrhosis: general malaise, fatigue; anorexia/weight loss; feeling of an enlarged abdomen; swollen abdomen/legs; nose bleeds/bleeding from lower limbs; jaundice/itch; hand tremors.\n\n"
   "Physical findings: skin pigmentation; xanthoma; spider angioma; palmar erythema; finger clubbing (hepatopulmonary syndrome); caput medusae; gynecomastia; fever; hepatocellular carcinoma ('Hepatoceleoma' as printed); hepatic halitosis (dimethylsulphide, ketones in the expired breath); jaundice; ascites, lower limb oedema; hepatic encephalopathy; bleeding plaques/purpura.\n\n"
   "An illustration shows: xanthoma, jaundice, spider angioma, paper-money skin, gynecomastia, hepatomegaly/hepatic atrophy, caput medusae, ascites, palmar erythema, oedema, finger clubbing, white nails, bloody spots.",
   ["'Hepatoceleoma', 'Pancrease', 'crythema', 'lower thigh edema' printed in the box and illustration."]),
 T("tbl-cld-investigations", 163, LD + " > Investigations",
   "Investigations in chronic liver disease and their purpose (LFTs, INR, CBC, viral hepatitis screen, renal function, ultrasound, elastography, endoscopy, Child-Pugh)", ["0444"],
   [[C("Investigation"), C("Purpose")]],
   [[C("Liver function tests (AST, ALT, ALP, GGT, bilirubin, albumin)"), C("Assess hepatocellular injury, cholestasis, and synthetic function")],
    [C("Coagulation Profile (INR)"), C("Evaluate liver synthetic function and risk of bleeding")],
    [C("Complete blood count"), C("Detect anaemia, leukopenia, or thrombocytopenia")],
    [C("Viral hepatitis screen (HBsAg, HCV Ab)"), C("Identify viral causes of chronic liver disease")],
    [C("Renal function (Creatinine, BUN)"), C("Assess kidney function, important in advanced liver disease")],
    [C("Abdominal Ultrasound"), C("Evaluate liver size, texture, ascites, and portal hypertension")],
    [C("Elastography (FibroScan)"), C("Assess degree of liver fibrosis / non-invasively stage disease")],
    [C("Upper GI endoscopy"), C("Detect and manage oesophageal or gastric varices")],
    [C("Child-Pugh Score (A, B, C)"), C("Assess severity of cirrhosis and prognosis")]]),
 T("tbl-child-pugh", 163, LD + " > Child-Pugh Staging",
   "Child-Pugh staging of cirrhosis: points for bilirubin, albumin, prothrombin time/INR, ascites and encephalopathy; class A/B/C and prognosis", ["0445", "0446"],
   [[C("Parameter"), C("1 Point"), C("2 Points"), C("3 Points")]],
   [[C("Total bilirubin, μmol/L (mg/dL)"), C("<34 (<2)"), C("34–50 (2–3)"), C(">50 (>3)")],
    [C("Serum albumin (g/L)"), C(">35"), C("28–35"), C("<28")],
    [C("Prothrombin time prolongation (sec) or INR"), C("<4 sec or INR <1.7"), C("4–6 sec or INR 1.7–2.3"), C(">6 sec or INR >2.3")],
    [C("Ascites"), C("None"), C("Mild (controlled)"), C("Moderate to severe (poorly controlled)")],
    [C("Hepatic encephalopathy"), C("None"), C("Grade I–II (mild/moderate)"), C("Grade III–IV (severe)")],
    {"section": "Child-Pugh class (total points) and prognosis"},
    [C("Class A"), C("5–6 points"), C("Well-compensated disease", cs=2)],
    [C("Class B"), C("7–9 points"), C("Significant functional compromise", cs=2)],
    [C("Class C"), C("10–15 points"), C("Decompensated disease, poor prognosis", cs=2)]],
   pages=[163, 164], source_flags=["The class table is a separate small table on p.164; added here as a section."]),
 T("tbl-cld-diagnosis-classification", 164, LD + " > Diagnosis & Classification",
   "Chronic liver disease vs compensated and decompensated cirrhosis: key features, diagnostics and Child-Pugh classification", ["0447"],
   [[C("Condition"), C("Key Features"), C("Diagnostics"), C("Classification/Stage")]],
   [[C("CLD"), C("Chronic liver injury, mild symptoms"), C("LFTs, US, Fibroscan"), C("Early vs advanced fibrosis")],
    [C("Compensated Cirrhosis"), C("Few symptoms, labs may be abnormal"), C("LFTs, US, Fibroscan, Endoscopy"), C("Child-Pugh A")],
    [C("Decompensated Cirrhosis"), C("Ascites, variceal bleed, encephalopathy"), C("Labs + imaging + endoscopy"), C("Child-Pugh B/C")]]),
]
LM = CH5 + " > Diagnosis and Management of Chronic Liver Disease"
ITEMS += [
 T("tbl-cld-complications", 164, LM + " > Management of Complications",
   "Management of complications of chronic liver disease: ascites, variceal bleeding, infections (spontaneous bacterial peritonitis)", ["0449"],
   [[C("Complication"), C("Management")]],
   [[C("Ascites"), C("- Sodium restriction: <2 g/day<br/>- Diuretics: Spironolactone ± Furosemide<br/>- Large-volume paracentesis for tense ascites<br/>- Monitor electrolytes and renal function")],
    [C("Variceal Bleeding"), C("- Resuscitation: IV fluids, blood products<br/>- IV antibiotic prophylaxis (e.g., Ceftriaxone)<br/>- Endoscopic variceal ligation<br/>- Non-selective beta-blockers for prophylaxis")],
    [C("Infections"), C("- Spontaneous bacterial peritonitis (SBP): Ceftriaxone IV<br/>- Early recognition vital<br/>- Monitor for other infections (UTI, pneumonia, skin infections)")]],
   pages=[164, 165], context_before="General management: avoid alcohol and hepatotoxic drugs; vaccinations (hepatitis A, B, influenza, pneumococcal); nutrition with adequate protein, low sodium if ascites. Monitor liver function, coagulation and renal function; screen for HCC with ultrasound ± AFP every 6 months in cirrhosis; variceal surveillance.",
   source_flags=["Table continues onto p.165 (infections row)."]),
 D("fig-hepatic-encephalopathy-west-haven", 165, LM + " > Hepatic Encephalopathy Grading (West Haven)",
   "Hepatic encephalopathy: West Haven grading (unimpaired, grade 0-1 minimal/covert, grades 2-4) and management", ["0450", "0451", "0452"],
   "West Haven grading, as summarised in the text:\n"
   "- Grade 0: minimal, normal exam. Grade 1: mild confusion, sleep disturbance. Grade 2: lethargy, disorientation. Grade 3: somnolent but arousable. Grade 4: coma.\n\n"
   "West Haven grading chart (beside the text):\n"
   "- Unimpaired: 1. no signs or symptoms; 2. normal psychometric or neuropsychological tests.\n"
   "- Grade 0-1: 1. also known as minimal or covert hepatic encephalopathy; 2. no overt clinical symptoms to mild decrease in attention span, awareness, altered sleep rhythm; 3. abnormal psychometric or neuropsychological tests.\n"
   "- Grade 2: 1. obvious personality change, inappropriate behaviour, asterixis, dyspraxia, disoriented, lethargy; 2. objectively disoriented to time.\n"
   "- Grade 3: 1. somnolence, gross disorientation, bizarre behaviour; 2. objectively disoriented to time and space.\n"
   "- Grade 4: 1. coma.\n\n"
   "Management: identify and treat precipitating factors (infection, GI bleed, constipation, drugs); lactulose orally or rectally (goal: 2-3 soft stools/day); rifaximin if recurrent; supportive care (hydration, nutrition).\n"
   "Monitoring: mental status, electrolytes, renal function.",
   ["The text list (grade 0 'minimal, normal exam'; grade 1 'mild confusion') and the chart (grade 0-1 combined as minimal/covert HE) grade the lower levels differently. 'cover hepatic encephalopathy', 'dyspraxis' printed."]),
 T("tbl-cld-drugs", 165, LM + " > Pharmacological Treatment Table for CLD",
   "Drugs for chronic liver disease: lactulose, rifaximin, spironolactone, furosemide, propranolol: indication, dose and monitoring", ["0453"],
   [[C("Drug/Class"), C("Indication"), C("Dose/Notes"), C("Monitoring")]],
   [[C("Lactulose"), C("HE"), C("20–30 mL PO TID"), C("Stool frequency, electrolytes")],
    [C("Rifaximin"), C("Recurrent HE"), C("550 mg PO BID"), C("Liver function")],
    [C("Spironolactone"), C("Ascites"), C("100 mg PO daily, titrate"), C("K+, renal function")],
    [C("Furosemide"), C("Ascites"), C("40 mg PO daily, titrate"), C("K+, renal function")],
    [C("NSBB (Propranolol)"), C("Varices prophylaxis"), C("20–40 mg BID, titrate"), C("HR, BP")]],
),
]
