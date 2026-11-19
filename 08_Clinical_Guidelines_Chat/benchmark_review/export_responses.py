"""Export clinician reviews to one CSV (latest answer per reviewer and question), joined with the question text.

Usage, from 08_Clinical_Guidelines_Chat/:
    python3 benchmark_review/export_responses.py --sheet responses.csv     [--out reviews.csv]
        Google Sheet version: open the "responses" tab, File > Download > Comma-separated values.
    python3 benchmark_review/export_responses.py --dataset your-org/eswatini-benchmark-reviews
        Hugging Face Space version (reading a private dataset needs `hf auth login` or HF_TOKEN).
    python3 benchmark_review/export_responses.py --local path/to/folder_with_responses           (for testing)
Columns match the review page's own CSV download, so both can be analysed the same way.
"""
import argparse
import csv
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COLS = ['id', 'area', 'reviewer', 'safety_critical', 'needs_decision', 'question', 'question_decision',
        'suggested_question', 'reference_answer', 'reference_decision', 'final_reference_answer', 'must_include',
        'must_not_include', 'comments', 'reviewed_at', 'saved_at']


def read_jsonl(args):
    if args.dataset:
        from huggingface_hub import snapshot_download
        folder = Path(snapshot_download(args.dataset, repo_type='dataset', allow_patterns='responses/*.jsonl'))
    else:
        folder = Path(args.local)
    for f in sorted(folder.glob('responses/*.jsonl')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if line.strip():
                yield json.loads(line)


def read_sheet(path):
    """Rows of the Sheet's responses tab; list cells hold one item per line."""
    with open(path, newline='', encoding='utf-8-sig') as fh:
        for row in csv.DictReader(fh):
            r = {k: (v[1:] if v.startswith("'") else v) for k, v in row.items()}
            if not r.get('question_id'):
                continue
            for k in ('must_include', 'must_not_include'):
                r[k] = r[k].split('\n') if r[k] else []
            yield r


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--sheet', help='CSV download of the Google Sheet\'s "responses" tab')
    src.add_argument('--dataset', help='Hugging Face dataset repo id')
    src.add_argument('--local', help='folder containing responses/*.jsonl')
    ap.add_argument('--out', default='benchmark_reviews.csv')
    args = ap.parse_args()
    latest, names = {}, {}
    for r in read_sheet(args.sheet) if args.sheet else read_jsonl(args):
        names.setdefault(r['reviewer_key'], r['reviewer'])   # first spelling used for this reviewer
        k = (r['reviewer_key'], r['question_id'])
        if k not in latest or (r.get('reviewed_at') or '', r['saved_at']) >= (latest[k].get('reviewed_at') or '', latest[k]['saved_at']):
            latest[k] = r
    questions = {q['id']: q for q in json.loads((HERE / 'review_data.json').read_text(encoding='utf-8'))}
    order = {qid: i for i, qid in enumerate(questions)}
    with open(args.out, 'w', newline='', encoding='utf-8-sig') as fh:
        w = csv.writer(fh)
        w.writerow(COLS)
        for (key, qid), r in sorted(latest.items(), key=lambda kv: (kv[0][0], order.get(kv[0][1], 9999))):
            q = questions.get(qid, {})
            final = {'edit': r['reference_edit'], 'approve': q.get('reference', '')}.get(r['reference_decision'], '')
            w.writerow([qid, q.get('area', ''), names[key], q.get('safety', ''), 'yes' if q.get('needs_decision') else 'no',
                        q.get('question', ''), r['question_decision'],
                        r['question_suggestion'] if r['question_decision'] == 'rewrite' else '', q.get('reference', ''),
                        r['reference_decision'], final, ' ; '.join(x for x in r['must_include'] if x.strip()),
                        ' ; '.join(x for x in r['must_not_include'] if x.strip()), r['comments'], r['reviewed_at'],
                        r['saved_at']])
    reviewers = {k for k, _ in latest}
    print(f'{args.out}: {len(latest)} answers from {len(reviewers)} reviewer(s)')


if __name__ == '__main__':
    main()
