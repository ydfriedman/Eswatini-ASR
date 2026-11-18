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
| `build_review_data.py`, `build_review_html.py`, `review_template.html` | Rebuild the page (both the offline file and the hosted version). |
| `hf_space/` | The hosted version: a Hugging Face Space (Docker, FastAPI) that serves the page and saves each answer to a private dataset. |
| `export_responses.py` | Exports the saved answers from the dataset to one CSV (latest answer per reviewer and question). |

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

## Hosted version (Hugging Face Space)
`hf_space/` serves the same page; answers are saved to a private Hugging Face dataset as reviewers work (the
browser copy and **Download CSV** stay as backups). Reviewers continue on any device by entering the same name.
An optional access code keeps strangers out of a public Space.

**Live:** Space https://huggingface.co/spaces/YoniFriedman/guideline-answer-review (page:
https://yonifriedman-guideline-answer-review.hf.space), answers in the private dataset
`YoniFriedman/eswatini-benchmark-reviews`. The free CPU Space sleeps after 48 hours without visits and takes
about a minute to wake; saved answers are read back from the dataset when it starts.

To redeploy after changing the questions: rebuild with `build_review_html.py`, then upload `hf_space/` to the Space
(e.g. `hf upload YoniFriedman/guideline-answer-review benchmark_review/hf_space . --repo-type space`).

Deploy from scratch: create a Docker Space and upload the contents of `hf_space/`; in the Space settings set the variable
`DATASET_REPO` (e.g. `your-org/eswatini-benchmark-reviews`, created private on first save), the secret `HF_TOKEN`
(write access to that dataset) and optionally the secret `REVIEW_ACCESS_CODE`. Rebuild `hf_space/static/index.html`
with `build_review_html.py` after changing the questions, and upload it again.

Collect the answers:
```
python3 benchmark_review/export_responses.py --dataset YoniFriedman/eswatini-benchmark-reviews --out reviews.csv
```
Test locally without a dataset: `cd benchmark_review/hf_space && DATA_DIR=/tmp/review REVIEW_ACCESS_CODE=test uvicorn app:app --port 7860`.

