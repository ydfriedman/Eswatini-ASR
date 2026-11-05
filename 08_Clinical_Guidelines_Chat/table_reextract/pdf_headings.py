"""Section labels for text chunks taken from the PDF's own headings (font style), for guidelines where the
markdown heading levels are unreliable.

pdftohtml -xml gives every text line with its font. Headings are bold lines in the heading colours; a heading
that names a topic (not 'Pharmacological Treatment', 'Monitoring' ...) starts a new topic, a generic heading or a
subheading-colour heading becomes the sub-level under it. Each chunk is located on its page by its first words,
and gets 'Chapter > topic > sub' at that position. Proposed labels are reviewed by hand; corrections go in the
spec's 'label_overrides' {chunk_id: label}.

Usage (as a module): stream = heading_stream(xml_path, first_page, chapters, colours); labels = label_chunks(...)
"""
import re
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'chunks_v2', 'scripts'))
from toc_headings import is_generic  # noqa: E402
from fix_headings import tidy_case  # noqa: E402


def _key(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def page_lines(xml_path):
    """{page: [(top, left, text, font)]} and {font_id: (size, family, colour)}."""
    x = open(xml_path, encoding='utf-8', errors='ignore').read()
    fonts = {m.group(1): (int(m.group(2)), m.group(3), m.group(4)) for m in
             re.finditer(r'<fontspec id="(\d+)" size="(-?\d+)" family="([^"]+)" color="([^"]+)"', x)}
    pages = {}
    for pg in re.finditer(r'<page number="(\d+)"(.*?)</page>', x, re.S):
        p = int(pg.group(1))
        rows = []
        for m in re.finditer(r'<text top="(\d+)" left="(\d+)"[^>]*font="(\d+)"[^>]*>(.*?)</text>', pg.group(2)):
            t = re.sub(r'<[^>]+>', '', m.group(4)).replace('&amp;', '&').strip()
            if t:
                rows.append((int(m.group(1)), int(m.group(2)), t, m.group(3)))
        rows.sort()
        pages[p] = rows
    return pages, fonts


def heading_stream(pages, fonts, page_offset, start_page, colours, chapter_of_page, junk=()):
    """Ordered list of (page, top, kind, text): kind 'T' topic or 'S' sub. page_offset maps part pages to
    document pages (document page = part page + page_offset)."""
    topic_col, sub_col = colours
    out = []
    for p, rows in sorted(pages.items()):
        dp = p + page_offset
        if dp < start_page:
            continue
        prev = None
        for top, left, t, f in rows:
            size, fam, col = fonts[f]
            if 'Bold' not in fam or col not in (topic_col, sub_col) or size < 14:
                prev = None
                continue
            if re.match(r'^-?\s*Ministry of Health$|^CHAPTER\s+\d+', t, re.I) or any(re.match(j, t, re.I) for j in junk):
                continue
            # continuation of a multi-line heading
            if prev and prev[2] == col and 0 < top - prev[0] < 22:
                kind = out[-1][2]
                out[-1] = (dp, out[-1][1], kind, out[-1][3] + ' ' + t)
                prev = (top, left, col)
                continue
            text = t
            sentence = (len(text) > 90 or text.endswith('.') or text[:1].islower() or text.endswith(':')
                        or re.match(r'^(n\.?b|note|important|refer|at least)\b', text, re.I))
            if sentence:
                prev = None
                continue
            if chapter_of_page(dp) and _key(text) == _key(chapter_of_page(dp).split(': ', 1)[-1]):
                continue
            kind = 'T' if col == topic_col and not is_generic(text) else 'S'
            out.append((dp, top, kind, text))
            prev = (top, left, col)
    return out


def page_text_positions(pages, page_offset):
    """{doc_page: [(top, normalised line)]}"""
    return {p + page_offset: [(top, _key(t)) for top, left, t, f in rows] for p, rows in pages.items()}


def locate(chunk_text, page, positions):
    """Top coordinate on `page` where the chunk's body starts (first matching body line), else None."""
    body = [l for l in chunk_text.split('\n') if l.strip() and not re.match(r'^\s*#', l)]
    lines = positions.get(page, [])
    for b in body[:4]:
        k = _key(re.sub(r'[*_\\>]|\|', ' ', b))[:40]
        if len(k) < 12:
            continue
        for top, lk in lines:
            if lk and (lk.startswith(k[:25]) or k.startswith(lk[:25]) and len(lk) >= 12):
                return top
    return None


def label_at(stream, page, top, chapter):
    topic = sub = None
    for p, t, kind, text in stream:
        if (p, t) > (page, top if top is not None else 10 ** 6):
            break
        if kind == 'T':
            topic, sub = text, None
        else:
            sub = text
    parts = [chapter] + [tidy_case(x) for x in (topic, sub) if x]
    return ' > '.join(dict.fromkeys(parts))
