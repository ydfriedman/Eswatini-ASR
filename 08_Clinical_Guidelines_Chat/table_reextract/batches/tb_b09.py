exec(open('batches/tb_common.py').read())
# Repairs from the completeness audit (audit/REPAIR_WORKLIST.md): cell text that the old parse had split off into
# separate text chunks is put back into its cell (from the PDF's ruled grid, grid_repair.py, checked against the
# page images), and the text chunk is absorbed into the table item. Loaded after tb_b08.
import copy as _c, json as _j
_prev = {t['table_id']: t for t in _j.load(open('tb-2025_tables.json'))['tables']}


def P(tid, cells=None, absorb=(), **kw):
    """Copy the current item, replace cells {'b:row:col' or 'h:row:col': text}, absorb text chunks."""
    d = _c.deepcopy(_prev['tb-2025-' + tid])
    for key, txt in (cells or {}).items():
        part, ri, ci = key.split(':')
        d['header' if part == 'h' else 'body'][int(ri)][int(ci)]['t'] = txt
    d['replaces_chunks'] = d['replaces_chunks'] + [c for c in absorb if c not in d['replaces_chunks']]
    d.update(kw)
    return d


_ns = {}
exec(open('batches/tb_b03.py').read(), _ns)  # the original fused Table 20/21/22 item, so this batch gives the same result on re-runs
_t20 = next(t for t in _ns['ITEMS'] if t['table_id'] == 'tb-2025-tbl-p112-0274')
ITEMS = [
 # Table 1: three screening-strategy bullets were in text chunk 0022
 P("tbl-p23-0021", {"b:0:1": "New screening tool: CXR and CAD use both in health facilities and community, CRP for PLHIV, revised symptom screening tool to increase presumption index on lung cancer<br/>Approaches: Bidirectional screening of TB and COVID, Integrated Screening in the Community<br/>Strategies to ensure optimal screening coverage:<br/>• Checking the copy of the screening tool that is given out to the client (recording in the CMIS) by the screening officer/any community cadre by the attending clinicians.<br/>• Using a stamp strategy (i.e. giving a stamped slip to the client and checking by attending clinicians if screening is done or not)<br/>• Repeated screening at the multi-service delivery points<br/>• Cascade analysis and continuous quality improvement using the data of screening activities"},
   absorb=["tb-2025-0022"]),
 # Table 11: second diagnosis bullet of LN, pleural and TBM rows were in text chunk 0182
 P("tbl-p80-0181", {
   "b:0:2": "• Fine needle aspiration of the LN and send the specimen for Xpert MTB/RIF Ultra® and Xpert MTB/XDR testing and culture/DST, and tNGS where applicable.<br/>• If the aspirate is dry then an LN biopsy should be taken, sending the material for histological examination.",
   "b:1:2": "• By therapeutic/diagnostic tap and sending the fluid for Xpert MTB/RIF Ultra® and Xpert MTB/XDR testing and culture / DST and tNGS where applicable.<br/>• If the patient has empyema, he must be admitted; the empyema drained and the material for Xpert MTB/RIF Ultra® testing, culture/DST, and tNGS where applicable.",
   "b:2:2": "• Lumbar puncture for CSF examination: increased lymphocytes, increased proteins and decreased glucose.<br/>• CSF should be sent for Xpert MTB/RIF Ultra®, and Xpert MTB/XDR testing and culture/DST.<br/>• If the patient is HIV+, CSF should also be sent for CrAg and India ink staining."},
   absorb=["tb-2025-0182"]),
 # Table 32: the Sputum Induction cell was empty; its bullets were in text chunk 0355
 P("tbl-p142-0356", {"b:0:1": "• Can be performed at any age<br/>• Collection of sputa after the child inhales 3-5% hypertonic saline (induction improves the yield of sputa collection for all ages)<br/>• The child should not have eaten for 2 hours before the procedure and pretreated with salbutamol<br/>• Nasopharyngeal suctioning can be performed following the procedure if the child is unable to expectorate<br/>• Can be performed at any time but morning is preferred<br/>• 5 ml is recommended for Gene Xpert and Culture<br/>• Do not perform in children with respiratory distress or wheeze<br/>• A nebulizer and mask must be sterilized after each use"},
   absorb=["tb-2025-0355"]),
 # Tables 20, 21 and 22 had been joined into one item with Table 20's rows shifted; split and Table 20 re-done from the images (pp.112-113)
 T("tbl-p112-0274", 112, _t20['heading_path'], "Table 20: Assessment of post-TB lungs disease and indication for pulmonary resuscitation",
   [c[len('tb-2025-'):] for c in _t20['replaces_chunks']] + ["0275"],
   [r("Assessment Parameter", "Examination", "Indication for Pulmonary Rehabilitation")],
   [[C("Clinical Assessment", rs=2),
     C("Respiratory focused history taking:<br/>• Pulmonary disease: asthma including childhood asthma, bronchiectasis, COPD and previous TB treatment history, frequent respiratory tract infection during childhood, COVID-19<br/>• Vaccination history: COVID-19, Influenza, Pneumococcal<br/>• Comorbidity: HIV, Diabetes<br/>• Health hazardous exposure: smoking, biomass fuel, silica dust<br/>• History of hospitalization for chronic repository disease"),
     C("• Presence of comorbid conditions such as chronic obstructive pulmonary disease, asthma, bronchiectasis, pulmonary fibrosis, pulmonary hypertension, and/or a need for surgery. At least one hospitalization or two exacerbations in the past 12 months.")],
    [C("• Clinical examination: Weight, height, BMI, Vital signs (Temperature, Heart rate, Respiratory rate)<br/>• Sings of repository distress<br/>• Clubbing, coarse crepitation, raised jugular venous pressure, oedema, anaemia<br/>• Oxygen saturation by pulse oximeter<br/>• Blood and urine as clinically indicated (e.g. CBC if anemia is present, urea & creatinine and electrolyte if oedema is present)"),
     C("• Reported/presence of respiratory symptoms (dyspnoea, cough, sputum, wheeze, chest pain, fatigue)<br/>• Ineffective cough and/or difficult to clear bronchial secretions<br/>• Abnormal blood gas PaO2, 80 mmHg/10.6 kPa and/or PaCO2.45 mmHg/6.0 kPa and/or nocturnal and exercise-induced desaturation")],
    [C("Imaging CXR", cs=3)],
    r("Functional Assessment", "• Spirometry test<br/>• Minute walking test (6MWT) – can apply for 4-year-old and above",
      "• Impaired pulmonary function showing airflow obstruction or restriction or mixed abnormalities and bronchodilator response and/or impaired diffusing capacity for carbon monoxide<br/>• Impaired exercise test"),
    r("Subjective Evaluation", "Quality of life (QOL) questionnaire<br/>(TB specific QOL questionnaires: EUROHIS-QOL (see Table 22)", "Impaired quality of life ≥16")],
   footnotes=["(Source: Adapted from the Clinical standards for the assessment, management and rehabilitation of post-TB lung disease, INT J TUBERC LUNG DIS 25 (10):797–813 Q, 2021 The Union)"],
   pages=[112, 113],
   source_flags=_t20.get('source_flags', []) + ["Blood gas thresholds read 'PaO2, 80 mmHg/10.6 kPa and/or PaCO2.45 mmHg/6.0 kPa' – the comparison signs are missing (presumably PaO2 < 80 mmHg, PaCO2 > 45 mmHg).",
                                          "'Imaging CXR' has no examination or indication entries."]),
 T("tbl-21-pulmonary-rehab-strategies", 113, _t20['heading_path'].replace("Table 20: Assessment of post-TB lungs disease and indication for pulmonary resuscitation", "Table 21: Management strategies for pulmonary resuscitation"),
   "Table 21: Management strategies for pulmonary resuscitation", [],
   [r("Problem", "Management strategy")],
   [[C(c['t']) for c in row[:2]] for row in _t20['body'][5:11]],
   pages=[113, 114], context_before="The core components of pulmonary resuscitation and suggested management strategies are briefly outlined in the table below.",
   source_flags=["The table has no column headings in the PDF; 'Problem' / 'Management strategy' were added here.",
          "Malnutrition threshold reads 'body mass index ,16 kg/m2 or ... ,17 kg/m2' – presumably '<16' and '<17'.",
          "The resting-hypoxaemia criterion is cut off ('... polycythaemia (haematocrit > 55%) or pulmonary')."]),
 T("tbl-22-eurohis-qol8", 114, _t20['heading_path'].replace("Table 20: Assessment of post-TB lungs disease and indication for pulmonary resuscitation", "Table 22: TB Specific QOL Assessment: EUROHIS-QOL8"),
   "Table 22: TB Specific QOL Assessment: EUROHIS-QOL8", [],
   [r("QOL Assessment Parameter", "Score")],
   [[C(c['t']) for c in row[:2]] for row in _t20['body'][12:] if not row[0]['t'].startswith('QOL Assessment')],
   pages=[114, 115], context_before="The questionnaire has 8 parameters, and each question was answered using a five-point Likert response scale numerically scored with \"0\" being very dissatisfied and \"4\" being very satisfied. A score ≤16 is defined as \"ill-being\" or \"impaired quality of life\" and indicates pulmonary rehabilitation."),
 # Table 34 (p.148): the algorithm's branches had been flattened into a 9-column table; written out as a decision tree from the page image
 D("tbl-p148-0368", 148, _prev['tb-2025-tbl-p148-0368']['heading_path'], "Table 34: DS-TB treatment algorithm in Children and Adolescents (0-19 years old)", ["0368"],
   "Assess the site of TB disease*.\n"
   "A. Pulmonary TB (PTB), both new and re-registered – what is the child's age?\n"
   "   - <3 months: 2HRZE/4HR\n"
   "   - 3 months to <16 years: assess severity\n"
   "       - Non-severe: 2HRZE/2HR\n"
   "       - Severe: 2HRZE/4HR\n"
   "   - 16-19 years: 2HRZE/4HR\n"
   "B. Extra-pulmonary TB (EP-TB), both new and re-registered – what is the child's age?\n"
   "   - <3 months: 2HRZE/4HR\n"
   "   - 3 months to 19 years: assess severity\n"
   "       - Non-severe (isolated peripheral lymphadenopathy): 2HRZE/2HR\n"
   "       - Severe, bone & joint TB (incl. spine): 2HRZE/10HR\n"
   "       - Severe, TB meningitis: 6HRZ+Eto or 2HRZE/10HR\n"
   "       - Severe, all other forms of EP-TB: 2HRZE/4HR",
   footnotes=["*If a child has both PTB and EP-TB severe form, treat with the regimen for the EP-TB severe form. Adjuvant steroid therapy: administer steroids for TB Meningitis, also for pericardial, spinal (sometimes), airway obstruction and TB-IRIS."],
   flags=_prev['tb-2025-tbl-p148-0368'].get('source_flags', [])),
 # p.184 'Other toxicities': the first rows (nausea/vomiting and heartburn) were taken as the header and dropped by the rebuild
 P("tbl-p184-0463", caption="Other toxicities: suggested drugs to manage adverse drug reactions (ADRs) during DR-TB treatment",
   header=[r("ADRs", "Suggested drugs to manage the ADR")],
   body=[r("Nausea, vomiting, abdominal upset", "Metoclopramide, ondansetron, dimenhydrinate, prochlorperazine, promethazine, bismuth subsalicylate"),
         r("Heartburn, acid indigestion, sour stomach, ulcer", "H2-blockers (ranitidine, cimetidine, etc.), proton pump inhibitors (omeprazole, etc.). Avoid antacids because they can decrease the absorption of fluoroquinolones.")]
        + _prev['tb-2025-tbl-p184-0463']['body'][-15:]),
 # Table 2 (p.28): the year/target header rows were dropped, leaving percentages without years; re-done from the page image
 T("tbl-p28-0037", 28, _prev['tb-2025-tbl-p28-0037']['heading_path'], "Table 2: End TB Strategy Milestones", ["0037", "0038"],
   [r("Pillars of The End TB Strategy", "Key Principles of the End TB Strategy")],
   [r("1. Integrated, patient-centred TB care and prevention.", "1. Government stewardship and accountability, with monitoring and evaluation."),
    r("2. Bold policies and supportive systems.", "2. Strong coalition with civil society organizations and communities."),
    r("3. Intensified research and innovation", "3. Protection and promotion of human rights, and ethics.<br/>4. Adaptation of the strategy and targets at the country level, with global collaboration."),
    [C("Vision: A World Free of TB (Zero deaths, disease, suffering due to TB). Goal: End The Global TB epidemic.", cs=2)],
    [C("Milestones and targets: 2020 milestone | 2025 milestone | 2030 SDG* target | 2035 End TB target", cs=2)],
    r("Reduction in number of TB deaths compared with 2015 (%)", "2020: 35% | 2025: 75% | 2030 (SDG): 90% | 2035 (End TB): 95%"),
    r("Reduction in TB incidence rate compared with 2015 (%)", "2020: 20% | 2025: 50% | 2030 (SDG): 80% | 2035 (End TB): 90%"),
    r("TB-affected families facing catastrophic costs due to TB (%)", "2020: 0% | 2025: 0% | 2030 (SDG): 0% | 2035 (End TB): 0%")],
   footnotes=["*The United Nations Sustainable Development Goals (SDGs) include ending the TB epidemic by 2030 under Goal 3."]),
]
