# Overnight evaluation report (in progress)

Branch `overnight-eval-2026-11-25`. This file is updated as runs finish; the summary at the top is written last.

## Setup and decisions

- Machine: Apple M4 (10-core), 16 GB unified memory, macOS 15.6.
- Homebrew is not installed on this Mac and its installer needs an admin password, so Ollama was installed from
  the official GitHub release (`ollama-darwin.tgz` v0.40.18, SHA-256 checked against GitHub's digest, Apple
  Developer ID signed) into `~/.local/opt/ollama`, run as `ollama serve` (no app). Python: the existing
  uv-managed 3.12 (`~/.local/bin/python3.12`), in a venv at `~/.local/venvs/oeval`. The system Python is 3.9.
- App: `retrieval_eval/app_snapshot/guideline_chat` (the updated app, 26 Nov, review directive applied), copied to
  `retrieval_eval/work/guideline_chat` with the deployed `.env`. Its 78 tests pass.

## Status (26 Nov, after the Mac crashed)

The first session stopped soon after its only commit (25 Nov, 22:52 EST): the Mac crashed. Everything it saved is in
`results/`. The findings below were written from those files by the cloud session; the cloud session's own runs are in
`results/cloud_cpu/` (question-only retrieval, same conclusions). **Resume from "Still to do".**

### Done
- Setup, the app's tests, `rank_eval`, planner run on all 188 (`planner_baseline.json`), retrieval with the question
  only and with the planner's queries (production path), and the first retrieval sweeps (`ret_*.json`).
- Follow-up rule test (`followup_eval.json`, 7 made-up two-turn conversations).
- Answers for Q001-Q033 with production settings (`ans_baseline.jsonl`) and their grades (`baseline_grades.jsonl`).

### Still to do (in this order)
1. Finish the answer baseline: `answer_run.py` resumes, so rerun it with the same output file for Q034-Q188, then
   grade the new answers the same way (same grader rules, append to `baseline_grades.jsonl`).
2. Reranker (plan experiment 4; `make_exp_app.py` already has `EXP_RERANK*` switches): retrieval first, then answers.
3. Answer-step experiments aimed at the failure types below (plan experiment 6), on all 188.
4. Routing fix for clinical questions sent to out-of-scope (below).
5. Embedding-text experiment (plan experiment 5) if time allows.
6. Write the summary and recommendations at the top of this file.

## Findings so far

### Answers (Q001-Q033 only; all in the tuned set, so treat as indicative)
| Grade | n |
|---|---|
| correct | 10 |
| partial | 14 |
| wrong | 3 |
| unsafe | 6 |

Median 54 s per answer on the M4 (max 93 s). Validation retries: 5 for "far too long", 1 for source talk; no errors.
Retrieval is not the main problem for these: at least one gold passage reached the model for all 33, and every gold passage for 19 (including 4 of the 6 unsafe ones). The unsafe answers fall into three types:
- **Older guidance used where a newer one applies** (Q005 CrAg threshold, Q007 2022 viral-load bands, Q010 2022
  infant prophylaxis rule): the 2024 Amendment / TB 2025 passages are there or retrievable, but the model follows
  the 2022 text. Candidate fix: label each source with its guideline and year in the prompt and add one general rule
  ("where sources disagree, follow the most recent guideline and say so").
- **A one-word verdict that contradicts the rule the answer then states** (Q001 consent age, Q026 LAM). Candidate
  fix: ask for the rule first and the verdict after it, or check the verdict against the body in validation.
- **Misreading the passage** (Q016 300 mL antepartum haemorrhage called minor, Q031 IUCD at day 4).
Partial answers mostly miss the second half of multi-step management (Q021, Q022, Q024).

### Routing
With the planner's queries, 9 questions are routed out of scope (1 with the question only). Two are clinical
questions with gold passages that users would see refused: **Q093** "Who should be screened for diabetes?" and
**Q127** "Can I use the dapivirine ring for a man who has sex with men?". The app's clinical-subject backstop
does not catch them. Q152 "Syphilis?" goes to clarification (acceptable). The other 7 are correct refusals.

### Retrieval with the planner's queries (production path, 178 questions with gold)
"Input" is the estimated model input in tokens (instructions + passages, from `scripts/brief.py`); it must stay
under `LLM_NUM_CTX=16384` minus the 1,200 output tokens, about 15,000.

| Run | Any gold | Held out Q153+ (of 36) | All gold | Input median / max |
|---|---|---|---|---|
| Question only (no planner) | 153 (86%) | 30 | 91 (51%) | 6,677 / 11,850 |
| **Production baseline** (top-k 6) | 156 (88%) | 33 | 93 (52%) | 6,849 / 12,342 |
| top-k 4 | 147 (83%) | 30 | 86 (48%) | 5,544 / 9,234 |
| top-k 8 | 160 (90%) | 34 | 98 (55%) | 8,231 / 14,761 |
| top-k 10 | 162 (91%) | 34 | 101 (57%) | 9,221 / **17,547 (over the limit)** |
| expand 3 seeds (`RETRIEVAL_EXPANSION_HITS=3`) | 156 (88%) | 33 | 94 (53%) | 6,639 / 12,342 |
| per-document cap 2 | 148 (83%) | 32 | 85 (48%) | 6,806 / 10,437 |
| per-document cap 4 | 155 (87%) | 32 | 98 (55%) | 6,852 / 12,526 |
| expansion off | 149 (84%) | 31 | 80 (45%) | 5,364 / 7,871 |
| expansion off, top-k 8 | 159 (89%) | 33 | 87 (49%) | 6,191 / 9,213 |
| semantic only | 144 (81%) | 32 | 88 (49%) | 6,812 / 12,225 |

- Keep hybrid search and expansion. `RETRIEVAL_EXPANSION_HITS=3` is free (same coverage, less text).
- Per-document cap 4 gets more of the passages a multi-part answer needs (all gold 52% -> 55%) at no context cost.
- top-k 8 gains on the held-out set too, but its largest inputs come close to the limit: it needs a cap on total
  passage length before it is safe. top-k 10 overflows; do not use.
- Ceiling (`rank_eval.json`): gold is in the hybrid top 50 for 174 of 178, so most misses are ordering: the reranker
  is the most promising retrieval change.

### Follow-up questions
Appending the previous question to short follow-ups found a gold passage in 4 of 7 made-up conversations, against 3 of 7
without it. That is a small gain on a small test. "And for children under 5?" after a household-contact TPT question still misses.

## Run log

| Time | Label | What | Result |
|---|---|---|---|
