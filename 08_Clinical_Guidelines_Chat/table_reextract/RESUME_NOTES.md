# Where the work paused

## Done and committed
- HIV Amendment 2024: all tables, boxes and flowcharts re-extracted (`hiv-amendment-2024_*`).
- NCDIMH part 1 (pp.1-89): 74 tables, boxes and flowcharts re-extracted (`ncdimh_*`, `batches/ncd_b01-b21.py`).
- Both are merged into `../chunks_v3` by `apply_reextraction.py`.

## Done: NCDIMH text-chunk fixes for pp.1-89
Labels (`text_labels` in `ncdimh_tables.json`, range `text_fix_pages`), fragment merges, trailing headings and embedding noise are all handled by `apply_reextraction.py`. For each new NCDIMH part, extend `text_fix_pages`, then run `pdf_headings.py` to propose labels, review them by hand and add them to `text_labels`.
`../SOURCE_ISSUES.md` is built from every item's `source_flags`, leaving out notes about layout or typos (`make_source_issues.py`, run from `table_reextract/`), plus a hand-written text-sections table.

## Next after that
NCDIMH parts 2-5 (the user uploads them one at a time). Then the other guidelines. Keep a running "source issues" list from each item's `source_flags`.
