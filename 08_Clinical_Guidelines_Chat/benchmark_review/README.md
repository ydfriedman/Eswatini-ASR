# Benchmark review for clinicians

The benchmark questions packaged for clinician review: the original 152, revised and re-checked against chunks_v3
(Q001-Q152), plus 26 new questions (Q153-Q178). The new ones cover NCD guideline chapters that had no questions
(cervical and breast cancer, stroke, heart failure, CKD, COPD, epilepsy, injuries, poisoning and others) and add 7
questions whose answer has to be combined from two or more sources. New questions have no original; their metadata
is stored in `revised_questions.jsonl` under `meta`, and the page marks them "New question".

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

Questions are grouped by disease area in the sidebar (collapsible, with a reviewed count per area), and the
"All disease areas" menu narrows the list to one area, so a reviewer can take just their specialty. Areas are
assigned in `build_review_data.py` (`AREAS`).

CSV columns: id, area, reviewer, document, safety_critical, original_question, proposed_question, question_decision
(keep / rewrite), suggested_question, proposed_reference_answer, reference_decision (approve / edit / reject),
final_reference_answer, must_include, must_not_include (items separated by " ; "), comments, reviewed_at.

## Rebuild
From `08_Clinical_Guidelines_Chat/`:
```
python3 benchmark_review/build_review_data.py
python3 benchmark_review/build_review_html.py
```
