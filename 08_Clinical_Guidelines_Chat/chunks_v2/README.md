# Chunks v2: cleaned chunk set

This is a cleaned version of the `chunks.jsonl` used in the k=8 run. It contains 4,061 input chunks: **3,805 are kept, 256 are dropped**, and 17 acronym lists move to a glossary. It has the same fields as v1, plus a few new ones. `embed_text` is rebuilt, so **re-embed everything**.

There is one thing v2 cannot fix: **the STI guideline must be added to the index.** Its 330 kept chunks are in this file. After indexing, check the vector count for `doc_id = sti-vh-draft-2026`.

## What changed

| Fix | Result |
|---|---|
| **Merged table cells** | Spanning values are copied into the empty cells they cover. 222 fills across 69 tables, each marked `merged_cells_expanded: true`. See *Tables* below. |
| **Section labels (`heading_path`)** | 3,788 labels rebuilt. The old one is kept in `heading_path_original`. See *Labels* below. |
| **Front/back matter dropped** | 109 chunks: foreword, preface, acknowledgements, references, contributors, and similar. Clinical annexes and appendices are **kept**. |
| **Acronym lists** | 17 chunks moved to `glossary.jsonl`. They are not embedded, but are useful for query expansion ("CAB-LA" ↔ "cabotegravir"). |
| **Contents and cover pages** | 8 leftover contents / list-of-figures pages (incl. the NCDIMH plain-text TOC) and 6 cover pages dropped. |
| **Near-empty chunks** | 39 dropped: running footers ("MENTAL HEALTH DESKGUIDE 17"), "x", "flow_chart", page numbers. |
| **Duplicates** | 13 dropped. A chunk counts as a duplicate only if its text **and** its section label are both identical. The same table repeated in two different sections is kept. |
| **Orphan captions** | 40 "Table 10. …" / heading-only chunks merged into the table or text that follows. |
| **Orphan fragments** | 24 tiny trailing pieces ("Source: …", "Note: …", one-line spill-overs) merged into the chunk before them. |
| **Footnote glue** | "DTG2" becomes "DTG [note 2]". |
| **Section links** | New fields `section_id`, `parent_section_id`, `prev_chunk_id`, `next_chunk_id` for retrieval-time expansion. See *Expansion* below. |

Every dropped chunk is in `dropped_chunks.jsonl` with a `drop_reason`, so nothing is lost. `logs/dropped_summary.csv` lists them in one sheet for review.

## Tables: merged cells

Two kinds of repair are applied.

1. **Row-label carry-down (all tables).** A row whose first cell is blank, but whose other cells are filled, is a continuation of the row above. The label from the row above is copied in. For example, the "3–29.9 kg" weight band in Amendment 9.7 now appears on all 5 regimen rows instead of only the first. This rule is high-precision, so it is applied everywhere.
2. **Horizontal and vertical spans.** A value that spans several columns, such as "≥ 16 years" for all four PrEP products, or several rows. Blank cells next to a filled one are often genuinely blank ("not applicable"), and on a sample this rule was right only about 60% of the time. So it is **applied only to tables checked by eye** (PrEP Table 10 `prep-2025-0093`, HIV 2022 Table 2.5 `hiv-2022-0083`). The other 122 candidate fills are listed in `logs/table_span_candidates.csv`, which has an empty `verdict` column. Mark each row `merged` or `blank`, add the confirmed chunk ids to `VERIFIED_HV` in `scripts/fix_tables.py`, and rebuild.

Long spanning text (over 150 characters) is written in full once and then as "(same as left)" / "(same as above)", so the chunk does not balloon.

The lasting fix belongs in your PDF→markdown converter. If it can read `colspan` / `rowspan`, fill spans there and these heuristics become unnecessary.

## Labels

- **Numbered documents** (HIV 2022, the Amendment, TB, PrEP, FP, the UNAIDS SOP, ANC). The hierarchy is rebuilt from printed section numbers: 7.1 always sits under Chapter 7. Page numbers, tables, figures, boxes, "ACRONYMS" and "References" are never parents. A heading with no number is attached to the right numbered section. Where the old "1.1 PrEP Products > Oral / Ring / CAB-LA" lost LEN to an H1, LEN is now placed back under 1.1. ALL-CAPS headings become title case, with acronyms kept (`PrEP`, `HIV`, `DTG`).
  - Before: `CHAPTER 5: BASIC CARE PACKAGE… > CHAPTER 7: ADULT ANTIRETROVIRAL THERAPY > 7.1 ROUTINE VL MONITORING`
  - After: `Chapter 7: Adult Antiretroviral Therapy > 7.1 Routine VL Monitoring`
- **STI draft.** Labels come from the real Heading 1–4 styles in the Word file (`sources/sti-vh-draft-2026_docx_headings.md`, made with pandoc). Previously 223 of 361 chunks had only the document title.
- **NCDIMH and the MH Deskguide (no section numbers).** The parser's `#` levels in these are unreliable (callouts and tables show up as H1/H2), so labels are anchored on each document's **printed table of contents** (`scripts/toc_headings.py`, using the source markdown in `sources/`). Structure: `Chapter > TOC entry > nearest short heading`, plus a table/figure caption as leaf. Chapters can only move forward through the document, so text repeated in another chapter cannot drag a chunk there.
  - Before: `Insulin Therapy in Type 2 Diabetes > Capillary Blood Glucose (CBG)…`
  - After: `Chapter 2: Endocrinology > Glycemic Control in Non-Critical Hospitalized Adult Patients Protocols > Capillary Blood Glucose (CBG)…`
  - The TOC is sparse in places (e.g. one entry for all of Dermatology), so the middle level is sometimes too coarse or stale; the chapter is reliable.
- When a chunk's own first heading or table caption is missing from its path, it is added as the leaf.

`logs/heading_changes.csv` lists every old → new label.

## Expansion: the "list split into tiny chunks" problem

Keep the small chunks for **embedding** (they match precise questions well), and send the model **more than the hit**:

```python
by_id   = {c["chunk_id"]: c for c in chunks}
by_sec  = defaultdict(list)                    # section_id -> chunks, document order
for c in chunks: by_sec[c["section_id"]].append(c)
children = defaultdict(list)                   # parent_section_id -> chunks
for c in chunks: children[c["parent_section_id"]].append(c)

def expand(hit, budget_tokens=1200):
    group = by_sec[hit["section_id"]]                       # 1. the whole section the hit is in
    if sum(c["approx_tokens"] for c in group) < 250:        # 2. tiny section -> its parent's chunks
        group = children[hit["parent_section_id"]] or group
    if sum(c["approx_tokens"] for c in group) > budget_tokens:   # 3. too big -> hit +/- 1 neighbour
        group = [by_id[i] for i in (hit["prev_chunk_id"], hit["chunk_id"], hit["next_chunk_id"]) if i]
    return group
```

Expand the top 3–5 hits, then de-duplicate by `chunk_id` and keep document order. Sizes in v2: a section is a median of 220 tokens (90th percentile 650); a parent section is a median of 410 (90th percentile 1,700). So most expansions are cheap.

## Files

| File | Contents |
|---|---|
| `chunks.jsonl` / `chunks.csv` | The 3,805 kept chunks. **Embed `embed_text`** (for diagrams, optionally `narrative_embed_text`). Give the model `text`. |
| `dropped_chunks.jsonl` | The 256 removed or merged chunks, each with `drop_reason`. |
| `glossary.jsonl` | The 17 acronym lists. |
| `logs/heading_changes.csv` | Every label change. |
| `logs/table_fixes_applied.csv` | Every cell filled. |
| `logs/table_span_candidates.csv` | Span fills **not** applied. Review and set `verdict`. |
| `logs/dropped_summary.csv` | One row per dropped chunk. |
| `scripts/` | `build_v2.py` (the pipeline), `fix_tables.py`, `fix_headings.py`, `sti_headings.py`, `toc_headings.py`. |
| `sources/` | The STI docx converted to markdown (heading levels), and the NCDIMH and MH Deskguide markdown (tables of contents). |

New fields: `heading_path_original`, `section_id`, `parent_section_id`, `prev_chunk_id`, `next_chunk_id`, `merged_cells_expanded`, and `absorbed_chunk_ids` (the caption or fragment chunks merged into this one). `chunk_id`s are unchanged, so they still match v1 and the k=8 results.

## Rebuild

```bash
cd scripts
python3 build_v2.py /path/to/v1/chunks.jsonl ../sources/sti-vh-draft-2026_docx_headings.md .. \
  --toc ncdimh=../sources/ncdimh.md --toc mental-health-deskguide=../sources/mental-health-deskguide.md
```

The build is deterministic (no LLM) and takes a few seconds.

## Caveats

- 2 `embed_text`s are slightly over 512 estimated tokens: `tb-2025-0251` (516) and `sti-vh-draft-2026-0269` (514). Check them with your embedder's tokenizer.
- In NCDIMH and the MH Deskguide the middle label level is sometimes coarse (see *Labels*). A few HIV 2022 labels inherit a stale heading from the parser (e.g. "Special considerations for TPT" carried into 9.10 and 9.11).
- Short bold headings that end a chunk are occasionally merged forward instead of back.
- Dropping and merging used rules. Skim `logs/dropped_summary.csv` before you rely on it.
