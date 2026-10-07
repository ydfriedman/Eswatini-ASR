"""Real-sentence code-switch generation by dictionary + alignment-checked noun swaps (matrix-language-frame style).

Take a REAL siSwati sentence (SADiLaR bilingual corpus, CC BY 4.0). If it contains a siSwati noun that the Autshumato dictionary (CC BY 2.5 ZA)
translates to exactly one English word, AND that English word occurs in the aligned English sentence (so the dictionary sense is the one
used), replace the noun with the English word. Everything else in the sentence is untouched, so its concords stay as the original writer
made them; the English noun takes the prefix of the class it replaces: ema- (cl.6), bo- (cl.2), i- (cl.5/9).
Classes whose replacement prefix would be ambiguous (um-, si-, tin-, ...) are skipped, not guessed.

Usage: python realswitch.py --n 3000 --out ../data/synth_text
"""
import argparse, collections, glob, json, os, random, re

HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, "..", "data", "raw")
DICT = os.path.join(RAW, "dict", "Autshumato-Multilingual Word & Phrase Translations", "english_siswati.txt")
TOK = re.compile(r"[A-Za-z][A-Za-z'\-]*")

def load_dict():
    d = collections.defaultdict(set)                       # siSwati single-token translation -> {English words}
    for line in open(DICT, encoding="utf-8", errors="replace"):
        if "\t" not in line: continue
        e, t = line.rstrip("\n").split("\t", 1); e = e.strip()
        if not re.fullmatch(r"[a-z]{3,}", e): continue        # lowercase headwords only: skips proper nouns (Pretoria, Africa, ...)
        for x in t.split(";"):
            x = x.strip().lower()
            if re.fullmatch(r"[a-z]{4,}", x): d[x].add(e)
    return {t: next(iter(es)) for t, es in d.items() if len(es) == 1}      # keep only unambiguous siSwati -> English

def noun_class(token):
    """Replacement prefix for the loan, or None if the class is ambiguous. Tokens come from dictionary NOUN translations."""
    if token.startswith("ema") and len(token) > 6: return "ema"      # cl.6 plural
    if token.startswith("aba") and len(token) > 6: return "bo"       # cl.2 plural persons
    if re.match(r"i[bcdfghjklmnpqrstvwxyz]", token) and not token.startswith("imi") and len(token) > 5: return "i"   # cl.5 (cl.9 shares the loan prefix i-); imi- = cl.4, skipped
    return None

def surface(eng_sentence_tokens, e, plural, rel_pos, tol=0.35):
    """The English surface form to insert: the form actually used in the aligned English sentence (plural/singular must match) and located
    at a similar relative position (guards against a dictionary sense that merely co-occurs somewhere in the sentence)."""
    n = len(eng_sentence_tokens)
    for j, w in enumerate(eng_sentence_tokens):
        lw = w.lower()
        if abs(j / max(1, n - 1) - rel_pos) > tol: continue
        if plural and lw in (e + "s", e + "es"): return lw
        if not plural and lw == e: return lw
    return None

def hash_split(text):
    """Deterministic ~10% validation split by sentence (sentences are unique real sentences)."""
    import hashlib
    return int(hashlib.md5(text.encode()).hexdigest(), 16) % 10 == 0


def build(n_max=10**9, seed=0, max_words=18, min_words=5, cap_per_swap=25):
    d = load_dict(); rng = random.Random(seed); out = []; per_swap = collections.Counter()
    for en in sorted(glob.glob(os.path.join(RAW, "ssw_text", "bilingual*", "*.en.txt"))):
        E = open(en, encoding="utf-8", errors="replace").read().split("\n"); S = open(en[:-6] + "ss.txt", encoding="utf-8", errors="replace").read().split("\n")
        for e_line, s_line in zip(E, S):
            if re.search(r"[0-9]|[A-Z]{2,}", s_line): continue
            st = TOK.findall(s_line)
            if not (min_words <= len(st) <= max_words): continue
            et = TOK.findall(e_line); swaps = []
            for i, t in enumerate(st):
                e = d.get(t.lower()); pre = noun_class(t.lower()) if e else None
                if not pre: continue
                sf = surface(et, e, pre in ("ema", "bo"), i / max(1, len(st) - 1))
                if sf: swaps.append((i, pre, sf))
            if not swaps: continue
            i, pre, sf = rng.choice(swaps)                     # at most one swap per sentence keeps the sentence mostly real siSwati
            if per_swap[(pre, sf)] >= cap_per_swap: continue     # diversity: no single noun dominates
            per_swap[(pre, sf)] += 1
            words = [w.lower() for w in st]
            tagged = " ".join(words[:i] + [f"{pre}-[[{sf}]]"] + words[i + 1:])
            out.append({"tagged": tagged, "text": tagged.replace("[[", "").replace("]]", ""), "original": " ".join(words), "swapped": f"{words[i]} -> {pre}-{sf}",
                        "english": e_line.strip(), "switch_type": "real_swap"})
    rng.shuffle(out)
    return out[:n_max]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=3000); ap.add_argument("--out", default=os.path.join(HERE, "..", "data", "synth_text"))
    ap.add_argument("--seed", type=int, default=0); a = ap.parse_args()
    rows = build(a.n, a.seed)
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "real_swaps.jsonl"), "w") as f:
        for k, r in enumerate(rows):
            r["id"] = f"rsw{k:06d}"; r["split"] = "val" if hash_split(r["original"]) else "train"; r["synthetic"] = True
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    types = collections.Counter(r["swapped"].split(" -> ")[1] for r in rows)
    print(f"{len(rows)} sentences, {len(types)} distinct swapped nouns, prefixes {dict(collections.Counter(t.split('-')[0] for t in types.elements()))}")
    print("top:", types.most_common(12))
