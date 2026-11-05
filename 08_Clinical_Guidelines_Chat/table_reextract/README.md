# Table re-extraction (pilot)

The chunk validation showed that most tables lost their structure in the LlamaParse markdown: merged cells, section rows and notes that apply to several rows. This folder re-extracts tables from the PDF page images while keeping that structure.

**Pilot:** HIV Amendment 2024, pages 37–41 (sections 9.2, 9.3, 9.4 and 9.7), which are the tables covered by the first 20 validation notes.

| File | What it is |
|---|---|
| `amendment_pilot_tables.json` | The tables as structured data: cells with row/column spans, section rows, footnotes, and points to check in the source. Transcribed by Claude from the page images. |
| `build_tables.py` | Turns the structured data into an HTML table (spans kept), readable markdown for the model (merged cells filled in, notes that span every row shown once, footnotes attached) and row-by-row embedding text split into parts under 512 tokens. Checks every number against the PDF text layer and the old chunks. |
| `make_review.py` | Builds the review page and chunk records. |
| `amendment_pilot_review.html` | **Review this:** each table next to its PDF page, with your original notes and the number-check result. |
| `amendment_pilot_chunks.jsonl` | Replacement chunks (one table per `table_id`; large tables have several embedding parts that all carry the whole table in `text`). |

Rebuild: `python3 build_tables.py amendment_pilot_tables.json <dir with pN.txt from pdftotext -layout> ../chunks_v2/chunks.jsonl <out>` then `make_review.py`.
