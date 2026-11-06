# Where the work paused

## Done and committed
- HIV Amendment 2024: all tables, boxes and flowcharts re-extracted (`hiv-amendment-2024_*`).
- NCDIMH part 1 (pp.1-89): 74 tables, boxes and flowcharts re-extracted (`ncdimh_*`, `batches/ncd_b01-b21.py`).
- NCDIMH part 2 (pp.90-171, NCD_2.pdf = document pages 90-171, offset 89): 82 items (`batches/ncd_b22-b40.py`), text labels for all 103 text chunks, `text_merge` for 3 fragments, `text_fix_pages` [1,171].
- Both are merged into `../chunks_v3` by `apply_reextraction.py`.

## Done: NCDIMH text-chunk fixes for pp.1-89
Labels (`text_labels` in `ncdimh_tables.json`, range `text_fix_pages`), fragment merges, trailing headings and embedding noise are all handled by `apply_reextraction.py`. For each new NCDIMH part, extend `text_fix_pages`, then run `pdf_headings.py` to propose labels, review them by hand and add them to `text_labels`.
`../SOURCE_ISSUES.md` is built from every item's `source_flags`, leaving out notes about layout or typos (`make_source_issues.py`, run from `table_reextract/`), plus a hand-written text-sections table.

- NCDIMH part 3 (pp.172-250, NCD_3.pdf, offset 171): 81 items (`batches/ncd_b41-b54.py`), hand labels for all text chunks, `text_merge`/`text_drop` for fragments, `text_fix_pages` [1,250].

## Next after that
NCDIMH parts 4-5 (part 4 starts at document page 251, Chapter 9 Oncology) (the user uploads them one at a time). Then the other guidelines. Keep a running "source issues" list from each item's `source_flags`.

## Notes for the next part
- Page images/text: `pdftotext -layout` and `pdftoppm -r 110` per page, named by document page (part page + offset).
- `pdftohtml -xml` of NCD_2 dropped the '-BoldMT' from bold font names; patch the family names (GCOESG/FQGDEI+Arial → +Arial-BoldMT) before `pdf_headings.py`. Its proposals were poor for part 2, so labels were written by hand.
- Source problems in text sections go in the 'Text sections' table of `../SOURCE_ISSUES.md`; item flags are collected by `make_source_issues.py`.
