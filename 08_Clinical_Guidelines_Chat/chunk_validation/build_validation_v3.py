"""Build a validation sample from chunks_v3 for the eight re-extracted guidelines.

Weighted toward the places most likely to be wrong after re-extraction:
  - tables rebuilt from the old chunks (cell placement is not verified automatically),
  - hand-transcribed dosing tables (to double-check the transcription),
  - flowcharts kept from the old parse,
  - items carrying source flags (guideline problems to confirm or reject),
  - safety-critical text chunks and their section labels,
plus a random baseline per document.

Outputs (next to this script):
  chunk_validation_v3.xlsx  - review sheet (dropdown verdicts), sorted by document + PDF page
  chunk_viewer_v3.html      - the same items rendered (merged cells kept), to read next to the PDF

Usage: python3 build_validation_v3.py   (deterministic: fixed random seed)
"""
import collections, html, json, os, random, re
import openpyxl
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)
TR = os.path.join(BASE, 'table_reextract')
random.seed(20261106)

DOCS = ['hiv-amendment-2024', 'ncdimh', 'prep-2025', 'anc', 'unaids-linkages-sop', 'tb-2025', 'fp-2021', 'mental-health-deskguide']
SHORT = {'hiv-amendment-2024': 'HIV Amendment 2024', 'ncdimh': 'NCDIMH', 'prep-2025': 'PrEP 2025', 'anc': 'ANC',
         'unaids-linkages-sop': 'Linkages SOP', 'tb-2025': 'TB 2025', 'fp-2021': 'FP 2021', 'mental-health-deskguide': 'Mental Health desk guide'}
K = [json.loads(l) for l in open(os.path.join(BASE, 'chunks_v3', 'chunks.jsonl'))]
K = [k for k in K if k['doc_id'] in DOCS]

# one review unit per re-extracted item (all embedding parts share the full text), one per other chunk
units = collections.OrderedDict()
for k in K:
    key = k.get('table_id') or k['chunk_id']
    if key not in units:
        units[key] = k

# ---------- how each item was produced ----------
GENERATED = re.compile(r'-tbl-p\d+-\d{4}$')
HAND_BATCHES = ['tb_b02.py', 'tb_b04.py', 'tb_b08.py', 'mh_b03.py', 'lk_b02.py', 'lk_b03.py']
CHECKED_KEPT = ['tb_b06.py']


def batch_ids(name):
    ids = set()
    src = open(os.path.join(TR, 'batches', name)).read()
    for m in re.finditer(r'''(?:T|D|B|X)\(\s*["']([a-z0-9-]+)["']''', src):
        ids.add(m.group(1))
    return ids


hand_ids = set().union(*(batch_ids(b) for b in HAND_BATCHES))
checked_kept = set().union(*(batch_ids(b) for b in CHECKED_KEPT))


def how(u):
    tid = u.get('table_id')
    if not tid:
        return 'Kept from old parse' if u['type'] in ('diagram', 'table') else 'Text (labels checked)'
    short = tid[len(u['doc_id']) + 1:]
    if short in checked_kept:
        return 'Old flowchart text, checked against image'
    if tid.endswith('annex4-counselling-messages'):
        return 'Rebuilt from old chunks (word-checked)'
    if GENERATED.search(tid) and short not in hand_ids:
        return 'Rebuilt from old chunks (word-checked)'
    return 'Transcribed from page image'


# ---------- signals ----------
DOSE = re.compile(r'\b\d+(?:[.,]\d+)?\s*(?:mg|mcg|µg|g|ml|mL|units?|IU|mmol|mEq|mg/kg|ml/kg|mcg/kg|tabs?|tablets?|vials?)\b', re.I)
SAFETY = re.compile(r'\b(dose|dosing|dosage|max(?:imum)?|contraindicat\w*|overdose|toxic\w*|stat\b|loading|IV|IM|infusion|'
                    r'weight band|kg|do not|never|avoid|stop|refer urgently|emergency|interaction|pregnan\w*|breastfeed\w*|'
                    r'neonat\w*|infant|MEC|category)\b', re.I)


def safety(u):
    t = u['text']
    return 2 * len(DOSE.findall(t)) + len(SAFETY.findall(t))


FLAG_CLINICAL = re.compile(r'\b(dose|mg|kg|WHO|category|recommend|contradict|conflict|regimen|maximum|threshold|'
                           r'definition|criteria|should|mmHg|ml/min|weeks?|months?|days?)\b', re.I)

picked = collections.OrderedDict()


def pick(key, prio, why, check):
    if key in units and key not in picked:
        picked[key] = (prio, why, check)


def capped(cands, n, cap):
    out, cnt = [], collections.Counter()
    for u in cands:
        if len(out) >= n:
            break
        key = u.get('table_id') or u['chunk_id']
        if cnt[u['doc_id']] < cap and key not in picked:
            out.append(u)
            cnt[u['doc_id']] += 1
    return out


U = list(units.values())
H = {id(u): how(u) for u in U}

# A1. rebuilt tables with safety content: cell placement is the main unverified risk
rebuilt = sorted((u for u in U if H[id(u)].startswith('Rebuilt')), key=lambda u: -safety(u))
for u in capped(rebuilt, 45, 10):
    pick(u['table_id'], 'A', 'Rebuilt from old chunks; safety content (doses / criteria)',
         'Every value sits in the right row and column (compare cell by cell); nothing from the PDF table is missing.')
# A2. hand-transcribed dosing tables
hand_dose = sorted((u for u in U if H[id(u)] == 'Transcribed from page image' and u['type'] == 'table' and len(DOSE.findall(u['text'])) >= 4),
                   key=lambda u: -safety(u))
for u in capped(hand_dose, 30, 6):
    pick(u['table_id'], 'A', 'Dosing table transcribed from the page image',
         'Every dose, unit, frequency and weight band matches the PDF exactly.')
# A3. items with clinically significant source flags
flagged = [u for u in U if u.get('source_flags') and any(FLAG_CLINICAL.search(f) for f in u['source_flags'])]
flagged.sort(key=lambda u: -(len(u['source_flags']) * 3 + safety(u)))
for u in capped(flagged, 40, 7):
    pick(u.get('table_id') or u['chunk_id'], 'A', 'Carries a source flag (possible problem in the guideline itself)',
         'Is the flagged problem really in the PDF (not an extraction error)? Mark "Source flag correct?". Also check the item itself.')
# B1. flowcharts kept from the old parse (or old text checked against image)
kept = sorted((u for u in U if u['type'] == 'diagram' and H[id(u)] in ('Kept from old parse', 'Old flowchart text, checked against image')),
              key=lambda u: -safety(u))
for u in capped(kept, 20, 6):
    pick(u.get('table_id') or u['chunk_id'], 'B', 'Flowchart text from the old parse',
         'Each decision and branch matches the arrows in the PDF flowchart; no step or outcome is missing.')
# B2. other rebuilt tables (structure only)
other_rebuilt = [u for u in rebuilt if u['table_id'] not in picked]
random.shuffle(other_rebuilt)
for u in capped(other_rebuilt, 20, 5):
    pick(u['table_id'], 'B', 'Rebuilt from old chunks',
         'Rows and columns line up with the PDF; no values shifted, merged with another table, or lost.')
# B3. safety-critical text chunks (doses outside tables) and their labels
texts = sorted((u for u in U if u['type'] == 'text'), key=lambda u: -safety(u))
for u in capped(texts, 24, 3):
    pick(u['chunk_id'], 'B', 'Safety-critical text (doses / emergency steps)',
         'Every dose and step matches the PDF; nothing cut off at the start or end; the section label is right.')
# C. random baseline per document: 2 hand-transcribed items + 2 text chunks
for doc in DOCS:
    pool_i = [u for u in U if u['doc_id'] == doc and u.get('table_id') and u['table_id'] not in picked]
    pool_t = [u for u in U if u['doc_id'] == doc and u['type'] == 'text' and u['chunk_id'] not in picked]
    for u in random.sample(pool_i, min(2, len(pool_i))):
        pick(u['table_id'], 'C', 'Random baseline (re-extracted item)', 'Content and layout match the PDF; label is right.')
    for u in random.sample(pool_t, min(2, len(pool_t))):
        pick(u['chunk_id'], 'C', 'Random baseline (text chunk)', 'Text is complete and readable; the section label is right.')

# ---------- reduce to 50: core 25 + next 25 ----------
# Tables the automatic completeness audit already caught are being repaired, so they are left out.
# What remains is what a script cannot judge, plus audit-clean rebuilt tables to test the audit itself.
AUD = json.load(open(os.path.join(TR, 'audit', 'cell_audit.json')))
REPAIR = set(json.load(open(os.path.join(TR, 'audit', 'repair_ids.json'))))
for k in list(picked):
    if k in REPAIR:
        del picked[k]
clean = [u for u in rebuilt if u['table_id'] in AUD and AUD[u['table_id']].get('pdf_words_in_table') and not AUD[u['table_id']]['issues']
         and not AUD[u['table_id']]['lost'] and not AUD[u['table_id']]['elsewhere'] and u['table_id'] not in REPAIR]
for u in capped(clean, 10, 3):
    picked[u['table_id']] = ('A', 'Rebuilt table that passed the automatic completeness audit',
                             'Tests the audit: is every value in the right row and column, and is anything missing? An error here means the audit misses things.')
CATS = [('source flag', 9), ('transcribed from the page image', 5), ('passed the automatic', 4), ('Flowchart', 3),
        ('Safety-critical text', 2), ('Random baseline (text', 2)]
core, nxt = [], []
for key_, n in CATS:
    cand = [k for k, v in picked.items() if key_.lower() in v[1].lower()]
    cnt = collections.Counter()
    for k in cand:  # spread across documents: at most 2 per document per category in the core set
        d = units[k]['doc_id']
        if len([c for c in core if c[1] == key_]) < n and cnt[d] < 2:
            core.append((k, key_)); cnt[d] += 1
    rest = [k for k in cand if k not in [c[0] for c in core]]
    nxt += [(k, key_) for k in rest[:n]]
picked = collections.OrderedDict([(k, ('A',) + picked[k][1:]) for k, _ in core] + [(k, ('B',) + picked[k][1:]) for k, _ in nxt])
rows = sorted(picked.items(), key=lambda kv: (kv[1][0], DOCS.index(units[kv[0]]['doc_id']), units[kv[0]]['page_start'], kv[0]))
print('sample size', len(rows), collections.Counter(v[0] for _, v in rows),
      collections.Counter(SHORT[units[k]['doc_id']] for k, _ in rows), collections.Counter(H[id(units[k])] for k, _ in rows))

# ---------- workbook ----------
wb = openpyxl.Workbook()
ins = wb.active
ins.title = 'How to validate'
lines = [
    ('Chunk validation sample (v3: re-extracted chunks)', True),
    (f'{len(rows)} items from chunks_v3 across eight guidelines, weighted toward where errors are most likely after re-extraction.', False),
    ('', False),
    ('How to work through it', True),
    ('1. Open chunk_viewer_v3.html in a browser next to the PDF. Tables are drawn with their merged cells; source flags are shown under each item.', False),
    ('2. Rows 1-25 are the core set, rows 26-50 the next set; within each, sorted by document then PDF page.', False),
    ('   "PDF page" is the page in the full original PDF (TB, FP, NCDIMH and Mental Health were uploaded in parts; use the full document page).', False),
    ('3. Read "What to check", compare with the PDF, and pick a value in each yellow column.', False),
    ('4. Do the core 25 first. Tables the automatic audit found incomplete are not here: they are being repaired separately (table_reextract/audit/REPAIR_WORKLIST.md).', False),
    ('5. Only write a note when something is wrong: say what the PDF has, e.g. "PDF says 10 mg, chunk says 1 mg", or "this value belongs in the 16-24 kg column".', False),
    ('', False),
    ('"How produced" (the main risk signal)', True),
    ('Transcribed from page image: typed from the page image, every number checked against the PDF text. Main risk: a cell misread or misplaced.', False),
    ('Rebuilt from old chunks (word-checked): the old parse was repaired automatically (split rows joined, pieces merged); every word is in the PDF, but cell positions were NOT checked. Main risk: a value in the wrong row/column, or two tables joined.', False),
    ('Kept from old parse / old flowchart text: not re-extracted. Main risk: wrong or missing branches.', False),
    ('Text (labels checked): an ordinary text chunk; its section label was fixed by rule or by hand.', False),
    ('', False),
    ('Columns to fill (yellow)', True),
    ('Text complete?  Yes / Partly / No: is anything missing, cut off or out of order?', False),
    ('Numbers correct?  Yes / No / No numbers: doses, units, thresholds, weight bands exactly as in the PDF.', False),
    ('Table structure OK?  Yes / Minor issue / Wrong / Not a table: every value in the right row and column; one table per item.', False),
    ('Label correct?  Yes / Roughly / Wrong: does the section label describe where this sits in the document?', False),
    ('Source flag correct?  Only for items with flags: Correct / Partly / Wrong (extraction error) / n/a. Is the guideline problem real?', False),
    ('Overall  OK / Minor (cosmetic) / Major (could mislead a clinician): your bottom line.', False),
    ('', False),
    ('What happens next', True),
    ('Major issues are fixed in the batch files (table_reextract/batches) and the chunks rebuilt; confirmed source flags stay in SOURCE_ISSUES.md, rejected ones are removed.', False),
    ('The Summary sheet counts your verdicts, including by "How produced", so we can see which method needs more checking.', False),
]
for i, (t, bold) in enumerate(lines, start=1):
    c = ins.cell(i, 1, t)
    c.font = Font(bold=bold, size=14 if i == 1 else 11)
    c.alignment = Alignment(wrap_text=True)
ins.column_dimensions['A'].width = 150

ws = wb.create_sheet('Review')
head = ['#', 'Set (A = core 25, B = next 25)', 'Document', 'PDF page', 'Item / chunk id', 'Type', 'How produced', 'Section label', 'Why picked', 'What to check',
        'Source flags (guideline problems to confirm)',
        'Text complete?', 'Numbers correct?', 'Table structure OK?', 'Label correct?', 'Source flag correct?', 'Overall', 'Note',
        'Chunk text (also in chunk_viewer_v3.html)']
widths = [5, 8, 16, 9, 30, 8, 22, 40, 28, 42, 50, 12, 12, 14, 12, 14, 12, 40, 70]
ws.append(head)
fill_cols = range(12, 19)
for j, w in enumerate(widths, start=1):
    ws.column_dimensions[openpyxl.utils.get_column_letter(j)].width = w
    c = ws.cell(1, j)
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor='B8860B' if j in fill_cols else '0F3B3A')
    c.alignment = Alignment(wrap_text=True, vertical='center')
yellow = PatternFill('solid', fgColor='FFF2CC')
thin = Border(bottom=Side(style='thin', color='D9D9D9'))
for n, (key, (prio, why, check)) in enumerate(rows, start=1):
    u = units[key]
    ps, pe = u['page_start'], u.get('page_end') or u['page_start']
    page = str(ps) if ps == pe else f'{ps}–{pe}'
    flags = '\n'.join('• ' + f for f in (u.get('source_flags') or []))
    text = u['text'] if len(u['text']) < 32000 else u['text'][:32000] + ' …'
    ws.append([n, prio, SHORT[u['doc_id']], page, key, u['type'],
               H[id(u)], u['heading_path'], why, check, flags,
               '', '', 'Not a table' if u['type'] != 'table' else '', '', '' if flags else 'n/a', '', '', text])
    for j in range(1, len(head) + 1):
        cell = ws.cell(n + 1, j)
        cell.alignment = Alignment(wrap_text=True, vertical='top')
        cell.border = thin
        if j in fill_cols and not (j == 16 and not flags):
            cell.fill = yellow
    ws.row_dimensions[n + 1].height = 100
last = len(rows) + 1
for col, opts in [('L', 'Yes,Partly,No'), ('M', 'Yes,No,No numbers'), ('N', 'Yes,Minor issue,Wrong,Not a table'),
                  ('O', 'Yes,Roughly,Wrong'), ('P', 'Correct,Partly,Wrong (extraction error),n/a'), ('Q', 'OK,Minor,Major')]:
    dv = DataValidation(type='list', formula1=f'"{opts}"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f'{col}2:{col}{last}')
ws.freeze_panes = 'F2'
ws.auto_filter.ref = f'A1:S{last}'

sm = wb.create_sheet('Summary')
sm.append(['Measure', 'Count', 'Share of reviewed'])
for c in sm[1]:
    c.font = Font(bold=True)
R = f'Review!Q2:Q{last}'
items = [('Rows reviewed (Overall filled)', f'=COUNTA({R})', None),
         ('Overall: OK', f'=COUNTIF({R},"OK")', 1), ('Overall: Minor', f'=COUNTIF({R},"Minor")', 1), ('Overall: Major', f'=COUNTIF({R},"Major")', 1),
         ('Numbers wrong', f'=COUNTIF(Review!M2:M{last},"No")', 1),
         ('Text incomplete (Partly or No)', f'=COUNTIF(Review!L2:L{last},"Partly")+COUNTIF(Review!L2:L{last},"No")', 1),
         ('Table structure wrong', f'=COUNTIF(Review!N2:N{last},"Wrong")', 1),
         ('Label wrong', f'=COUNTIF(Review!O2:O{last},"Wrong")', 1),
         ('Source flags confirmed', f'=COUNTIF(Review!P2:P{last},"Correct")', None),
         ('Source flags wrong (extraction error)', f'=COUNTIF(Review!P2:P{last},"Wrong (extraction error)")', None)]
for how_label in ['Transcribed from page image', 'Rebuilt from old chunks (word-checked)', 'Kept from old parse',
                  'Old flowchart text, checked against image', 'Text (labels checked)']:
    items.append((f'Major – {how_label}', f'=COUNTIFS(Review!G2:G{last},"{how_label}",{R},"Major")', None))
    items.append((f'Reviewed – {how_label}', f'=COUNTIFS(Review!G2:G{last},"{how_label}",{R},"<>")', None))
for i, (lab, f, share) in enumerate(items, start=2):
    sm.cell(i, 1, lab)
    sm.cell(i, 2, f)
    if share:
        sm.cell(i, 3, f'=IF($B$2=0,"",B{i}/$B$2)').number_format = '0%'
sm.column_dimensions['A'].width = 55
sm.column_dimensions['B'].width = 10
sm.column_dimensions['C'].width = 18
wb.move_sheet('Summary', offset=-1)
wb.save(os.path.join(HERE, 'chunk_validation_v3.xlsx'))


# ---------- HTML viewer ----------
def render_md(md):
    out, i, ls = [], 0, md.split('\n')

    def inline(s):
        s = html.escape(s)
        s = re.sub(r'&lt;br\s*/?&gt;', '<br>', s)
        s = re.sub(r'&lt;/?(mark|sup|sub|u)&gt;', '', s)
        return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    while i < len(ls):
        l = ls[i]
        if l.strip().startswith('|'):
            block = []
            while i < len(ls) and ls[i].strip().startswith('|'):
                block.append(ls[i])
                i += 1
            out.append('<table>')
            for r in block:
                if re.match(r'^\s*\|[\s:|-]+\|\s*$', r):
                    continue
                out.append('<tr>' + ''.join(f'<td>{inline(x.strip())}</td>' for x in r.strip().strip('|').split('|')) + '</tr>')
            out.append('</table>')
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', l)
        if m:
            out.append(f'<h4>{inline(m.group(2))}</h4>')
        elif l.strip():
            out.append(f'<p>{inline(l)}</p>')
        i += 1
    return '\n'.join(out)


def body(u):
    if u.get('html'):
        return re.sub(r'&lt;br\s*/?&gt;', '<br>', u['html'])
    return render_md(u['text'])


cards = []
for n, (key, (prio, why, check)) in enumerate(rows, start=1):
    u = units[key]
    ps, pe = u['page_start'], u.get('page_end') or u['page_start']
    page = str(ps) if ps == pe else f'{ps}–{pe}'
    flags = ''.join(f'<li>{html.escape(f)}</li>' for f in (u.get('source_flags') or []))
    flags = f'<div class="flags"><b>Source flags to confirm:</b><ul>{flags}</ul></div>' if flags else ''
    cards.append(f'''<section class="card p{prio}" id="r{n}"><div class="meta"><span class="num">#{n}</span><span class="prio">{prio}</span>
<b>{html.escape(SHORT[u['doc_id']])}</b> · PDF page <b>{page}</b> · <code>{html.escape(key)}</code> · {html.escape(u['type'])} · <span class="how">{html.escape(H[id(u)])}</span></div>
<div class="label">{html.escape(u['heading_path'])}</div>
<div class="why"><b>Why:</b> {html.escape(why)}<br><b>Check:</b> {html.escape(check)}</div>{flags}
<div class="body">{body(u)}</div></section>''')
toc = ''.join(f'<a href="#r{n}" class="p{v[0]}" title="{html.escape(SHORT[units[k]["doc_id"]])}">{n}</a>' for n, (k, v) in enumerate(rows, start=1))
doc_jump = ' · '.join(f'<a href="#r{next(n for n, (k, _) in enumerate(rows, start=1) if units[k]["doc_id"] == d)}">{html.escape(SHORT[d])}</a>'
                      for d in DOCS if any(units[k]['doc_id'] == d for k, _ in rows))
page_html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chunk Validation v3</title><style>
:root{{--bg:#fff;--fg:#1b2b2b;--muted:#5c6b73;--line:#d6e2df;--card:#f6faf9;--a:#e4572e;--b:#0e7c7b;--c:#8a9a9f;--th:#e3efec;--flag:#fff4e5}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111a1a;--fg:#e6efed;--muted:#9fb0b4;--line:#2c3b3b;--card:#172322;--th:#203232;--flag:#2d2414}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.45 Calibri,Arial,sans-serif;margin:0 auto;padding:16px;max-width:1150px}}
h1{{font-size:22px;margin:4px 0}} .intro{{color:var(--muted)}}
nav{{position:sticky;top:0;background:var(--bg);padding:8px 0;border-bottom:1px solid var(--line);z-index:2}}
nav .nums{{display:flex;flex-wrap:wrap;gap:3px;margin-top:6px}}
nav .nums a{{font-size:11px;text-decoration:none;color:#fff;border-radius:4px;padding:0 4px}} nav a.pA{{background:var(--a)}} nav a.pB{{background:var(--b)}} nav a.pC{{background:var(--c)}}
.card{{scroll-margin-top:190px;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;margin:14px 0}}
.meta{{font-size:14px}} .num{{font-weight:bold;margin-right:6px}} .prio{{color:#fff;border-radius:4px;padding:0 6px;margin-right:6px}}
.pA .prio{{background:var(--a)}} .pB .prio{{background:var(--b)}} .pC .prio{{background:var(--c)}} .how{{font-style:italic}}
.label{{color:var(--muted);font-size:13px;margin:4px 0}} .why{{font-size:13px;margin:6px 0 10px}}
.flags{{background:var(--flag);border-left:4px solid var(--a);padding:6px 10px;font-size:13px;margin-bottom:8px}} .flags ul{{margin:4px 0 0 18px;padding:0}}
.body{{overflow-x:auto}} table{{border-collapse:collapse;margin:6px 0;font-size:13px}} td,th{{border:1px solid var(--line);padding:4px 6px;vertical-align:top}}
th{{background:var(--th)}} td:empty{{background:repeating-linear-gradient(45deg,transparent,transparent 4px,rgba(228,87,46,.12) 4px,rgba(228,87,46,.12) 8px)}}
h4{{margin:8px 0 4px}} p{{margin:3px 0}} code{{font-size:12px}} pre{{white-space:pre-wrap}}
</style></head><body><h1>Chunk validation viewer (v3)</h1>
<p class="intro">{len(rows)} items from chunks_v3, same order as the Review sheet in chunk_validation_v3.xlsx. Red = core 25, teal = next 25. Empty table cells are hatched.</p>
<nav><div>Jump to: {doc_jump}</div><div class="nums">{toc}</div></nav>
{''.join(cards)}
</body></html>'''
open(os.path.join(HERE, 'chunk_viewer_v3.html'), 'w').write(page_html)
print('wrote chunk_validation_v3.xlsx and chunk_viewer_v3.html')
