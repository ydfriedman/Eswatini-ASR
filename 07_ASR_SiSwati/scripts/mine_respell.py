"""Mine nativised spellings of English loans (e.g. account -> akhawunti, agency -> ejensi, internet -> inthanethi) from the SADiLaR
sentence-aligned English-siSwati corpora (CC BY 4.0). A pair (English word w, siSwati token t) is kept when
  (1) their consonant skeletons are similar (siSwati orthography adds aspiration 'h', maps c/q/x->k, g/j, adds vowels), and
  (2) t reliably occurs in the siSwati side of exactly the sentence pairs whose English side contains w (alignment evidence).
Outputs data/synth_text/respell_pairs.tsv (aggregates + pairs of single words; CC BY 4.0 derived). Review before use: this is a heuristic.
Usage: python mine_respell.py
"""
import collections, glob, os, re, sys
from difflib import SequenceMatcher
HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, "..", "data", "raw", "ssw_text"); OUT = os.path.join(HERE, "..", "data", "synth_text")

def load():
    pairs = []
    for en in glob.glob(f"{RAW}/bilingual*/*.en.txt"):
        ss = en[:-6] + "ss.txt"
        E = open(en, encoding="utf-8", errors="replace").read().split("\n"); S = open(ss, encoding="utf-8", errors="replace").read().split("\n")
        pairs += [(e, s) for e, s in zip(E, S) if e.strip() and s.strip()]
    return pairs

CLS = {**{c: "k" for c in "cqxgjk"}, **{c: "t" for c in "dt"}, **{c: "p" for c in "bp"}, **{c: "f" for c in "vfw"}, **{c: "s" for c in "zs"},
       **{c: "n" for c in "mn"}, **{c: "l" for c in "rl"}}
def skel(w):
    w = re.sub(r"(?<=[bcdfgjklmnpqrstvwxz])h", "", w.lower())          # drop aspiration h after a consonant (th->t, kh->k, ph->p)
    w = re.sub(r"^(?:i|ema|em|im|in|ti|tin|e|a|u|um|aba|ku|ne|nge|se|we|ye|le)-", "", w)   # explicit hyphenated prefix
    s = "".join(CLS.get(c, "") for c in w)                              # vowels, y, h dropped
    return re.sub(r"(.)\1+", r"\1", s)

TOK = re.compile(r"[A-Za-z][A-Za-z'\-]+")
pairs = load(); print(len(pairs), "aligned sentence pairs")
en_tok = [set(t.lower() for t in TOK.findall(e)) for e, _ in pairs]
ss_tok = [set(t.lower().strip("-'") for t in TOK.findall(s)) for _, s in pairs]
c_en = collections.Counter(w for s in en_tok for w in s); c_ss = collections.Counter(t for s in ss_tok for t in s)
E = {w for w, c in c_en.items() if 3 <= c <= 3000 and len(w) >= 4 and len(skel(w)) >= 3 and w.isalpha()}
Sx = {t for t, c in c_ss.items() if c >= 3 and len(t) >= 4 and len(skel(t)) >= 3}
sk_e = {w: skel(w) for w in E}; sk_s = {t: skel(t) for t in Sx}
ok = {}                                                                  # (w,t) -> skeleton ratio, cached
def similar(w, t):
    k = (w, t)
    if k not in ok:
        a, b = sk_e[w], sk_s[t]
        ok[k] = SequenceMatcher(None, a, b).ratio() if a[:1] == b[:1] and abs(len(a) - len(b)) <= 2 else 0.0
    return ok[k]

co = collections.Counter()
for es, ts in zip(en_tok, ss_tok):
    ew = [w for w in es if w in E]; tw = [t for t in ts if t in Sx]
    for w in ew:
        for t in tw:
            if similar(w, t) >= 0.75: co[(w, t)] += 1
rows = []
for (w, t), n in co.items():
    if n < 3: continue
    p_t_given_w = n / c_en[w]; p_w_given_t = n / c_ss[t]
    if p_t_given_w >= 0.4 and p_w_given_t >= 0.4 and w != t:
        rows.append((w, t, n, round(p_t_given_w, 2), round(p_w_given_t, 2), round(ok[(w, t)], 2)))
best = {}
for r in sorted(rows, key=lambda r: -r[2]):            # keep the best siSwati form per English word
    best.setdefault(r[0], []).append(r)
os.makedirs(OUT, exist_ok=True)
with open(f"{OUT}/respell_pairs.tsv", "w") as f:
    f.write("english\tsiswati_form\tn_sentences\tp_ss_given_en\tp_en_given_ss\tskeleton_ratio\treview_ok\n")
    for w in sorted(best):
        for r in best[w][:2]: f.write("\t".join(map(str, r)) + "\t\n")
print(len(best), "English words with an aligned nativised form")
for w in sorted(best, key=lambda w: -best[w][0][2])[:60]: print(" ", w, "->", ", ".join(f"{r[1]}({r[2]})" for r in best[w][:2]))
