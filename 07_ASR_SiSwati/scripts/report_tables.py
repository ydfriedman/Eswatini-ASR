"""Collect report tables (formatted strings) from results/*.csv -> report/tables.json"""
import json, os
import pandas as pd
from common import RESULTS, ROOT
d = pd.read_csv(os.path.join(RESULTS, "per_utt.csv"))
NAMES = {"simba_s": "Simba-S", "simba_w": "Simba-W (auto language)", "simba_w_en": "Simba-W (English forced)", "simba_m": "Simba-M (CTC)",
         "seamless_zul": "SeamlessM4T-v2 (Zulu target)", "seamless_eng": "SeamlessM4T-v2 (English target)", "mms_zul": "MMS-1b-all (Zulu adapter)",
         "whisper_v3": "Whisper-large-v3", "whisper_v3_prompt": "Whisper-large-v3 + clinical prompt", "whisper_v3_sw": "Whisper-large-v3 (Swahili)",
         "whisper_v3_auto": "Whisper-large-v3 (auto language)"}
pct = lambda x: f"{100 * x:.1f}%"
def agg(g):
    return dict(n=len(g), WER=g.w_err.sum() / g.w_n.sum(), LEN=g.w_err_len.sum() / g.w_n.sum(), CER=g.c_err.sum() / g.c_n.sum(),
                EMPTY=g.is_empty.mean(), EXACT=(g.w_err == 0).mean())
T = {}
def table(s, tags, cols, sortkey):
    rows = []
    for t in tags:
        g = d[(d.set == s) & (d.tag == t)]
        if len(g): rows.append((t, agg(g)))
    rows.sort(key=lambda r: r[1][sortkey])
    return [[NAMES[t]] + [str(a["n"]) if c == "n" else pct(a[c]) for c in cols] for t, a in rows]

T["siswati"] = table("ssw_real_nchlt", ["simba_s", "simba_m", "simba_w", "mms_zul", "seamless_zul", "whisper_v3_sw", "whisper_v3_auto"], ["WER", "CER", "EXACT"], "CER")
eng = ["whisper_v3", "whisper_v3_prompt", "seamless_eng", "simba_w", "simba_s"]
T["eng_ssw"] = table("eng_real_afrispeech_sswaccent", eng, ["WER", "LEN", "CER", "EMPTY"], "LEN")
T["eng_zul"] = table("eng_real_afrispeech_zuluaccent", eng, ["WER", "LEN", "CER", "EMPTY"], "LEN")
# Simba-W forced English vs auto on the same subset
sub = d[d.tag == "simba_w_en"]
if len(sub):
    ids = set(sub.id); rows = []
    for s, lab in [("eng_real_afrispeech_sswaccent", "SiSwati accent (96)"), ("eng_real_afrispeech_zuluaccent", "Zulu accent (random 300)")]:
        for t in ["simba_w", "simba_w_en", "whisper_v3"]:
            g = d[(d.set == s) & (d.tag == t) & d.id.isin(ids)]
            a = agg(g); rows.append([lab, NAMES[t], pct(a["LEN"]), pct(a["CER"]), pct(a["EMPTY"])])
    T["simbaw_en"] = rows
# domain split (Zulu-accent set, lenient)
rows = []
for t in eng:
    r = [NAMES[t]]
    for dom in ["clinical", "general"]:
        g = d[(d.set == "eng_real_afrispeech_zuluaccent") & (d.tag == t) & (d.domain == dom)]
        r.append(pct(agg(g)["LEN"]))
    rows.append(r)
T["domain"] = rows
# code-switched
cs = pd.read_csv(os.path.join(RESULTS, "cs_by_language.csv")).pivot(index="tag", columns="lang", values="word_error_rate")
rec = pd.read_csv(os.path.join(RESULTS, "cs_recoverability.csv")).set_index("tag")
rows = []
for t in cs.index:
    g = d[(d.set == "cs_tts") & (d.tag == t)]; a = agg(g)
    ctrl = d[(d.set == "ssw_tts_control") & (d.tag == t)]
    rows.append([NAMES[t], pct(a["CER"]), pct(agg(ctrl)["CER"]) if len(ctrl) else "–", pct(cs.loc[t, "siswati"]), pct(cs.loc[t, "english"]),
                 pct(rec.loc[t, "recoverable"]) if t in rec.index else "–"])
rows.sort(key=lambda r: float(r[1][:-1]))
T["cs"] = rows
# real vs TTS on identical text
rows = []
for t in ["simba_s", "simba_m", "simba_w", "mms_zul", "seamless_zul"]:
    ids = set(d[(d.set == "ssw_tts_control") & (d.tag == t)].id.str.replace("tts_", "", regex=False))
    real = d[(d.set == "ssw_real_nchlt") & (d.tag == t) & d.id.isin(ids)]; tts = d[(d.set == "ssw_tts_control") & (d.tag == t)]
    if len(real) and len(tts): rows.append([NAMES[t], pct(agg(real)["CER"]), pct(agg(tts)["CER"]), pct(agg(real)["WER"]), pct(agg(tts)["WER"])])
T["tts_gap"] = rows
json.dump(T, open(os.path.join(ROOT, "report", "tables.json"), "w"), indent=1)
for k, v in T.items(): print(k); [print("  ", r) for r in v]
