"""Two-turn conversations: does the follow-up's answer passage reach the model, with and without the rule that
appends the previous user question as an extra search query for short follow-ups?

usage: python3 followup_eval.py EXP_APP_DIR OUT.json
Uses the real planner (llama) once per conversation, then replays it for each variant. Conversations are made up
for this test (not benchmark questions); gold ids were found by searching the chunk text.
"""
import json, os, sys
sys.path.insert(0, sys.argv[1])
import app  # noqa: E402

CONVS = [
    ('How is syphilis treated in pregnancy?', 'Benzathine penicillin 2.4 million units IM weekly for 3 doses.',
     'What if she is allergic to penicillin?', ['sti-vh-draft-2026-txt-p79-t0210', 'sti-vh-draft-2026-chart-syphilis-in-pregnancy']),
    ('What TB preventive treatment do household contacts get?', '3HP (rifapentine and isoniazid weekly for 3 months) or 6 months of isoniazid.',
     'And for children under 5?', ['tb-2025-0390']),
    ('What is the first-line drug treatment for hypertension in adults?', 'A thiazide-like diuretic, ACE inhibitor or calcium channel blocker, depending on the patient.',
     'What if she is pregnant?', ['ncdimh-0298', 'ncdimh-0299']),
    ('Which PrEP products are available in Eswatini?', 'Oral PrEP, the dapivirine vaginal ring, injectable CAB-LA and lenacapavir.',
     'Can a breastfeeding woman use them?', ['prep-2025-tbl-product-eligibility', 'prep-2025-tbl-ring-pbfw-contraindications', 'prep-2025-0046', 'prep-2025-0015']),
    ('When is viral load monitored after starting ART?', 'At 3 months and 9 months after initiation, then routinely.',
     'What if it is above 1000?', ['hiv-2022-fig-7.4-high-vl-management']),
    ('When can a woman start the injectable contraceptive after delivery?', 'It depends on whether she is breastfeeding.',
     'She is breastfeeding.', ['fp-2021-0079']),
    ('What is the first-line ART regimen for adults?', 'TLD: tenofovir, lamivudine and dolutegravir.',
     'What about pregnant women?', ['hiv-2022-txt-p184-t0360']),
]

real_llm = app.llm_json
planner_cache = {}
current = {}

class Captured(Exception):
    pass

def fake_llm(instructions, content, schema, name):
    if name == 'retrieval_queries':
        key = json.dumps([content.get('question'), content.get('history'), instructions[:40]])
        if key not in planner_cache:
            planner_cache[key] = real_llm(instructions, content, schema, name)
        return planner_cache[key]
    if name == 'guideline_answer':
        raise Captured()
    raise RuntimeError(name)
app.llm_json = fake_llm

real_amb = app.evidence_is_ambiguous
def rec_amb(question, sources, queries):
    current['ids'] = [s.get('chunk_id') for s in sources]
    current['queries'] = list(queries)
    return real_amb(question, sources, queries)
app.evidence_is_ambiguous = rec_amb

import sqlite3
db = sqlite3.connect(app.INDEX)
table_of = dict(db.execute('SELECT chunk_id, table_id FROM chunks'))
db.close()

out = []
for variant, envs in [('append_on', {'EXP_FOLLOWUP_APPEND': '1'}), ('append_off', {'EXP_FOLLOWUP_APPEND': '0'})]:
    os.environ.update(envs)
    hits = 0
    for q1, a1, q2, gold in CONVS:
        current.clear()
        history = [{'role': 'user', 'content': q1}, {'role': 'assistant', 'content': a1}]
        try:
            res = app.ai_answer(q2, history, 'All programs', True)
            outcome = 'routed:' + res.get('kind', '')
        except Captured:
            outcome = 'answer_call'
        ids = current.get('ids', [])
        have = set(ids) | {table_of.get(i) for i in ids if table_of.get(i)}
        found = [g for g in gold if g in have]
        hits += bool(found)
        out.append({'variant': variant, 'q1': q1, 'q2': q2, 'outcome': outcome, 'queries': current.get('queries'),
                    'found': found, 'gold': gold, 'ids': ids})
        print(variant, outcome, bool(found), q2, '|', current.get('queries'), flush=True)
    print(variant, f'{hits}/{len(CONVS)} follow-ups with gold in context', flush=True)
json.dump(out, open(sys.argv[2], 'w'), indent=1)
