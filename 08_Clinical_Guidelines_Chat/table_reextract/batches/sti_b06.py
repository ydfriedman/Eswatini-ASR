# STI/VH draft part 1: source issues in the rebuilt running text, appended as source flags by heading. Loaded after sti_t01.
import copy as _c, json as _j, re as _re
_all = _j.load(open('sti-vh-draft-2026_tables.json'))['tables']
RULES = [
 (r'> Foreword$', "The Foreword gives 357 million new curable STIs a year (a 2012 WHO estimate); the Background gives 374 million in 2020."),
 (r'> 5\.5 Scrotal swelling \(SSS\) > Etiology:$', "The scrotal swelling Etiology text starts mid-sentence ('responsible micro-organism: E. coli, Klebsiella, and P. Aeruginosa...'); the sexually transmitted causes (N. gonorrhoeae, C. trachomatis) and the sentence introducing the enteric organisms are missing from the draft."),
 (r'> 5\.2 Male Urethral Syndrome \(MUS\) > Description$', "The male urethral syndrome Description is incomplete: 'should be examined for evidence of.' (the object is missing)."),
 (r'> 3\.8 STI Reporting Systems$', "Section numbering jumps from 3.3 to 3.8 in the Health Promotion Package chapter."),
 (r'> Patient information to be gathered$', "The medical history list ends with a truncated item ('Any known allergi')."),
 (r'> Cervical Infections > Syndromic treatment:$', "The cervical infection syndromic treatment repeats the vaginal discharge regimen, including metronidazole and clotrimazole for vulval candidiasis, which do not treat cervical gonorrhoea or chlamydia (Table 7 has no metronidazole)."),
 (r'> 5\.4 Lower abdominal pain \(LAP\) > Treatment options for lower abdominal pain$', "The first treatment option reads 'Ceftriaxone, 1g I.M STAT, Gentamycin 240mg IM Stat and Spectinmycin 2 grams IM PLUS', which can be read as giving all three injectables together; they are alternatives."),
 (r'Bacterial STIs:$', "The 'bacterial STIs' list includes pelvic inflammatory disease (a syndrome, not an organism) and bacterial vaginosis (not an STI in the strict sense, as Table 2 notes)."),
]
ITEMS = []
for t in _all:
    if not t['table_id'].startswith('sti-vh-draft-2026-txt-'):
        continue
    key = t['table_id'] + ' | ' + t['heading_path']
    notes = [n for pat, n in RULES if _re.search(pat, key)]
    if notes:
        d = _c.deepcopy(t)
        d['source_flags'] = d.get('source_flags', []) + [n for n in notes if n not in d.get('source_flags', [])]
        ITEMS.append(d)
