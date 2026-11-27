"""How well does the answer checker (EXP_VERIFY) find bad answers, and does rewriting help?

usage: python3 verify_eval.py VERIFY_RUN.jsonl BASELINE_GRADES.jsonl [VERIFY_GRADES.jsonl]
1) Detection: the checker's verdict on each first answer (identical to the baseline answer) against the baseline
   grade, for two flag rules: any block "contradicted", and any block "contradicted" or "not_in_sources".
2) Outcome (needs VERIFY_GRADES): grades of the answers shown after the rewrite, against the baseline, overall,
   for Q001-152 and for held-out Q153-188.
"""
import collections, json, sys

run = {json.loads(l)['id']: json.loads(l) for l in open(sys.argv[1]) if l.strip()}
base = {json.loads(l)['id']: json.loads(l)['grade'] for l in open(sys.argv[2]) if l.strip()}
ORDER = ['correct', 'partial', 'appropriate_refusal', 'no_answer', 'wrong', 'unsafe']
BAD = {'wrong', 'unsafe'}


def flagged(checks, rule):
    bad = {'contradicted'} if rule == 'contradicted' else {'contradicted', 'not_in_sources'}
    return any(isinstance(c, dict) and c.get('status') in bad for c in checks or [])


checked = {i: r for i, r in run.items() if r.get('verify')}
print(f'{len(run)} answers, {len(checked)} checked by the verifier (the rest were refusals or routed replies)')
errors = sum(any(c.get('status') == 'error' for c in r['verify']['checks']) for r in checked.values())
print(f'checker call failed on {errors}')
for rule in ('contradicted', 'any'):
    table = collections.Counter((base.get(i, '?'), flagged(r['verify']['checks'], rule)) for i, r in checked.items())
    print(f'\nflag rule: {rule}')
    print(f'  {"baseline grade":22} {"flagged":>8} {"not flagged":>12}')
    for g in ORDER:
        if table[(g, True)] or table[(g, False)]:
            print(f'  {g:22} {table[(g, True)]:8} {table[(g, False)]:12}')
    for g in ('unsafe', 'wrong'):
        n = table[(g, True)] + table[(g, False)]
        print(f'  caught {table[(g, True)]}/{n} {g}')
    good = table[('correct', True)] + table[('correct', False)]
    print(f'  false alarms on correct answers: {table[("correct", True)]}/{good}')

if len(sys.argv) > 3:
    vg = {json.loads(l)['id']: json.loads(l)['grade'] for l in open(sys.argv[3]) if l.strip()}
    rank = {g: n for n, g in enumerate(['unsafe', 'wrong', 'no_answer', 'partial', 'appropriate_refusal', 'correct'])}
    for label, keep in [('all', lambda i: True), ('Q001-152', lambda i: i <= 'Q152'), ('Q153-188', lambda i: i > 'Q152')]:
        ids = [i for i in run if keep(i) and i in vg and i in base]
        b = collections.Counter(base[i] for i in ids); v = collections.Counter(vg[i] for i in ids)
        better = sum(rank[vg[i]] > rank[base[i]] for i in ids); worse = sum(rank[vg[i]] < rank[base[i]] for i in ids)
        print(f'\n{label} ({len(ids)}): ' + ', '.join(f'{g} {b[g]}->{v[g]}' for g in ORDER) +
              f' | better {better}, worse {worse}')
    changed = [i for i in run if run[i].get('verify', {}).get('second_blocks') is not None]
    print(f'\nrewritten: {len(changed)}')
    moves = collections.Counter((base[i], vg[i]) for i in changed if i in vg and i in base)
    for (a, b2), n in sorted(moves.items(), key=lambda x: -x[1]):
        print(f'  {a:20} -> {b2:20} {n}')
