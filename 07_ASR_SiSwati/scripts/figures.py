"""Report figures + summary numbers -> report/fig_*.png, report/summary.json"""
import json, os, sys
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from common import RESULTS, ROOT
OUT = os.path.join(ROOT, "report"); os.makedirs(OUT, exist_ok=True)
d = pd.read_csv(os.path.join(RESULTS, "per_utt.csv"))
rng = np.random.default_rng(0)
NAMES = {"simba_s": "Simba-S", "simba_w": "Simba-W (auto lang)", "simba_w_en": "Simba-W (English forced)", "simba_m": "Simba-M (CTC)",
         "seamless_zul": "SeamlessM4T-v2 (Zulu)", "seamless_eng": "SeamlessM4T-v2", "mms_zul": "MMS-1b (Zulu adapter)",
         "whisper_v3": "Whisper-v3", "whisper_v3_prompt": "Whisper-v3 + prompt", "whisper_v3_sw": "Whisper-v3 (Swahili)", "whisper_v3_auto": "Whisper-v3 (auto lang)"}

def stat(g, err, n, cluster=None, B=2000):
    """corpus rate + 95% bootstrap CI, resampling clusters (speakers) if given, else utterances"""
    if cluster is not None:
        a = g.groupby(cluster)[[err, n]].sum().to_numpy()
    else:
        a = g[[err, n]].to_numpy()
    idx = rng.integers(0, len(a), (B, len(a))); b = a[idx, 0].sum(1) / a[idx, 1].sum(1)
    return a[:, 0].sum() / a[:, 1].sum(), np.percentile(b, 2.5), np.percentile(b, 97.5)

summary = {}
def panel(ax, s, tags, err, n, title, cluster=None):
    rows = []
    for t in tags:
        g = d[(d.set == s) & (d.tag == t)]
        if len(g): rows.append((NAMES[t], *stat(g, err, n, cluster), len(g)))
    rows.sort(key=lambda r: r[1])
    summary[s + "|" + err] = {r[0]: dict(value=round(r[1], 4), lo=round(r[2], 4), hi=round(r[3], 4), n=r[4]) for r in rows}
    y = np.arange(len(rows))[::-1]
    v = np.array([r[1] for r in rows]) * 100; lo = np.array([r[2] for r in rows]) * 100; hi = np.array([r[3] for r in rows]) * 100
    ax.barh(y, v, height=0.55, color="#2a78d6")
    ax.errorbar(v, y, xerr=[v - lo, hi - v], fmt="none", ecolor="#52514e", elinewidth=1.2, capsize=3)
    for yi, vi, hii in zip(y, v, hi): ax.text(hii + 1.5, yi, f"{vi:.1f}%", va="center", fontsize=9, color="#0b0b0b")
    ax.set_yticks(y); ax.set_yticklabels([r[0] for r in rows], fontsize=9, color="#0b0b0b")
    ax.set_title(title, fontsize=10.5, loc="left", color="#0b0b0b")
    ax.set_xlim(0, max(hi) * 1.18 + 5)
    for sp in ["top", "right"]: ax.spines[sp].set_visible(False)
    for sp in ["left", "bottom"]: ax.spines[sp].set_color("#bdbcb6")
    ax.tick_params(colors="#52514e", labelsize=9); ax.xaxis.grid(True, color="#e6e5e0", lw=0.8); ax.set_axisbelow(True)

d["wl_err"] = d.w_err_len
plt.rcParams["font.family"] = "DejaVu Sans"
fig, axes = plt.subplots(1, 1, figsize=(7.2, 3.6))
panel(axes, "ssw_real_nchlt", ["simba_s", "simba_m", "simba_w", "mms_zul", "seamless_zul", "whisper_v3_sw", "whisper_v3_auto"],
      "c_err", "c_n", "Real siSwati (NCHLT, 500 clips): character error rate, % (lower is better)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_siswati_cer.png"), dpi=200); plt.close(fig)

fig, axes = plt.subplots(1, 1, figsize=(7.2, 3.6))
panel(axes, "ssw_real_nchlt", ["simba_s", "simba_m", "simba_w", "mms_zul", "seamless_zul", "whisper_v3_sw", "whisper_v3_auto"],
      "w_err", "w_n", "Real siSwati (NCHLT, 500 clips): word error rate, % (lower is better)")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_siswati_wer.png"), dpi=200); plt.close(fig)

eng_tags = ["whisper_v3", "whisper_v3_prompt", "seamless_eng", "simba_w", "simba_s"]
fig, axes = plt.subplots(2, 1, figsize=(7.2, 5.6))
panel(axes[0], "eng_real_afrispeech_sswaccent", eng_tags, "wl_err", "w_n",
      "SiSwati-accented English (96 clips, 5 speakers): lenient WER, %", cluster="speaker")
panel(axes[1], "eng_real_afrispeech_zuluaccent", eng_tags, "wl_err", "w_n",
      "Zulu-accented English (2,835 clips, 100 speakers): lenient WER, %", cluster="speaker")
fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_english_wer.png"), dpi=200); plt.close(fig)

# extra numbers for the text
for s in ["eng_real_afrispeech_sswaccent", "eng_real_afrispeech_zuluaccent", "cs_tts", "ssw_tts_control", "eng_tts_control", "ssw_real_nchlt"]:
    for t in d[d.set == s].tag.unique():
        g = d[(d.set == s) & (d.tag == t)]
        summary.setdefault("all", {})[f"{s}|{t}"] = dict(n=len(g), WER=round(g.w_err.sum() / g.w_n.sum(), 4), WER_lenient=round(g.wl_err.sum() / g.w_n.sum(), 4),
                                                        CER=round(g.c_err.sum() / g.c_n.sum(), 4), empty=round(g.is_empty.mean(), 4))
json.dump(summary, open(os.path.join(OUT, "summary.json"), "w"), indent=1)
print("ok", list(summary.keys()))
