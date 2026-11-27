"""Score review flags on recorded answers against their grades.

usage: python3 flag_eval.py RUN.jsonl GRADES.jsonl INDEX.sqlite [--module review_flags]
Prints, for each rule and for combinations, how many unsafe / wrong / partial / correct answers it flags, for
Q001-152 (used to design the rules) and held-out Q153-188 separately.
"""
import argparse, collections, importlib, json, sqlite3, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument('run'); ap.add_argument('grades'); ap.add_argument('index')
ap.add_argument('--module', default='review_flags'); ap.add_argument('--show', default='')
args = ap.parse_args()
sys.path.insert(0, str(Path(__file__).parent))
mod = importlib.import_module(args.module)

db = sqlite3.connect(args.index)
rows = {r[0]: {'chunk_id': r[0], 'heading_path': r[1], 'text': r[2], 'caption': r[3]}
        for r in db.execute('SELECT chunk_id, heading_path, text, caption FROM chunks')}
grades = {json.loads(l)['id']: json.loads(l)['grade'] for l in open(args.grades) if l.strip()}
GROUPS = ['unsafe', 'wrong', 'partial', 'correct']
res = {}
for line in open(args.run):
    r = json.loads(line)
    if r.get('kind') != 'answer' or r['id'] not in grades:
        continue
    sources = [rows[s['chunk_id']] for s in r['sources']]
    res[r['id']] = (grades[r['id']], mod.review_flags(r['question'], r['blocks'], sources))

def table(name, pick):
    out = []
    for part, keep in (('Q001-152', lambda i: i <= 'Q152'), ('Q153+', lambda i: i > 'Q152')):
        c = collections.Counter(); n = collections.Counter()
        for i, (g, f) in res.items():
            if not keep(i) or g not in GROUPS:
                continue
            n[g] += 1; c[g] += bool(pick(f))
        out.append(f'{part}: ' + ' '.join(f'{g[:4]} {c[g]}/{n[g]}' for g in GROUPS)
                   + f' | flagged {sum(c.values())}/{sum(n.values())}')
    print(f'{name:34} ' + '   '.join(out))

rules = sorted({k for _, f in res.values() for k in f})
for rule in rules:
    table(rule, lambda f, rule=rule: rule in f)
table('ANY', lambda f: f)
if args.show:
    for i, (g, f) in sorted(res.items()):
        if g in args.show.split(','):
            print(i, g, sorted(f))
