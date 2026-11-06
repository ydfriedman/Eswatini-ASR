import json, re
DROP = re.compile(r"^(Image in the PDF|Flowchart is an image|This table is an image|Highlighted box|Two-column box|Infographic|"
                  r"Order-form layout|Table continues|Table spans|The .* continue onto|The old chunk|In chunks_v2|"
                  r"The PDF lays this out|The PDF prints the schedule as|Glucose targets are printed|Boxes are side by side|"
                  r"Empty 2022|The 6-month refill|The DR-TB contacts|The Notes cell spans|Side effects and contraindications|"
                  r"Section numbers in the 2022|The LPV/r 200mg|Path A is ONE|The first block has no regimen|"
                  r"The PDF prints two overlapping|The PDF prints the osmolality|The temperature criteria are printed|"
                  r"The PDF table has no header row|The volume-status table is|Phototherapy is a separate|The class table is a separate|"
                  r"This part has no 'STEP 4'|Two rows are both labelled|'Oxygen Monitoring'|The PDF lays the newborn|"
                  r"'Isolated Systolic'|The PDF text layer for this page|The old chunk for this|The two columns are independent|"
                  r"'Cardiac U/C'|The PDF lays each stage|The PDF prints the antipsychotics|The PDF prints one small table|"
                  r"Flowchart-style chart|The PDF table is laid out|The timeline is an image|Bar extents|The motor section is headed|"
                  r"The first column is headed|The PDF lays the targets|Risk colours are not printed|The immunisation row is labelled|"
                  r"The footnote markers in the table|The dermis fractions|Table spans pp|The PDF has the|The tick-mark sub-items|"
                  r"The PDF prints a summary box|The table has no column headers|Branch layout read|'Risk Stratification' is printed|"
                  r"The codeine row is split|The lymphoma text on|The summary box spells)", re.I)
TYPO = re.compile(r"(^'[^']+'.*printed|printed; correct|printed; written|; corrected\.?$|written as MTB|duplicated words removed|"
                  r"Interaction category is shown only)", re.I)
src = open('../SOURCE_ISSUES.md').read()
head = src.split('## HIV Amendment 2024')[0]
tail = '## Text sections' + src.split('## Text sections')[1]
out = [head.rstrip(), '']
n = 0
for path, title in (('hiv-amendment-2024_tables.json', 'HIV Amendment 2024'), ('ncdimh_tables.json', 'NCDIMH (pages 1-356, complete)'), ('prep-2025_tables.json', 'PrEP Implementation Guidelines 2025'), ('anc_tables.json', 'ANC Guidelines'), ('unaids-linkages-sop_tables.json', 'UNAIDS Linkages SOP'), ('tb-2025_tables.json', 'TB Guidelines 2025 (pages 1-231 so far)')):
    rows = sorted((t['page'], t['caption'], t['table_id'], f) for t in json.load(open(path))['tables']
                  for f in t.get('source_flags', []) if not DROP.match(f.strip()) and not TYPO.search(f))
    out += [f'## {title}', '', '| Page | Item | Issue |', '|---|---|---|']
    out += [f'| {p} | {c} (`{i}`) | {f.replace("|", "/")} |' for p, c, i, f in rows] + ['']
    n += len(rows)
open('../SOURCE_ISSUES.md', 'w').write('\n'.join(out) + '\n' + tail)
print(n)
