"""Print answers next to the benchmark reference, compactly, for grading.

usage: python3 grade_sheet.py REVISED RUN.jsonl [RUN2.jsonl ...] [--ids Q001,Q002] [--from Q001 --to Q040]
       [--blind SEED]
With two or more runs and --blind, each question's answers are shown as A/B/... in a random order per question,
and the key (which letter is which run) is written to stderr only, so grades can be given without knowing the
variant. Grades are then saved per run as results/<label>_grades.jsonl by the grader.
"""
import argparse, json, random, sys

ap = argparse.ArgumentParser()
ap.add_argument('revised'); ap.add_argument('runs', nargs='+')
ap.add_argument('--ids', default=''); ap.add_argument('--from', dest='start', default='')
ap.add_argument('--to', dest='end', default=''); ap.add_argument('--blind', type=int, default=None)
ap.add_argument('--key', default='', help='write the blind key (JSON) to this file instead of stderr')
args = ap.parse_args()

rev = {}
for line in open(args.revised, encoding='utf-8'):
    if line.strip():
        q = json.loads(line); rev[q['id']] = q
runs = []
for path in args.runs:
    recs = {}
    for line in open(path, encoding='utf-8'):
        if line.strip():
            r = json.loads(line); recs[r['id']] = r
    runs.append((path, recs))
want = set(filter(None, args.ids.split(',')))
rng = random.Random(args.blind)
key = {}

def answer_text(r):
    if r is None:
        return '(not run)'
    if r.get('error'):
        return 'ERROR: ' + r['error'][:200]
    kind = r.get('kind'); mode = r.get('mode')
    blocks = r.get('blocks') or []
    txt = ' | '.join(b.get('text', '') for b in blocks)
    return f'[{kind}{"/" + mode if mode != "llm" else ""}] {txt}'

for qid in sorted(rev):
    if want and qid not in want:
        continue
    if args.start and qid < args.start or args.end and qid > args.end:
        continue
    q = rev[qid]
    print(f"## {qid} {q['question']}")
    print(f"REF: {q['reference_answer']}")
    print(f"MUST: {' ; '.join(q.get('must_include') or [])}")
    if q.get('must_not_include'):
        print(f"NOT: {' ; '.join(q['must_not_include'])}")
    if q.get('needs_decision'):
        print(f"DECISION NOTE: {q.get('check', '')}")
    order = list(range(len(runs)))
    if args.blind is not None and len(runs) > 1:
        rng.shuffle(order)
    for letter, i in zip('ABCDEFGH', order):
        key.setdefault(qid, {})[letter] = runs[i][0]
        tag = letter if (args.blind is not None and len(runs) > 1) else runs[i][0].rsplit('/', 1)[-1]
        print(f"{tag}: {answer_text(runs[i][1].get(qid))}")
    print()
if args.blind is not None and len(runs) > 1:
    if args.key:
        json.dump(key, open(args.key, 'w'), indent=0)
    else:
        print(json.dumps(key), file=sys.stderr)
