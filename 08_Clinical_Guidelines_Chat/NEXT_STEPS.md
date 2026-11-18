# Guideline chat: next steps

Last updated 16 Nov 2026. Code for each change is in `app_review/app_py_changes.md` (section numbers below);
background and test results are in `APP_REVIEW_NOTES.md`.

## Where things stand
- Running qwen2.5:14b (10 GB, 100% GPU, context 8192) with bge-m3 on the CPU; both stay loaded. Measured 13-21 s per
  answer after the CPU-embedding fix, accepted in favour of accuracy.
- In place: prompt v2 with the cotrimoxazole examples, shorter response contract, generation settings, repeated-
  sentence check, source-talk check, clarification blocks stripped from answers, token logging, embeddings on CPU.
- qwen2.5:14b fixed the 8B safety error (VIA every 2 years, not 5) and reads tables far better. The remaining gaps are
  mostly retrieval: the cervical summary table was missed while unrelated 2024 Amendment passages took slots.

## Next session: apply together, then retest
- [ ] Add a relevance check to the extra 2024 Amendment search (section 7). Code change only: no chunks are deleted,
      and the Amendment is still searched like every other document.
      Today, whenever any HIV 2022 passage is retrieved, `ai_answer()` runs a second search of the Amendment alone
      and adds its top 2 hits per query, however unrelated (this is so newer guidance sits beside the 2022 text it
      replaces). For "Who should be screened for cervical cancer?" that put two HIV-testing passages into the 5
      source slots and pushed out the cervical summary table. The change keeps that extra search but only adds an
      Amendment passage if its similarity score is close to the best passage the main search found
      (`AMENDMENT_SCORE_MARGIN`, default 0.08). Tune the margin by printing the scores for questions where the
      Amendment matters (HIVST consent age, CrAg threshold, viral load) and where it doesn't (cervical screening).
- [ ] One retrieval slot per split table (section 8).
- [ ] Check `app.py` has the wider source-talk pattern (catches "this source", "the sources").
- [ ] Pin in `.env`: `LLM_MODEL=qwen2.5:14b`, `LLM_NUM_CTX=8192`, `LLM_NUM_PREDICT=1200`, `EMBEDDING_NUM_GPU=0`,
      and `RETRIEVAL_TOP_K` (try 6-8; answer calls use ~3,500 of 8,192 tokens).
- [ ] Send only the last ~6 history messages.
- [ ] Restart the app, then rerun the five test questions with `--sources`:
  1. Who should be screened for cervical cancer?
     (expect: start at 25, or at HIV diagnosis; stop after 50 with 2 negative screens; HPV every 3/5 years or VIA
     yearly/every 2 years)
  2. How often do I screen a 35-year-old HIV-negative woman if we don't have HPV testing? (VIA every 2 years)
  3. 32-year-old woman living with HIV: VIA positive, small lesion, whole transformation zone visible. What now?
     (same-day ablation; repeat VIA at 12 months)
  4. 38-year-old HIV-negative woman, VIA positive, lesion covers about 80% of the ectocervix, nothing looks like
     cancer. Can I treat her today? (no; refer for LEEP; follow-up at 6 months)
  5. Adult living with HIV, CD4 280. Does he need cotrimoxazole? (yes, CD4 ≤350; no closing question)

## Smaller, when convenient
- [ ] Retry message: `f'{exc} Fix this in the new answer.'` instead of the citation-only reminder.
- [ ] STI draft flag: check what `drafts` the web app and `chat.py` pass before setting it, or the STI guideline
      drops out of search.
- [ ] Try loosening the per-document (3) and per-page (2) retrieval caps.
- [ ] Short follow-ups (12 words or fewer) also search the previous question; can pull in an old topic.
- [ ] Log `prompt_eval_duration` / `eval_duration` per call for a real timing breakdown.

## Going forward
- [ ] Benchmark: clinicians review the 188 questions (`benchmark_review/clinician_review.html`); then run all of them
      for a baseline score and re-run after every change (runner script still to write).
- [ ] Send `SOURCE_ISSUES.md` to the guideline authors (cervical algorithm vs tables, PrEP row, three pyridoxine doses
      and others that make the chat give conflicting answers).
- [ ] Add sources: 2021 Standard Treatment Guidelines and Essential Medicines List (adult and paediatric) and the 2018
      Neonatal Care Clinical Guidelines, through the same chunking pipeline and checks.
- [ ] Later: stream answers as they are written; retest other models only if quality plateaus.
