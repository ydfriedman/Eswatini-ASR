"""Build review_data.json for the clinician review page: original question set + revised questions + source chunk text.
Run from 08_Clinical_Guidelines_Chat/:  python3 benchmark_review/build_review_data.py"""
import json
Q = {json.loads(l)['id']: json.loads(l) for l in open('sample_questions.jsonl')}
R = [json.loads(l) for l in open('benchmark_review/revised_questions.jsonl')]
K = [json.loads(l) for l in open('chunks_v3/chunks.jsonl')]
DOCS = {'hiv-2022': 'Integrated HIV Management Guidelines 2022', 'hiv-amendment-2024': 'HIV Management Amendment 2024',
        'prep-2025': 'PrEP Implementation Guidelines 2025', 'unaids-linkages-sop': 'Enhanced Linkages Case Management SOP 2021',
        'tb-2025': 'Integrated TB Management Guidelines 2025', 'ncdimh': 'NCDs, Injuries and Mental Health Guidelines 2025',
        'mental-health-deskguide': 'Mental Health Desk Guide 2022', 'anc': 'Antenatal Care Guidelines',
        'fp-2021': 'Family Planning Services Guidelines 2021', 'sti-vh-draft-2026': 'STI and Viral Hepatitis Guidelines 2026 (draft)'}

# Disease areas for the review page sidebar, in display order. Edge-case questions go with their clinical area;
# tests of the assistant's behaviour (off-topic, prompt injection, privacy ...) have their own group.
def ids(spec):
    out = []
    for part in spec.split():
        a, _, b = part.partition('-')
        out += [f'Q{n:03d}' for n in range(int(a), int(b or a) + 1)]
    return out
AREAS = [
    ('HIV testing, treatment and PMTCT', ids('1-3 5 7-11 19-20 23-24 84-91 100-101 118 120 129 132 137')),
    ('HIV prevention: PrEP and PEP', ids('4 37-48 81-83 102 116 121 124 127 130 136 140 144-145 149')),
    ('TB and TB/HIV', ids('6 69-80 104 117 123 125 133 135 148')),
    ('STIs and viral hepatitis', ids('58-68 126 152')),
    ('Pregnancy and antenatal care', ids('12-18 103 122 146')),
    ('Family planning', ids('26-36 134')),
    ('NCDs and emergencies', ids('21-22 25 92-98 128 131 139 141 150')),
    ('Mental health and substance use', ids('49-57 99 105 138 142')),
    ('Assistant behaviour (non-clinical tests)', ids('106-115 119 143 147 151')),
]
AREA = {q: name for name, qs in AREAS for q in qs}
ORDER = {name: i for i, (name, _) in enumerate(AREAS)}

def source(s):
    cid = s.split(' ')[0]
    label = s[len(cid):].strip(' ()')
    hits = [k for k in K if k['chunk_id'] == cid or (k.get('table_id') or '') == cid or k['chunk_id'].startswith(cid + '-p')]
    if not hits:
        return dict(id=cid, label=label, doc='', pages='', heading='', text='(source text not found)')
    k = hits[0]
    text = k['text'] if k.get('table_id') else '\n\n'.join(h['text'] for h in hits)
    p1, p2 = k['page_start'], max(h.get('page_end') or h['page_start'] for h in hits)
    return dict(id=cid, label=label, doc=DOCS.get(k['doc_id'], k['doc_id']), pages=f'{p1}' if p1 == p2 else f'{p1}-{p2}',
                heading=k['heading_path'], text=text)

out = []
for r in R:
    q = Q[r['id']]
    out.append(dict(id=r['id'], area=AREA[r['id']], document=q['document'], topic=q['topic'], type=q['question_type'],
                    category=q['edge_case_category'], expected=q['expected_behavior'], safety=q['safety_critical'],
                    original_question=q['question'], original_reference=q['reference_answer'],
                    question=r['question'], change=r['change'], reference=r['reference_answer'],
                    must_include=r['must_include'], must_not_include=r['must_not_include'], check=r['check'],
                    sources=[source(s) for s in r['sources']]))
assert len(AREA) == sum(len(qs) for _, qs in AREAS) == len(out), 'each question needs exactly one area'
out.sort(key=lambda o: (ORDER[o['area']], o['id']))
json.dump(out, open('benchmark_review/review_data.json', 'w'), ensure_ascii=False)
for name, qs in AREAS: print(f'{len(qs):4d}  {name}')
print(len(out), 'questions;', sum(len(o['sources']) for o in out), 'sources')
