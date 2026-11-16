# Benchmark review for clinicians

The 152 benchmark questions, revised and re-checked against chunks_v3, packaged for clinician review.

| File | What it is |
|---|---|
| `clinician_review.html` | The review page. Send this one file to reviewers; it works offline. |
| `revised_questions.jsonl` | Revised questions: question, reference answer, must_include, must_not_include, source chunk ids, source-check note. |
| `review_data.json` | Revised questions joined with the original questions and the source chunk text (generated). |
| `build_review_data.py`, `build_review_html.py`, `review_template.html` | Rebuild the page. |

`../sample_questions.jsonl` (the original set) is unchanged.

## Reviewers
Open `clinician_review.html` in Chrome, Edge, Firefox or Safari (double-click the file; it must be opened from disk
or a normal web server, not inside a preview pane that blocks downloads). Work is saved in the browser as you go.
**Download CSV** exports every question (one row each) and is how the review comes back; **Load saved CSV**
restores a review on another computer.

CSV columns: id, reviewer, document, safety_critical, original_question, proposed_question, question_decision
(keep / rewrite), suggested_question, proposed_reference_answer, reference_decision (approve / edit / reject),
final_reference_answer, must_include, must_not_include (items separated by " ; "), comments, reviewed_at.

## Rebuild
From `08_Clinical_Guidelines_Chat/`:
```
python3 benchmark_review/build_review_data.py
python3 benchmark_review/build_review_html.py
```
