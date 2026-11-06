# Table and flowchart re-extraction

Chunk validation showed that most tables had lost their structure in the LlamaParse markdown (merged cells, section rows, notes spanning several rows), and some flowcharts had wrong branches. This folder re-extracts tables, highlighted boxes and flowcharts from the PDF page images, one guideline at a time.

**Progress**

| Guideline | Status | Items | Review page |
|---|---|---|---|
| HIV Amendment 2024 | Complete | 36 (18 tables, 2 boxes, 16 flowcharts), replacing 64 old chunks | `hiv-amendment-2024_review.html` |
| NCDIMH | Complete (all 5 parts, pp.1-356: Ch.1 prevention and screening, Ch.2 endocrinology, Ch.3 cardiology, Ch.4 dermatology, Ch.5 gastroenterology, Ch.6 injuries and trauma, Ch.7 nephrology, Ch.8 neurology to status epilepticus, Ch.9 oncology, Ch.10 ophthalmology, Ch.11 palliation, Ch.12 podiatry, Ch.13 psychiatry, Ch.14 pulmonology, Ch.15 urology) | Part 1: 74 items replacing 144 old chunks. Part 2: 82 (63 tables, 2 boxes, 17 flowcharts) replacing 135. Part 3: 81 (60 tables, 5 boxes, 16 flowcharts) replacing 157. Part 4: 52 (33 tables, 7 boxes, 12 flowcharts) replacing 106. Part 5: 39 (31 tables, 1 box, 7 flowcharts) replacing 65 | `ncdimh_part1_review.html`, `ncdimh_part2_review.html`, `ncdimh_part3_review.html`, `ncdimh_part4_review.html`, `ncdimh_part5_review.html` |
| PrEP 2025 | Complete (86 pages) | 43 items (30 tables, 4 boxes, 9 flowcharts/figures) replacing 97 old chunks. Annex 4 counselling messages rebuilt into one table; Figure 9's invented concentration values removed | `prep-2025_review.html` |
| ANC | Complete (48 pages) | 13 items (12 tables, 1 flowchart) replacing 36 old chunks; most table pages have no text layer, so cells were read from page images | `anc_review.html` |
| UNAIDS Linkages SOP | Done (tables + annexure 1-2 flowcharts) | 32 tables and 2 flowcharts replacing 70 old chunks; tables rebuilt from the old chunks (split rows merged, pieces joined) with every word checked against the PDF text layer; no image transcription | `unaids-linkages-sop_review.html` |
| TB 2025 | Complete (4 parts, pp.1-286) | 100 items. Tables rebuilt from the old chunks (split rows merged, pieces joined, a new bold header starts a new table) with every word checked against the PDF text; invented chart values removed (Figures 1-4, growth chart Figure 37); clinically important flowcharts checked against the page images (Figures 11, 12, 18, 23, 24 re-done) | `tb-2025_part1_review.html` ... `tb-2025_part4_review.html` |
| FP 2021 | Complete (2 parts, pp.1-118) | 28 items: method tables (advantages/disadvantages kept as two independent lists, MEC 'who can use' tables, when to start, missed pills), MEC summary appendix, side-effect management, ARV interactions; the MEC wheel (image only) is described rather than transcribed. Tables rebuilt from the old chunks with every word checked against the PDF text, key tables against the images | `fp-2021_part1_review.html`, `fp-2021_part2_review.html` |
| Mental Health desk guide | Part 1 (pp.1-69) | 26 tables (definitions, assessment, classification/management and stepwise management tables per condition) rebuilt from the old chunks with every word checked against the PDF text | `mental-health-deskguide_part1_review.html` |

NCDIMH, PrEP and ANC items are written as small Python batches (`batches/ncd_b*.py`, `batches/prep_b*.py`, `batches/anc_b*.py`, with shared helpers in `batches/ncd_common.py` and `batches/prep_common.py`), then added to `ncdimh_tables.json` with `add_items.py`.

| File | What it is |
|---|---|
| `<guideline>_tables.json` (e.g. `hiv-amendment-2024_tables.json`) | The source of truth. Tables as cells with row/column spans, section rows and footnotes. Flowcharts as step-by-step text that keeps branches and combined conditions. Each item has `replaces_chunks` and `source_flags` (problems in the guideline itself). |
| `<guideline>_review.html` | **Review page.** Each item next to its PDF page(s), with your validation notes and the number-check result. |
| `<guideline>_chunks.jsonl` | Replacement chunk records. `text` is what the model receives (always the whole table or flowchart); `embed_text` is an embedding part under 512 tokens (bge); `html` keeps the merged cells for display; all parts of one item share `table_id`. |
| `build_tables.py` | Turns the JSON into HTML, model text and embedding parts, and checks every number against the PDF text layer (where one exists) and against the old chunks. |
| `make_review.py` | Builds the review page and chunk records. |

At retrieval: take the top-k embedding parts, de-duplicate by `table_id`, and give the model each unit's `text`.

Rebuild:
```bash
pdftotext -layout -f N -l N guideline.pdf work/pN.txt          # per page; and pdftoppm -jpeg -r 110 for page images (pgN.jpg)
python3 build_tables.py hiv-amendment-2024_tables.json work ../chunks_v2/chunks.jsonl out
python3 make_review.py out/tables_out.json work notes.json hiv-amendment-2024_review.html hiv-amendment-2024_chunks.jsonl "<doc title>"
```

`apply_reextraction.py` merges all finished guidelines into `../chunks_v3` (see its README).
