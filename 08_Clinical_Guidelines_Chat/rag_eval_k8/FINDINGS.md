# RAG Evaluation (k=8): Row-by-Row Findings

Source: `copilot_results_k8.xlsx` (152 questions, 8 retrieved chunks each, Llama-generated answers, Llama judge scores).
Method: I compared every row's answer with the reference answer and checked the retrieved chunks to see whether the needed fact was actually there. Per-row grades, tags and notes are in `row_review.xlsx` (and `row_review_notes.tsv`).

## Headline numbers

| My grade | All 152 | Standard (Q001–Q108) | Edge cases (Q109–Q152) |
|---|---|---|---|
| Correct (incl. correct declines) | 52 (34%) | 40 | 12 |
| Partial | 51 (34%) | 38 | 13 |
| Wrong / failed | 49 (32%) | 30 | 19 |

- **9 answers are clinically unsafe**: Q003 (start ART on a self-test), Q046 (keep PrEP at CrCl 55), Q062 (treponemal tests for monitoring), Q063 (adult penicillin dose for a newborn), Q072 (5 RHZE tablets for 60 kg), Q104 (6H for MDR contacts), Q125 (affirms a phased-out TPT), Q140 (no PEP advice to a patient), Q142 (dose information in reply to a lethal-dose question).
- **Retrieval mostly worked; generation is the main bottleneck.** In 100 rows the retrieved chunks contained what was needed, yet only 44 of those answers were fully correct (36 partial, 20 wrong).
- **The Llama judge does not separate good answers from bad ones.** It gave exactly 5/10 to 41 of 49 wrong answers and 35 of 51 partial ones; it gave 10/10 to 5 wrong answers (e.g. Q075, an empty answer). My grade disagreed with it on 33 rows.

## Root causes, by number of rows affected (a row can have several)

| # | Root cause | Rows | Examples |
|---|---|---|---|
| 1 | **STI & Viral Hepatitis guideline is not indexed**: zero chunks from it across all 152 queries, although the model calls it "document 8" | 15 | Q058–Q068, Q103, Q119, Q126, Q146 |
| 2 | **Answers capped at ~4 paragraphs**: 110/152 answers are exactly 4 paragraphs; lists are cut after ~3 items or emptied | 14 | Q002, Q008, Q024, Q053, Q069, Q075 (empty), Q095, Q114 (empty) |
| 3 | **Table/chunk parsing**: merged cells lost, misaligned columns, "2022 vs 2024" two-column tables read as one, lists and headings split across chunks | 10 | Q040, Q104, Q006, Q010, Q037, Q098 |
| 4 | **Retrieval misses**: the chunk with the answer was not in the top 8 | 12 | Q003, Q030, Q032, Q035, Q046, Q073, Q148 |
| 5 | **Generator reasoning**: had the right chunk but misapplied it (table lookups, numeric thresholds, scenarios), or said "not stated" when it was | 32 | Q029, Q072, Q078, Q130, Q136, Q020 |
| 6 | **Version/conflict handling**: mixes superseded 2022 rules with 2024 ones, misses real conflicts, invents fake ones, sometimes prefers the older document | 7 | Q007, Q010, Q102, Q131, Q132 |
| 7 | **Hallucination**: invented numbers, document dates/versions, parametric medical "facts" | 11 | Q022, Q013, Q062, Q063, Q103 |
| 8 | **Degenerate output**: the same paragraph repeated 2–4×, echoing the question back, output-limit error | 16 | Q055 (4.9k chars), Q060, Q115, Q137, Q087 |
| 9 | **Answer hygiene**: irrelevant facts from off-topic chunks appended, "Source A says… Source B says…" narration instead of a synthesis | 16 | Q017, Q041, Q054, Q108 |
| 10 | **Edge-case behaviour**: never asks for clarification, accepts false premises, weak urgency, privacy overclaim, treats "Hi" as out-of-scope, refuses neutral comparisons | 22 | Q115, Q117, Q124, Q125, Q140, Q142, Q151, Q113, Q145 |

### Details worth knowing

- **Hub chunks.** A few Amendment chunks appear in almost every result: *PrEP F/U Visits* (p.12) in 44 queries, *TPT for LTBI* (p.38) in 37, *PrEP (re-)Initiation* (p.12) in 27, *ACRONYMS* (p.4) in 13. They take up slots the right chunk needed. The Amendment supplies 38% of all retrieved chunks.
- **Broken heading hierarchy in the Amendment.** Breadcrumbs like "CHAPTER 5: BASIC CARE PACKAGE … > 9.7 SECOND LINE ART" and "ACRONYMS > 3.1 HIV TESTING…" show that the parser nested most of the document under the wrong parents. This pollutes the embedded context.
- **Merged table cells.** In PrEP Table 10, "Age ≥16" spans all four product columns in the PDF but was parsed into the oral-PrEP column only, so the model concluded the ring has no age limit (Q040).
- **"2022 GUIDANCE | 2024 GUIDANCE" summary tables.** The model reads both columns as current. This produced self-contradictory answers (Q006: "bacteriologically confirmed" and "clinically diagnosed") and affirmed a phased-out regimen (Q125).
- **Lead-in sentences turned into headings.** "First Line: Any of these unless there are compelling contra-indications" became a breadcrumb, and the drug list ended up in a different chunk (Q098).
- **Same table chunk retrieved repeatedly.** For example, MHDG Table 13 came back 4× in Q057; ACRONYMS and REFERENCES chunks are retrieved for off-topic questions.
- **Small-model reasoning limits.** It picked the >70 kg column for a 60 kg patient (Q072), read "28 days" as "28 weeks" (Q130), called CrCl 55 "above threshold" (Q046), and failed to use "2-month-old" from the question (Q029).

### Reference-set corrections (my side)

- Q150 (asthma): their corpus includes the NCD pulmonology chapter, so my "not available" reference is wrong for this system. Replace it with the guideline's actual step-1 recommendation.
- The STI-based questions can't be judged fairly until that document is indexed.

## Recommendations, in priority order

1. **Index the STI & Viral Hepatitis guideline** (it's a .docx, so it may have been skipped by a PDF-only loader). Check that the document list in the system prompt matches what is actually in the index. This fixes ~15 rows directly.
2. **Remove the 4-paragraph cap.** Find it in the prompt, a `max_tokens` setting, or post-processing. Allow complete lists and tables, and ask for "concise but complete". Also find out why Q075/Q114 produced a list heading with no items, since something may be stripping bullet lines. This fixes ~14 rows.
3. **Use a stronger generator, or tune decoding.** In 56 of 100 rows the chunks were right and the answer wasn't. Try a larger model (e.g. a 70B-class Llama or a frontier model). Set low temperature, add a repetition penalty, and detect and regenerate looping output. Fix the output-limit error (Q087).
4. **Fix ingestion of tables and structure:**
   - Repeat spanning cell values into every column they cover.
   - Serialise each table row as self-contained text (e.g. "PrEP ring — Age: ≥16 years; Weight: —").
   - For "2022 vs 2024" tables, label the columns "SUPERSEDED (2022)" and "CURRENT (2024)", or index only the current column.
   - Rebuild the heading tree, keep lists whole, never turn a lead-in sentence into a heading, and strip footnote markers (e.g. "DTG2").
5. **Improve retrieval:**
   - Use hybrid search (BM25 + dense) with a cross-encoder reranker.
   - Down-weight or exclude acronym lists, TOCs, references and acknowledgements.
   - Remove duplicate chunks.
   - Add parent-section expansion: retrieve the small chunk, pass its full section to the model.
   - Attach document and version metadata, and route queries by topic (PrEP → PrEP 2025; TB → TB 2025).
   - For scenario questions, rewrite the query into its clinical entities before searching.
   - Skip retrieval for greetings and clearly off-topic messages.
6. **Rewrite the system prompt:**
   - Give one synthesised answer, not a summary per source.
   - Newer documents supersede older ones (give the document dates explicitly), and real conflicts get flagged.
   - Only say "not found" after checking every chunk, and never fill gaps with outside knowledge or invented numbers.
   - Leave out facts that don't answer the question.
   - Correct false premises.
   - Ask a clarifying question when a key variable is missing (drug, weight, age, viral load value, PrEP product).
   - Add safety rules: emergency-first answers, no lethal-dose information, PEP advice for exposures within 72 hours, no memory or PII claims.
   - Answer greetings with a short orientation.
7. **Fix the evaluation itself:**
   - Replace the 0/5/10 judge with a rubric of key facts per question (each fact present or missing, plus a contradiction or safety flag).
   - Use a stronger judge model.
   - Score retrieval separately from the answer ("is the key fact in the top k?" versus "is the answer faithful and correct?"), so fixes can be attributed.
   - Have a clinician spot-check the safety-critical rows.

Suggested order of work: items 1–2 are cheap and should recover ~25 rows. Then re-run and compare item 3 (model) against item 4 (ingestion), using the improved judge from item 7.
