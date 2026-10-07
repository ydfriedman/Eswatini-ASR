import re, unicodedata, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA = os.path.join(ROOT, "data"); RESULTS = os.path.join(ROOT, "results")
MANIFEST = os.path.join(DATA, "manifest.jsonl")

SPOKEN_PUNCT = {"comma", "coma", "fullstop", "period"}

def normalize_lenient(s):
    """Sensitivity variant: also drop spoken-punctuation words that readers voiced but references omit."""
    w = normalize(s).replace("full stop", "fullstop").split()
    return " ".join(x for x in w if x not in SPOKEN_PUNCT)

def normalize(s):
    """WER normalization: NFKC, lowercase, hyphens/slashes -> space, drop punctuation, collapse spaces."""
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"\[[a-z]+\]", " ", s)   # NCHLT noise tags, e.g. [s]
    s = re.sub(r"[-/_]", " ", s)
    s = re.sub(r"[^\w\s']", " ", s)
    s = s.replace("'", "")
    return re.sub(r"\s+", " ", s).strip()
