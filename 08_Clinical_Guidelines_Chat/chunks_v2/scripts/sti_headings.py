"""Heading paths for the STI/VH draft taken from the Word file's own heading styles.

The .docx carries real heading levels (Heading 1-4), which the PDF-style parser flattened. We convert the
docx to markdown with pandoc, track the heading stack line by line, then locate each chunk's text in the
document and use the stack at that position.
"""
import re
from fix_headings import clean_part, tidy_case


def _norm(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = re.sub(r'[#*_`|\\\[\]{}()>:;,.\-–•▪○"\'“”’]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip().lower()


def heading_index(md_text):
    """Return (normalised full text, list of (char_offset, stack))."""
    stack, marks, buf, pos = [], [], [], 0
    for line in md_text.split('\n'):
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            level = len(m.group(1))
            title = clean_part(m.group(2))
            if title:
                stack = [s for s in stack if s[0] < level] + [(level, title)]
                marks.append((pos, [t for _, t in stack]))
            continue
        n = _norm(line)
        if n:
            buf.append(n)
            pos += len(n) + 1
    return ' '.join(buf), marks


def body_start(marks):
    """Offset of the first numbered chapter heading: matches before it are front matter (lists of tables...)."""
    for off, st in marks:
        if st and re.match(r'^\d+(\.\d+)*\s', st[-1]):
            return off
    return 0


def path_for(chunk_text, full, marks, min_len=40, body_only=False):
    """body_only=True: search the main body only; False: search the front matter first, then the body."""
    body = '\n'.join(l for l in chunk_text.split('\n') if not re.match(r'^\s*#{1,6}\s', l))
    n = _norm(body)
    if len(n) < min_len:
        return None
    b = body_start(marks)
    for lo, hi in (((b, len(full)),) if body_only else ((0, b), (b, len(full)))):
      for start in (0, len(n) // 3, (2 * len(n)) // 3):
        snippet = n[start:start + 60]
        if len(snippet) < 30:
            continue
        i = full.find(snippet, lo, hi)
        while i >= 0:
            stack = None
            for off, st in marks:
                if off <= i:
                    stack = st
                else:
                    break
            if stack and not any(re.search(r'list of|contents|toc-heading', t, re.I) for t in stack):
                return [tidy_case(re.sub(r'\{[^}]*\}', '', t).strip()) for t in stack]
            i = full.find(snippet, i + 1, hi)
    return None


def sti_paths(chunks, md_text):
    """Docx-derived path per chunk; unmatched chunks inherit the previous matched path."""
    full, marks = heading_index(md_text)
    out, prev, in_body = [], None, False
    for c in chunks:
        if re.search(r'(?m)^#+\s*\**\s*1\.[01]\b', c['text']):
            in_body = True          # the chunk where chapter 1 starts: everything after is main body
        p = path_for(c['text'], full, marks, body_only=in_body)
        if p:
            prev = p
        out.append(p or prev)
    return out
