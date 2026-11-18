# Chunk validation sample (chunks_v3)

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
Tables the second pass had judged only by text or length (Mental Health Table 25; Linkages role tables pp.43-60; FP advantages/disadvantages tables pp.46-94) were compared with the page images on 10 Nov 2026: content matched in every case (cosmetic fixes only, batches mh_b06 and lk_b06).

The earlier 189-chunk sample of `chunks_v2` (no verdicts recorded) was removed; it is in git history.
