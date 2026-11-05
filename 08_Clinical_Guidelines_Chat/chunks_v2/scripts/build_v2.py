"""Build chunks_v2 from the original chunks.jsonl.

usage: python3 build_v2.py <chunks.jsonl> <sti_docx_as_markdown.md> <out_dir>

Steps (each change is logged in <out_dir>/logs):
  1. heading_path rebuilt (fix_headings.py; STI/VH from the Word file's heading styles, sti_headings.py)
  2. merged table cells expanded (fix_tables.py): rule L everywhere, rules H/V only on verified tables;
     H/V candidates elsewhere written to logs/table_span_candidates.csv for review
  3. front/back matter, contents pages, page footers, near-empty and duplicate chunks removed
     (kept in dropped_chunks.jsonl); acronym lists kept separately in glossary.jsonl
  4. caption-only chunks merged into the chunk that follows them
  5. footnote digits glued to drug names separated ('DTG2' -> 'DTG [note 2]')
  6. section_id / parent_section_id / prev_chunk_id / next_chunk_id added for retrieval-time expansion
  7. embed_text rebuilt from the new breadcrumb and text
"""
import collections
import csv
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fix_headings import rebuild, FRONT, clean_part, tidy_case  # noqa: E402
from fix_tables import fix_text, VERIFIED_HV  # noqa: E402
from sti_headings import sti_paths  # noqa: E402
from toc_headings import toc_paths  # noqa: E402

STI = 'sti-vh-draft-2026'
BACK = re.compile(r'^(references?|bibliography|document change history)$', re.I)
TEAM = re.compile(r'(writing|editorial|validation|core|technical working)\s+team|contributors|signature', re.I)
FOOTER = re.compile(r'^[A-Z][A-Z &]{6,}\s+\d{1,3}$|^\d{1,3}\s+[A-Z][A-Z &]{6,}$')
GLUED = re.compile(r'\b(DTG|TDF|3TC|ABC|AZT|NVP|EFV|LPV/r|ATV/r|DRV/r)([1-9])\b')  # not TLD: "TLD1/TLD2" is source text
GLOSSARY_LEAF = re.compile(r'^(acronyms?|abbreviations?|acronyms and abbreviations|abbreviations and acronyms)$', re.I)


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def plain(text):
    return re.sub(r'<[^>]+>', '', re.sub(r'<br\s*/?>', ' ', text))


def page_label(c):
    a, b = c['page_start'], c['page_end']
    return f'(page {a})' if a == b else f'(pages {a}-{b})'


def toc_table(text):
    """Contents-style table: >=4 rows whose last cell is a page number and whose other cells hold no digits
    except a leading section number (e.g. '4.1 Infection control | 24')."""
    hits, pages = 0, []
    for line in text.split('\n'):
        if not line.strip().startswith('|') or re.match(r'^\|\s*-', line.strip()):
            continue
        cells = [x.strip() for x in line.strip().strip('|').split('|')]
        cells = [x for x in cells if x]
        if 2 <= len(cells) <= 3 and re.fullmatch(r'\*?[ivxlc]*\d{0,3}\*?|\.?[ivxlc]+', cells[-1] or 'x', re.I):
            others = ' '.join(cells[:-1])
            others = re.sub(r'^\d+(\.\d+)*\s*', '', others)
            if not re.search(r'\d', others):
                hits += 1
                num = re.sub(r'\D', '', cells[-1])
                if num:
                    pages.append(int(num))
    ascending = len(pages) >= 4 and max(pages) >= 5 and sum(b >= a for a, b in zip(pages, pages[1:])) >= 0.8 * (len(pages) - 1)
    return hits >= 4 and ascending


TRAILER = re.compile(r'^\W*(source|adapted from|note|notes|nb|key|\*)\b', re.I)
RUNNING = set()   # whole-chunk texts that repeat >=3 times in a document (running headers/footers)


def heading_only(c):
    lines = [l.strip() for l in c['text'].split('\n') if l.strip()]
    if c['type'] not in ('text', 'table') or len(lines) != 1:
        return False
    core = norm(re.sub(r'[#*_]', ' ', lines[0]))
    return (len(core) <= 70 and not core.endswith('.') and not TRAILER.match(core)
            and re.match(r'^(#{1,6}\s|\*\*)', lines[0]) is not None and core.lower() not in RUNNING)


def classify_drop(c, path):
    parts = [p.strip() for p in path.split(' > ')]
    leaf, root = parts[-1], parts[0]
    body = norm(re.sub(r'[#*_|\-]', ' ', plain(c['text'])))
    orig_leaf = c.get('heading_path_original', '').split(' > ')[-1]
    if c['type'] == 'diagram':
        return None
    if GLOSSARY_LEAF.match(leaf) or (GLOSSARY_LEAF.match(root) and len(parts) == 1):
        return 'glossary'
    if FRONT.match(leaf) or BACK.match(leaf) or ((FRONT.match(root) or BACK.match(root)) and len(parts) == 1):
        return 'front/back matter'
    toc = re.compile(r'^\W*(table of contents|contents|list of (tables|figures))\W*$', re.I)
    if toc.match(leaf) or toc.match(clean_part(orig_leaf)) or (toc.match(root) and len(parts) == 1):
        return 'contents page'
    if toc_table(c['text']):
        return 'contents page'
    lines = [l for l in c['text'].split('\n') if l.strip()]
    paged = [l for l in lines if re.search(r'[A-Za-z]{3}.*\s\d{1,3}\s*$', l) and '|' not in l]
    if c['page_start'] <= 15 and len(paged) >= 5 and len(paged) >= 0.6 * len(lines):
        return 'contents page'           # plain-text contents page: 'Diagnosis of Hypertension 82'
    if len(re.findall(r'(?m)^\s*\W*(figure|table)\s*\d+.*\s\d{1,3}\s*$', c['text'], re.I)) >= 3:
        return 'contents page'
    if c['chunk_id'].endswith('-0001') and re.search(r'ministry of health', c['text'], re.I) and len(c['text']) < 500:
        return 'cover'
    if re.fullmatch(r'(webster print.*|[A-Z][A-Z ]{6,})', body.strip()) and len(body) < 40:
        return 'near-empty'
    if leaf.lower().strip(': ') == 'notes' and len(re.sub(r'[^A-Za-z]', '', body)) < 300 and 'national' in body.lower():
        return 'front/back matter'
    if TEAM.search(c['text'][:200]) and not re.search(r'\d+\.\d', path):
        return 'front/back matter'
    if body.lower() in RUNNING or re.search(r'webster print', body, re.I):
        return 'near-empty'
    if heading_only(c) and len(re.sub(r'\W', '', body)) >= 3:
        return None
    if len(body) < 40:
        if FOOTER.match(body) or body.lower() in {'x', 'flow chart', 'flow_chart', 'or', 'and'} or len(body) < 12:
            return 'near-empty'
        if re.search(r'ministry of health|kingdom of eswatini|volume \d|^(january|february|march|april|may|june|july|'
                     r'august|september|october|november|december) \d{4}|^chapter \d+$', body, re.I):
            return 'cover'
    return None


def is_caption_only(c):
    """Caption, bare heading or lead-in line ('Failure to respond give:') that belongs to the next chunk."""
    lines = [l.strip() for l in c['text'].split('\n') if l.strip()]
    if c['type'] != 'text' or len(lines) != 1 or len(lines[0]) >= 160:
        return False
    return (re.match(r'^[#*_ ]*(table|figure|box|flowchart|diagram)\b', lines[0], re.I) is not None
            or heading_only(c) or lines[0].rstrip('*_ ').endswith(':'))


def sid(doc, path):
    return doc + ':' + hashlib.sha1(path.encode()).hexdigest()[:10]


def first_caption(text):
    """'Table 7: ...' / 'Figure 2 ...' heading of a chunk, used as the label leaf."""
    for line in text.split('\n')[:4]:
        h = clean_part(line)
        if re.match(r'^(table|figure|fig\.|box|algorithm)\s*\d', h, re.I) and len(h) < 140:
            return tidy_case(h)
    return None


def main(src, sti_md, out, toc_md=None):
    toc_md = toc_md or {}
    os.makedirs(os.path.join(out, 'logs'), exist_ok=True)
    chunks = [json.loads(l) for l in open(src)]
    counts = collections.Counter((c['doc_id'], norm(re.sub(r'[#*_|\-]', ' ', plain(c['text']))).lower()) for c in chunks)
    RUNNING.update(t for (d, t), k in counts.items() if k >= 3 and 0 < len(t) < 60)
    by_doc = collections.OrderedDict()
    for c in chunks:
        by_doc.setdefault(c['doc_id'], []).append(c)

    # 1. headings
    heading_log, new_path = [], {}
    sti_md_text = open(sti_md).read()
    for doc, cs in by_doc.items():
        paths = rebuild(cs)
        if doc == STI:
            docx = sti_paths(cs, sti_md_text)
            paths = [' > '.join(d) if d else p for d, p in zip(docx, paths)]
        if doc in toc_md:                  # unnumbered documents: labels anchored on the printed TOC
            with open(toc_md[doc]) as fh:
                tp = toc_paths(cs, fh.read())
            leaf = [tidy_case(clean_part(c['caption'])) if c['type'] == 'diagram' and c.get('caption')
                    else first_caption(c['text']) for c in cs]
            paths = [' > '.join(d + ([l] if l and l.lower() not in ' '.join(d).lower() else [])) if d else p
                     for d, l, p in zip(tp, leaf, paths)]
        for c, p in zip(cs, paths):
            new_path[c['chunk_id']] = p
            if p != c['heading_path']:
                heading_log.append((c['chunk_id'], c['heading_path'], p))

    # 2. tables
    table_log, candidates, new_text = [], [], {}
    for c in chunks:
        t, n = fix_text(c['text'], c['chunk_id'], table_log, allow_hv=c['chunk_id'] in VERIFIED_HV)
        if n:
            new_text[c['chunk_id']] = t
        if c['chunk_id'] not in VERIFIED_HV:
            dry = []
            fix_text(new_text.get(c['chunk_id'], c['text']), c['chunk_id'], dry, allow_hv=True)
            candidates += [d + (c['page_start'],) for d in dry if d[1] in 'HV']

    # 3. drops (duplicates by normalised text, first occurrence kept)
    kept, dropped, glossary, seen = [], [], [], {}
    for c in chunks:
        c = dict(c)
        c['heading_path_original'] = c['heading_path']
        c['heading_path'] = new_path[c['chunk_id']]
        if c['chunk_id'] in new_text:
            c['text'] = new_text[c['chunk_id']]
            c['merged_cells_expanded'] = True
        reason = classify_drop(c, c['heading_path'])
        key = norm(plain(c['text'])) + ' || ' + c['heading_path'].split(' > ')[-1].lower()
        if not reason and len(key) > 60 and key in seen:
            reason = 'duplicate of ' + seen[key]
        if reason == 'glossary':
            glossary.append(c)
            reason = 'acronym list (moved to glossary.jsonl)'
        if reason:
            c['drop_reason'] = reason
            dropped.append(c)
            continue
        seen.setdefault(key, c['chunk_id'])
        kept.append(c)

    # 4. caption-only chunks -> prepend to the next chunk of the same document
    merged = []
    i = 0
    while i < len(kept):
        c = kept[i]
        if is_caption_only(c) and i + 1 < len(kept) and kept[i + 1]['doc_id'] == c['doc_id']:
            nxt = dict(kept[i + 1])
            nxt['text'] = c['text'].strip() + '\n\n' + nxt['text']
            nxt['page_start'] = min(nxt['page_start'], c['page_start'])
            nxt['absorbed_chunk_ids'] = nxt.get('absorbed_chunk_ids', []) + [c['chunk_id']]
            nxt['absorbed_caption'] = norm(plain(c['text']).replace('#', ' ').replace('*', ' '))
            c2 = dict(c)
            c2['drop_reason'] = 'caption merged into ' + nxt['chunk_id']
            dropped.append(c2)
            kept[i + 1] = nxt
            i += 1
            continue
        merged.append(c)
        i += 1
    kept = merged

    # 4b. heading-less fragments (< 30 letters/digits): append to the previous chunk of the same document
    merged = []
    for c in kept:
        one_line = len([l for l in c['text'].split('\n') if l.strip()]) == 1
        trailer = one_line and TRAILER.match(norm(re.sub(r'[#*_]', ' ', c['text']))) is not None
        frag = c['type'] != 'diagram' and (trailer or (len(re.sub(r'\W', '', c['text'])) < 30
                                                       and not re.match(r'^\s*#', c['text'])))
        if frag and merged and merged[-1]['doc_id'] == c['doc_id']:
            prev = dict(merged[-1])
            prev['text'] = prev['text'].rstrip() + '\n\n' + c['text'].strip()
            prev['page_end'] = max(prev['page_end'], c['page_end'])
            prev['absorbed_chunk_ids'] = prev.get('absorbed_chunk_ids', []) + [c['chunk_id']]
            merged[-1] = prev
            c2 = dict(c)
            c2['drop_reason'] = 'fragment merged into ' + prev['chunk_id']
            dropped.append(c2)
            continue
        merged.append(c)
    kept = merged

    # 5-7. footnotes, ids, embed_text
    for j, c in enumerate(kept):
        glued = bool(GLUED.search(c['text']))
        c['text'] = GLUED.sub(lambda m: f'{m.group(1)} [note {m.group(2)}]', c['text'])
        parts = c['heading_path'].split(' > ')
        c['section_id'] = sid(c['doc_id'], c['heading_path'])
        c['parent_section_id'] = sid(c['doc_id'], ' > '.join(parts[:-1])) if len(parts) > 1 else c['section_id']
        c['prev_chunk_id'] = kept[j - 1]['chunk_id'] if j and kept[j - 1]['doc_id'] == c['doc_id'] else None
        c['next_chunk_id'] = (kept[j + 1]['chunk_id'] if j + 1 < len(kept) and kept[j + 1]['doc_id'] == c['doc_id']
                              else None)
        header = f"{c['doc_title']} | {c['heading_path']} {page_label(c)}"
        old_body = c['embed_text'].partition('\n\n')[2]
        changed_text = c['chunk_id'] in new_text or c.get('absorbed_chunk_ids') or glued
        body = plain(c['text']) if (c['type'] != 'diagram' and changed_text) else old_body
        if c['type'] == 'diagram' and c.get('absorbed_caption'):
            body = c['absorbed_caption'] + '\n\n' + old_body
        c['embed_text'] = header + '\n\n' + body
        if c.get('narrative_embed_text'):
            c['narrative_embed_text'] = header + '\n\n' + c['narrative_embed_text'].partition('\n\n')[2]
        c.pop('absorbed_caption', None)
        c['n_chars'] = len(c['text'])
        c['approx_tokens'] = len(c['text']) // 4

    # write
    with open(os.path.join(out, 'chunks.jsonl'), 'w') as fh:
        for c in kept:
            fh.write(json.dumps(c, ensure_ascii=False) + '\n')
    with open(os.path.join(out, 'dropped_chunks.jsonl'), 'w') as fh:
        for c in dropped:
            fh.write(json.dumps(c, ensure_ascii=False) + '\n')
    with open(os.path.join(out, 'glossary.jsonl'), 'w') as fh:
        for c in glossary:
            fh.write(json.dumps({k: c[k] for k in ('chunk_id', 'doc_id', 'doc_title', 'page_start', 'text')},
                                ensure_ascii=False) + '\n')
    cols = ['chunk_id', 'doc_id', 'doc_title', 'heading_path', 'heading_path_original', 'type', 'page_start',
            'page_end', 'section_id', 'parent_section_id', 'prev_chunk_id', 'next_chunk_id', 'text', 'embed_text',
            'n_chars', 'approx_tokens']
    with open(os.path.join(out, 'chunks.csv'), 'w', newline='') as fh:
        w = csv.DictWriter(fh, cols, extrasaction='ignore')
        w.writeheader()
        for c in kept:
            w.writerow(c)
    with open(os.path.join(out, 'logs', 'heading_changes.csv'), 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['chunk_id', 'old_heading_path', 'new_heading_path'])
        w.writerows(heading_log)
    with open(os.path.join(out, 'logs', 'table_fixes_applied.csv'), 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['chunk_id', 'rule', 'row_label', 'filled_with'])
        w.writerows(table_log)
    with open(os.path.join(out, 'logs', 'table_span_candidates.csv'), 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['chunk_id', 'rule', 'row_label', 'would_fill_with', 'pdf_page', 'verdict (merged / genuinely blank)'])
        w.writerows(candidates)
    with open(os.path.join(out, 'logs', 'dropped_summary.csv'), 'w', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['chunk_id', 'doc_id', 'reason', 'heading_path', 'text_start'])
        for c in dropped:
            w.writerow([c['chunk_id'], c['doc_id'], c['drop_reason'], c['heading_path'], norm(c['text'])[:120]])

    print('kept', len(kept), 'dropped', len(dropped), 'glossary', len(glossary))
    print('heading paths changed', len(heading_log), '| table fixes applied', len(table_log),
          '| span candidates for review', len(candidates))
    print(collections.Counter(c['drop_reason'].split(' of ')[0].split(' into ')[0] for c in dropped))


if __name__ == '__main__':
    # optional: --toc doc_id=path/to/markdown (repeatable)
    args, toc = sys.argv[1:], {}
    while '--toc' in args:
        i = args.index('--toc')
        k, v = args[i + 1].split('=', 1)
        toc[k] = v
        del args[i:i + 2]
    main(*args[:3], toc_md=toc)
