# HIV 2022 part 4: source issues in rebuilt running text (Chapter 10), appended as source flags by heading. Loaded after hiv_b37.
import copy as _c, json as _j, re as _re
_all = _j.load(open('hiv-2022_tables.json'))['tables']
RULES = [
 (r'txt-p25[78]-t04.*> Cervical cancer staging system$', "Cervical cancer staging: stage 2 is printed as 'Tumour has spread to the cervix'; FIGO stage II is spread beyond the uterus/cervix to the upper vagina or parametrium, not reaching the pelvic wall or lower third of the vagina."),
 (r'txt-p256-t04.*> 10\.8 Kaposi Sarcoma > Special considerations$', "Premedication list gives no oral diphenhydramine dose (only '50 mg IV just before administration') and does not say which chemotherapy it is for (the dexamethasone/H2-blocker/antihistamine pattern is the paclitaxel hypersensitivity premedication)."),
 (r'txt-p252-t04.*> 10\.7 HIV related Malignancies$', "Lists 'Hodgkin's lymphoma (AIDS-related primary CNS lymphoma)' among non-AIDS-defining cancers; primary CNS lymphoma is a non-Hodgkin lymphoma and is AIDS-defining."),
 (r'txt-p257-t04.*> Screening for cervical cancer$', "Says 'both screening methods' after listing three tests (HPV DNA, VIA, Pap smear), and gives yearly screening for HIV-positive women; check against the national cervical cancer screening guidelines (WHO now recommends HPV DNA testing every 3-5 years for women living with HIV)."),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('hiv-2022-txt-') or not (240 <= t['page'] <= 263):
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
