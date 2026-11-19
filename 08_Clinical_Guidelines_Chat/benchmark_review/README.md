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
| `apps_script/` | **The hosted version reviewers use:** a Google Apps Script web app bound to a Google Sheet (`Code.gs`), plus the page split into cells for the Sheet (`page_sheet.csv`). Answers land in the Sheet, one row per reviewer per question. |
| `hf_space/` | Earlier hosted version (Hugging Face is blocked on the reviewers' machines): a Hugging Face Space (Docker, FastAPI) that serves the page and saves answers to a private dataset (one file per reviewer, one line per question). |
| `export_responses.py` | Joins the saved answers (from the Sheet's CSV download, or the HF dataset) with the question text in one CSV. |

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

## Hosted version (Google Sheet + Apps Script)
Used because Hugging Face and Claude are blocked on the reviewers' machines while Google is not. Reviewers open a
link and need no Google account; the page is the same as the offline one. A question is saved when the reviewer clicks
**Save and next** or moves to another question (and when the tab is closed or hidden), only if they changed it. The
`responses` tab holds one row per reviewer per question; saving a question again updates its row. Reviewers continue
on any device by entering the same name (case and spacing are ignored). Must-include / must-not-include lists are
stored one item per line in their cell. The browser copy and **Download CSV** remain as backups.

**Sheet:** "Guideline answer review (Eswatini benchmark)" in Google Drive
(https://docs.google.com/spreadsheets/d/1csQS2SqImjmL2fdAtANRC-Qq0JeD5D7JIZLsDkPoDx4/edit). Its first tab holds the
page (A1 = `REVIEW_PAGE_V1 ...`, then the page in cells A2:A30); do not edit that tab. The script adds the
`responses` tab on the first save.

Set up the web app (once):
1. Open the Sheet > **Extensions > Apps Script**. Replace the contents of `Code.gs` with
   `apps_script/Code.gs` from this folder and save.
2. **Project Settings** (gear) > **Script properties** > add `REVIEW_ACCESS_CODE` = the code you will give reviewers.
3. **Deploy > New deployment** > type **Web app**; Execute as **Me**; Who has access **Anyone** > Deploy.
4. Authorise: Google warns the app is unverified (it is your own script) > Advanced > Go to project. The script can
   only touch this one spreadsheet (`@OnlyCurrentDoc`).
5. Send reviewers the web app URL (`https://script.google.com/macros/s/.../exec`) and the access code.

After changing the questions: rebuild, then in the Sheet's page tab import `apps_script/page_sheet.csv`
(**File > Import > Upload > Replace current sheet**) and paste the new `apps_script/Code.gs` (it lists the question
ids); then **Deploy > Manage deployments > Edit > Version: New version**, which keeps the same URL.

Collect the answers: open the `responses` tab, **File > Download > Comma-separated values**, then
```
python3 benchmark_review/export_responses.py --sheet responses.csv --out reviews.csv
```
which adds the question, area and reference answer to each row (same columns as the page's own CSV download).

## Earlier hosted version (Hugging Face Space)
`hf_space/` serves the same page; answers are saved to a private Hugging Face dataset (the browser copy and
**Download CSV** stay as backups). A question is saved when the reviewer clicks **Save and next** or moves to another
question, and when the tab is closed or hidden. The dataset holds one file per reviewer
(`responses/<name>-<id>.jsonl`) with one line per question answered; saving a question again replaces its line. Reviewers continue on any device by entering the same name.
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

