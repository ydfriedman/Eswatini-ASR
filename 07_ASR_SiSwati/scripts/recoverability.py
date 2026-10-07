"""Code-switched set: can each English reference word be recovered from the hypothesis by fuzzy matching?
For each English ref word, find the best-matching character span in the (space-stripped) hypothesis and take
similarity = 1 - edit_distance / len(word). A word counts as recoverable if similarity >= 0.6.
Proxy for how well a clinical-vocabulary post-corrector could work; not a full correction experiment."""
import os, pandas as pd
from common import RESULTS, DATA

ENG = set(open(os.path.join(DATA, "codeswitch_english_words.txt")).read().split())
d = pd.read_csv(os.path.join(RESULTS, "per_utt.csv")); d = d[d.set == "cs_tts"]

def best_sim(word, hyp):
    """min edit distance of word against any substring of hyp (approximate substring match)"""
    h = hyp.replace(" ", ""); n, m = len(word), len(h)
    prev = [0] * (m + 1)                              # free start anywhere in hyp
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (word[i - 1] != h[j - 1]))
        prev = cur
    return 1 - min(prev) / n                          # free end anywhere

rows = []
for _, r in d.iterrows():
    hyp = str(r.hyp_n) if isinstance(r.hyp_n, str) else ""
    for w in r.ref_n.split():
        if w in ENG and len(w) >= 4: rows.append(dict(tag=r.tag, word=w, sim=best_sim(w, hyp)))
x = pd.DataFrame(rows)
out = x.groupby("tag").agg(n_words=("sim", "size"), mean_similarity=("sim", "mean"), recoverable=("sim", lambda s: (s >= 0.6).mean())).round(3)
out = out.sort_values("recoverable", ascending=False); out.to_csv(os.path.join(RESULTS, "cs_recoverability.csv")); print(out.to_string())

# Chance baseline: match each English word against the hypothesis of a different sentence (rotated by 7)
base = []
for t, g in d.groupby("tag"):
    g = g.sort_values("id").reset_index(drop=True); hyps = g.hyp_n.fillna("").tolist()
    for i, r in g.iterrows():
        other = hyps[(i + 7) % len(hyps)]
        for w in r.ref_n.split():
            if w in ENG and len(w) >= 4 and w not in other.split(): base.append(dict(tag=t, sim=best_sim(w, other)))
b = pd.DataFrame(base).groupby("tag").agg(chance_recoverable=("sim", lambda s: (s >= 0.6).mean())).round(3)
out = out.join(b); out["above_chance"] = (out.recoverable - out.chance_recoverable).round(3)
out.to_csv(os.path.join(RESULTS, "cs_recoverability.csv")); print(out.to_string())
