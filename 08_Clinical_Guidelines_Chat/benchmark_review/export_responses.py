"""Export clinician reviews saved by the Hugging Face Space to one CSV (latest answer per reviewer and question).

Usage, from 08_Clinical_Guidelines_Chat/:
    python3 benchmark_review/export_responses.py --dataset your-org/eswatini-benchmark-reviews  [--out reviews.csv]
    python3 benchmark_review/export_responses.py --local path/to/folder_with_responses           (for testing)
Reading a private dataset needs a Hugging Face token (`hf auth login` or HF_TOKEN).
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


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument('--dataset', help='Hugging Face dataset repo id')
    src.add_argument('--local', help='folder containing responses/*.jsonl')
    ap.add_argument('--out', default='benchmark_reviews.csv')
    args = ap.parse_args()
    if args.dataset:
        from huggingface_hub import snapshot_download
        folder = Path(snapshot_download(args.dataset, repo_type='dataset', allow_patterns='responses/*.jsonl'))
    else:
        folder = Path(args.local)
    latest, names = {}, {}
    for f in sorted(folder.glob('responses/*.jsonl')):
        for line in f.read_text(encoding='utf-8').splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
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
