# STI/VH draft part 2: source issues in rebuilt running text (Chapters 7-16), appended as source flags by heading. Loaded after sti_t02.
import copy as _c, json as _j, re as _re
_all = _j.load(open('sti-vh-draft-2026_tables.json'))['tables']
RULES = [
 (r'txt-p74-.*> Treatment regimens for reactive syphilis test cases$', "Reactive syphilis tests are treated with benzathine penicillin weekly for 3 weeks 'after testing for sensitivity' for everyone; a single dose is the treatment for early syphilis (Table 3), and routine penicillin skin testing is not recommended (see Annex 5 flag)."),
 (r'txt-p79-.*> Treatment regimens for Syphilis in pregnancy$', "Syphilis in pregnancy: erythromycin for the mother does not prevent congenital syphilis (the newborn must be treated), and the neonatal procaine penicillin dose ('150 000 IU/kg IM, 12 hourly for 14 days') does not match standard dosing (procaine penicillin 50 000 IU/kg once daily for 10 days). Ceftriaxone 1 g daily for 8-10 days is listed without saying it is the penicillin-allergy alternative."),
 (r'txt-p111-.*> Treatment for sexually transmitted proctitis$', "Proctitis treatment in the text gives ceftriaxone 250 mg IM, while the MSM ano-rectal chart on p.112 gives 500 mg and the section 5 anorectal chart gives 250 mg; the draft's adult gonorrhoea dose elsewhere is 1 g."),
 (r'txt-p117-.*> 11\.3 Neonatal Herpes$', "Chapter 11 numbering skips 11.2 (11.1 Congenital syphilis is followed by 11.3 Neonatal Herpes)."),
 (r'txt-p85-.*> 7\.3 Genital Warts > Description$', "The genital warts description calls HPV 'Herpes Papiloma Virus' (human papillomavirus) and lists syphilis among the causes of warts (condylomata lata are a different lesion)."),
 (r'txt-p81-.*> 7\.2 Balanitis and balanoposthitis > Etiology$', "Balanitis etiology lists only 'Candida albicans or lactobacilli'; lactobacilli are normal flora, not a cause of balanitis (anaerobes, streptococci and T. vaginalis are usual non-candidal causes)."),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('sti-vh-draft-2026-txt-') or t['page'] < 71:
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
