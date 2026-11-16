# Benchmark review for clinicians

The benchmark questions packaged for clinician review: the original 152, revised and re-checked against chunks_v3
(Q001-Q152), plus 36 added questions (Q153-Q188) covering NCD guideline chapters that had none, paediatric NCD
content, and questions whose answer must be combined from two or more sources.

The page is written for clinicians: it shows the question, reference answer, must-include / must-not-include lists and
the guideline text, but not the original wording or change history (those stay in `revised_questions.jsonl`:
`change`, and `meta` for added questions). Two notes guide reviewers:
- a green note under questions that are unusual on purpose (vague, misspelled, wrong premise, emergencies...), from
  `HOW_TO_READ` in `build_review_data.py`, so reviewers judge the answer instead of rewriting the question;
- a "Please decide" note where the guidelines disagree, are unclear, or the answer goes beyond them
  (`needs_decision` in `revised_questions.jsonl`; 23 questions).

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

CSV columns: id, area, reviewer, safety_critical, needs_decision, question, question_decision (keep / rewrite),
suggested_question, reference_answer, reference_decision (approve / edit / reject), final_reference_answer, must_include, must_not_include (items separated by " ; "), comments, reviewed_at.

## Rebuild
From `08_Clinical_Guidelines_Chat/`:
```
python3 benchmark_review/build_review_data.py
python3 benchmark_review/build_review_html.py
```
