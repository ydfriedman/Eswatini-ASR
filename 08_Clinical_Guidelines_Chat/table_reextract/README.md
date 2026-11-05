# Table and flowchart re-extraction

Chunk validation showed that most tables had lost their structure in the LlamaParse markdown (merged cells, section rows, notes spanning several rows), and some flowcharts had wrong branches. This folder re-extracts tables, highlighted boxes and flowcharts from the PDF page images, one guideline at a time.

**Done: HIV Amendment 2024.** 36 items: 18 tables, 2 boxes and 16 flowcharts. They replace 54 old chunks and become 44 chunk records, because large items have several embedding parts.

| File | What it is |
|---|---|
| `hiv-amendment-2024_tables.json` | The source of truth. Tables as cells with row/column spans, section rows and footnotes. Flowcharts as step-by-step text that keeps branches and combined conditions. Each item has `replaces_chunks` and `source_flags` (problems in the guideline itself). |
| `hiv-amendment-2024_review.html` | **Review page.** Each item next to its PDF page(s), with your validation notes and the number-check result. |
| `hiv-amendment-2024_chunks.jsonl` | Replacement chunk records. `text` is what the model receives (always the whole table or flowchart); `embed_text` is an embedding part under 512 tokens (bge); `html` keeps the merged cells for display; all parts of one item share `table_id`. |
| `build_tables.py` | Turns the JSON into HTML, model text and embedding parts, and checks every number against the PDF text layer (where one exists) and against the old chunks. |
| `make_review.py` | Builds the review page and chunk records. |

At retrieval: take the top-k embedding parts, de-duplicate by `table_id`, and give the model each unit's `text`.

Rebuild:
```bash
pdftotext -layout -f N -l N guideline.pdf work/pN.txt          # per page; and pdftoppm -jpeg -r 110 for page images (pgN.jpg)
python3 build_tables.py hiv-amendment-2024_tables.json work ../chunks_v2/chunks.jsonl out
python3 make_review.py out/tables_out.json work notes.json hiv-amendment-2024_review.html hiv-amendment-2024_chunks.jsonl "<doc title>"
```

**Not yet done:** merging these records into `chunks_v2`, which removes the replaced chunks and strips leftover "Figure X" or "Flowchart:" lines from neighbouring text chunks. That step will be done once the remaining guidelines are re-extracted.
