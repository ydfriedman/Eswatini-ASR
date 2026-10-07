"""Nguni noun-class morphotactics for English loan stems in siSwati code-switching.

Everything linguistic lives in plain tables so a native speaker can edit it without reading code. NONE of these tables
has been reviewed by a native speaker; every class assignment for a loan noun is a lexical choice, not a predictable one
(see NOUNS in lexicon.py, where each item carries a `conf` flag). Orthography: prefix is attached to the English stem with a
hyphen ("ema-pills"), which the repo's scorer already splits on. Use sep="" or sep=" " to get other conventions.
"""

# class -> (prefix_sg, prefix_pl, plural class); "1a" = personal nouns with a zero singular prefix
NOUN_CLASSES = {
    "5/6":   {"sg": "i",  "pl": "ema"},   # i-/ema-   (default for loans)
    "9/10":  {"sg": "i",  "pl": "ti"},    # i-/ti-    (siSwati plural of cl.9 is ti(n)-)
    "1a/2a": {"sg": "",   "pl": "bo"},    # zero / bo- (personal loans)
    "3/4":   {"sg": "um", "pl": "imi"},
}

# class actually governing agreement for (pair, number)
AGR_CLASS = {("5/6", "sg"): "5", ("5/6", "pl"): "6", ("9/10", "sg"): "9", ("9/10", "pl"): "10",
             ("1a/2a", "sg"): "1", ("1a/2a", "pl"): "2", ("3/4", "sg"): "3", ("3/4", "pl"): "4"}

# agreement morphemes per governing class. sc = subject concord; poss1/poss2 = 'my'/'your' (possessive concord + -mi/-kho);
# dem = 'this'; new = 'new' (relative-concord form of -sha)
AGR = {
    "1":  {"sc": "u",  "poss1": "wami", "poss2": "wakho", "dem": "lo",   "new": "lomusha"},
    "2":  {"sc": "ba", "poss1": "bami", "poss2": "bakho", "dem": "laba", "new": "labasha"},
    "3":  {"sc": "u",  "poss1": "wami", "poss2": "wakho", "dem": "lo",   "new": "lomusha"},
    "4":  {"sc": "i",  "poss1": "yami", "poss2": "yakho", "dem": "le",   "new": "lemisha"},
    "5":  {"sc": "li", "poss1": "lami", "poss2": "lakho", "dem": "leli", "new": "lelisha"},
    "6":  {"sc": "a",  "poss1": "ami",  "poss2": "akho",  "dem": "lawa", "new": "lamasha"},
    "9":  {"sc": "i",  "poss1": "yami", "poss2": "yakho", "dem": "le",   "new": "lensha"},
    "10": {"sc": "ti", "poss1": "tami", "poss2": "takho", "dem": "leti", "new": "letinsha"},
}

# verb loans: infinitive ku-V, subjunctive (2sg, after 'ngicela') u-V
VERB_PREFIX = {"inf": "ku", "subj": "u"}


def prefix(cls_pair, number):
    return NOUN_CLASSES[cls_pair][number]


def nominal(stem, cls_pair, number, sep="-"):
    """'pills' + '5/6' + 'pl' -> 'ema-[[pills]]' (English span marked with [[ ]])."""
    p = prefix(cls_pair, number)
    return f"{p}{sep}[[{stem}]]" if p else f"[[{stem}]]"


def agree(cls_pair, number, attr):
    return AGR[AGR_CLASS[(cls_pair, number)]][attr]


def verb(stem, form, sep="-"):
    return f"{VERB_PREFIX[form]}{sep}[[{stem}]]"
