import json, re
DROP = re.compile(r"^(Image in the PDF|Flowchart is an image|This table is an image|Highlighted box|Two-column box|Infographic|"
                  r"Order-form layout|Table continues|Table spans|The .* continue onto|The old chunk|In chunks_v2|"
                  r"The PDF lays this out|The PDF prints the schedule as|Glucose targets are printed|Boxes are side by side|"
                  r"Empty 2022|The 6-month refill|The DR-TB contacts|The Notes cell spans|Side effects and contraindications|"
                  r"Section numbers in the 2022|The LPV/r 200mg|Path A is ONE|The first block has no regimen|"
                  r"The PDF prints two overlapping|The PDF prints the osmolality|The temperature criteria are printed)", re.I)
TYPO = re.compile(r"(printed; correct|printed; written|; corrected\.?$|written as MTB|duplicated words removed|"
                  r"Interaction category is shown only)", re.I)
src = open('../SOURCE_ISSUES.md').read()
head = src.split('## HIV Amendment 2024')[0]
tail = '## Text sections' + src.split('## Text sections')[1]
out = [head.rstrip(), '']
n = 0
for path, title in (('hiv-amendment-2024_tables.json', 'HIV Amendment 2024'), ('ncdimh_tables.json', 'NCDIMH (pages 1-89 so far)')):
    rows = sorted((t['page'], t['caption'], t['table_id'], f) for t in json.load(open(path))['tables']
                  for f in t.get('source_flags', []) if not DROP.match(f.strip()) and not TYPO.search(f))
    out += [f'## {title}', '', '| Page | Item | Issue |', '|---|---|---|']
    out += [f'| {p} | {c} (`{i}`) | {f.replace("|", "/")} |' for p, c, i, f in rows] + ['']
    n += len(rows)
open('../SOURCE_ISSUES.md', 'w').write('\n'.join(out) + '\n' + tail)
print(n)
