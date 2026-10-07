"""Score hypotheses against the soap-opera manifest: overall WER/CER, WER by utterance type (mixed / mono), error rate on English vs
isiZulu REFERENCE words (alignment-based), with 95% bootstrap CIs resampling SPEAKERS (the test set has only 17).
usage: python score_cs.py --manifest ../data/manifest_soapies_engzul.jsonl --hyp ../results/ft_hyp_base.jsonl [--hyp ...] --out ../results/ft_scores.csv
Hypothesis files: one json per line with {id, hyp}; the file name stem becomes the condition name unless the row has `tag`."""
import argparse, glob, json, os, sys
import numpy as np, pandas as pd, jiwer
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from common import normalize

ap = argparse.ArgumentParser(); ap.add_argument("--manifest", required=True); ap.add_argument("--hyp", action="append", required=True)
ap.add_argument("--split", default="test"); ap.add_argument("--split_key", default="split_v2"); ap.add_argument("--out", default=None)
ap.add_argument("--boot", type=int, default=2000); a = ap.parse_args()
man = {r["id"]: r for r in map(json.loads, open(a.manifest))}
rng = np.random.default_rng(0)

def ref_words_with_lang(r):
    ws, ls = [], []
    for s in r["segments"]:
        for w in normalize(s["text"]).split(): ws.append(w); ls.append(s["lang"])
    return ws, ls

rows = []
for path in a.hyp:
    tag = os.path.splitext(os.path.basename(path))[0].replace("ft_hyp_", "")
    for line in open(path):
        h = json.loads(line); r = man.get(h["id"])
        if r is None or r[a.split_key] != a.split: continue
        rw, rl = ref_words_with_lang(r); hw = normalize(h["hyp"]).split()
        o = jiwer.process_words(" ".join(rw), " ".join(hw) if hw else "<empty>")
        ok = [False] * len(rw)
        for ch in o.alignments[0]:
            if ch.type == "equal":
                for i in range(ch.ref_start_idx, ch.ref_end_idx): ok[i] = True
        c = jiwer.process_characters(" ".join(rw), " ".join(hw) if hw else " ")
        rows.append(dict(cond=h.get("tag", tag), id=h["id"], speaker=r["speaker"], cs_type=r["cs_type"],
                         w_err=o.substitutions + o.deletions + o.insertions, w_n=len(rw),
                         c_err=c.substitutions + c.deletions + c.insertions, c_n=len(" ".join(rw)),
                         eng_n=sum(l == "eng" for l in rl), eng_wrong=sum((not k) and l == "eng" for k, l in zip(ok, rl)),
                         zul_n=sum(l == "zul" for l in rl), zul_wrong=sum((not k) and l == "zul" for k, l in zip(ok, rl)),
                         is_empty=not hw))
df = pd.DataFrame(rows)
def agg(g, num, den): return g[num].sum() / max(1, g[den].sum())
def ci(g, num, den):
    spk = g.groupby("speaker")[[num, den]].sum().to_numpy()
    if len(spk) < 2 or spk[:, 1].sum() == 0: return (np.nan, np.nan)
    idx = rng.integers(0, len(spk), (a.boot, len(spk))); d = spk[idx, 1].sum(1)
    v = np.where(d > 0, spk[idx, 0].sum(1) / np.maximum(d, 1), np.nan); return tuple(np.nanpercentile(v, [2.5, 97.5]))
out = []
for cond, g in df.groupby("cond"):
    row = dict(cond=cond, n=len(g), speakers=g.speaker.nunique(), WER=agg(g, "w_err", "w_n"), WER_ci=ci(g, "w_err", "w_n"), CER=agg(g, "c_err", "c_n"),
               eng_word_err=agg(g, "eng_wrong", "eng_n"), zul_word_err=agg(g, "zul_wrong", "zul_n"), empty=g.is_empty.mean())
    for t, gt in g.groupby("cs_type"): row[f"WER_{t}"] = agg(gt, "w_err", "w_n"); row[f"n_{t}"] = len(gt)
    out.append(row)
res = pd.DataFrame(out).round(4)
print(res.to_string(index=False))
if a.out: res.to_csv(a.out, index=False); df.to_csv(a.out.replace(".csv", "_per_utt.csv"), index=False)
if len(res) > 1:   # paired speaker-bootstrap differences against the first condition
    base = res.cond.iloc[0]; b = df[df.cond == base].set_index("id")
    for cond in res.cond.iloc[1:]:
        g = df[df.cond == cond].set_index("id"); common = g.index.intersection(b.index)
        d = pd.DataFrame({"speaker": g.loc[common, "speaker"], "e": g.loc[common, "w_err"] - b.loc[common, "w_err"], "n": b.loc[common, "w_n"]})
        spk = d.groupby("speaker")[["e", "n"]].sum().to_numpy(); idx = rng.integers(0, len(spk), (a.boot, len(spk)))
        v = spk[idx, 0].sum(1) / spk[idx, 1].sum(1)
        print(f"paired WER diff {cond} - {base}: {spk[:,0].sum()/spk[:,1].sum():+.3f} [{np.percentile(v,2.5):+.3f}, {np.percentile(v,97.5):+.3f}] over {len(common)} clips")
