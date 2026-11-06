# HIV 2022 part 2 (pp.76-142): where the 2024 Amendment supersedes this content (Amendment Chapters 4-6). Matches items by id or by
# heading so it survives regeneration of the text sections; appends a source flag. Loaded after hiv_t02.
import copy as _c, json as _j, re as _re
_all = _j.load(open('hiv-2022_tables.json'))['tables']
A = "Superseded by the 2024 Amendment: "
RULES = [
 (r'tbl-6\.17-ahd-package|box-6\.2-ahd-definition|6\.2\.1 Management of Clients', A + "CrAg screening and TB LAM are recommended for all PLHIV with CD4 ≤200 cells/µL (inpatients and outpatients); VISITECT CD4 is the platform of choice for baseline/AHD CD4 testing where available (Amendment Chapter 6)."),
 (r'fig-6\.3-crag-screening|tbl-6\.19-ccm-management|Cryptococcal antigen screening in PLHIV', A + "CrAg screening threshold is CD4 ≤200 cells/µL (was ≤100) (Amendment Chapter 6)."),
 (r'tbl-5\.2-baseline-labs|tbl-5\.17-care-at-art-initiation', A + "pretreatment viral load for all newly diagnosed clients initiating ART (not for clients returning to care); CrAg and TB LAM for all with CD4 ≤200 cells/µL; VISITECT CD4 for baseline where available (Amendment Chapters 5-6)."),
 (r'fig-6\.2-tb-evaluation-plhiv|tbl-6\.2-tb-screening-tests|6\.1\.3 TB Diagnosis', A + "TB LAM is recommended for inpatients and outpatients with CD4 ≤200 cells/µL, and TB diagnosed by TB LAM is classified as bacteriologically confirmed (Amendment Chapter 6)."),
 (r'tbl-6\.3-tpt-options|tbl-6\.5-tpt-dosing|tbl-6\.8-drtb-contact-pt|6\.1\.5 TB Prevention$|Preventive treatment for Drug-Resistant TB$', A + "INH/CTX/Vit B6 FDC is phased out as a TPT option; 3HP is for children and adolescents >14 years and ≥30 kg (was >12 years and 25 kg); TPT for MDR/INH-mono/PDR contacts is levofloxacin alone (no ethambutol) (Amendment Chapter 6)."),
 (r'tbl-5\.6-mmd-by-population|5\.7\.3 Multimonth|tbl-5\.8-package-first-year|tbl-5\.9-package-established', A + "first routine VL at 3 months after ART initiation (all clients must have a VL by 6 months); up to 3MMD after an initial suppressed VL at 3 months; up to 6MMD after 2 consecutive suppressed VL results (Amendment Chapter 5)."),
 (r'5\.3 Changing Role of CD4', A + "VISITECT CD4 for advanced HIV disease is used for AHD screening of new positives, returners after ≥6 months' interruption and clients with VL >1000 copies/mL; quantitative CD4 for follow-up (Amendment Chapter 6)."),
 (r'Chapter 4: Referral and Linkages > 4\.1 Introduction|box-4\.1-linkages-introduction|tbl-4\.2-linkage-types', A + "providers should implement a status-neutral approach: everyone receiving HTS is linked directly to prevention or ART services according to need; clients re-engaging without a transfer letter should not be turned away (Amendment Chapter 4)."),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('hiv-2022-') or t['page'] < 76 or t['page'] > 142:
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
