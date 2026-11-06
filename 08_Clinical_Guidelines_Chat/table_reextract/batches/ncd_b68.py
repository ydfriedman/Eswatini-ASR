exec(open('batches/ncd_common.py').read())
AE = CH14 + " > Management of Acute Asthma Exacerbations"; CO = CH14 + " > Chronic Obstructive Pulmonary Disease"; BR = CH14 + " > Bronchiectasis"
def r(*v): return [C(x) for x in v]
ITEMS = [
 D("fig-acute-asthma-hospital", 339, AE + " > Management of Acute Asthma Exacerbations (adults, adolescents, children 6-11)",
   "Management of acute asthma exacerbations in adults, adolescents and children 6-11 (flowchart): triage by worst feature, treatment, reassessment at 1 hour; IV salbutamol and aminophylline", ["0972", "0973"],
   "1. Initial assessment: A airway, B breathing, C circulation. Any of drowsiness, confusion, silent chest? → consult ICU, start SABA and O2, and prepare the patient for intubation.\n"
   "2. Further triage by clinical status, according to the worst feature:\n"
   "   - Mild or moderate: talks in phrases; prefers sitting to lying down; not agitated; respiratory rate increased; accessory muscles not used; pulse rate 100-120 bpm (printed '100-200'); O2 saturation (on air) 90-95%; PEF >50% predicted or best. Treat: short-acting beta agonists; O2 to maintain saturation 94-98%; oral corticosteroids.\n"
   "   - Severe: talks in words; sits hunched forwards; agitated; respiratory rate >30/min; accessory muscles being used; pulse rate >120 bpm; O2 saturation (on air) <90%; PEF <50% predicted or best. Treat: short-acting beta2 agonists; ipratropium bromide; O2 to maintain saturation 94-98%; oral or IV corticosteroids; consider IV magnesium sulfate; IV terbutaline/IV aminophylline.\n"
   "   - If continuing deterioration, treat as severe and reassess for ICU; transfer if necessary.\n"
   "3. Assess clinical progress frequently; measure lung function in all patients one hour after initial treatment:\n"
   "   - FEV1 or PEF 60-80% of predicted or personal best and symptoms improved (moderate): consider discharge.\n"
   "   - FEV1 or PEF <60% of predicted or personal best, or lack of clinical response (severe): continue treatment as above and reassess frequently.\n\n"
   "IV salbutamol can be used in severe asthma failing other treatments, mainly to prevent intubation; evidence that IV beta2-agonists shorten recovery or improve lung function is very limited. Inhaled drugs may have limited effect with near-complete obstruction and in ventilated patients. Side effects: arrhythmia, tachycardia, raised lactate and anxiety (may increase respiratory workload). Patients on IV salbutamol should be in an ICU setting.\n"
   "Most guidelines do not recommend IV aminophylline (low efficacy and safety). If used, reserve it for severe exacerbations failing maximal therapy (continuous inhaled beta2-agonists, IV corticosteroids, IV magnesium sulfate), generally in high care/ICU. Its risk-benefit balance is unfavourable.",
   ["Mild/moderate pulse rate is printed '100-200 bpm' (100-120 on p.338). IV terbutaline/aminophylline are listed in the severe treatment box although the text below says aminophylline is generally not recommended."]),
 T("tbl-copd-symptoms-signs", 341, CO + " > Symptoms and Signs",
   "COPD clinical features: chronic cough, sputum, acute bronchitis, dyspnoea, exposure history, advanced disease features, physical signs", ["0976"],
   [[C("Feature"), C("Details")]],
   [r("Chronic cough", "Persistent, intermittently or every day; often present throughout the day, seldom only nocturnal"),
    r("Chronic sputum production", "Any pattern of chronic sputum production may indicate COPD"),
    r("Acute bronchitis", "Repeated episodes, often in winter"),
    r("Dyspnoea that is", "Progressive; persistent; worse with exercise; worse during respiratory infections"),
    r("History of exposure to risk factors", "Tobacco smoke; occupational dusts and chemicals; indoor and outdoor pollution"),
    r("With advanced disease", "Fatigue; anorexia; weight loss"),
    r("Signs on physical examination", "Tachypnoea; reduced chest expansion; hyperinflated lungs; hyper-resonant percussion; use of accessory respiratory muscles and paradoxical indrawing of lower intercostal spaces (Hoover sign); cyanosis (blue bloater) – oedematous and central cyanosis; pink puffer – always breathless; elevated JVP; peripheral oedema; wheezing on forced and unforced expiration; diffusely decreased breath sounds; signs of respiratory failure; signs of cor pulmonale")],
   context_before="COPD: a slowly progressive group of disorders with airway inflammation and airflow limitation that is not fully reversible. Two types: chronic bronchitis (productive cough for at least 3 months a year for more than 2 consecutive years) and emphysema (pathological diagnosis: abnormal dilation of terminal air spaces with destruction of alveolar septa). Risk factors: smoking; indoor and outdoor air pollution; recurrent childhood respiratory infection; occupational; alpha-1 antitrypsin deficiency; genetic predisposition.",
   footnotes=["Signs may be completely absent in early stages of COPD."]),
 T("tbl-copd-bronchitis-vs-emphysema-ddx", 341, CO + " > Bronchitis vs Emphysema and Differential Diagnosis",
   "COPD: predominant bronchitis vs predominant emphysema; differential diagnosis (asthma, cardiac failure, interstitial lung disease, cystic fibrosis); asthma vs COPD", ["0978", "0979", "0980"],
   [[C("Feature"), C("Column 1"), C("Column 2")]],
   [{"section": "Predominant bronchitis vs predominant emphysema"},
    r("Age (years)", "Bronchitis: 40-45", "Emphysema: 50-75"), r("Appearance", "Bronchitis: blue bloater", "Emphysema: pink puffer"),
    r("Dyspnoea", "Bronchitis: mild; late", "Emphysema: severe; early"), r("Cough", "Bronchitis: early, copious sputum", "Emphysema: late, scanty sputum"),
    r("Infections", "Bronchitis: common", "Emphysema: occasional"), r("Cor pulmonale", "Bronchitis: common", "Emphysema: rare, terminal"),
    r("Airway resistance", "Bronchitis: increased", "Emphysema: normal or slightly increased"), r("Elastic recoil", "Bronchitis: normal", "Emphysema: low"),
    r("Chest radiograph", "Bronchitis: prominent vessels; large heart", "Emphysema: hyperinflation; small heart"),
    {"section": "Differential diagnosis of COPD: alternative diagnosis and suggestive features"},
    [C("Asthma"), C("Onset early in life; day-to-day variability; nocturnal cough and/or wheeze; family history; substantial reversibility with bronchodilator; nonsmoker", cs=2)],
    [C("Cardiac failure"), C("History of hypertension, ischaemic heart disease; elevated JVP, peripheral oedema; cardiac enlargement", cs=2)],
    [C("Interstitial lung diseases"), C("Tachypnoea, clubbing; bibasal fine inspiratory crackles; basal reticulonodular shadowing on CXR; HRCT: septal thickening, honeycombing", cs=2)],
    [C("Cystic fibrosis"), C("Family history; usually diagnosed in childhood; history of childhood chest disorder; malabsorption; finger clubbing, failure to thrive", cs=2)],
    {"section": "Asthma vs COPD"},
    r("Symptoms <35 years", "COPD: rare", "Asthma: common"), r("Smoking history", "COPD: nearly all", "Asthma: maybe"),
    r("Breathlessness", "COPD: persistent and progressive", "Asthma: variable through the day and from day to day"),
    r("Chronic productive cough", "COPD: common", "Asthma: uncommon"), r("Waking at night with cough/wheeze", "COPD: uncommon", "Asthma: common"),
    r("Response to inhaled therapy", "COPD: poor", "Asthma: good"), r("Atopy", "COPD: uncommon", "Asthma: common"),
    r("Post-bronchodilator reversibility", "COPD: not completely reversible", "Asthma: completely reversible")],
   pages=[341, 342, 343],
   source_flags=["Three separate tables in the PDF are combined here with sections. 'Blue boater' printed. The bronchitis age band '40-45' is printed as is."]),
 T("tbl-copd-severity", 343, CO + " > Diagnosis and Investigation > Severity classification",
   "COPD severity: by FEV1 % predicted (spirometry-capable facilities) or MRC dyspnoea scale (facilities without spirometry)", ["0981", "0982", "0983"],
   [[C("Grade / severity"), C("Criterion")]],
   [{"section": "By FEV1 (for spirometry-capable health facilities)"},
    r("Mild COPD", "FEV1 60-80% predicted"), r("Moderate COPD", "FEV1 40-59% predicted"), r("Severe COPD", "FEV1 <40% predicted"),
    {"section": "MRC dyspnoea scale (for facilities unable to provide spirometry): degree of breathlessness related to physical activity"},
    r("0", "Not troubled by breathlessness except on strenuous exercise"), r("1", "Short of breath when hurrying or walking up a slight hill"),
    r("2", "Walks slower than contemporaries on level ground because of breathlessness, or has to stop for breath when walking at own pace"),
    r("3", "Stops for breath after walking about 100 m or after a few minutes on level ground"), r("4", "Too breathless to leave the house, or breathless on dressing/undressing")],
   context_before="Spirometry is the gold standard for diagnosis, assessment and management of COPD. A post-bronchodilator FEV1/FVC ratio below 0.7 confirms persistent airflow limitation, suggesting COPD with relevant symptoms; FEV1 <80% predicted indicates the severity of obstruction. Measure after a bronchodilator to help distinguish from asthma. Other tests: CXR, high-resolution CT.",
   source_flags=["FEV1 ≥80% is not covered (GOLD grades: mild ≥80%, moderate 50-79%, severe 30-49%, very severe <30%); the bands here differ from GOLD."]),
 D("fig-copd-stepwise", 344, CO + " > Step-Wise Management for COPD: Pharmacological Interventions",
   "Stepwise pharmacological management of COPD: short-acting bronchodilators, combinations, long-acting bronchodilator, ICS, theophylline; asthma-COPD overlap", ["0984", "0985"],
   "Non-pharmacological: smoking cessation and/or nicotine replacement therapy.\n"
   "1. Start a short-acting bronchodilator for relief of breathlessness: beta2 agonist, e.g. salbutamol 100-200 mcg (1-2 puffs) as needed, OR anticholinergic, e.g. ipratropium 20-40 mcg 3-4 times a day.\n"
   "2. Poor symptom control → combine short-acting bronchodilators from different groups, e.g. salbutamol and ipratropium (as above).\n"
   "3. Poor symptom control → consider adding a long-acting bronchodilator (beta2 agonist or anticholinergic), e.g. salmeterol 50 mcg BD, with short-acting bronchodilator(s) as above.\n"
   "4. Poor symptom control → consider combining a long-acting bronchodilator and an inhaled corticosteroid, e.g. beclomethasone 200 mcg, with a short-acting bronchodilator. Discontinue corticosteroids after 4 weeks if no benefit.\n"
   "5. Poor symptom control → consider adding SR theophylline 250-500 mg BD; monitor plasma levels and interactions.\n\n"
   "Asthma-COPD overlap, initial treatment: predominant asthma features → inhaled corticosteroids (long-acting bronchodilators should not be used as monotherapy). Predominant COPD features → appropriate long-acting bronchodilators; consider ICS + long-acting bronchodilator combination; ICS should not be used as monotherapy for COPD."),
 T("tbl-bronchiectasis", 345, BR + " > Bronchiectasis: features and management",
   "Bronchiectasis: predisposing factors, symptoms, imaging findings, complications, differential diagnosis, and management (non-pharmacological, acute, chronic, referral)", ["0987", "0988"],
   [[C("Category"), C("Details")]],
   [r("Predisposing Factors", "Infectious: whooping cough, measles, tuberculosis. Obstructive: inhaled foreign body, bronchial carcinoma. Genetic/congenital: cystic fibrosis, Kartagener syndrome"),
    r("Symptoms", "Daily cough, worse on walking. Mild cases: yellow or green sputum only after infection. Advanced: daily profuse sputum; persistent halitosis; haemoptysis (occasional and recurrent); shortness of breath and wheezing; recurrent chest infections; fevers and/or chills"),
    r("Findings on Imaging", "Tram tracks (dilated airways), signet-ring sign, lack of bronchial tapering, cystic lesions at the lung bases in some patients. The gold standard for diagnosis is high-resolution computed tomography (HRCT)"),
    r("Complications", "Pneumonia, pleurisy, pleural effusion, pneumothorax, sinusitis, haemoptysis (>600 mL/day = life-threatening), brain abscess"),
    r("Differential Diagnosis", "Tuberculosis, asthma, COPD, interstitial fibrosis, chronic lung abscess, foreign body aspiration, cystic fibrosis, lung carcinoma"),
    {"section": "Management"},
    r("Non-pharmacologic therapy", "Postural drainage (e.g. lie head down 10–20 min ×3/day), adequate hydration, supplemental oxygen, patient education & preventive care"),
    r("Acute care", "Antibiotics guided by Gram stain; target common pathogens (H. influenzae, P. aeruginosa if unknown); bronchodilators if bronchospasm present"),
    r("Chronic therapy", "Avoid tobacco; maintain nutrition & hydration; prompt treatment of infections; vaccination (pneumococcal, influenza)"),
    r("Referral", "Consider partial lung resection for severe cases unresponsive to medical therapy")],
   context_before="Bronchiectasis: dilation of the bronchi when their walls become inflamed, thickened and irreversibly damaged, usually after obstruction followed by infection. The left lower lobe and lingula are the commonest sites of localized disease."),
 D("fig-bronchiectasis-algorithm", 346, BR + " > Diagnosis and management algorithm",
   "Bronchiectasis diagnosis and management (flowchart): chest X-ray, CT, routine and further tests, cause-specific and general management", ["0990"],
   "Risk factors, symptoms and/or signs suggestive of bronchiectasis? → request a chest X-ray.\n"
   "- Chest X-ray in keeping with bronchiectasis? Yes → bronchiectasis confirmed. No → request thin-slice CT chest or high-resolution CT.\n"
   "- CT chest in keeping with bronchiectasis? Yes → bronchiectasis confirmed. No → consider an alternative diagnosis.\n"
   "Once confirmed:\n"
   "- Routine tests: FBC, U&E and creatinine, LFTs, glucose, HIV, sputum MCS and TB culture, Aspergillus IgE, sweat chloride.\n"
   "- Further tests guided by history and examination: IgG, IgM, IgA, IgG subclasses, total IgE, sweat conductivity, nasal or bronchial mucosa biopsy.\n"
   "- If an underlying cause is identified, treat it specifically.\n"
   "- General management: airway clearance techniques; vaccination (influenza, pneumococcal, SARS-CoV-2); antibiotics; other: nutrition, diuretics, lung transplant.",
   ["'Asperillus', 'or conductivity' printed."]),
]
