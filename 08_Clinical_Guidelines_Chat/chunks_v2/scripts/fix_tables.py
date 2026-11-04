"""Expand merged (spanning) table cells that the PDF->markdown conversion left blank.

Three conservative rules, applied per markdown table:
  H  colspan  : a short row label + one value + all remaining value cells blank, in a table whose
                other rows normally fill those columns -> copy the value across the row.
  V  rowspan  : a row whose trailing value cells are all blank directly under a row whose same
                cells are filled -> copy the values down (e.g. 'Breastfeeding' under 'Pregnancy').
  L  label    : first-column cell blank under a short label, rest of row filled -> carry the label down
                (e.g. weight band '3-29.9 kg' spanning several regimen rows).
Only rule L is applied automatically (high precision on review). Rules H and V are applied only to
tables verified against the source PDF (VERIFIED_HV); elsewhere they are run in dry-run mode to produce a
review list, because a true merged cell and a genuinely blank cell look identical in the markdown.
Every change is logged so it can be reviewed.
"""
import re

LONG = 150
SEP = re.compile(r'^\|\s*:?-{2,}')


def _split(line):
    body = line.strip()
    if body.startswith('|'):
        body = body[1:]
    if body.endswith('|'):
        body = body[:-1]
    return [c.strip() for c in body.split('|')]


def _join(cells):
    return '| ' + ' | '.join(cells) + ' |'


SEPARATORS = {'or', 'and', 'plus', '+', '/', 'and/or'}


def _is_label(s, maxlen):
    core = s.strip('*_ ').lower()
    return (bool(s) and len(s) <= maxlen and core not in SEPARATORS
            and not s.lstrip('*_ ').startswith(('•', '-', '*  ', '○', '▪')))


def _is_group_header(s):
    core = s.strip()
    bold = core.startswith('**') and core.endswith('**')
    letters = re.sub(r'[^A-Za-z]', '', core)
    caps = len(letters) >= 6 and letters.isupper()
    return bold or caps


def _fix_table(lines, log, cid, allow_hv):
    hdr = _split(lines[0])
    rows = [_split(l) for l in lines[2:]]
    n = len(hdr)
    rows = [r + [''] * (n - len(r)) if len(r) < n else r[:n] for r in rows]
    named = [bool(h) for h in hdr]
    changed = 0
    h_rows = set()

    def rule_l():
        nonlocal changed
        if not (hdr[0] and _is_label(hdr[0], 60)):
            return
        last = None
        for i, r in enumerate(rows):
            if r[0]:
                last = r[0] if (_is_label(r[0], 40) and not _is_group_header(r[0])) else None
                continue
            if last and r[1] and r[1].strip('*_ ').lower() not in SEPARATORS and (any(r[2:]) or len(r[1]) <= 60):
                log.append((cid, 'L', last[:40], r[1][:40]))
                rows[i] = [last] + r[1:]
                changed += 1

    def rule_v():
        nonlocal changed
        for i in range(1, len(rows)):
            r, p = rows[i], rows[i - 1]
            filled = [j for j, x in enumerate(r) if x]
            if not filled or not _is_label(r[0], 40):
                continue
            k = max(filled)
            if filled != list(range(k + 1)) or k >= n - 1:
                continue
            if _is_group_header(r[0]):
                continue
            two_labels = k >= 1 and all(_is_label(x, 40) for x in r[:k + 1]) and all(_is_label(x, 40) for x in p[:k + 1])
            chained = (i - 1) in h_rows
            if not (two_labels or chained):
                continue
            if all(p[k + 1:]) and any(p[1:]):
                log.append((cid, 'V', r[0][:40], ' / '.join(x[:25] for x in p[k + 1:])))
                rows[i] = r[:k + 1] + [x if len(x) <= LONG else '(same as above)' for x in p[k + 1:]]
                changed += 1

    def rule_h():
        nonlocal changed
        if not (n >= 4 and all(named[2:])):
            return
        for i, r in enumerate(rows):
            if _is_label(r[0], 60) and not _is_group_header(r[0]) and r[1] and len(r[1]) <= 100 and not any(r[2:]):
                others = [o for j, o in enumerate(rows) if j != i and sum(bool(x) for x in o[2:]) >= 2]
                if others:
                    log.append((cid, 'H', r[0][:40], r[1][:60]))
                    rows[i] = r[:2] + [r[1] if len(r[1]) <= LONG else '(same as left)'] * (n - 2)
                    h_rows.add(i)
                    changed += 1

    rule_l()
    if allow_hv:
        rule_v(); rule_h(); rule_v()
    if not changed:
        return lines, 0
    return [lines[0], lines[1]] + [_join(r) for r in rows], changed


def fix_text(text, cid, log, allow_hv=False):
    out, block, total = [], [], 0
    lines = text.split('\n')

    def flush():
        nonlocal block, total
        if len(block) >= 3 and SEP.match(block[1].strip()):
            fixed, c = _fix_table(block, log, cid, allow_hv)
            total += c
            out.extend(fixed)
        else:
            out.extend(block)
        block = []

    for line in lines:
        if line.strip().startswith('|'):
            block.append(line)
        else:
            if block:
                flush()
            out.append(line)
    if block:
        flush()
    return '\n'.join(out), total


# Tables whose spanning cells were checked against the source PDF.
VERIFIED_HV = {
    'prep-2025-0093',   # PrEP Table 10: age, pregnancy/breastfeeding, attendance span all products
    'hiv-2022-0083',    # Table 2.5: 'Yes / any age' and 'No / 50+' share baseline and follow-up cells
}
