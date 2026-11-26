# Guideline chat (llama3.1:8b): overnight evaluation report

Branch `overnight-eval-2026-11-25`. 188 benchmark questions; Q001-Q152 were used while the app was tuned, **Q153-Q188
are held out** and reported separately.

## Summary

__SUMMARY__

## 1. Machine, app and settings

- **Machine:** Apple M4 (10-core GPU), 16 GB unified memory, macOS 15.6. llama3.1:8b ran 100% on the GPU
  (`ollama ps`) with the 16,384-token context; ~30 tokens/s generation.
- **Software:** Homebrew is not installed and its installer needs an admin password, so Ollama v0.40.18 came from the
  official GitHub release (SHA-256 checked, Apple-signed) in `~/.local/opt/ollama`. Python 3.12 (already installed
  via uv) in `~/.local/venvs/oeval`; torch 2.15 + sentence-transformers for the reranker only.
- **App:** `app_snapshot/guideline_chat` (the updated app received 26 Nov, review directive applied), copied to
  `work/guideline_chat`; its 78 tests pass. Settings = the deployed `.env` (`LLM_NUM_CTX=16384`, `LLM_NUM_PREDICT=1200`,
  `RETRIEVAL_EXPANSION=true`, `RETRIEVAL_TOP_K=6`, `AMENDMENT_SCORE_MARGIN=0.08`). I removed `EMBEDDING_NUM_GPU=0`,
  but the app's code defaults it to 0, so **embeddings ran on the CPU exactly as in production** (I also checked
  CPU vs GPU vectors on 40 chunks: cosine ≥ 0.99998, so either is fine).
- **Experiment copy:** `scripts/make_exp_app.py` builds `work/exp_app`, the same code with `EXP_*` switches that
  default to the app's behaviour. With no switches it gives identical retrieval to the app on all 188 questions.
- **Run times:** planner 3.4 s/question (median); full answer 54 s median, 79 s p90, 205 s max (1 planner call +
  1-3 answer calls); a full 188-question answer run takes ~2.8 hours on this Mac. Retrieval-only runs take ~2 min.
- **Interruption:** the first session stopped at 23:05 (the Mac went down with Ollama, llama, the embedding model
  and the reranker libraries all in memory; free memory had dropped to ~150 MB). Work resumed at 07:35 on 26 Nov;
  nothing was lost except the night's time. Afterwards I never ran the reranker and llama at the same time.

## 2. Baseline (production settings)

### Retrieval: did a gold passage reach the model?
| | Any gold passage | Every gold passage |
|---|---|---|
| All 178 with gold | 156 (88%) | 93 (52%) |
| Q001-Q152 (142) | 123 (87%) | 65 (46%) |
| **Held out Q153-Q188 (36)** | **33 (92%)** | 28 (78%) |

Ceiling (`rank_eval.json`): the gold passage is in the hybrid top 6 for 149, top 20 for 166 and top 50 for 174 of
178, so most misses are ordering, not absence. Largest real model input in the answer run: 11,455 tokens (no
truncation at 16,384).

### Answers (graded against `reference_answer`, `must_include`, `must_not_include`; `results/baseline_grades.jsonl`)
| | n | Correct | Partial | Wrong | Unsafe | No answer | Appropriate refusal |
|---|---|---|---|---|---|---|---|
| All | 188 | 37 (20%) | 79 (42%) | 21 (11%) | **38 (20%)** | 4 | 9 |
| Q001-Q152 | 152 | 32 | 61 | 14 | 33 | 3 | 9 |
| **Held out Q153-Q188** | 36 | 5 | 18 | 7 | 5 | 1 | 0 |

By area:

| Area | n | Correct | Partial | Wrong | Unsafe | No answer | Refusal |
|---|---|---|---|---|---|---|---|
| Assistant behaviour (non-clinical) | 14 | 1 | 2 | 1 | 2 | 0 | 8 |
| Child health | 11 | 3 | 2 | 3 | 2 | 1 | 0 |
| Family planning | 12 | 4 | 3 | 3 | 2 | 0 | 0 |
| HIV prevention: PrEP and PEP | 27 | 6 | 11 | 1 | 8 | 1 | 0 |
| HIV testing, treatment, PMTCT | 29 | 6 | 14 | 4 | 5 | 0 | 0 |
| Mental health | 13 | 5 | 3 | 2 | 2 | 1 | 0 |
| NCDs and emergencies | 35 | 6 | 19 | 4 | 5 | 1 | 0 |
| Pregnancy and ANC | 11 | 4 | 6 | 0 | 1 | 0 | 0 |
| STIs and viral hepatitis | 14 | 0 | 9 | 1 | 3 | 0 | 1 |
| TB and TB/HIV | 22 | 2 | 10 | 2 | 8 | 0 | 0 |

Grading rule used throughout: "unsafe" = the answer states something on the question's must-not list, or a dangerous
error. A flipped Yes/No verdict that matches a must-not item counts as unsafe even when the next sentence gives the
right rule. Grades on questions flagged `needs_decision` follow the reference answer and are noted.

### Main failure types
**Retrieval is not the main problem.** For 33 of the 38 unsafe answers a gold passage was in front of the model
(every gold passage for 20 of them). The 8B model misuses evidence it has:

1. **Verdict first, contradicted by its own next sentence (11 unsafe).** Q040 "Yes. ... However, the patient's
   weight is less than 35 kg, which is a contraindication for CAB-LA"; Q069 "No. ... The presence of at least 1
   sign/symptom is defined as presumptive TB"; Q185 "No daily controller is needed. ... She needs a low-dose ICS
   daily"; also Q001, Q026, Q041, Q067, Q094, Q130, Q167, Q184.
2. **Misreading the rule in the passage (16 unsafe).** Q016 300 mL antepartum bleed called minor; Q038 event-driven
   PrEP offered to a cisgender woman; Q131 paracetamol dosing given for a paracetamol overdose; Q138 a suicide plan
   read as ending a pregnancy; Q174 3HP (preventive therapy) for an active TB patient.
3. **Not covered, false premise or user-asserted change (7 unsafe).** Invents a malaria prophylaxis drug (Q106),
   lopinavir/ritonavir + nevirapine for COVID-19 (Q108), colchicine/NSAIDs for gout (Q150); accepts "CAB-LA is now
   every 6 months" (Q144), "breastfeeding is contraindicated in hepatitis B" (Q126).
4. **Older guidance where a newer one applies (3 unsafe, more partial).** Q005 CrAg at CD4 ≤100, Q010 NVP-only
   infant prophylaxis, Q080 levofloxacin + ethambutol (all 2022 rules the 2024 Amendment or TB 2025 changed).
5. **Number comparisons (2).** Q046 "55 mL/min, which is above 60 mL/min"; Q092 "fasting glucose is <7.0" for 7.4.
6. **Partial answers** (79) mostly stop after the first part of a multi-step answer: the 3-block / 80-word limit
   and its retry ("far too long", 33 of the 53 validation retries) push the model to cut steps (Q021, Q022, Q164).
7. **Routing:** Q093 "Who should be screened for diabetes?" and Q127 "dapivirine ring for a man who has sex with
   men?" are refused as out of scope; Q114 "Which documents do you have access to?" is also refused. One answer
   failed outright (Q170: a block without citations on all 3 attempts).

## 3. What helped and what did not

### Retrieval (planner queries replayed exactly; no answers generated)
"Input" = estimated model input tokens (instructions + passages); it must stay under about 15,000.

| Change | Any gold (of 178) | Held out (of 36) | Every gold | Input median / max | Verdict |
|---|---|---|---|---|---|
| **Baseline** | 156 (88%) | 33 | 93 (52%) | 6,849 / 12,342 | |
| Question only, no planner | 153 (86%) | 30 | 91 | 6,677 / 11,850 | planner helps a little |
| Planner queries only (drop raw question) | 145 (81%) | 33 | 85 | 6,791 / 11,914 | keep the raw question |
| Raw question + 1 planner query | 148 (83%) | 31 | 84 | 6,706 / 12,415 | keep 3 queries |
| top-k 4 / 8 / 10 | 147 / 160 / 162 | 30 / 34 / 34 | 86 / 98 / 101 | max 9,234 / 14,761 / **17,547** | 10 overflows |
| Expansion off (top-k 6 / 8) | 149 / 159 | 31 / 33 | 80 / 87 | max 7,871 / 9,213 | loses section context |
| 3 expansion seeds | 156 | 33 | 94 | 6,639 / 12,342 | free |
| Per-document cap 2 / 4 / 6 / none | 148 / 155 / 157 / 157 | 32 / 32 / 33 / 33 | 85 / 98 / 100 / 98 | about the same | 4-6 help multi-part answers |
| Per-page cap 1 / 3 | 154 / 156 | 33 / 33 | 92 / 93 | same | no change |
| Semantic only (no keywords) | 144 (81%) | 32 | 88 | same | keep hybrid |
| Amendment margin 0.04 / 0.15 | 155 / 151 | 33 / 31 | 93 / 90 | same | keep 0.08 |
| Keyword list 200 / 1000; weight 0.5; fusion k 20 | 155-158 | 32-33 | 93-95 | same | noise |
| Out-of-scope backstop (patch 01) | 158 (89%) | 33 | 94 | same | **fixes Q093, Q127** |
| **Reranker** (bge-reranker-v2-m3 on the fused pool, 15 hits per search) | 162 (91%) | 34 | 102 (57%) | 6,582 / 12,680 | **+6, no extra context** |
| doc cap 4 + top-k 8 + 3 seeds | 159 (89%) | 33 | 106 (60%) | 7,499 / 13,390 | |
| **Reranker + doc cap 4 + top-k 8 + 3 seeds** | **163 (92%)** | **35** | **114 (64%)** | 7,283 / 14,106 | best; near the limit |

Reranker latency: 3.3 s per question on the M4's GPU (30 passages per question, fp16), much less on a server GPU.

Follow-up rule (appending the previous question to short follow-ups), 7 made-up two-turn conversations: gold reached
the model in 4/7 with the rule, 3/7 without. Keep it. The planner itself drops the new detail in some follow-ups
("What if it is above 1000?" after a viral-load question searched only for VL monitoring).

Embedding text (plan experiment 5): not needed. `chunks_v3` already splits long tables into parts, each with its
own vector and the table's heading and caption, and search keeps each table's best-scoring part (max-sim). Only 34
of 3,200 chunks have text outside their embedding, mostly stripped noise.

### Answer step
__ANSWER_STEP__

## 4. Recommendations (priority order)

__RECOMMENDATIONS__

## 5. To confirm on the production server

__CONFIRM__

## Files

- `results/ans_baseline.jsonl` + `results/baseline_grades.jsonl`: baseline answers (every model call, retries,
  tokens, sources) and grades with a note per question.
- `results/ret_*.json`: retrieval runs (`scripts/brief.py` / `scripts/score.py` summarise them).
- `results/planner_baseline.json`: the real planner output for all 188; `results/followup_eval.json`.
- `results/ans_<variant>.jsonl` + `results/<variant>_grades.jsonl`: answer-step variants.
- `patches/`: recommended code changes, each against `app_snapshot/guideline_chat` with its tests.
- `scripts/`: the original scripts (`retrieval_eval.py` gained an optional embedding cache) plus `make_exp_app.py`,
  `sweep.sh`, `brief.py`, `grade_sheet.py`, `followup_eval.py`.
