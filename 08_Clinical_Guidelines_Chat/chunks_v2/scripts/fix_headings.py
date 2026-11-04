"""Rebuild heading_path breadcrumbs.

Problems fixed:
  * page numbers and markdown fragments used as headings ('11 > ...', '63 ## Treatment ...')
  * tables / figures / boxes acting as parents of later sections
  * front-matter headings ('ACRONYMS', 'PREFACE') swallowing the chapters that follow
  * chapters nested under the wrong chapter ('CHAPTER 5 > CHAPTER 6 > ...')
  * flat paths that only contain the document title
The hierarchy is rebuilt from printed section numbers (6.1.2 sits under 6.1 under Chapter 6) wherever
they exist; otherwise the cleaned original path is kept.
"""
import re

FRONT = re.compile(r'^(acronyms?|abbreviations?( and acronyms)?|acronyms and abbreviations|preface|foreword|'
                   r'acknowledge?ments?|table of contents?|contents|list of (tables|figures))$', re.I)
CAPTION = re.compile(r'^(table|figure|fig\.|box|chart|diagram|flowchart)\s*[\w.]*\d', re.I)
CHAPTER = re.compile(r'^chapter\s+(\d+)\s*[:.\-–]?\s*(.*)$', re.I)
SECTION = re.compile(r'^(\d{1,2}(?:\.\d{1,2}){1,4})\.?\s+(\S.*)$')
TOPSEC = re.compile(r'^([1-9]\d?)\.?\s+([A-Za-z][^.]{2,70})$')
KEEP_UPPER = {'HIV', 'TB', 'ART', 'ARV', 'PREP', 'PEP', 'STI', 'STIS', 'ANC', 'PNC', 'PMTCT', 'DSD', 'NCD', 'NCDS',
              'TPT', 'AHD', 'DR-TB', 'MDR-TB', 'HTS', 'HIVST', 'VL', 'LCM', 'SOP', 'CD4', 'CAB-LA', 'LEN', 'FP',
              'IUCD', 'MEC', 'ECP', 'ECPS', 'PID', 'HBV', 'HCV', 'VH', 'IPV', 'GBV', 'KP', 'KPS', 'PLHIV', 'CALHIV',
              'ALHIV', 'CLHIV', 'MOH', 'WHO', 'UNAIDS', 'CMIS', 'EID', 'PCR', 'TLD', 'DTG', 'AZT', 'ABC', 'NVP',
              'EFV', 'LPV/R', 'ATV/R', 'SUAC', 'LTBI', 'IRIS', 'COVID-19', 'MSM', 'FSW', 'AGYW', 'PBFW', 'DM',
              'HTN', 'CKD', 'COPD', 'PTSD', 'ADHD', 'MDD', 'GAD', 'BAD', 'MSE', 'OPD', 'ICU', 'AKI', 'DKA', 'HHS',
              'ECG', 'BP', 'BMI', 'RDT', 'RPR', 'VDRL', 'TPHA', 'LAM', 'LF-LAM', 'CRP', 'CXR', 'CAD', 'AI'}
SMALL = {'and', 'or', 'of', 'for', 'the', 'in', 'on', 'to', 'with', 'a', 'an', 'by', 'at', 'from', 'vs'}


def clean_part(p):
    p = re.sub(r'<[^>]+>', ' ', p)
    p = re.sub(r'^\s*\d{1,3}\s*#+\s*', '', p)          # '63 ## Treatment ...'
    p = re.sub(r'[#*_`]+', '', p)
    p = p.replace('\\', '')
    p = re.sub(r'\s+', ' ', p).strip(' :;-–')
    return p


def tidy_case(p):
    """ALL-CAPS heading -> Title Case, keeping acronyms ('PrEP DELIVERY' -> 'PrEP Delivery')."""
    def core(w):
        return re.sub(r'[^A-Za-z0-9/\-]', '', w).upper()
    letters = ''.join(re.sub(r'[^A-Za-z]', '', w) for w in p.split(' ') if core(w) not in KEEP_UPPER)
    if len(letters) < 6 or not letters.isupper():
        return p
    fixed = {'PREP': 'PrEP', 'STIS': 'STIs', 'NCDS': 'NCDs', 'ECPS': 'ECPs', 'KPS': 'KPs'}
    def word(w, i):
        if '-' in w and core(w) not in KEEP_UPPER:
            return '-'.join(word(x, 1 if j else i) for j, x in enumerate(w.split('-')))
        if core(w) in KEEP_UPPER or re.match(r'^[\d.]+$', w):
            return fixed.get(core(w), w)
        if i > 0 and w.lower() in SMALL:
            return w.lower()
        return w[:1].upper() + w[1:].lower()
    return ' '.join(word(w, i) for i, w in enumerate(p.split(' ')))


def classify(p):
    """Return (kind, number, title)."""
    m = CHAPTER.match(p)
    if m:
        return 'chapter', m.group(1), m.group(2).strip()
    m = SECTION.match(p)
    if m:
        return 'section', m.group(1), m.group(2).strip()
    m = TOPSEC.match(p)
    if m and int(m.group(1)) <= 40 and not re.match(r'^\d+\s+(mg|g|ml|kg|weeks?|days?|months?|years?|tabs?)\b', p, re.I):
        return 'section', m.group(1), m.group(2).strip()
    if CAPTION.match(p):
        return 'caption', None, p
    if FRONT.match(p):
        return 'front', None, p
    if re.fullmatch(r'[\d\s.]+', p) or len(p) < 2:
        return 'junk', None, p
    return 'plain', None, p


def first_heading(text):
    for line in text.split('\n'):
        s = line.strip()
        if re.match(r'^#{1,6}\s', s) or (s.startswith('**') and s.endswith('**') and 3 < len(s) < 140):
            h = clean_part(s)
            if h:
                return h
    return None


def build_index(chunks):
    """Per document: section number -> title, chapter number -> title."""
    secs, chaps = {}, {}
    pending_chapter = None
    for c in chunks:
        for raw in c['heading_path'].split(' > '):
            p = clean_part(raw)
            kind, num, title = classify(p)
            if kind == 'chapter':
                if title:
                    chaps.setdefault(num, title)
                else:
                    pending_chapter = num
                continue
            if pending_chapter and kind == 'plain' and p.isupper():
                chaps.setdefault(pending_chapter, p)
            pending_chapter = None
            if kind == 'section':
                secs.setdefault(num, title)
    return secs, chaps


def rebuild(chunks):
    """chunks: list of one document's chunks in document order. Returns list of new paths."""
    secs, chaps = build_index(chunks)
    firsts = {}
    for c in chunks:
        f = clean_part(c['heading_path'].split(' > ')[0])
        firsts[f] = firsts.get(f, 0) + 1
    allparts = {}
    for c in chunks:
        for x in c['heading_path'].split(' > '):
            f = clean_part(x)
            allparts[f] = allparts.get(f, 0) + 1
    title_like = {f for f, k in allparts.items() if k >= 5 and 'guideline' in f.lower() and not classify(f)[1]}
    anchored = sum(any(classify(clean_part(x))[0] in ('chapter', 'section') for x in c['heading_path'].split(' > '))
                   for c in chunks)
    numbered_doc = anchored / max(1, len(chunks)) >= 0.2
    out = []
    last_anchor = None
    current_top = None   # last chapter / top-level section seen, for unnumbered parts of the document

    prev_was_subpart = False

    def sentence_like(p):
        return p.endswith('.') or len(p) > 80

    for c in chunks:
        parts = [clean_part(x) for x in c['heading_path'].split(' > ')]
        parts = [x for x in parts if x]
        parts = [x for x in parts if x not in title_like and not x.lower().startswith(c['doc_title'][:25].lower())]
        typed = [(classify(p), p) for p in parts]
        # merge 'CHAPTER 9' + 'ONCOLOGY'
        merged = []
        for (kind, num, title), p in typed:
            if merged and merged[-1][0][0] == 'chapter' and not merged[-1][0][2] and kind == 'plain':
                merged[-1] = (('chapter', merged[-1][0][1], p), merged[-1][1])
                continue
            merged.append(((kind, num, title), p))
        typed = [t for t in merged if t[0][0] != 'junk']
        # front/back-matter headings ('References', 'Table of Contents') are never parents of real content
        typed = [t for i, t in enumerate(typed)
                 if i == len(typed) - 1 or not (t[0][0] == 'front' or re.match(r'^references?$', t[1], re.I))]

        anchor_idx = None
        for i, ((kind, num, title), p) in enumerate(typed):
            if kind in ('chapter', 'section'):
                anchor_idx = i
        if anchor_idx is not None:
            kind, num, title = typed[anchor_idx][0]
            if kind == 'chapter':
                prefix = [f'Chapter {num}: {tidy_case(title or chaps.get(num, ""))}'.rstrip(': ')]
                last_anchor = prefix
                current_top = prefix[0]
            else:
                pieces = num.split('.')
                prefix = []
                top = pieces[0]
                if top in chaps:
                    prefix.append(f'Chapter {top}: {tidy_case(chaps[top])}')
                elif len(pieces) > 1 and top in secs:
                    prefix.append(f'{top} {tidy_case(secs[top])}')
                for k in range(2, len(pieces)):
                    anc = '.'.join(pieces[:k])
                    if anc in secs:
                        prefix.append(f'{anc} {tidy_case(secs[anc])}')
                prefix.append(f'{num} {tidy_case(title)}')
                last_anchor = prefix
                current_top = prefix[0]
            tail = [p for (k, n, t), p in typed[anchor_idx + 1:] if k in ('plain', 'caption')]
        else:
            body = [(k, p) for (k, n, t), p in typed if k in ('plain', 'caption', 'front')]
            if not body and last_anchor:
                prefix, tail = list(last_anchor), []
            elif (numbered_doc and last_anchor and prev_was_subpart and len(body) == 1 and body[0][0] == 'plain'
                  and not re.match(r'^(annex|appendix|references?|bibliography|glossary)', body[0][1], re.I)):
                # a lone heading right after an unnumbered sub-part of the same section is its sibling
                # ('1.1 Products > Oral / Ring / CAB-LA', then 'Lenacapavir' promoted to H1 by the parser)
                prefix, tail = list(last_anchor), [body[0][1]]
            elif numbered_doc and last_anchor and not any(k == 'front' for k, p in body):
                # unnumbered sub-part: attach to the parent of the last numbered section (safer than the leaf)
                parent = last_anchor[:-1] if len(last_anchor) > 1 else last_anchor
                prefix, tail = list(parent), [p for k, p in body][-2:]
            else:
                plain = [p for k, p in body]
                # drop sentence-like parents (body text promoted to a heading); keep the leaf
                plain = [p for i, p in enumerate(plain) if i == len(plain) - 1 or not sentence_like(p)]
                prefix = []
                tail = plain
        # captions only as the final element
        tail = [p for i, p in enumerate(tail) if classify(p)[0] != 'caption' or i == len(tail) - 1]
        path = prefix + [tidy_case(p) for p in tail]
        # leaf: add the chunk's own heading / caption when the path does not already end with it
        h = first_heading(c['text'])
        if h and (h in title_like or h.lower().startswith(c['doc_title'][:25].lower())):
            h = None
        if h and len(h) < 140:
            hk = classify(h)[0]
            if hk not in ('junk', 'front') and (not path or h.lower()[:30] not in ' '.join(path).lower()):
                if hk in ('chapter', 'section') and path:
                    pass
                elif not path or hk == 'caption' or not tail:
                    path.append(tidy_case(h))
        dedup = []
        for p in path:
            if not dedup or dedup[-1].lower() != p.lower():
                dedup.append(p)
        prev_was_subpart = bool(last_anchor) and len(dedup) == len(last_anchor) + 1 and dedup[:-1] == last_anchor
        out.append(' > '.join(dedup) if dedup else c['doc_title'])
    return out
