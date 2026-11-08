# Chunk validation sample

189 chunks from `chunks_v2`, weighted toward risky tables and safety-critical content.

| File | What it is |
|---|---|
| `chunk_validation.xlsx` | Where you record verdicts. **How to validate** has the instructions; **Review** has one row per chunk (yellow columns are dropdowns); **Summary** counts your verdicts. |
| `chunk_viewer.html` | The same 189 chunks with tables laid out properly. Open it in a browser next to the PDF. Empty table cells are hatched. |
| `build_validation_sample.py` | Rebuilds both files (fixed random seed, so the result is the same each time). |

Rows are sorted by document, then PDF page, so you can work through each PDF once, front to back.

| Why picked | Rows | Priority |
|---|---|---|
| Possible merged cells that were **not** filled (your verdict decides) | 31 | A |
| Merged cells that were filled automatically | 29 | A |
| Safety-critical tables (doses, weight bands, contraindications) | 32 | A |
| Safety-critical text (doses, emergency steps) | 20 | A |
| Sources of the new benchmark reference answers | 22 | A |
| Tables with formatting risk (blank cells, ragged rows, merged headers) | 20 | B |
| Safety flowcharts | 15 | B |
| Random baseline, 2 per document (gives a general error rate) | 20 | C |

When you are done, your "Merged" verdicts go into `VERIFIED_HV` in `chunks_v2/scripts/fix_tables.py`, and any Major issues become fixes in the build.

## v3 sample (re-extracted chunks, all ten guidelines)

`build_validation_v3.py` → `chunk_validation_v3.xlsx` + `chunk_viewer_v3.html`: 50 items (core 25 + next 25) from `chunks_v3`, regenerated on 8 Nov 2026 after the image second pass
(HIV 2022, HIV Amendment 2024, NCDIMH, PrEP 2025, ANC, STI/VH draft, Linkages SOP, TB 2025, FP 2021, Mental Health desk guide). At most 7 items per document; every document has at least one.
One row per re-extracted table/flowchart (embedding parts collapsed), plus text chunks.

| Core-set category | Items |
|---|---|
| Items carrying a clinically significant source flag (is the guideline problem real?) | 6 |
| Dosing tables transcribed from page images | 5 |
| Rebuilt tables the second pass left unchanged (most compared with the image, some only by text) | 4 |
| Rebuilt tables corrected in the second pass | 3 |
| Flowcharts kept from the old parse | 3 |
| Safety-critical text chunks | 2 |
| Random baseline | 2 |

"How produced" is derived from the batch files in `table_reextract/batches` (second-pass batches: tb_b10, mh_b05, fp_b04-b05, lk_b04); the Summary sheet counts Major issues per method.
Tables known not to have been compared with the page image in the second pass: Mental Health Table 25 (p.72); Linkages role tables pp.43-60 not changed (judged by content length); FP advantages/disadvantages tables pp.46-94 (checked by text).
