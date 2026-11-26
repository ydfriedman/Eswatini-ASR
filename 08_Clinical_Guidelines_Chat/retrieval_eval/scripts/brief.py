"""One line per retrieval run: gold-in-context overall / tuned / held-out, all-gold, estimated model input tokens.

usage: python3 brief.py RUN.json [RUN2.json ...]
"""
import json, sys

def found(gold, sources):
    have = {s['chunk_id'] for s in sources} | {s.get('table_id') for s in sources if s.get('table_id')}
    return [g for g in gold if g in have]

print(f"{'label':44} {'any':>8} {'Q1-152':>7} {'Q153+':>6} {'all':>8} {'in med':>7} {'p90':>6} {'max':>6} {'>12k':>4}")
for path in sys.argv[1:]:
    run = json.load(open(path))
    rows = [r for r in run['results'] if r['gold']]
    hit = {r['id']: bool(found(r['gold'], r['sources'])) for r in rows}
    allg = sum(len(found(r['gold'], r['sources'])) == len(r['gold']) for r in rows)
    tuned = [h for i, h in hit.items() if i <= 'Q152']; held = [h for i, h in hit.items() if i > 'Q152']
    # estimated real model input: ~3,000 tokens of instructions/JSON + passage characters / 3.3 (fits the answer runs)
    toks = sorted(int(3000 + r['passage_chars'] / 3.3) for r in run['results'] if r['outcome'] == 'answer_call')
    print(f"{run['label'][:44]:44} {sum(hit.values()):3} {sum(hit.values()) / len(rows):4.0%} {sum(tuned):7} {sum(held):6} "
          f"{allg:3} {allg / len(rows):4.0%} {toks[len(toks) // 2]:7} {toks[int(len(toks) * .9)]:6} {toks[-1]:6} "
          f"{sum(t > 12000 for t in toks):4}")
