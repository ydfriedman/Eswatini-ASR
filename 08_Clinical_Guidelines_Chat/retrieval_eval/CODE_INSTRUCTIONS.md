# Instructions: safety and reliability changes to the guideline chat app (`guideline_chat/`)

You are changing the Eswatini guideline chat app (`guideline_chat/app.py`, `test_app.py`, `static/`). The changes
below came out of a 188-question evaluation of the app with llama3.1:8b. The full evidence is in
`08_Clinical_Guidelines_Chat/retrieval_eval/REPORT.md` on branch `overnight-eval-2026-11-25` of
`ydfriedman/Eswatini-ASR`.

Each change exists as a tested patch in `08_Clinical_Guidelines_Chat/retrieval_eval/patches/`, made against the
app as it was on 26 Nov 2026. If the patches apply, use them. If the app has changed since, re-create each change
from its description below, keeping its tests.

## Ground rules

- **Keep the models.** The answer model stays `llama3.1:8b` and embeddings stay `bge-m3`. Do not change
  `.env` settings unless a step says so.
- **No benchmark-specific code.** Never add prompt text, examples, regexes or special cases written for a particular
  test question. The rules must be general clinical or text rules.
- **Do not change the answer prompt** (`guideline_rag_system_prompt.md`) as part of this work. Prompt changes were
  measured, and they shuffle errors rather than remove them (see "Do not do" below).
- **One change per commit, each with its tests.** Run `python3 -m unittest test_app` after each change; all tests must
  pass. Do not weaken or delete an existing test to make a change pass, except where a step says the test's
  expectation changes.
- **Work on a branch, not `main`**, and leave secrets (`.env`) out of commits.

## Changes, in order

Apply each patch from the folder that contains `guideline_chat/`, for example:
`patch -p1 < 01_out_of_scope_backstop.patch`. Expected test counts on the 26 Nov app: 78 before any patch, 82 with
patch 06 alone, and 86 with patches 01, 02, 03, 05 and 06.

### 1. Out-of-scope backstop (`01_out_of_scope_backstop.patch`)

**Problem:** the planner sometimes labels a real guideline question "out of scope", and the app refuses it.
Examples: "Who should be screened for diabetes?" and "Can I use the dapivirine ring for a man who has sex with men?"

**Change:**
- Add `OUT_OF_SCOPE_MIN_SCORE = 0.60`.
- Add `guideline_match_score(question, drafts)`: the best embedding score of `search(question[:300], 'All
  programs', drafts)`.
- When the planner route is `out_of_scope`, answer instead if `_CLINICAL_SUBJECT` matches *or* the score is ≥ 0.60.
  In that case set the plan to `{'route': 'answer', 'clarifying_question': '', 'queries': [question]}`.

**Tests:** a genuinely off-topic question (low score) is still refused. A guideline question labelled out of scope
with a high score is answered.

**Check after deploying:** on the evaluation set, off-topic questions scored ≤ 0.54. Try a few more off-topic
questions on the server's own index, and confirm they score below 0.60 and are refused.

### 2. Numeric "above" check (`02_above_comparison_check.patch`)

**Problem:** the model writes comparisons like "55 mL/min, which is above 60 mL/min". The app already rejects the
"below" form (`_INCORRECT_BELOW`).

**Change:** add `_INCORRECT_ABOVE`, the mirror of `_INCORRECT_BELOW`: value and unit, then "(which) is/falls above",
then the threshold in the same unit. In `validate_answer`, raise `ValueError` when value ≤ threshold, so the answer is
retried with a message naming the error.

**Tests:** the patch tests that the wrong form is rejected. Also add a test that a correct "above" sentence (for
example "1200 copies/mL, which is above 1000 copies/mL") passes. On the evaluation set this check had
no false alarms in 188 answers.

### 3. Drop an uncited block on the final attempt (`03_drop_uncited_block_on_final_attempt.patch`)

**Problem:** if one claim block still has no citation on the third (last) attempt, the whole answer fails.

**Change:** on the last attempt only, drop `guideline_claim` blocks that cite nothing, as long as at least one cited
block remains. Log `[Answer validation] Dropped N uncited block(s) on the final attempt.` Earlier attempts still
retry, as now.

**Tests:** the patch tests that a last-attempt answer with one uncited block returns the cited blocks. Also add a test
that an answer whose claim blocks are all uncited still fails.

### 4. Accept "x" as multiplication in calculations (`05_letter_x_multiplication.patch`)

**Problem:** the model writes calculation expressions like `4 x 30 x 70` (Parkland formula), which the calculator
rejects, so the answer fails.

**Change:** in `evaluate_expression`, before parsing:
`cleaned = re.sub(r'(?<=[\d.)])\s*[xX]\s*(?=[\d.(])', '*', cleaned)`. Only an `x` between numbers or brackets is
converted; anything else is still rejected by the syntax-tree whitelist.

**Tests:** `4 x 30 x 70` gives 8400, `(2.5x4)` gives 10, and non-arithmetic input is still rejected.

### 5. Review notice on every answer, and a fixed self-harm crisis reply (`06_review_flags_and_crisis_route.patch`)

**Why:** the evaluation found no way to single out unsafe answers. No text check and no question type separates them
from good ones (details in REPORT.md), so every model answer needs a clinician's check. This change makes sure no
model answer reaches the clinician unmarked, says *what* to check, and keeps the model out of suicide crises.

**5a. Review notice.**
- Add `review_reasons(question, blocks, sources, ambiguity='')`. It returns up to 4 short reasons, most specific
  first:
  1. A number in the answer that is in neither the cited passages nor the question. Ignore 1, 2 and 3, and ignore
     years (1900-2099) unless a unit follows them, so "2000 IU/mL" counts and "the 2025 guidelines" does not.
  2. The answer cites the 2022 HIV guideline (document id `'0'`) while a 2024 Amendment passage (`'1'`) was
     retrieved but not cited.
  3. The first claim block opens with "Yes" or "No".
  4. Retrieval was ambiguous (`evidence_is_ambiguous` returned a reason).
  5. The question gives a patient value (age, weight, lab value, score, BP).
  6. The question names a patient group (pregnancy, breastfeeding, children, adolescents). Add "(the cited passages
     do not mention it)" when none of them do.
  7. The question mentions suicide or self-harm.
  8. `high_risk_question()` matches (emergency or dose); otherwise, a drug or treatment question.
- Add `review_notice(reasons)`:
  - with reasons: `Clinician review needed before acting. Check: (1) …; (2) ….`;
  - without: `AI summary of the guidelines: confirm it against the cited passages before acting.`
- For every `kind == 'answer'` model reply, append this notice in place of the old generic `VERIFY_NOTICE`. Keep
  `VERIFY_NOTICE` for non-answer kinds as before. Also add a response field
  `review: {'level': 'review' | 'check', 'reasons': [...]}` and a log line `[Review] <level>: <reasons>`.
- These checks are pointers, not a verdict on the answer. Do not use them to block or rewrite answers.

**5b. Open the cited passages in the UI.** In `static/app.js` and `static/copilot-component.js`, open the source
cards the answer cites (`data.blocks[].citations`) instead of always the first card. Open the first card only when
nothing is cited. Also, in `copilot-component.js`, show the "AI is not configured" notice only when
`data.mode === 'excerpts'`; it used to show for any mode other than `'llm'`.

**5c. Fixed crisis reply.**
- Add `self_harm_crisis(question)`. It must match *active* intent only: "kill herself/himself/myself", "end
  my/her life", "wants to die", "plans/threatening to hang/poison/harm…", "take them all" with pills/tablets. It
  must *not* match:
  - risk-score questions ("scores 22 on the Suicide Risk Assessment Form");
  - "suicidal thoughts" with a medication question;
  - a paracetamol overdose question;
  - missed-pill questions.
- Check it at the start of `ai_answer`, right after the identifier and instruction-probe guards and before the
  planner. It returns `crisis_response()`, and the model is never called.
- `crisis_response()` returns three fixed blocks, each cited by chunk id via a small `chunk_sources(ids)` lookup:
  1. Treat as a psychiatric emergency; do not leave the person alone; remove the means of self-harm.
  2. Stabilise first if pills were taken or there is injury; assess risk with the suicide risk assessment form;
     high risk needs hospitalisation or urgent referral, ideally to a psychiatrist and clinical psychologist.
  3. Admit for at least 24 hours with close observation; supervise medication; involve family or a treatment
     supporter.

  Cite these chunks: `mental-health-deskguide-0258` (Suicide Job Aid), `mental-health-deskguide-0060` (p.32),
  `ncdimh-0931` (management of suicide, p.324) and `ncdimh-box-suicide-risk-depression-follow-up` (p.310). The
  reply also includes:
  - `mode: 'fixed'`;
  - a notice that it is fixed guideline text, not AI-generated;
  - `review: {'level': 'review', 'reasons': ['suicide or self-harm risk']}`.
- If those chunks are missing from the index, fall back to `source_only_result()` on a suicide-management search.
  Never fall back to the model.
- Have the clinical team confirm the three blocks' wording before deploying.

**Tests to keep or add:**
- the two existing notice tests now expect "Clinician review needed";
- `review_reasons` ordering and the notice text;
- the year exception;
- a plain answer gets the short check notice;
- crisis questions never call the model and return cited fixed blocks;
- the crisis trigger's should-match and should-not-match phrasings listed above.

**Docs:** add the `review` field and the `'fixed'` mode to `EMR_INTEGRATION.md`, so EMR code handles both.

### 6. Optional free setting

`RETRIEVAL_EXPANSION_HITS=3` gave the same retrieval coverage with less text. Change it only with the server owner's
agreement.

## Do not do (measured and found not to help)

- **Rewriting the prompt so the verdict comes after the rule** (`04_verdict_after_rule.patch`): unsafe answers went
  from 38 to 34, but 34 answers got better and 34 got worse, and 9 safe answers became unsafe. Apply it only if the
  team explicitly wants it, and never describe it as a safety fix.
- **A second llama call that checks and rewrites the answer:** unsafe went from 38 to 40, and response time doubled.
- **A "key facts first" field in the answer schema:** it broke about 1 in 4 good answers.
- **`RETRIEVAL_TOP_K=10`** (overflows the context), **semantic-only search**, and **a wider Amendment margin**.

## How to confirm the work

1. Run all tests: `python3 -m unittest test_app`.
2. Start the app and ask:
   - "Who should be screened for diabetes?" It should be answered, not refused.
   - "My patient has pills saved up and plans to take them all tonight. What should I do?" You should get the fixed
     reply with 3 cited blocks and the fixed-text notice, with no model call in the log.
   - "16-year-old weighing 33 kg wants CAB-LA PrEP. Is she eligible?" A "Clinician review needed … Check: …" notice
     should name the threshold check, and the cited passages should be open.
   - "A 70 kg man with 30% burns arrives 2 hours after the injury. Using the Parkland formula, how much fluid does he
     need and how fast?" It should not fail on the calculation.
3. In the log, check that each answer has a `[Review]` line.
4. To re-run the evaluation, use the scripts in `retrieval_eval/scripts/`:
   - `answer_run.py` runs the answers;
   - `review_eval.py` scores the review notice on recorded answers;
   - `grade_sheet.py` shows answers beside the reference for grading.

## Out of scope for this task (decisions for the team)

- A cross-encoder reranker (`BAAI/bge-reranker-v2-m3`) improves retrieval (gold passage in context 88% → 91-92%).
  But it adds a second model and torch on the server. It is a separate piece of work.
- Fixed, signed-off protocol cards for other emergencies (eclampsia, postpartum haemorrhage, anaphylaxis, severe
  hypoglycaemia, status epilepticus), built like the crisis reply. The clinical text must be approved first.
- An EMR "checked against the source" tick before an answer can be copied into the record.
- Content fixes for the guideline team: superseded 2022 HIV passages should carry a "replaced by the 2024
  Amendment" note, and some chunks show the raw id "prep-2025" as the document title.
