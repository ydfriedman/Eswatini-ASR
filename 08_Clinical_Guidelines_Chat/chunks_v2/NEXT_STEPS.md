# Next steps: testing chunks v2

1. **Re-index from scratch** with `chunks.jsonl` (3,805 chunks). Embed `embed_text`; for diagrams you can try `narrative_embed_text` instead. Store `chunk_id`, `doc_id`, `heading_path`, `section_id`, `parent_section_id`, `prev_chunk_id`, `next_chunk_id` and the pages as metadata. Don't mix in v1 vectors.
2. **Confirm STI is indexed.** Count the vectors with `doc_id = sti-vh-draft-2026`; it should be 330. Then search "syndromic treatment of urethral discharge" and check that STI chunks come back.
3. **Baseline.** Re-run the 152 questions with the v1 settings (k=8, same prompt), changing only the chunks. Save the results next to the k=8 run.
4. **Add neighbourhood retrieval** (code in README, *Expansion*). For each of the top 3–5 hits, add its section, or its parent section if the section is under ~250 tokens. If that is over ~1,200 tokens, add just the previous and next chunk instead. Remove duplicates and keep document order. Re-run the 152 questions.
5. **Prompt changes**, then re-run:
   - remove the 4-paragraph cap;
   - cite the guideline and section for each claim;
   - copy doses and thresholds exactly as written in the table;
   - say so when the guidelines don't cover a question, and ask when a question is ambiguous.
6. **Optional:** hybrid search (BM25 + vectors) for drug names, acronyms and numbers. Use `glossary.jsonl` to expand acronyms in queries.
7. **Compare runs one change at a time** (steps 3 → 4 → 5 → 6). Watch the STI questions, Q037 (PrEP products), Q040 (PrEP eligibility) and Q046, and score retrieval separately from answer quality.
8. **Tables:** review `logs/table_span_candidates.csv`. Mark each row merged or blank, add the confirmed chunk ids to `VERIFIED_HV` in `scripts/fix_tables.py`, and rebuild (command in README).

Known limits are listed in the README under *Caveats*.
