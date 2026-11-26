"""Score retrieval runs: did the gold source passages reach the model?

usage: python3 score.py RUN.json [RUN2.json ...] [--detail]
A gold id matches a retrieved chunk by chunk_id or by table_id (gold often names a whole table; chunks are its parts).
"""
import json, sys, collections

detail = '--detail' in sys.argv
runs = [json.load(open(p)) for p in sys.argv[1:] if not p.startswith('--')]

def found(gold, sources):
    have = {s['chunk_id'] for s in sources} | {s.get('table_id') for s in sources if s.get('table_id')}
    return [g for g in gold if g in have]

def first_pos(gold, sources):
    for i, s in enumerate(sources, 1):
        if s['chunk_id'] in gold or (s.get('table_id') and s['table_id'] in gold):
            return i
    return None

def summarise(rows):
    rows = [r for r in rows if r['gold']]
    n = len(rows)
    sent = [r for r in rows if r['outcome'] == 'answer_call']
    any_hit = sum(bool(found(r['gold'], r['sources'])) for r in rows)
    all_hit = sum(len(found(r['gold'], r['sources'])) == len(r['gold']) for r in rows)
    blocked = sum(r['outcome'] == 'source_only' for r in rows)
    toks = sorted(sum(s['approx_tokens'] for s in r['sources']) for r in sent) or [0]
    return n, any_hit, all_hit, blocked, toks[len(toks) // 2], toks[-1]

for run in runs:
    res = run['results']
    print(f"\n=== {run['label']}  {run['env']}")
    print(f"{'subset':34}{'n':>4} {'any gold':>9} {'all gold':>9} {'gate':>5} {'ctx tok med/max':>16}")
    groups = [('all with gold', res),
              ('Q001-Q152 (code tuned on these)', [r for r in res if r['id'] <= 'Q152']),
              ('Q153-Q188 (held out)', [r for r in res if r['id'] > 'Q152'])]
    by_area = collections.defaultdict(list)
    for r in res:
        by_area[r['area']].append(r)
    groups += [('  ' + a[:32], rs) for a, rs in sorted(by_area.items())]
    for name, rows in groups:
        n, a, al, b, med, mx = summarise(rows)
        if n:
            print(f"{name:34}{n:4} {a:4} {a / n:4.0%} {al:4} {al / n:4.0%} {b:5} {med:7}/{mx:<7}")
    pos = collections.Counter(first_pos(set(r['gold']), r['sources']) for r in res if r['gold'])
    print('position of first gold passage among the sources sent:', sorted((k or 99, v) for k, v in pos.items()))
    outc = collections.Counter(r['outcome'] for r in res)
    print('outcomes:', dict(outc))
    if detail:
        for r in res:
            if r['gold'] and not found(r['gold'], r['sources']):
                print(' MISS', r['id'], r['gold'], '| got:', [s['chunk_id'] for s in r['sources']][:8])
