"""Review page + chunk records for re-extracted tables.

Usage: python3 make_review.py TABLES_OUT.json PAGE_IMAGE_DIR NOTES.json OUT_HTML OUT_CHUNKS_JSONL DOC_TITLE
  PAGE_IMAGE_DIR holds pgN.jpg page renders; NOTES.json maps old chunk_id -> reviewer note.
"""
import base64, html as H, json, os, re, sys

tables_path, img_dir, notes_path, out_html, out_chunks, doc_title = sys.argv[1:7]
T = json.load(open(tables_path))
notes = json.load(open(notes_path)) if os.path.exists(notes_path) else {}


def md_to_html(md):
    out, lines, i = [], md.split('\n'), 0
    def inline(s):
        s = s.replace('\\*', '\x00')
        s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', H.escape(s).replace('&lt;br/&gt;', '<br>'))
        return s.replace('\x00', '*')
    while i < len(lines):
        if lines[i].startswith('|'):
            block = []
            while i < len(lines) and lines[i].startswith('|'):
                block.append(lines[i]); i += 1
            out.append('<table>')
            for j, r in enumerate(block):
                if re.match(r'^\|[\s:|-]+\|$', r):
                    continue
                tag = 'th' if j == 0 else 'td'
                out.append('<tr>' + ''.join(f'<{tag}>{inline(c.strip())}</{tag}>' for c in r.strip().strip('|').split('|')) + '</tr>')
            out.append('</table>')
            continue
        l = lines[i]
        if l.startswith('#'):
            out.append(f'<h4>{inline(l.lstrip("# "))}</h4>')
        elif l.strip():
            out.append(f'<p>{inline(l)}</p>')
        i += 1
    return '\n'.join(out)


cards, records = [], []
for t in T:
    pages = t.get('pages') or [t['page']]
    imgs = ''.join(f'<img src="data:image/jpeg;base64,{base64.b64encode(open(os.path.join(img_dir, f"pg{p}.jpg"), "rb").read()).decode()}" alt="PDF page {p}">'
                   for p in pages if os.path.exists(os.path.join(img_dir, f'pg{p}.jpg')))
    chk = t['checks']
    ok = all(not v for v in chk.values())
    chk_html = ('<span class="ok">All numbers match</span>' if ok else '<span class="bad">Check: ' +
                H.escape(json.dumps(chk)) + '</span>') + (' (image-only table: compared with the old chunks, no PDF text layer)'
                                                          if t['image_only'] else ' (compared with the PDF text layer and the old chunks)')
    your = ''.join(f'<li><code>{c}</code>: {H.escape(notes[c])}</li>' for c in t['replaces_chunks'] if c in notes)
    flags = ''.join(f'<li>{H.escape(f)}</li>' for f in t['source_flags'])
    cards.append(f'''<section class="card"><h2>{H.escape(t["caption"])}</h2>
<div class="meta">PDF page {t["page"]} · <code>{t["table_id"]}</code> · replaces {", ".join(f"<code>{c}</code>" for c in t["replaces_chunks"])}</div>
<div class="meta">{chk_html}</div>
{f"<div class='flags'><b>Points to check in the source:</b><ul>{flags}</ul></div>" if flags else ""}
{f"<div class='notes'><b>Your notes on the old chunks:</b><ul>{your}</ul></div>" if your else ""}
<div class="grid"><div><h3>PDF page</h3>{imgs}</div>
<div><h3>New: {"flowchart" if t.get("kind") == "diagram" else "box" if t.get("kind") == "box" else "table with merged cells (as in the PDF)"}</h3><div class="tbl">{t["html"]}</div>
<h3>New: what the model receives</h3><div class="tbl">{md_to_html(t["text"])}</div></div></div>
<details><summary>New: embedding text ({len(t["embed_text"])} part{"s" if len(t["embed_text"]) > 1 else ""})</summary><pre>{H.escape(chr(10).join(t["embed_text"]))}</pre></details>
<details><summary>Old chunks</summary><div class="tbl">{md_to_html(t["old_text"])}</div></details></section>''')
    n = len(t['embed_text'])
    for i, e in enumerate(t['embed_text']):
        records.append(dict(chunk_id=f'{t["table_id"]}-p{i + 1}' if n > 1 else t['table_id'], table_id=t['table_id'],
                            table_part=f'{i + 1}/{n}', doc_title=doc_title, type={'diagram': 'diagram', 'box': 'text'}.get(t.get('kind'), 'table'), heading_path=t['heading_path'],
                            page_start=t['page'], page_end=t['page'], text=t['text'], html=t['html'], embed_text=e,
                            replaces_chunks=t['replaces_chunks'], source_flags=t['source_flags'],
                            extraction='claude-vision', number_check=chk))

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Re-extraction Review</title><style>
:root{{--bg:#fff;--fg:#1b2b2b;--muted:#5c6b73;--line:#cfdcd9;--card:#f6faf9;--th:#e3efec;--ok:#0e7c7b;--bad:#c0392b;--sec:#fde7dc}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111a1a;--fg:#e6efed;--muted:#9fb0b4;--line:#2c3b3b;--card:#172322;--th:#203232;--sec:#3a2a22}}}}
body{{background:var(--bg);color:var(--fg);font:15px/1.45 Calibri,Arial,sans-serif;margin:0 auto;padding:16px;max-width:1500px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:14px;margin:16px 0}}
h1{{font-size:22px}} h2{{font-size:18px;margin:0 0 4px}} h3{{font-size:14px;color:var(--muted);margin:10px 0 4px}}
.meta{{font-size:13px;color:var(--muted);margin:2px 0}} .ok{{color:var(--ok);font-weight:bold}} .bad{{color:var(--bad);font-weight:bold}}
.flags,.notes{{font-size:13px;margin:6px 0}} .notes{{color:var(--muted)}}
.grid{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:16px}} @media (max-width:900px){{.grid{{grid-template-columns:1fr}}}}
img{{width:100%;border:1px solid var(--line)}} .tbl{{overflow-x:auto}}
table{{border-collapse:collapse;font-size:13px;margin:4px 0}} td,th{{border:1px solid var(--line);padding:4px 6px;vertical-align:top}}
th{{background:var(--th)}} th.section{{background:var(--sec);text-align:left}} td.note{{font-style:italic}} caption{{text-align:left;font-weight:bold;padding:4px 0}}
pre{{white-space:pre-wrap;font-size:12px}} pre.diagram{{font-size:13px;font-family:Calibri,Arial,sans-serif}} .box{{border:2px solid #f2b134;padding:8px;border-radius:6px}} summary{{cursor:pointer;color:var(--muted);margin-top:8px}}
</style></head><body><h1>{H.escape(doc_title)}: re-extracted tables, boxes and flowcharts</h1>
<p>Every table, highlighted box and flowchart in the Amendment, read from the PDF page image by Claude: merged cells, section rows and footnotes kept for tables; branches, combined conditions and line breaks kept for flowcharts, with their captions and printed notes folded in. Compare each with the page on the left. "Points to check in the source" lists problems in the guideline itself.
The "what the model receives" version fills merged cells in, shows a long note that spans every row once, and attaches footnotes. The embedding text is split into parts under 512 tokens that all return the whole table.</p>
{"".join(cards)}</body></html>'''
open(out_html, 'w').write(page)
with open(out_chunks, 'w') as fh:
    for r in records:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
print('review', out_html, 'chunks', len(records))
