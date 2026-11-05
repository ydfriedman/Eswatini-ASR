# Chunks v3

`chunks_v2` plus the re-extracted tables, boxes and flowcharts (see `../table_reextract/`). **Use this set for indexing.** It has the same fields as v2, plus a few new ones for re-extracted items.

**Status:** only the HIV Amendment 2024 is re-extracted so far. All other guidelines are passed through from v2 unchanged. This file is regenerated each time another guideline is finished.

| | |
|---|---|
| Chunks | 3,789 |
| HIV Amendment 2024 | 70 chunks: 36 re-extracted items (44 records, because larger items have several embedding parts) + 26 text chunks |

## New fields (re-extracted items only)

| Field | Meaning |
|---|---|
| `table_id` | One table, box or flowchart. Several chunk records can share it (`table_part` "1/2", "2/2"). |
| `text` | The **whole** item, as the model should receive it. It is identical in every part. |
| `embed_text` | One embedding part, under 512 tokens (for bge). |
| `html` | The table with merged cells, for display. |
| `source_flags` | Problems in the guideline itself, for a clinician to check. |
| `replaces_chunks` | The v2 chunk ids this item replaces. |

## Retrieval

Retrieve the top k by `embed_text`, then **de-duplicate by `table_id`** (keep the first part), then give the model `text`. Parent and neighbour expansion work as in v2 (`section_id`, `parent_section_id`, `prev_chunk_id`, `next_chunk_id`). All parts of one item share the same neighbours.

## What the merge step did (Amendment)

- **Replaced** 65 v2 chunks with the re-extracted items: old tables, flowcharts, and the caption, lead-in and footnote chunks that belonged to them.
- **Cleaned** neighbouring text chunks. It removed "Flowchart: …" and "Figure X" caption lines, chapter title-page fragments, and lines now duplicated inside a re-extracted item.
- **Fixed chapter labels** using the PDF's page-to-chapter map. For example, Chapter 10 text was labelled "Chapter 5". Unnumbered text chunks now carry the numbered section they sit in.
- **Merged very small text chunks** into a neighbour from the same chapter when the result stays under about 450 tokens.

Logs: `merge_log.csv` (every change) and `removed_chunks.jsonl` (every removed chunk, with its reason).

Rebuild:
```bash
cd ../table_reextract
python3 apply_reextraction.py ../chunks_v2 ../chunks_v3 hiv-amendment-2024_tables.json hiv-amendment-2024_chunks.jsonl
```
