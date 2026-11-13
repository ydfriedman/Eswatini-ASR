# Chunks v3

`chunks_v2` plus the re-extracted tables, boxes and flowcharts (see `../table_reextract/`). **Use this set for indexing.** It has the same fields as v2, plus a few new ones for re-extracted items.

**Status:** all ten guidelines are re-extracted (tables, boxes and flowcharts checked against the page images) and every text chunk has been through the quality sweep below. This file is regenerated each time the set changes; git history keeps earlier versions.

| Guideline | Chunks |
|---|---|
| ncdimh | 782 |
| hiv-2022 | 707 |
| tb-2025 | 664 |
| sti-vh-draft-2026 | 250 |
| mental-health-deskguide | 176 |
| prep-2025 | 175 |
| fp-2021 | 158 |
| unaids-linkages-sop | 126 |
| anc | 92 |
| hiv-amendment-2024 | 70 |
| **Total** | **3,200** |

## Quality sweep (chunk by chunk, against the page images)

Every document was compared with its PDF text layer (`../table_reextract/audit/full_sweep.py`, `audit/missing_paragraphs.py`) and each flagged page was checked against the page image. Repairs are in `../table_reextract/fixes/sweep_fixes.py` (one line per repair, with the page and the reason) and in `apply_reextraction.py`:

- **Text lost beside items:** where a table or flowchart item replaced an old chunk, the headings, intros and notes in that chunk that no other chunk holds are kept as `<chunk>-rest` / `-rest-a` chunks (each one checked).
- **Paragraphs missing from every chunk** were put back in place (`text_insert` / `text_add`), e.g. TB severe-hepatopathy referral, ITR switch, leprosy definition; ANC foreword; Amendment ch.3 introduction.
- **Lost sub-headings that change meaning** were restored, e.g. FP "Not breastfeeding" / "Mixed feeding" / "Exclusive breastfeeding" in the POP, COC, CIC, implant and IUCD start rules; POI and implant side-effect timing.
- **Flowcharts kept as garbled arrows** were rewritten from the page images with their footnotes (TB screening, diagnostic, trace-result, DR-TB selection and paediatric decision trees; neuropathy management; Linkages LCM models).
- **Duplicates:** text chunks that only repeat an item (captions, table bodies, footnotes) were dropped; the item is kept.
- **Splits and noise:** sentences cut at a page break are re-joined; tiny section chunks (<40 words) join their neighbour; running headers/footers, page numbers and decorative image captions are removed; text chunks over the 512-token embedding limit are split at a paragraph boundary; a chunk that landed between two parts of a split item is moved after it.
- **Left as printed:** sentences that are cut or inconsistent in the source PDF itself (e.g. NCDIMH colorectal "right sided once may present"), front matter (acknowledgements, contributor lists, tables of contents) and reference lists.

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
- **Merged very small text chunks** into a neighbour from the same chapter when the result stays under about 400 tokens.
- Context paragraphs copied into a table are left in place in the neighbouring text chunk, because they are not part of the table's embedding text.

## NCDIMH text chunks, pp.1-326

- **Section labels** taken from the PDF's own headings (font and colour), then checked by hand: pp.1-89: 58 labels changed, 48 of them hand-corrected; pp.90-326: all text-chunk labels written by hand (the heading fonts there are too inconsistent). For example, the thyroid chunks now say Hypothyroidism vs Hyperthyroidism vs Thyroid Storm correctly. The labels are stored in `text_labels` in `ncdimh_tables.json`.
- **Small fragments** (under 60 tokens) merged into the next text chunk of the same chapter, or into a chosen chunk (`text_merge` in the spec) when a table or flowchart follows; heading-only leftovers are dropped (`text_drop`); none are left.
- **Duplicate lines**: a line in a text chunk is removed only when it also appears in a re-extracted item printed within 2 pages. (Matching against the whole guideline had stripped repeated section headings and, in one case, the UGIB IV PPI doses on p.170; both are restored.)
- **Trailing headings** moved to the start of the chunk they introduce, or dropped when the next item is a table or flowchart that carries its own caption.
- **Embedding noise** ("image:", "icon:" lines, escaped asterisks, bold markers) is stripped from `embed_text`. `text` is unchanged.

Problems in the guideline itself are listed in `../SOURCE_ISSUES.md`.

Logs: `merge_log.csv` (every change) and `removed_chunks.jsonl` (every removed chunk, with its reason).

Rebuild:
```bash
cd ../table_reextract
python3 apply_reextraction.py ../chunks_v2 ../chunks_v3 \
  hiv-amendment-2024_tables.json hiv-amendment-2024_chunks.jsonl ncdimh_tables.json ncdimh_chunks.jsonl
```
