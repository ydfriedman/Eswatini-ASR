# Chunk Parsing Check

Input: `chunks.jsonl` (4,061 chunks, 10 guidelines), README and Issue_List.

## Verdict

Overall the parsing is good. Text is complete, diagrams are whole, chunk sizes are sensible, and most tables are readable. The problems below are specific and fixable. **The STI guideline is parsed fine. It was simply never loaded into the vector index.**

## 1. STI guideline: parsed, but not in the index

- 361 STI chunks exist (266 text, 75 tables, 20 diagrams).
- All 1,193 chunks retrieved in the k=8 run match this file exactly, and none of them is an STI chunk. So the index was built from this file without the `sti-vh-draft-2026` rows (possibly a doc-id filter or an older build).
- Content check: 12 key facts used by the STI test questions are all present and readable. Examples: urethral discharge ceftriaxone + azithromycin, congenital syphilis 50,000 IU/kg, neonatal conjunctivitis 50 mg/kg, the PID "patient is pregnant" criterion, HBV ALT 30/19 U/L, HCV SVR12, treponemal tests "positive for life", the sexual-assault regimen, and the pregnancy syphilis "repeat after 3 months".
- STI weaknesses (secondary):
  - **Flat headings.** 223 of 361 chunks have the document title as their only breadcrumb.
  - **Page numbers as headings.** 31 chunks start their breadcrumb with a page number ("11 > 3.2 Condom promotion…", "63 ## Treatment options…").
  - **Shifted table captions.** Several table captions in the source .docx belong to the neighbouring table. For example, the gonorrhoea/chlamydia table sits under "Treatment options for upper vaginal infection". The chunks inherit the wrong titles.

**Fix:** re-index including `sti-vh-draft-2026`, then confirm with a query like "syndromic treatment of urethral discharge".

## 2. Merged (spanning) table cells are not propagated: systematic

When a cell spans several columns or rows in the PDF, its value lands in the first cell only and the rest are left blank. The model then reads the blanks as "no requirement" or "not applicable".

| Chunk | What is lost | Effect |
|---|---|---|
| `prep-2025-0093` (PrEP Table 10) | "Age ≥16", "safe in pregnancy/breastfeeding" and "attend visits" span all four products; shown under Oral PrEP only | Q040: "the ring has no age limit" |
| `hiv-2022-0083` (Table 2.5 renal monitoring) | The "Yes / any age" and "No / 50+" rows share merged cells; the "50+" row is left empty | Looks like no monitoring is needed at 50+ (relevant to Q046) |
| `hiv-amendment-2024-0089` (9.7 second-line ART) | Weight band "3–29.9 kg" spans rows; continuation rows are blank | The weight band is lost for most regimens |
| `tb-2025-0233` (Table 13) | "Re-registered" spans two rows | Second row has no registration group |
| `ncdimh-0072` (CKD heat map) | Coloured risk grid is lost; headers are duplicated | The table is meaningless without the colours |

A heuristic scan flags about 150 tables (mostly NCDIMH, HIV 2022, MH Deskguide and TB) with rows that are filled in the first cell and blank in the rest. Not all are real errors, but the pattern is common.

**Fix:** in the table converter, copy a spanning cell's value into every column and row it covers (or write "(applies to all)"). Also, for each table row, add a row-wise serialisation to `embed_text`, e.g. "PrEP ring: Age ≥16 years; Weight —; Contraindication: vaginal antimicrobials…". Then re-check the five tables above by eye.

## 3. Breadcrumbs (`heading_path`) are wrong in places, and they are embedded

`embed_text` starts with the breadcrumb, so a wrong path pulls chunks toward the wrong queries.

| Document | Affected (lower bound) | Problem |
|---|---|---|
| HIV Amendment 2024 | ≥25 of 104 (24%), effectively most of the document | Chapters 6–10 nested under "CHAPTER 5"; Chapter 3 under "ACRONYMS". 65 of 104 chunks have "CHAPTER 5" (a ~3-page chapter) as their root, and 14 have "ACRONYMS" |
| TB 2025 | 96 of 739 (13%) | Tables/figures act as parents of later sections ("Table 2: End TB Milestones > Figure 3 > …") |
| HIV 2022 | ≥25 (tables as parents), plus unnumbered headings swallowing later sections | e.g. PrEP sections under "Voluntary medical male circumcision" |
| PrEP 2025 | 6+ | "2.3 CAB-LA" nested under "Table 5. Starting and Stopping PrEP Ring"; the LEN heading parsed at H1, which makes "1.2 Priority Populations" its child |
| STI draft | 31 page-number roots, 223 flat | see §1 |

**Fix:** rebuild paths from section numbers wherever they exist (6.1.2 is always under 6.1, under Chapter 6). Never let a Table, Figure or Box be a parent. Ignore bare numbers (page numbers). Demote headings that come from bold body text.

## 4. Junk and duplicate chunks

- **116 front/back-matter chunks** (Foreword, Acknowledgements, Preface, Acronyms, References, List of tables). The Amendment's table of contents (p.6) and TB's dot-leader TOC (`tb-2025-0708/0709`) are still present, despite the README saying contents pages are skipped.
- **59 near-empty chunks (<40 chars).** These include running page footers ("MENTAL HEALTH DESKGUIDE 17", ~20 of them), cover lines, "x" and "flow_chart".
- **13 duplicate-text groups**, e.g. the "KINGDOM OF ESWATINI / MINISTRY OF HEALTH" cover in three documents, and repeated MH Deskguide and ANC blocks.
- Acronym chunks were among the most-retrieved in the k=8 run.

**Fix:** drop footers and near-empty chunks, deduplicate, and either exclude front/back matter from the index or tag it (`section_type=frontmatter`) and filter it out at query time.

## 5. Enumerations split into tiny sibling chunks

The PrEP "1.1 Products and Regimens" section is four separate small chunks (oral, ring, CAB-LA, LEN). A question like "what PrEP products exist?" needs all four, but retrieval returned two (Q037).

**Fix:** parent-section expansion at retrieval time (when a chunk hits, also pass its parent section), or merge sibling chunks under ~150 tokens into their parent.

## 6. Minor

- Footnote digits glued to drug names in 4 chunks, e.g. "DTG2" (`hiv-amendment-2024-0079/0082`, `tb-2025-0516/0517`).
- 8 "Error! Reference source not found." strings (in the source; already in Issue_List).
- 101 tables have a blank header row. This is intended per the README, but those tables have no column meaning in `embed_text`.

## Corrections to my earlier findings

Seeing the raw chunks changes the cause of several failures:

- **Q104 (MDR contacts → 6H)** and **Q006 / Q125 (2022 vs 2024)** were generation errors, not parsing errors. Those tables are parsed correctly, with clear column headers.
- **Q098 (first-line antihypertensives)** was a retrieval miss. The list is intact in `ncdimh-0255`; it just wasn't retrieved.
- **Q040** is confirmed as merged-cell loss.
- **Q037** is caused by sibling-chunk splitting (§5).
- The ~15 STI failures are an indexing problem, not a parsing problem.

## Suggested order

1. Re-index with STI included.
2. Propagate spanning cells and add row-wise serialisation for tables.
3. Rebuild breadcrumbs from section numbers, focusing on the Amendment and TB.
4. Drop junk and duplicates; add parent-section expansion.
5. Re-run the 152 questions.
