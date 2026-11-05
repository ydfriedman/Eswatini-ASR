"""Build a ~180-chunk validation sample from chunks_v2, weighted toward risky tables and safety-critical content.

Outputs (next to this script):
  chunk_validation.xlsx  - the review sheet (one row per chunk, dropdown verdicts), sorted by document + PDF page
  chunk_viewer.html      - the same chunks with tables rendered, to read side by side with the PDF

Usage: python3 build_validation_sample.py   (deterministic: fixed random seed)
"""
import collections, csv, html, json, os, random, re
import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
V2 = os.path.join(BASE, 'chunks_v2')
random.seed(20261105)

K = [json.loads(l) for l in open(os.path.join(V2, 'chunks.jsonl'))]
BY = {k['chunk_id']: k for k in K}

# ---------- signals ----------
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s*(?:mg|mcg|µg|g|ml|mL|units?|IU|mmol|mg/kg|ml/kg|mcg/kg|tabs?|tablets?)\b', re.I)
SAFETY_WORDS = re.compile(r'\b(dose|dosing|dosage|max(?:imum)?|contraindicat\w*|overdose|toxic\w*|stat\b|loading|'
                          r'IV|IM|infusion|weight band|kg|do not|never|avoid|stop|refer urgently|emergency|resuscitat\w*|'
                          r'antidote|interaction|pregnan\w*|breastfeed\w*|neonat\w*|infant)\b', re.I)


def safety_score(c):
    t = c['text']
    return 2 * len(DOSE.findall(t)) + len(SAFETY_WORDS.findall(t))


def table_rows(t):
    return [l for l in t.split('\n') if l.strip().startswith('|') and not re.match(r'^\s*\|[\s:|-]+\|\s*$', l)]


def iffy_score(c):
    """Formatting risk for a table chunk: blank cells, ragged rows, blank/duplicated headers, crammed cells."""
    rows = table_rows(c['text'])
    if len(rows) < 2:
        return 0, []
    cells = [[x.strip() for x in r.strip().strip('|').split('|')] for r in rows]
    widths = collections.Counter(len(r) for r in cells)
    n = sum(len(r) for r in cells)
    blank = sum(1 for r in cells for x in r if not x)
    reasons, s = [], 0
    if blank / n > 0.3:
        s += 3; reasons.append(f'{round(100 * blank / n)}% empty cells')
    if len(widths) > 1:
        s += 3; reasons.append('rows with different numbers of columns')
    hdr = cells[0]
    if all(not x for x in hdr):
        s += 2; reasons.append('blank header row')
    elif len(set(x.lower() for x in hdr if x)) < len([x for x in hdr if x]):
        s += 2; reasons.append('repeated column headers (merged header cells)')
    if any(len(x) > 400 for r in cells for x in r):
        s += 1; reasons.append('very long cells')
    if c['text'].count('<br/>') > 15:
        s += 1; reasons.append('many line breaks inside cells')
    return s, reasons


fixes = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(V2, 'logs', 'table_fixes_applied.csv'))):
    fixes[r['chunk_id']].append(r)
spans = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(V2, 'logs', 'table_span_candidates.csv'))):
    spans[r['chunk_id']].append(r)
qsrc = collections.defaultdict(list)
for r in csv.DictReader(open(os.path.join(BASE, 'sample_questions.csv'))):
    for cid in r['source_chunks'].split(';'):
        if cid.strip():
            qsrc[cid.strip()].append(r['id'])

# ---------- sampling ----------
picked = collections.OrderedDict()   # chunk_id -> (priority, why, what_to_check)


def pick(cid, prio, why, check):
    if cid in BY and cid not in picked:
        picked[cid] = (prio, why, check)
        return True
    return False


def per_doc_cap(cands, n, cap):
    out, cnt = [], collections.Counter()
    for c in cands:
        if len(out) >= n:
            break
        if cnt[c['doc_id']] < cap and c['chunk_id'] not in picked:
            out.append(c); cnt[c['doc_id']] += 1
    return out


# 1. source chunks of the benchmark's new reference answers
for cid, qs in qsrc.items():
    pick(cid, 'A', f'Source of reference answer {", ".join(qs)}',
         'Every dose, threshold and condition matches the PDF exactly; nothing is cut off.')

# 2. tables where the span heuristic (not applied) flagged possible merged cells: verdict feeds the build
for cid in sorted(spans, key=lambda x: -safety_score(BY[x]) if x in BY else 0):
    ex = '; '.join(f'"{r["row_label"]}" → {r["would_fill_with"][:40]}' for r in spans[cid][:3])
    pick(cid, 'A', 'Possible merged cells, NOT filled (needs your decision)',
         f'In the PDF, are these blank cells really merged with the cell above/left? e.g. {ex}. '
         f'Record it in the "Merged cells?" column.')

# 3. tables where merged cells WERE filled automatically
filled = sorted((BY[c] for c in fixes if c in BY), key=lambda c: -safety_score(c))
for c in per_doc_cap(filled, 30, 6):
    ex = '; '.join(f'"{r["row_label"]}" ← {r["filled_with"][:40]}' for r in fixes[c['chunk_id']][:3])
    pick(c['chunk_id'], 'A', 'Merged cells were filled automatically',
         f'Check each filled value really applies to that row/column in the PDF, e.g. {ex}.')

# 4. high-safety tables (doses, weight bands, contraindications)
tabs = sorted((c for c in K if c['type'] == 'table'), key=lambda c: -(safety_score(c) + 3 * iffy_score(c)[0]))
for c in per_doc_cap(tabs, 32, 6):
    r = iffy_score(c)[1]
    pick(c['chunk_id'], 'A', 'Safety-critical table (doses / contraindications)' + (f'; {", ".join(r)}' if r else ''),
         'Every number, unit and frequency matches the PDF; each value sits in the right row and column.')

# 5. tables with the most formatting risk
risky = sorted((c for c in K if c['type'] == 'table'), key=lambda c: -iffy_score(c)[0])
for c in per_doc_cap([c for c in risky if iffy_score(c)[0] >= 3], 20, 4):
    pick(c['chunk_id'], 'B', 'Formatting risk: ' + ', '.join(iffy_score(c)[1]),
         'Rows and columns line up with the PDF; no values shifted, merged or lost.')

# 6. high-safety text chunks
texts = sorted((c for c in K if c['type'] == 'text'), key=lambda c: -safety_score(c))
for c in per_doc_cap(texts, 20, 3):
    pick(c['chunk_id'], 'A', 'Safety-critical text (doses / emergency steps)',
         'Every dose and step matches the PDF; nothing is missing at the start or end of the chunk.')

# 7. flowcharts with safety content
diags = sorted((c for c in K if c['type'] == 'diagram'), key=lambda c: -safety_score(c))
for c in per_doc_cap(diags, 15, 3):
    pick(c['chunk_id'], 'B', 'Flowchart (text derived from the diagram)',
         'Each decision and branch in the text matches the arrows in the PDF flowchart; doses are correct.')

# 8. random baseline: 2 per document
for doc in sorted({c['doc_id'] for c in K}):
    pool = [c for c in K if c['doc_id'] == doc and c['chunk_id'] not in picked]
    for c in random.sample(pool, 2):
        pick(c['chunk_id'], 'C', 'Random baseline', 'Text is complete and readable; the label (section) is right.')

rows = sorted(picked.items(), key=lambda kv: (BY[kv[0]]['doc_title'], BY[kv[0]]['page_start'], kv[0]))
print('sample size', len(rows), collections.Counter(v[0] for _, v in rows),
      collections.Counter(BY[k]['doc_id'] for k, _ in rows))

# ---------- workbook ----------
wb = openpyxl.Workbook()
ins = wb.active
ins.title = 'How to validate'
lines = [
    ('Chunk validation sample', True),
    (f'{len(rows)} chunks from chunks_v2, chosen to over-represent risky tables and safety-critical content.', False),
    ('', False),
    ('How to work through it', True),
    ('1. Open chunk_viewer.html in a browser next to the PDF. It shows each chunk with its tables properly laid out.', False),
    ('2. Rows are sorted by document, then PDF page: open one PDF and move forward through it.', False),
    ('   "PDF page" is the page number in the PDF viewer, not the number printed on the page. (STI draft: the Word-converter page; search for a phrase instead.)', False),
    ('3. Read "What to check" for each row, compare with the PDF, and pick a value in each yellow column.', False),
    ('4. Start with priority A (about two thirds of rows): these matter most. B and C can be skimmed.', False),
    ('5. Only write a note when something is wrong: say what the PDF has, e.g. "PDF says 10 mg, chunk says 1 mg".', False),
    ('', False),
    ('Columns to fill (yellow)', True),
    ('Text complete?  Yes / Partly / No: is anything missing, cut off or out of order?', False),
    ('Numbers correct?  Yes / No / No numbers: doses, units, thresholds, frequencies exactly as in the PDF.', False),
    ('Table structure OK?  Yes / Minor issue / Wrong / Not a table: every value in the right row and column.', False),
    ('Merged cells?  Only for "Possible merged cells" rows: Merged (fill them) / Really blank / Mixed (explain in note).', False),
    ('Label correct?  Yes / Roughly / Wrong: does the section label describe where this sits in the document?', False),
    ('Overall  OK / Minor (cosmetic) / Major (could mislead a clinician): your bottom line for the chunk.', False),
    ('', False),
    ('What happens next', True),
    ('Major issues are fixed in the build or flagged in Issue_List; "Merged" answers are added to VERIFIED_HV in fix_tables.py.', False),
    ('The Summary sheet counts your verdicts automatically.', False),
    ('', False),
    ('Why each chunk was picked', True),
    ('A: source of a benchmark reference answer; possible merged cells; auto-filled merged cells; safety-critical tables/text.', False),
    ('B: tables with formatting risk (blank cells, ragged rows, merged headers); safety flowcharts.', False),
    ('C: random baseline, 2 per document, to estimate the general error rate.', False),
]
for i, (t, bold) in enumerate(lines, start=1):
    c = ins.cell(i, 1, t)
    c.font = Font(bold=bold, size=14 if i == 1 else 11)
ins.column_dimensions['A'].width = 140

ws = wb.create_sheet('Review')
head = ['#', 'Priority', 'Document', 'PDF page', 'chunk_id', 'Type', 'Section label', 'Why picked', 'What to check',
        'Text complete?', 'Numbers correct?', 'Table structure OK?', 'Merged cells?', 'Label correct?', 'Overall', 'Note',
        'Chunk text (also in chunk_viewer.html)']
widths = [5, 8, 22, 9, 24, 8, 40, 30, 45, 12, 12, 14, 13, 12, 13, 40, 70]
ws.append(head)
hdr_fill = PatternFill('solid', fgColor='0F3B3A')
fill_cols = range(10, 17)
yellow = PatternFill('solid', fgColor='FFF2CC')
thin = Border(bottom=Side(style='thin', color='D9D9D9'))
for j, w in enumerate(widths, start=1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
    c = ws.cell(1, j)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = hdr_fill if j not in fill_cols else PatternFill('solid', fgColor='B8860B')
    c.alignment = Alignment(wrap_text=True, vertical='center')
for n, (cid, (prio, why, check)) in enumerate(rows, start=1):
    c = BY[cid]
    page = str(c['page_start']) if c['page_start'] == c['page_end'] else f"{c['page_start']}–{c['page_end']}"
    merged = '' if why.startswith('Possible merged') else 'n/a'
    text = c['text'] if len(c['text']) < 32000 else c['text'][:32000] + ' …'
    ws.append([n, prio, c['doc_title'], page, cid, c['type'], c['heading_path'], why, check,
               '', '', 'Not a table' if c['type'] != 'table' else '', merged, '', '', '', text])
    for j in range(1, len(head) + 1):
        cell = ws.cell(n + 1, j)
        cell.alignment = Alignment(wrap_text=True, vertical='top')
        cell.border = thin
        if j in fill_cols and not (j == 13 and merged == 'n/a'):
            cell.fill = yellow
    ws.row_dimensions[n + 1].height = 90
last = len(rows) + 1
for col, opts in [('J', 'Yes,Partly,No'), ('K', 'Yes,No,No numbers'), ('L', 'Yes,Minor issue,Wrong,Not a table'),
                  ('M', 'Merged,Really blank,Mixed,n/a'), ('N', 'Yes,Roughly,Wrong'), ('O', 'OK,Minor,Major')]:
    dv = DataValidation(type='list', formula1=f'"{opts}"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f'{col}2:{col}{last}')
ws.freeze_panes = 'F2'
ws.auto_filter.ref = f'A1:Q{last}'

sm = wb.create_sheet('Summary')
sm.append(['Measure', 'Count', 'Share of reviewed'])
sm['A1'].font = sm['B1'].font = sm['C1'].font = Font(bold=True)
items = [('Rows reviewed (Overall filled)', f'=COUNTA(Review!O2:O{last})', None),
         ('Overall: OK', f'=COUNTIF(Review!O2:O{last},"OK")', 1), ('Overall: Minor', f'=COUNTIF(Review!O2:O{last},"Minor")', 1),
         ('Overall: Major', f'=COUNTIF(Review!O2:O{last},"Major")', 1),
         ('Numbers wrong', f'=COUNTIF(Review!K2:K{last},"No")', 1),
         ('Text incomplete (Partly or No)', f'=COUNTIF(Review!J2:J{last},"Partly")+COUNTIF(Review!J2:J{last},"No")', 1),
         ('Table structure wrong', f'=COUNTIF(Review!L2:L{last},"Wrong")', 1),
         ('Label wrong', f'=COUNTIF(Review!N2:N{last},"Wrong")', 1),
         ('Merged cells confirmed (add to VERIFIED_HV)', f'=COUNTIF(Review!M2:M{last},"Merged")', None),
         ('Priority A rows reviewed', f'=COUNTIFS(Review!B2:B{last},"A",Review!O2:O{last},"<>")', None),
         ('Priority A Major', f'=COUNTIFS(Review!B2:B{last},"A",Review!O2:O{last},"Major")', None),
         ('Random baseline (C) Major', f'=COUNTIFS(Review!B2:B{last},"C",Review!O2:O{last},"Major")', None)]
for i, (lab, f, share) in enumerate(items, start=2):
    sm.cell(i, 1, lab); sm.cell(i, 2, f)
    if share:
        sm.cell(i, 3, f'=IF($B$2=0,"",B{i}/$B$2)').number_format = '0%'
sm.column_dimensions['A'].width = 48
sm.column_dimensions['B'].width = 10
sm.column_dimensions['C'].width = 18
wb.move_sheet('Summary', offset=-1)
wb.save(os.path.join(HERE, 'chunk_validation.xlsx'))


# ---------- HTML viewer ----------
def render(md):
    out, i, lines = [], 0, md.split('\n')
    def inline(s):
        s = html.escape(s)
        s = re.sub(r'&lt;br\s*/?&gt;', '<br>', s)
        s = re.sub(r'&lt;/?(mark|sup|sub|u)&gt;', '', s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
        return s
    while i < len(lines):
        l = lines[i]
        if l.strip().startswith('|'):
            block = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                block.append(lines[i]); i += 1
            out.append('<table>')
            first = True
            for r in block:
                if re.match(r'^\s*\|[\s:|-]+\|\s*$', r):
                    continue
                cells = r.strip().strip('|').split('|')
                tag = 'th' if first and len(block) > 1 and re.match(r'^\s*\|[\s:|-]+\|\s*$', block[1]) else 'td'
                out.append('<tr>' + ''.join(f'<{tag}>{inline(x.strip())}</{tag}>' for x in cells) + '</tr>')
                first = False
            out.append('</table>')
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', l)
        if m:
            out.append(f'<h4>{inline(m.group(2))}</h4>')
        elif l.strip():
            out.append(f'<p>{inline(l)}</p>')
        i += 1
    return '\n'.join(out)


cards = []
for n, (cid, (prio, why, check)) in enumerate(rows, start=1):
    c = BY[cid]
    page = str(c['page_start']) if c['page_start'] == c['page_end'] else f"{c['page_start']}–{c['page_end']}"
    cards.append(f'''<section class="card p{prio}" id="r{n}"><div class="meta"><span class="num">#{n}</span>
<span class="prio">{prio}</span><b>{html.escape(c['doc_title'])}</b> · PDF page <b>{page}</b> · <code>{cid}</code> · {c['type']}</div>
<div class="label">{html.escape(c['heading_path'])}</div>
<div class="why"><b>Why:</b> {html.escape(why)}<br><b>Check:</b> {html.escape(check)}</div>
<div class="body">{render(c['text'])}</div></section>''')
toc = ''.join(f'<a href="#r{n}" class="p{v[0]}">{n}</a>' for n, (_, v) in enumerate(rows, start=1))
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chunk Validation Viewer</title><style>
:root{{--bg:#fff;--fg:#1b2b2b;--muted:#5c6b73;--line:#d6e2df;--card:#f6faf9;--a:#e4572e;--b:#0e7c7b;--c:#8a9a9f;--th:#e3efec}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111a1a;--fg:#e6efed;--muted:#9fb0b4;--line:#2c3b3b;--card:#172322;--th:#203232}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.45 Calibri,Arial,sans-serif;margin:0;padding:16px;max-width:1100px;margin-inline:auto}}
h1{{font-size:22px;margin:4px 0}} .intro{{color:var(--muted)}}
nav{{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);display:flex;flex-wrap:wrap;gap:4px;z-index:2}}
nav a{{font-size:12px;text-decoration:none;color:#fff;border-radius:4px;padding:1px 5px}} nav a.pA{{background:var(--a)}} nav a.pB{{background:var(--b)}} nav a.pC{{background:var(--c)}}
.card{{scroll-margin-top:170px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;margin:14px 0}}
.meta{{font-size:14px}} .num{{font-weight:bold;margin-right:6px}} .prio{{color:#fff;border-radius:4px;padding:0 6px;margin-right:6px}}
.pA .prio{{background:var(--a)}} .pB .prio{{background:var(--b)}} .pC .prio{{background:var(--c)}}
.label{{color:var(--muted);font-size:13px;margin:4px 0}} .why{{font-size:13px;margin:6px 0 10px}}
.body{{overflow-x:auto}} table{{border-collapse:collapse;margin:6px 0;font-size:13px}} td,th{{border:1px solid var(--line);padding:4px 6px;vertical-align:top}}
th{{background:var(--th)}} td:empty{{background:repeating-linear-gradient(45deg,transparent,transparent 4px,rgba(228,87,46,.12) 4px,rgba(228,87,46,.12) 8px)}}
h4{{margin:8px 0 4px}} p{{margin:3px 0}} code{{font-size:12px}}
</style></head><body><h1>Chunk validation viewer</h1>
<p class="intro">{len(rows)} chunks, in the same order as the <b>Review</b> sheet of chunk_validation.xlsx (by document, then PDF page).
Record verdicts in the spreadsheet. Empty table cells are hatched so you can spot possible merged cells. Colours: <b>A</b> high priority, <b>B</b> medium, <b>C</b> random baseline.</p>
<nav>{toc}</nav>{''.join(cards)}</body></html>'''
open(os.path.join(HERE, 'chunk_viewer.html'), 'w').write(page)
print('written', os.path.join(HERE, 'chunk_validation.xlsx'), os.path.join(HERE, 'chunk_viewer.html'))
