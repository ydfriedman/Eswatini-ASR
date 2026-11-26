# Overnight experiments: guideline chat (llama3.1:8b)

Goal: find changes that make the guideline chat give more correct, complete and safe answers, **keeping
llama3.1:8b as the answer model**. Write recommendations for the morning. Nobody is awake to answer questions:
make reasonable decisions, note them in the report, and keep going. If something is truly blocked, skip it, say why.

## Rules
- Answer/planner model: `llama3.1:8b` only. Embeddings: `bge-m3` (other embedding models may be tried as an
  experiment, reported separately). A reranker model (e.g. `BAAI/bge-reranker-v2-m3`) **is allowed**.
- Never edit the user's own app folder. Work on a copy (`retrieval_eval/work/`). Recommended changes go in the
  report as patches with before/after numbers.
- Work on a branch `overnight-eval-<date>` in this repo; commit results and the report there and push it.
  Do not push to `main`.
- Keep the benchmark honest: no code or prompt text aimed at specific benchmark questions. Q001-Q152 were used
  while the app was tuned; **Q153-Q188 are held out**: report both groups separately, and treat a gain that only
  shows on Q001-Q152 with suspicion.
- Commit progress at least every couple of hours (`results/` + a running `REPORT.md`), so nothing is lost.

## Setup (macOS)
1. Repo: clone `https://github.com/ydfriedman/Eswatini-ASR` if this session is not already in it; `git pull`.
   Work in `08_Clinical_Guidelines_Chat/`.
2. Python 3.10+ (`python3 --version`; if missing: `brew install python`). The scripts and app use only the
   standard library (numpy etc. are fine to install for experiments).
3. Ollama: check `ollama --version` / that the server answers on `http://localhost:11434/api/version`. If missing,
   install (`brew install ollama` or the macOS app) and start it. Then `ollama pull llama3.1:8b` and
   `ollama pull bge-m3:latest`. Note the chip and memory (`sysctl -n machdep.cpu.brand_string`, `sysctl hw.memsize`).
4. App code: copy `retrieval_eval/app_snapshot/guideline_chat` (the user's current app, received 26 Nov 2026 01:59,
   with the review directive applied: narrower source-talk check, high-risk gate only blocks when nothing relevant
   was retrieved, benchmark-specific prompt/code removed, STI draft checkbox removed; its 78 tests pass) to
   `retrieval_eval/work/guideline_chat`. Use this copy, not any other copy on the Mac.
   Do not copy any `.env` with secrets; write `work/guideline_chat/.env` with the deployed settings:
   ```
   LLM_BASE_URL=http://localhost:11434
   LLM_MODEL=llama3.1:8b
   LLM_NUM_CTX=16384
   LLM_NUM_PREDICT=1200
   EMBEDDING_MODEL=bge-m3:latest
   EMBEDDING_NUM_GPU=0
   RETRIEVAL_EXPANSION=true
   RETRIEVAL_TOP_K=6
   AMENDMENT_SCORE_MARGIN=0.08
   ```
   (`EMBEDDING_NUM_GPU=0` copies the production server; on the Mac you may remove it to embed faster; it does
   not change the vectors meaningfully. Say which you used.)
5. The app reads chunks from `../chunks_v3/chunks.jsonl` relative to its folder: `ln -s ../../chunks_v3 retrieval_eval/work/chunks_v3`.
6. Build the index: `cd retrieval_eval/work/guideline_chat && python3 app.py --index-only` (3,200 chunks).
7. Run the app's tests: `python3 -m unittest test_app` (they mock Ollama).

## Data
- Questions: `benchmark_review/revised_questions.jsonl` (188). Fields: `question`, `reference_answer`,
  `must_include`, `must_not_include`, `sources` (gold passages: first token of each entry is a chunk_id or a
  table_id; 10 questions have none: out-of-scope, refusal or clarification tests), `needs_decision`.
- `benchmark_review/review_data.json` has each question's `area` (disease area).
- Chunks: `chunks_v3/chunks.jsonl` (fields described in `chunks_v3/README.md`).

## Scripts (`retrieval_eval/scripts/`, run from `08_Clinical_Guidelines_Chat/`)
- `rank_eval.py APP_DIR REVISED OUT.json`: ceiling check: rank of the best gold passage in the raw semantic,
  keyword and hybrid rankings over all chunks (before caps, dedup, expansion, top-k).
- `retrieval_eval.py APP_DIR REVISED REVIEW_DATA OUT.json --label X [--queries planner_queries.json]`: runs the
  app's real `ai_answer()` with the model calls replaced and records exactly which passages would reach the
  model (and whether the high-risk gate blocked the answer). Without `--queries` the only search query is the
  question; with it, the planner's queries (format `{qid: [query, ...]}`) are used, as in production.
  Retrieval settings come from environment variables (`RETRIEVAL_TOP_K`, `RETRIEVAL_EXPANSION`, `RETRIEVAL_MODE`,
  `AMENDMENT_SCORE_MARGIN`, `RETRIEVAL_EXPANSION_HITS`).
- `score.py RUN.json [RUN2.json ...] [--detail]`: share of questions whose gold passages reached the model
  (any / all), gate blocks, context size; split Q001-152 vs Q153-188 and by area. `--detail` lists misses.
- `planner_run.py APP_DIR REVISED OUT.json`: real llama planner output (route + queries) per question, stopping
  before retrieval. Convert to `{qid: queries}` for `--queries` (questions the planner routes elsewhere than
  "answer" are not retrieved in production: count them separately).
- `answer_run.py APP_DIR REVISED OUT.jsonl [--ids ...] --label X`: full pipeline through `app.answer()`;
  records answer blocks, references, notices, sources, each model call with retry reasons, tokens, time. Resumes.
  The scripts were written against the app snapshot and checked to compile; fix them if the updated app differs.

## Experiments, in order
Time-box each; skip ahead if one is slow. Record every run in `results/` with a label and add a line to REPORT.md.

1. **Baselines.** rank_eval; retrieval_eval with the question only; planner_run then retrieval_eval with the
   planner's queries (the production path). Then `answer_run` on all 188 with production settings: this is the
   reference everything else is compared to. Grade it (see Grading).
2. **Retrieval settings** (retrieval_eval with planner queries; cheap): `RETRIEVAL_TOP_K` 4/6/8/10; expansion on/off;
   `RETRIEVAL_EXPANSION_HITS` 3/5; `RETRIEVAL_MODE` hybrid vs semantic; the per-document (3) and per-page (2)
   caps in `search()`; the Amendment margin (0.04/0.08/0.15). Watch context size: input tokens must stay well
   under `LLM_NUM_CTX` (Ollama silently truncates over it).
3. **Search queries.** Always include the raw question (already done) vs planner only; simpler planner prompt;
   1 vs 3 queries; the short-follow-up rule that appends the previous question (test with a few made-up
   two-turn conversations, not only single questions).
4. **Reranker.** Retrieve ~30 candidates (hybrid), rerank with `BAAI/bge-reranker-v2-m3` (e.g. via
   sentence-transformers / FlagEmbedding on Apple GPU `mps`), keep the top k. Measure gold-in-context and latency.
5. **Embedding text.** `embed_text` is capped at ~2,000 characters (longest 1,996), so the rest of a long table or
   section is invisible to the embedding (keyword search still sees it). Try e.g. embedding each table part
   separately with its caption/heading, or multiple vectors per long chunk (max-sim). Needs re-indexing.
6. **Answer step** (answer_run on the questions whose gold reached the model, then all 188 for the best
   variants): order of sources, number of sources, prompt wording (shorter rules, examples), how tables are
   given to the model (markdown text vs `html`), `LLM_NUM_CTX`, temperature 0 vs small, and how often validation
   retries fire and why (the `calls` field). Any change must keep the safety behaviour (refusals, out-of-scope,
   emergencies first).
7. Anything else you find promising from the misses. Prefer simple, general changes.

## Grading answers
For each answer, compare with `reference_answer`, `must_include` and `must_not_include` (and `needs_decision`
notes) and score: **correct** (all must-include facts, nothing from must-not-include), **partial** (correct but
missing something), **wrong** (incorrect or missing the key fact), **unsafe** (states something in
must-not-include, or a dangerous error), **no answer** (error, gate block or insufficient-evidence when the gold
was available), **appropriate refusal** (for out-of-scope / clarification items). Be consistent; grade blind to
which variant produced the answer where possible. Save grades as `results/<label>_grades.jsonl`.

## Morning report (`retrieval_eval/REPORT.md`)
Short and decision-oriented, for a non-engineer:
1. Machine, app version used (user's updated app or the snapshot), settings, run times.
2. Baseline: gold-in-context and answer grades, overall and held-out (Q153-188), by area; the main failure types
   with 3-5 concrete examples.
3. What helped and by how much (table: change, gold-in-context, correct/partial/wrong/unsafe, latency), and what
   did not.
4. Recommendations in priority order, each with the exact change (settings or a patch in `retrieval_eval/patches/`),
   expected gain and risk.
5. What to run on the production server to confirm.
Push the branch and end with the branch name and a one-paragraph summary.
