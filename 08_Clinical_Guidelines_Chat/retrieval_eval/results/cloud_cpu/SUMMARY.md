# Cloud CPU runs (26 Nov 2026)

These runs used the app as received on 26 Nov (`app_snapshot/guideline_chat`), chunks `chunks_v3` (3,200), bge-m3 and llama3.1:8b in Ollama, on a 4-core Linux CPU with no GPU.

**What is in here:** retrieval only, with the **question as the only search query** (the planner is not used). Each run records which passages would reach the answer model. The scores are from `scripts/score.py`.

**What is not in here:** answers.
- On this machine, llama's planner calls slowed from about 10 s to about 3 minutes each once the other runs were competing for the 4 CPU cores. A full answer baseline would have taken more than a day.
- The local Ollama server then hit the 2-hour limit for background tasks and stopped.
- `planner_partial.json` therefore holds llama's real planner output for Q001 to Q026 only.
- The `AMENDMENT_SCORE_MARGIN=0.15` run did not finish.
- Answer quality and planner queries are left to the Mac session (`OVERNIGHT_PLAN.md`).

## Results

The table covers the 178 questions that have gold passages. "Any" means at least one gold passage reaches the model; "all" means every gold passage does. Context is the tokens of passages sent (median / max).

| Run (file) | Settings | Any gold | All gold | Held out Q153-188: any / all | Context med / max |
|---|---|---|---|---|---|
| `deployed_q` | top-k 6, expansion on, hybrid, margin 0.08 | 153 (86%) | 91 (51%) | 83% / 67% | 3,093 / 12,897 |
| `q_top4` | top-k 4 | 148 (83%) | 85 (48%) | 83% / 67% | 2,076 / 12,209 |
| `q_top8` | top-k 8 | 154 (87%) | 92 (52%) | 83% / 67% | 4,070 / 13,582 |
| `q_top10` | top-k 10 | 156 (88%) | 93 (52%) | 83% / 67% | 4,839 / 15,563 |
| `q_noexpand` | expansion off | 152 (85%) | 79 (44%) | 83% / 61% | 2,117 / 8,955 |
| `q_noexpand_top10` | expansion off, top-k 10 | 154 (87%) | 83 (47%) | 83% / 61% | 3,687 / 11,963 |
| `q_semantic` | semantic only (no keyword search) | 146 (82%) | 88 (49%) | 81% / 64% | 3,208 / 12,579 |
| `q_hits3` | expand 3 seeds instead of 5 | 154 (87%) | 91 (51%) | 86% / 67% | 2,747 / 12,897 |
| `q_margin004` | Amendment margin 0.04 | 152 (85%) | 91 (51%) | 83% / 67% | 3,105 / 12,897 |

`rank.json` is the ceiling check: the rank of the best gold passage among all chunks before any caps.

| Ranking | Top 1 | Top 6 | Top 20 | Top 50 |
|---|---|---|---|---|
| Semantic | 89 | 145 | 158 | 170 |
| Keyword | 94 | 139 | 162 | 169 |
| Hybrid | 109 | 149 | 166 | 174 |

## What this says

1. **The current settings are close to the best these knobs allow.**
   - Going from 6 to 10 sources adds only 3 questions with a gold passage, and none in the held-out set.
   - It also raises the largest context to about 15,600 tokens, which is too close to `LLM_NUM_CTX=16384` once the prompt is added.
   - Keep top-k 6. Top-k 8 is a reasonable try only if the answer step copes with more text.
2. **Keep section expansion.** Turning it off lowers "all gold" from 51% to 44%. It mostly hurts questions whose answer spans several passages (TB 27% → 18%, STI 57% → 36%).
3. **Keep hybrid search.** Semantic alone loses 7 questions.
4. **Expanding 3 seeds instead of 5 (`RETRIEVAL_EXPANSION_HITS=3`) is a free saving.**
   - Coverage is the same, and 1 more held-out question gets its gold passage.
   - The median context is about 350 tokens smaller.
   - This is worth confirming with answers.
5. **The remaining misses are ordering problems, not search problems.**
   - Gold is in the hybrid top 50 for 174 of 178 questions, but in the top 6 for only 149.
   - A reranker over about 30 candidates is the most promising next step (experiment 4 in the plan).
6. **"All gold" is low for TB (27%) and HIV testing/treatment (31%).** These questions need several passages: a reranker or a per-document cap that lets more of one guideline through could help, and should be tested.
7. **Planner (Q001-Q026 only):** llama routed Q002, a clinical question, as `out_of_scope`. The app's clinical-subject check overrides this in production, so it is a planner weakness rather than a user-facing failure.
