# HIV 2022 part 5: source issues in rebuilt annex text, appended as source flags by heading. Loaded after hiv_t05.
import copy as _c, json as _j, re as _re
_all = _j.load(open('hiv-2022_tables.json'))['tables']
RULES = [
 (r'txt-p281-t05.*> 11\.9 Supplementary Information on Dolutegravir$', "Annex 11.9 says DTG can be used in adults and children 12 years and older weighing more than 40 kg; Chapter 9 and the 2024 Amendment use DTG (pDTG 10 mg, pALD) from 4 weeks of age and 3 kg."),
 (r'txt-p281-t05.*> 11\.9 Supplementary Information on Dolutegravir$', "Annex 11.9 calls B1 a United States FDA pregnancy category; B1 is an Australian (TGA) category - the US FDA letter categories (A/B/C/D/X) do not include B1 and were replaced in 2015."),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('hiv-2022-txt-') or not (264 <= t['page'] <= 315):
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
