"""Score all results/hyp_*.jsonl -> results/scores.csv, results/per_utt.csv, results/cs_by_language.csv"""
import glob, json, os
import numpy as np, pandas as pd, jiwer
import re
from common import MANIFEST, RESULTS, normalize, normalize_lenient

man = pd.DataFrame([json.loads(l) for l in open(MANIFEST)]).set_index("id")
hyp = pd.concat([pd.read_json(p, lines=True) for p in glob.glob(os.path.join(RESULTS, "hyp_*.jsonl"))])
hyp["ref_n"] = hyp.id.map(man.ref).map(normalize); hyp["hyp_n"] = hyp.hyp.map(normalize)

def counts(ref, h):
    o = jiwer.process_words(ref, h if h else "<empty>")
    c = jiwer.process_characters(ref, h if h else " ")
    return o.substitutions + o.deletions + o.insertions, len(ref.split()), c.substitutions + c.deletions + c.insertions, len(ref)
hyp[["w_err", "w_n", "c_err", "c_n"]] = [counts(r, h) for r, h in zip(hyp.ref_n, hyp.hyp_n)]
hyp["wer"] = hyp.w_err / hyp.w_n
hyp["is_empty"] = hyp.hyp_n.str.len() == 0
hyp["ref_has_digit"] = hyp.id.map(man.ref).str.contains(r"\d")
hyp["speaker"] = hyp.id.map(man.speaker)
hyp["domain"] = hyp.id.map(man.source).str.extract(r"(clinical|general)")[0]
hyp["w_err_len"] = [jiwer.process_words(normalize_lenient(r), normalize_lenient(h) or "<empty>").wer * len(normalize_lenient(r).split())
                    for r, h in zip(hyp.id.map(man.ref), hyp.hyp)]
hyp.to_csv(os.path.join(RESULTS, "per_utt.csv"), index=False)

rng = np.random.default_rng(0)
def boot(g, k="w", B=2000):
    e, n = g[f"{k}_err"].to_numpy(), g[f"{k}_n"].to_numpy(); idx = rng.integers(0, len(g), (B, len(g)))
    s = e[idx].sum(1) / n[idx].sum(1); return np.percentile(s, [2.5, 97.5])
out = []
for (s, t), g in hyp.groupby(["set", "tag"]):
    lo, hi = boot(g)
    out.append(dict(set=s, condition=t, n=len(g), WER=g.w_err.sum() / g.w_n.sum(), WER_lo=lo, WER_hi=hi,
                    CER=g.c_err.sum() / g.c_n.sum(), exact_match=(g.w_err == 0).mean(), empty_output=g.is_empty.mean()))
    if s.startswith("eng_real"):
        spk = g.groupby("speaker")[["w_err", "w_n"]].sum().to_numpy()
        idx = rng.integers(0, len(spk), (2000, len(spk))); b = spk[idx, 0].sum(1) / spk[idx, 1].sum(1)
        out[-1].update(WER_spk_lo=np.percentile(b, 2.5), WER_spk_hi=np.percentile(b, 97.5), n_speakers=len(spk))
        gd = g[~g.ref_has_digit]
        out[-1].update(WER_lenient=g.w_err_len.sum() / g.w_n.sum(), WER_nodigit_lenient=gd.w_err_len.sum() / gd.w_n.sum(), n_nodigit=len(gd))
sc = pd.DataFrame(out).round(4); sc.to_csv(os.path.join(RESULTS, "scores.csv"), index=False)
print(sc.to_string(index=False))
spk = hyp[hyp.set.str.startswith("eng_real")].groupby(["tag", "speaker"]).apply(
    lambda g: pd.Series(dict(n=len(g), WER=g.w_err.sum() / g.w_n.sum(), CER=g.c_err.sum() / g.c_n.sum(), empty=g.is_empty.sum()))).round(3)
spk.to_csv(os.path.join(RESULTS, "afrispeech_by_speaker.csv"))
dom = hyp[hyp.set.str.startswith("eng_real")].groupby(["set", "domain", "tag"]).apply(
    lambda g: pd.Series(dict(n=len(g), WER=g.w_err.sum() / g.w_n.sum(), WER_lenient=g.w_err_len.sum() / g.w_n.sum(),
                             CER=g.c_err.sum() / g.c_n.sum(), empty=g.is_empty.mean()))).round(4)
dom.to_csv(os.path.join(RESULTS, "eng_by_domain.csv")); print(dom.to_string())

# Code-switched set: error rate on English vs siSwati reference words (via word alignment)
cs_words = pd.read_csv(os.path.join(os.path.dirname(MANIFEST), "codeswitch_english_words.txt"), header=None)[0].str.lower().tolist()
ENG = set(cs_words); rows = []
for _, r in hyp[hyp.set == "cs_tts"].iterrows():
    o = jiwer.process_words(r.ref_n, r.hyp_n or "<empty>"); ref = r.ref_n.split()
    ok = [False] * len(ref)
    for ch in o.alignments[0]:
        if ch.type == "equal":
            for i in range(ch.ref_start_idx, ch.ref_end_idx): ok[i] = True
    for w, good in zip(ref, ok): rows.append(dict(tag=r.tag, lang="english" if w in ENG else "siswati", correct=good))
if rows:
    cl = pd.DataFrame(rows).groupby(["tag", "lang"]).agg(n_words=("correct", "size"), word_error_rate=("correct", lambda c: 1 - c.mean())).round(3).reset_index()
    cl.to_csv(os.path.join(RESULTS, "cs_by_language.csv"), index=False); print(cl.to_string(index=False))

# Paired bootstrap: WER difference (A - B) on the same utterances
pairs = [(e, A, B) for e in ["eng_real_afrispeech_sswaccent", "eng_real_afrispeech_zuluaccent"]
         for A, B in [("whisper_v3", "seamless_eng"), ("whisper_v3", "simba_s"), ("whisper_v3_prompt", "whisper_v3"), ("seamless_eng", "simba_s"), ("whisper_v3_prompt", "seamless_eng"), ("simba_w_en", "simba_w"), ("whisper_v3", "simba_w")]] + [
         ("ssw_real_nchlt", "simba_s", "seamless_zul"), ("ssw_tts_control", "simba_s", "seamless_zul"),
         ("eng_tts_control", "simba_s", "seamless_eng"),
         ("cs_tts", "simba_s", "seamless_zul")]
pr = []
for s, A, Bm in pairs:
    h = hyp[(hyp.set == s) & hyp.tag.isin([A, Bm])]
    if set(h.tag) != {A, Bm}: continue
    g = h.pivot_table(index="id", columns="tag", values=["w_err", "w_n", "c_err", "c_n"]).dropna()  # clips scored by both
    for k in ["w", "c"]:
        ea, eb, n = g[f"{k}_err"][A].to_numpy(), g[f"{k}_err"][Bm].to_numpy(), g[f"{k}_n"][A].to_numpy()
        idx = rng.integers(0, len(n), (2000, len(n))); d = (ea[idx].sum(1) - eb[idx].sum(1)) / n[idx].sum(1)
        pr.append(dict(set=s, A=A, B=Bm, n=len(n), metric="WER" if k == "w" else "CER", diff=(ea.sum() - eb.sum()) / n.sum(),
                       lo=np.percentile(d, 2.5), hi=np.percentile(d, 97.5)))
pr = pd.DataFrame(pr).round(4); pr.to_csv(os.path.join(RESULTS, "paired_differences.csv"), index=False); print(pr.to_string(index=False))
