"""Candidate "clinician review" flags, computed from the question, the answer blocks and the retrieved sources.

No model call: every rule is a text check that can be explained to a clinician. Sources are dicts as in app.py
(text, heading_path, chunk_id); blocks are the answer blocks (text, citations). Returns {rule: reason}.
"""
import re

NUM = re.compile(r'(?<![\w.])\d+(?:[.,]\d+)*(?![\w])')
UNIT_VALUE = re.compile(
    r'\b\d+(?:\.\d+)?\s*(?:-?\s*(?:year|yr|month|week|day)s?[- ]old|kg|g/dl|mmol/l|mg/dl|copies|cells|%|'
    r'ml/min|mmhg|cm|weeks?|months?|years?|bpm|/min|u/l|iu/ml)\b'
    r'|\b(?:bmi|gcs|phq-?9|score|muac|cd4|hb|vl|viral load|crcl|egfr|bp)\s*(?:of|is|was|:)?\s*\d', re.I)
VERDICT = re.compile(r'^\s*(?:yes|no)\b', re.I)
YESNO_Q = re.compile(r'^\s*(?:can|could|should|shall|is|are|does|do|did|may|must|will|would|has|have)\b'
                     r'|\b(?:can|could|should|may) (?:i|we|she|he|they)\b|\beligible\b|\bdoes (?:she|he|this|the)\b', re.I)
NEGATIVE = re.compile(r"\b(?:not|never|no longer|cannot|can't|don't|do not|should not|must not|avoid|"
                      r"contraindicated|ineligible|exclude[ds]?|unless|only (?:for|if|when))\b", re.I)
GROUPS = {
    'pregnancy': (r'\bpregnan', r'\bpregnan|\bantenatal|\banc\b|\bgestation'),
    'breastfeeding': (r'\bbreast-?feed|\blactat', r'\bbreast-?feed|\blactat|\bbreast milk'),
    'child': (r'\b(?:child|children|infant|baby|newborn|neonat|toddler)\b|\b(?:[1-9]|1[0-4])[- ]?(?:year|yr)s?[- ]old',
              r'\bchild|\binfant|\bbaby|\bbabies|\bnewborn|\bneonat|\bpaediatric|\bpediatric|\bunder[- ](?:5|five|15)|\bkg\b'),
    'adolescent': (r'\badolescen|\b1[0-9][- ]?(?:year|yr)s?[- ]old|\bteen', r'\badolescen|\byouth|\byoung people|\b1[0-9] years'),
}
STOP = set('''the a an and or of to in on for with by at from as is are be was were this that these those it its
which who whom whose what when where why how if then than so such any all each every not no can may should must will
would could do does did have has had she he they them her his their you your we our i patient client woman man
also only more less other into after before over under per day days use used give given'''.split())


def _text(source):
    return ' '.join(filter(None, (source.get('heading_path'), source.get('caption'), source.get('text'))))


def _nums(text):
    out = set()
    for m in NUM.findall(text):
        m = m.replace(',', '')
        out.add(m.rstrip('0').rstrip('.') if '.' in m else m)
    return out


def _words(text):
    return {w for w in re.findall(r'[a-z][a-z0-9-]{2,}', text.lower()) if w not in STOP}


def review_flags(question, blocks, sources):
    flags = {}
    claim = [b for b in blocks if isinstance(b, dict) and b.get('type', 'guideline_claim') == 'guideline_claim']
    if not claim:
        return flags
    def cited(b):
        return [sources[i - 1] for i in b.get('citations', []) if isinstance(i, int) and 1 <= i <= len(sources)]
    answer = ' '.join(b['text'] for b in claim)
    cited_all = [s for b in claim for s in cited(b)]
    cited_text = ' '.join(_text(s) for s in cited_all)
    all_text = ' '.join(_text(s) for s in sources)

    # 1. Yes/no verdict: the commonest unsafe error is a verdict its own rule contradicts.
    first = claim[0]['text']
    if VERDICT.match(first) or (YESNO_Q.search(question) and re.search(r'\b(?:yes|no)\b', first[:40], re.I)):
        flags['verdict'] = 'Yes/no answer: check the verdict against the guideline rule it rests on.'
    # 2. The question gives a patient value that has to be compared with a threshold or band.
    if UNIT_VALUE.search(question):
        flags['patient_value'] = 'The answer depends on a patient value (age, weight, result): check which band or threshold applies.'
    # 3. A number in the answer that is neither in the cited passages nor in the question.
    qnums = _nums(question)
    missing = sorted(n for n in _nums(answer) - qnums - _nums(cited_text) if n not in {'1', '2', '3'})
    if missing:
        flags['number_not_in_source'] = 'Number(s) not found in the cited passages: ' + ', '.join(missing[:5]) + '.'
    # 4. The question names a patient group that none of the cited passages mention.
    for group, (q_pat, s_pat) in GROUPS.items():
        if re.search(q_pat, question, re.I) and not re.search(s_pat, cited_text, re.I):
            flags['group_not_in_source'] = f'The question is about {group}, but the cited passages do not mention it.'
            break
    # 5. HIV 2022 cited while a 2024 Amendment passage was retrieved but not cited.
    ids = [s.get('chunk_id') or '' for s in sources]
    cited_ids = {s.get('chunk_id') or '' for s in cited_all}
    if any(i.startswith('hiv-2022') for i in cited_ids) and any(
            i.startswith('hiv-amendment-2024') and i not in cited_ids for i in ids):
        flags['superseded'] = 'Cites the 2022 HIV guideline; check whether the 2024 Amendment changed this.'
    # 6. A claim block whose content words are mostly absent from the passages it cites.
    for b in claim:
        words = _words(b['text'])
        if len(words) >= 4:
            src = _words(' '.join(_text(s) for s in cited(b)))
            if len(words & src) / len(words) < 0.6:
                flags['weak_support'] = 'A statement is not clearly found in the passage it cites.'
                break
    # 7. Verdict whose polarity disagrees with the rule text in the same answer (heuristic).
    if VERDICT.match(first):
        rest = answer[len(re.match(r'^\s*(?:yes|no)\b[.,:;!]?', first, re.I).group(0)):]
        yes = first.strip().lower().startswith('yes')
        if yes and NEGATIVE.search(rest):
            flags['verdict_conflict'] = 'The answer says yes but then states a restriction.'
        elif not yes and rest.strip() and not NEGATIVE.search(rest):
            flags['verdict_conflict'] = 'The answer says no but states no restriction.'
    return flags
