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

## v3 sample (re-extracted chunks, eight guidelines)

`build_validation_v3.py` → `chunk_validation_v3.xlsx` + `chunk_viewer_v3.html`: 50 items (core 25 + next 25), chosen from a pool of 200 from `chunks_v3`
(HIV Amendment 2024, NCDIMH, PrEP 2025, ANC, Linkages SOP, TB 2025, FP 2021, Mental Health desk guide).
One row per re-extracted table/flowchart (embedding parts collapsed), plus text chunks.

| Priority | Why picked |
|---|---|
| A | Tables rebuilt from old chunks with doses/criteria (cell placement not auto-checked); dosing tables transcribed from page images; items carrying clinically significant source flags |
| B | Flowcharts kept from the old parse; other rebuilt tables; safety-critical text chunks |
| C | Random baseline per document (2 items + 2 text chunks) |

"How produced" is derived from the batch files in `table_reextract/batches`; the Summary sheet counts Major issues per method.

The set leaves out tables that the automatic completeness audit (`table_reextract/audit_cell_positions.py`, `classify_missing.py`)
found incomplete; those are listed in `table_reextract/audit/REPAIR_WORKLIST.md` and repaired from page images. Core 25: 9 items with
source flags, 5 hand-transcribed dosing tables, 4 audit-clean rebuilt tables (to test the audit), 3 old-parse flowcharts, 4 text chunks.
