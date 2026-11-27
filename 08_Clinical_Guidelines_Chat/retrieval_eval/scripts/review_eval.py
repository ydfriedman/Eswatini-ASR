"""Score the app's review notice (patch 06) on recorded answers, by grade, and list crisis-route matches.

usage: python3 review_eval.py APP_DIR RUN.jsonl GRADES.jsonl REVISED_QUESTIONS.jsonl
The answers are not regenerated: review_reasons() runs on each recorded answer and its retrieved passages.
"""
import collections, json, re, sqlite3, sys
sys.path.insert(0, sys.argv[1])
import app  # noqa: E402

db = sqlite3.connect(app.INDEX)
rows = {r[0]: r for r in db.execute('SELECT chunk_id, doc_id, heading_path, text, caption FROM chunks')}
def source(chunk_id):
    _, doc, heading, text, caption = rows[chunk_id]
    return {'chunk_id': chunk_id, 'document': {'id': app.CHUNK_DOCS[doc]}, 'heading_path': heading,
            'text': text, 'caption': caption}
grades = {json.loads(l)['id']: json.loads(l)['grade'] for l in open(sys.argv[3]) if l.strip()}
ORDER = ['unsafe', 'wrong', 'partial', 'correct']
by_part = {p: collections.Counter() for p in ('Q001-152', 'Q153-188')}
totals = {p: collections.Counter() for p in by_part}
reason_counts = collections.defaultdict(collections.Counter)
for line in open(sys.argv[2]):
    r = json.loads(line)
    g = grades.get(r['id'])
    if r.get('kind') != 'answer' or g not in ORDER:
        continue
    reasons = app.review_reasons(r['question'], r['blocks'], [source(s['chunk_id']) for s in r['sources']])
    part = 'Q001-152' if r['id'] <= 'Q152' else 'Q153-188'
    totals[part][g] += 1
    by_part[part][g] += bool(reasons)
    for reason in reasons:
        key = re.sub(r'\d[\d., ]*', 'N', reason.split(' (')[0])[:60]
        reason_counts[key][g] += 1
for part in by_part:
    print(part, 'answers with specific review reasons:',
          ', '.join(f'{g} {by_part[part][g]}/{totals[part][g]}' for g in ORDER))
print('\nreason (all 188)', ' '.join(f'{g:>8}' for g in ORDER))
for key, c in sorted(reason_counts.items(), key=lambda kv: -sum(kv[1].values())):
    print(f'{key:62}', ' '.join(f'{c[g]:8}' for g in ORDER))
print('\ncrisis route matches:')
for line in open(sys.argv[4]):
    q = json.loads(line)
    if app.self_harm_crisis(q['question']):
        print(' ', q['id'], grades.get(q['id']), q['question'][:110])
