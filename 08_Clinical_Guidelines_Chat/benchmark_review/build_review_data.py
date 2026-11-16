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
    out.append(dict(id=r['id'], document=q['document'], topic=q['topic'], type=q['question_type'],
                    category=q['edge_case_category'], expected=q['expected_behavior'], safety=q['safety_critical'],
                    original_question=q['question'], original_reference=q['reference_answer'],
                    question=r['question'], change=r['change'], reference=r['reference_answer'],
                    must_include=r['must_include'], must_not_include=r['must_not_include'], check=r['check'],
                    sources=[source(s) for s in r['sources']]))
json.dump(out, open('benchmark_review/review_data.json', 'w'), ensure_ascii=False)
print(len(out), 'questions;', sum(len(o['sources']) for o in out), 'sources')
