"""List answers in RUN.jsonl that still need a grade in GRADES.jsonl; answers identical to a graded run reuse its grade.

usage: python3 to_grade.py RUN.jsonl GRADES.jsonl [--reuse OTHER_RUN.jsonl OTHER_GRADES.jsonl] [--min N]
Prints the comma-separated ids still to grade (and appends reused grades to GRADES.jsonl).
"""
import argparse, json, os
ap = argparse.ArgumentParser()
ap.add_argument('run'); ap.add_argument('grades')
ap.add_argument('--reuse', nargs=2, default=None)
args = ap.parse_args()
run = {json.loads(l)['id']: json.loads(l) for l in open(args.run) if l.strip()}
done = {json.loads(l)['id'] for l in open(args.grades) if l.strip()} if os.path.exists(args.grades) else set()
reuse = {}
if args.reuse:
    other = {json.loads(l)['id']: json.loads(l) for l in open(args.reuse[0]) if l.strip()}
    og = {json.loads(l)['id']: json.loads(l) for l in open(args.reuse[1]) if l.strip()}
    for i, r in run.items():
        if i not in done and i in other and i in og and r.get('blocks') == other[i].get('blocks') \
                and r.get('kind') == other[i].get('kind') and not r.get('error') and not other[i].get('error'):
            reuse[i] = dict(og[i], note=(og[i].get('note', '') + ' [same answer as ' + os.path.basename(args.reuse[0]) + ']').strip())
    with open(args.grades, 'a') as fh:
        for i in sorted(reuse):
            fh.write(json.dumps(reuse[i]) + '\n')
print(','.join(sorted(i for i in run if i not in done and i not in reuse)))
