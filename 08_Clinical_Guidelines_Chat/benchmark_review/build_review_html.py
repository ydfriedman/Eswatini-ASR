"""Build the review page from review_template.html with review_data.json inlined, in three versions:
  clinician_review.html          offline file (answers kept in the browser; CSV download)
  hf_space/static/index.html     Hugging Face Space (saves to a dataset); also hf_space/qids.json
  apps_script/page_sheet.csv     Google Apps Script version, split into cells for the Google Sheet's page tab;
                                 also apps_script/Code.gs (from Code.gs.template, with the question ids)

Run from 08_Clinical_Guidelines_Chat/:
    python3 benchmark_review/build_review_data.py
    python3 benchmark_review/build_review_html.py
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'review_data.json').read_text(encoding='utf-8'))
blob = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
blob = blob.replace('</', '<\\/').replace('\u2028', '\\u2028').replace('\u2029', '\\u2029')
tpl = (HERE / 'review_template.html').read_text(encoding='utf-8')
marker = '/*__DATA__*/[]'
assert tpl.count(marker) == 1
server = '/*__SERVER__*/false'
assert tpl.count(server) == 1
page = tpl.replace(marker, blob)
for out, backend in ((HERE / 'clinician_review.html', 'false'), (HERE / 'hf_space' / 'static' / 'index.html', "'http'")):
    out.write_text(page.replace(server, backend), encoding='utf-8')
    print(f'{out.relative_to(HERE)}: {len(data)} questions, {out.stat().st_size // 1024} KB')
qids = json.dumps([q['id'] for q in data])
(HERE / 'hf_space' / 'qids.json').write_text(qids, encoding='utf-8')

# Google Apps Script version: the page goes into a Sheet tab, one chunk per cell (cells hold at most 50,000
# characters). Each chunk is wrapped in "|...|" so the CSV import keeps leading/trailing spaces; Code.gs strips them.
import csv
gas_page = page.replace(server, "'gas'")
marker = 'REVIEW_PAGE_V1 (generated - do not edit this tab)'
chunks = [gas_page[i:i + 30000] for i in range(0, len(gas_page), 30000)]
with open(HERE / 'apps_script' / 'page_sheet.csv', 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh, quoting=csv.QUOTE_ALL)   # quote every cell: Sheets' import also splits on ';'
    w.writerow([marker])
    for c in chunks:
        w.writerow(['|' + c + '|'])
code = (HERE / 'apps_script' / 'Code.gs.template').read_text(encoding='utf-8')
assert code.count('/*__QIDS__*/[]') == 1 and marker in code
(HERE / 'apps_script' / 'Code.gs').write_text(code.replace('/*__QIDS__*/[]', qids), encoding='utf-8')
print(f'apps_script/page_sheet.csv: {len(chunks)} cells; apps_script/Code.gs')
