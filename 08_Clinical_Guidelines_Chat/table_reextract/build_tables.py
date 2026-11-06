"""Turn re-extracted table specs (cells with rowspan/colspan, section rows, footnotes) into chunk-ready output.

For each table it produces:
  html         - the table with real rowspan/colspan (faithful to the PDF), for display
  text         - readable markdown for the language model: merged cells filled in, section rows as headings,
                 long cells that span many rows printed once as "Applies to all rows above", footnotes attached
  embed_text   - row-by-row sentences for the embedder ("Row label | column: value; ..."), with section
                 and merged-cell values filled in
and runs number checks:
  * every number in the new table must appear in the PDF text layer of its page(s) (if the page has one),
    and in the original chunks (always)
  * every number in the original chunks must appear in the new table (catches dropped rows/cells)

Usage: python3 build_tables.py SPEC.json PDF_TEXT_DIR CHUNKS.jsonl OUT_DIR
  PDF_TEXT_DIR holds pN.txt (pdftotext -layout per page).
"""
import html as H
import json
import os
import re
import sys

LONG_SPAN_CHARS, LONG_SPAN_ROWS = 120, 3


def grid(rows, ncols):
    """rows: list of data rows (lists of cells). Returns matrix of (cell, is_origin)."""
    out, pending = [], {}          # pending[(r, c)] = cell occupying it from a span above
    for r, row in enumerate(rows):
        line, c, it = [], 0, iter(row)
        while c < ncols:
            if (r, c) in pending:
                line.append((pending.pop((r, c)), False)); c += 1; continue
            cell = next(it, None)
            if cell is None:
                line.append(({'t': ''}, True)); c += 1; continue
            cs, rs = cell.get('cs', 1), cell.get('rs', 1)
            for dc in range(cs):
                line.append((cell, dc == 0))
                for dr in range(1, rs):
                    pending[(r + dr, c + dc)] = cell
            c += cs
        if next(it, None) is not None:
            raise ValueError(f'row {r} has more cells than columns: {row}')
        out.append(line)
    if pending:
        raise ValueError(f'spans run past the last row: {sorted(pending)}')
    return out


def ncols_of(header):
    return sum(c.get('cs', 1) for c in header[0])


def col_labels(header, ncols):
    """One label per column, joining stacked header rows ('Weight in KG' + '3 - 5.9')."""
    hg = grid(header, ncols)
    labels = []
    for c in range(ncols):
        parts = []
        for r in range(len(hg)):
            t = hg[r][c][0]['t']
            if t and (not parts or parts[-1] != t):
                parts.append(t)
        labels.append(' '.join(parts))
    return labels


def split_sections(body):
    """Data rows (for the grid) plus, for each data-row index, the section heading in force."""
    rows, section_of, current = [], [], None
    for item in body:
        if isinstance(item, dict) and 'section' in item:
            current = item['section']
        else:
            rows.append(item); section_of.append(current)
    return rows, section_of


def cross_cutting(g, section_of):
    """Origin positions of cells that span EVERY row of their section and are long text: these are notes
    for the whole block (e.g. a 'Special considerations' column), not values of one row."""
    blocks = {}
    for r, sec in enumerate(section_of):
        blocks.setdefault(sec, []).append(r)
    out = set()
    for sec, rows in blocks.items():
        for c in range(len(g[0])):
            cell = g[rows[0]][c][0]
            if (len(cell['t']) > LONG_SPAN_CHARS and cell.get('rs', 1) == len(rows) and len(rows) > 1
                    and all(g[r][c][0] is cell for r in rows)):
                out.add((sec, c))
    return out


def render_html(t, ncols):
    out = [f'<table data-table-id="{t["table_id"]}">', f'<caption>{H.escape(t["caption"])}</caption>', '<thead>']
    for row in t['header']:
        out.append('<tr>' + ''.join(
            f'<th{" colspan=%d" % c["cs"] if c.get("cs", 1) > 1 else ""}{" rowspan=%d" % c["rs"] if c.get("rs", 1) > 1 else ""}>'
            f'{H.escape(c["t"])}</th>' for c in row) + '</tr>')
    out.append('</thead><tbody>')
    for item in t['body']:
        if isinstance(item, dict):
            out.append(f'<tr><th colspan={ncols} class="section">{H.escape(item["section"])}</th></tr>')
        else:
            out.append('<tr>' + ''.join(
                f'<td{" colspan=%d" % c["cs"] if c.get("cs", 1) > 1 else ""}{" rowspan=%d" % c["rs"] if c.get("rs", 1) > 1 else ""}>'
                f'{H.escape(c["t"])}</td>' for c in item) + '</tr>')
    if t.get('table_note'):
        out.append(f'<tr><td colspan={ncols} class="note">{H.escape(t["table_note"])}</td></tr>')
    out.append('</tbody></table>')
    return '\n'.join(out)


def md_cell(s):
    return s.replace('|', '/').replace('\n', ' ').replace('*', '\\*')


def render_text(t, ncols):
    labels = col_labels(t['header'], ncols)
    rows, section_of = split_sections(t['body'])
    g = grid(rows, ncols)
    cc = cross_cutting(g, section_of)
    out = [f'### {t["caption"]}', '']
    if t.get('context_before'):
        out += [t['context_before'], '']
    blocks = []
    for r, sec in enumerate(section_of):
        if not blocks or blocks[-1][0] != sec:
            blocks.append((sec, []))
        blocks[-1][1].append(r)
    for sec, rs in blocks:
        cols = [c for c in range(ncols) if (sec, c) not in cc]
        if sec:
            out += [f'**{sec}**', '']
        out.append('| ' + ' | '.join(md_cell(labels[c]) for c in cols) + ' |')
        out.append('| ' + ' | '.join('---' for _ in cols) + ' |')
        for r in rs:
            vals = []
            for c in cols:
                cell = g[r][c][0]
                same_left = c > 0 and (c - 1) in cols and g[r][c - 1][0] is cell
                vals.append('(same as left)' if same_left and len(cell['t']) > 60 else md_cell(cell['t']))
            out.append('| ' + ' | '.join(vals) + ' |')
        for c in range(ncols):
            if (sec, c) in cc:
                out += ['', f'**{labels[c]} (applies to every row{" in this section" if sec else ""}):** {g[rs[0]][c][0]["t"]}']
        out.append('')
    if t.get('table_note'):
        out += [f'**Note:** {t["table_note"]}', '']
    if t.get('footnotes'):
        out += t['footnotes']
    return '\n'.join(out).strip()


def render_embed(t, ncols, doc_title):
    labels = col_labels(t['header'], ncols)
    rows, section_of = split_sections(t['body'])
    g = grid(rows, ncols)
    cc = cross_cutting(g, section_of)
    k = t.get('row_header_cols', 1)
    lines = [f'{doc_title} | {t["heading_path"]} (page {t["page"]})', '', t['caption'] + '.']
    done = set()
    for r, line in enumerate(g):
        sec = section_of[r]
        key = ' / '.join(line[c][0]['t'] for c in range(k) if line[c][0]['t'])
        if sec:
            key = f'{sec} > {key}'
        vals, c = [], k
        while c < ncols:
            cell, c2 = line[c][0], c
            while c2 + 1 < ncols and (line[c2 + 1][0] is cell or line[c2 + 1][0]['t'] == cell['t']):
                c2 += 1
            if cell['t'] and (sec, c) not in cc:
                lab = labels[c] if c2 == c else (f'{labels[c]} / {labels[c2]}' if c2 == c + 1
                                                   else f'{labels[c]} to {labels[c2]}')
                vals.append(f'{lab}: {cell["t"].rstrip(".")}')
            c = c2 + 1
        lines.append(f'{key}: ' + '; '.join(vals) + '.')
        last_of_block = r + 1 == len(g) or section_of[r + 1] != sec
        if last_of_block:
            for c in range(ncols):
                if (sec, c) in cc and (sec, c) not in done:
                    done.add((sec, c))
                    lines.append(f'{labels[c]} (all rows{" of " + sec if sec else ""}): {line[c][0]["t"]}')
    if t.get('table_note'):
        lines.append(t['table_note'])
    lines += t.get('footnotes', [])
    return lines


def embed_parts(lines, budget_tokens=480):
    """Split row sentences into parts under the budget; every part repeats the header and caption."""
    head, body = lines[:3], []
    limit = budget_tokens * 4 * 2 // 3          # a single line longer than this is split at sentence/list breaks
    for ln in (x for l in lines[3:] for x in l.split('\n')):
        while len(ln) > limit:
            cut = max(ln.rfind(sep, 0, limit) for sep in ('<br/>', '; ', '. ', ', '))
            if cut <= 0:
                break
            body.append(ln[:cut + 1].rstrip()); ln = ln[cut + 1:].lstrip('/> ')
        body.append(ln)
    parts, cur = [], []
    size = lambda xs: len('\n'.join(head + xs)) // 4
    for ln in body:
        if cur and size(cur + [ln]) > budget_tokens:
            parts.append(cur); cur = []
        cur.append(ln)
    if cur:
        parts.append(cur)
    n = len(parts)
    return ['\n'.join(head[:1] + ([''] if True else []) + [head[2][:-1] + (f' (part {i + 1} of {n}).' if n > 1 else '.')] + p)
            for i, p in enumerate(parts)]


NUM = re.compile(r'(?<![A-Za-z])\d+(?:\.\d+)?')


def numbers(s):
    s = re.sub(r'\[note \d\]', ' ', s)
    return [n for n in NUM.findall(s.replace(',', ''))]


def check(t, text_all, pdf_text, old_text):
    text_all = '\n'.join(l for l in text_all.split('\n') if not l.startswith('### '))   # caption is ours
    new = numbers(text_all)
    res = {}
    if pdf_text is not None:
        pdf = set(re.findall(r'\d+(?:\.\d+)?', pdf_text.replace(',', '')))
        res['new_not_in_pdf_text'] = sorted(set(n for n in new if n not in pdf), key=float)
    old_body = '\n'.join(l for l in old_text.split('\n') if not re.match(r'^\s*(#|\*\*CHAPTER|\*\*HIV|\*\*Refer)', l))
    old = set(numbers(old_text))
    res['new_not_in_old_chunks'] = sorted(set(n for n in new if n not in old), key=float)
    res['old_not_in_new'] = sorted(set(n for n in numbers(old_body) if n not in set(new)), key=float)
    return res


def main(spec_path, pdf_dir, chunks_path, out_dir):
    spec = json.load(open(spec_path))
    chunks = {json.loads(l)['chunk_id']: json.loads(l) for l in open(chunks_path)}
    os.makedirs(out_dir, exist_ok=True)
    results = []
    for t in spec['tables']:
        if t.get('kind') == 'diagram':
            html_s = f'<pre class="diagram" data-table-id="{t["table_id"]}">{H.escape(t["content"])}</pre>'
            text_s = f'### {t["caption"]}\n\n{t["content"]}'
            embed_s = embed_parts([f'{spec["doc_title"]} | {t["heading_path"]} (page {t["page"]})', '', t['caption'] + '.']
                                  + [p for p in t['content'].split('\n\n')])
        elif t.get('kind') == 'box':
            html_s = (f'<div class="box" data-table-id="{t["table_id"]}"><b>{H.escape(t["caption"])}</b>'
                      + ''.join(f'<p>{H.escape(l)}</p>' for l in t['content'].split('\n')) + '</div>')
            text_s = f'> **{t["caption"]}**\n>\n' + '\n'.join('> ' + l for l in t['content'].split('\n'))
            embed_s = embed_parts([f'{spec["doc_title"]} | {t["heading_path"]} (page {t["page"]})', '', t['caption'] + '.']
                                  + [p for p in t['content'].split('\n\n')])
        elif t.get('kind') == 'section':   # running text rebuilt from the PDF text layer (headings + paragraphs/bullets)
            html_s = (f'<div class="section" data-table-id="{t["table_id"]}"><h4>{H.escape(t["caption"])}</h4>'
                      + ''.join(f'<p>{H.escape(l)}</p>' for l in t['content'].split('\n')) + '</div>')
            text_s = f'## {t["caption"]}\n\n{t["content"]}'
            embed_s = embed_parts([f'{spec["doc_title"]} | {t["heading_path"]} (page {t["page"]})', '', t['caption'] + '.']
                                  + [p for p in t['content'].split('\n')])
        else:
            n = ncols_of(t['header'])
            html_s, text_s = render_html(t, n), render_text(t, n)
            embed_s = embed_parts(render_embed(t, n, spec['doc_title']))
        pages = set(t.get('pages', [t['page']])) | {t.get('footnotes_page', t['page'])}
        pdf_text = None if t.get('image_only') else '\n'.join(
            open(os.path.join(pdf_dir, f'p{p}.txt')).read() for p in sorted(pages))
        if t.get('image_only') and t.get('footnotes_page'):
            pdf_text = None
        old_text = '\n'.join(chunks[c]['text'] for c in t['replaces_chunks'] if c in chunks)
        chk = check(t, text_s, pdf_text, old_text)
        results.append(dict(table_id=t['table_id'], page=t['page'], html=html_s, text=text_s, embed_text=embed_s,
                            checks=chk, source_flags=t.get('source_flags', []), replaces_chunks=t['replaces_chunks'],
                            old_text=old_text, caption=t['caption'], heading_path=t['heading_path'],
                            image_only=t.get('image_only', False), kind=t.get('kind', 'table'),
                            pages=sorted(set(t.get('pages', [t['page']])) | {t['page']})))
        print(t['table_id'], json.dumps(chk))
    json.dump(results, open(os.path.join(out_dir, 'tables_out.json'), 'w'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main(*sys.argv[1:5])
