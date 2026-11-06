# HIV 2022: notes where later guidance supersedes this text (2024 Amendment, Chapter 3; 2025 PrEP implementation guidelines).
# Appends to the items' source flags; loaded after the other HIV batches.
import copy as _c, json as _j
_prev = {t['table_id']: t for t in _j.load(open('hiv-2022_tables.json'))['tables']}
AMD = "Superseded by the 2024 Amendment (Chapter 3): "
NOTES = {
 'fig-3.5-hiv-eligibility-screening-adults': AMD + "the risk-based HIV testing screening tool is replaced by HIVST screening for everyone 12 years and above, and the paediatric risk assessment tool for children 2-11 years (Amendment Figure 3.1), except clients eligible for routine testing.",
 'fig-3.6-hiv-risk-assessment-retesting': AMD + "for individuals 12 years and above HIVST replaces this risk assessment tool; children 2-11 years use the paediatric risk assessment tool. Rescreen at every facility encounter.",
 'txt-p57-55': AMD + "HIVST replaces the risk-based HTS screening tool for all individuals 12 years and above; children 2-11 years use the paediatric screening tool; routine testing continues for malnourished and sick children, HIV-exposed children, TB, STI, index contacts, inpatients, pregnant and lactating women and key populations.",
 'tbl-3.1-five-cs': AMD + "the age of consent for HIVST is reduced from 16 years to 12 years.",
 'txt-p52-46': AMD + "the age of consent for HIVST is reduced from 16 years to 12 years; HIVST is now also used as the screening tool for everyone 12 years and above.",
 'box-1.2-summary-ch3': AMD + "HIVST age of consent 12 years (not 16); HIVST replaces the screening tool for 12 years and above; children 2-11 years use the paediatric screening tool.",
 'tbl-3.4-retesting-frequencies': AMD + "for individuals 12 years and above rescreen at every facility encounter using HIVST; children 2-11 years at every encounter using the risk assessment tool. ANC/PMTCT, routine-testing and PrEP retesting rules remain as in this table.",
 'fig-3.3-pihts-master-client-flow': AMD + "the 'HIV risk assessment' step is replaced by HIVST screening (12 years and above) or the paediatric risk assessment (2-11 years).",
 'txt-p35-09': "Partly superseded by the 2025 Eswatini PrEP implementation guidelines (new methods CAB-LA and lenacapavir, updated eligibility, follow-up and kidney monitoring) and by the 2024 Amendment (HIVST at PrEP initiation and follow-up).",
 'tbl-2.4-prep-initiation-visit': "Partly superseded by the 2025 PrEP implementation guidelines and the 2024 Amendment (HIVST-based testing at PrEP initiation and follow-up; CAB-LA and lenacapavir visits).",
}
ITEMS = []
for k, note in NOTES.items():
    t = _c.deepcopy(_prev['hiv-2022-' + k])
    if note not in t.get('source_flags', []):
        t['source_flags'] = t.get('source_flags', []) + [note]
    ITEMS.append(t)
