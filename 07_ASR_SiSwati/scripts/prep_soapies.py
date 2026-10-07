"""Prepare the SADiLaR soap-opera English-isiZulu code-switch subset for fine-tuning.
RESEARCH-ONLY DATA (SADiLaR 20.500.12185/545). Outputs (audio + manifest with transcripts) are gitignored; do not commit or redistribute.

Inputs  (data/raw/soapies_engzul/): balanced_engzul.xml, wav32k/audio/*.wav (unzipped balanced_engzul.zip), ids/ (official dev/test id lists)
Outputs: data/audio/soapies_engzul/<id>.wav (16 kHz mono PCM16), data/manifest_soapies_engzul.jsonl, data/soapies_engzul_summary.json (aggregates only)

Splits: `split` = official dev/test from the dataset authors, rest train (note: all dev speakers also occur in train).
        `split_v2` = official test kept, dev replaced by whole held-out speakers (speaker-disjoint from train), recommended for model selection.
Usage: python prep_soapies.py [--min_s 0.5] [--max_s 30]
"""
import argparse, collections, json, os, random, re
import numpy as np, soundfile as sf, soxr
import xml.etree.ElementTree as ET
from common import DATA

ap = argparse.ArgumentParser(); ap.add_argument("--min_s", type=float, default=0.5); ap.add_argument("--max_s", type=float, default=30.0)
ap.add_argument("--dev_hours", type=float, default=0.4); ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()
RAW = os.path.join(DATA, "raw", "soapies_engzul"); OUT = os.path.join(DATA, "audio", "soapies_engzul"); os.makedirs(OUT, exist_ok=True)

def clean(t):
    """Verbatim transcripts are lowercase without punctuation, but contain a few stray marks: '_' (truncation), '!' '.', digits."""
    t = re.sub(r"[_!.]", " ", t.lower())
    return re.sub(r"\s+", " ", t).strip()

ids = {k: set(open(os.path.join(RAW, "ids", "cs_engzul_balanced", "transcriptions", f"engzul_{k}_set_utterance_ids.txt")).read().split()) for k in ("dev", "tst")}
root = ET.parse(os.path.join(RAW, "balanced_engzul.xml")).getroot()
drops = collections.Counter(); rows = []
for ep in root.iter("episode"):
    for u in ep.iter("utterance"):
        uid = u.findtext("audio")[:-4]
        segs, off = [], 0.0
        for s in u.iter("utterance_segment"):
            d = float(s.findtext("duration") or 0) / 1000; t = clean(s.findtext("transcription") or "")
            if t: segs.append({"lang": s.findtext("lang_id", "").strip(), "text": t, "start": round(off, 3), "end": round(off + d, 3)})
            off += d
        if not segs: drops["empty_transcript"] += 1; continue
        if any(re.search(r"[0-9]", s["text"]) for s in segs): drops["digit_in_transcript"] += 1; continue
        path = os.path.join(RAW, "wav32k", "audio", uid + ".wav")
        wav, sr = sf.read(path, dtype="float32")
        if wav.ndim > 1: wav = wav.mean(axis=1)
        if sr != 16000: wav = soxr.resample(wav, sr, 16000)
        dur = len(wav) / 16000
        if dur < a.min_s: drops["too_short"] += 1; continue
        if dur > a.max_s: drops["too_long"] += 1; continue
        dst = os.path.join(OUT, uid + ".wav"); sf.write(dst, wav, 16000, subtype="PCM_16")
        langs = {s["lang"] for s in segs}
        n_eng = sum(len(s["text"].split()) for s in segs if s["lang"] == "eng"); n_w = sum(len(s["text"].split()) for s in segs)
        rows.append({"set": "soapies_engzul", "id": uid, "path": os.path.relpath(dst, DATA), "ref": " ".join(s["text"] for s in segs),
                     "lang": "zul+eng", "segments": segs, "cs_type": "mixed" if len(langs) > 1 else f"mono_{next(iter(langs))}",
                     "n_words": n_w, "n_eng_words": n_eng, "speaker": u.findtext("speaker_id"), "episode": ep.findtext("ep_number"),
                     "date": ep.findtext("broadcast_date"), "duration": round(dur, 2), "synthetic": False,
                     "source": "SADiLaR soap-opera corpus, English-isiZulu balanced (Rhythm City, Generations)", "license": "research-only",
                     "split": "dev" if uid in ids["dev"] else "test" if uid in ids["tst"] else "train"})

# speaker-disjoint dev: move whole speakers (not in test) out of train. Random subsets are scored so the dev set's mixed-utterance
# share and English word share match the non-test data (a plain random draw landed on English-heavy speakers: 85% English).
test_spk = {r["speaker"] for r in rows if r["split"] == "test"}
pool = [r for r in rows if r["split"] != "test"]
st = collections.defaultdict(lambda: [0.0, 0, 0, 0, 0])      # hours, utts, mixed utts, eng words, words
for r in pool:
    x = st[r["speaker"]]; x[0] += r["duration"]; x[1] += 1; x[2] += r["cs_type"] == "mixed"; x[3] += r["n_eng_words"]; x[4] += r["n_words"]
tgt_mixed = sum(x[2] for x in st.values()) / sum(x[1] for x in st.values()); tgt_eng = sum(x[3] for x in st.values()) / sum(x[4] for x in st.values())
cand = sorted(s for s in st if s not in test_spk and st[s][1] >= 5); rng = random.Random(a.seed); best = (9, None)
for _ in range(5000):
    k = rng.randint(8, 30); pick = rng.sample(cand, min(k, len(cand)))
    h = sum(st[s][0] for s in pick) / 3600
    if not (a.dev_hours * 0.8 <= h <= a.dev_hours * 1.25): continue
    mx = sum(st[s][2] for s in pick) / sum(st[s][1] for s in pick); en = sum(st[s][3] for s in pick) / max(1, sum(st[s][4] for s in pick))
    sc = abs(mx - tgt_mixed) + abs(en - tgt_eng)
    if sc < best[0]: best = (sc, set(pick))
dev_spk = best[1]
for r in rows: r["split_v2"] = "test" if r["split"] == "test" else "dev" if r["speaker"] in dev_spk else "train"

with open(os.path.join(DATA, "manifest_soapies_engzul.jsonl"), "w") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")

def agg(key):
    out = {}
    for sp in ("train", "dev", "test"):
        rs = [r for r in rows if r[key] == sp]
        out[sp] = {"utts": len(rs), "hours": round(sum(r["duration"] for r in rs) / 3600, 2), "speakers": len({r["speaker"] for r in rs}),
                   "mixed_share": round(sum(r["cs_type"] == "mixed" for r in rs) / max(1, len(rs)), 3),
                   "english_word_share": round(sum(r["n_eng_words"] for r in rs) / max(1, sum(r["n_words"] for r in rs)), 3)}
    tr = {r["speaker"] for r in rows if r[key] == "train"}
    out["speaker_overlap_with_train"] = {sp: len({r["speaker"] for r in rows if r[key] == sp} & tr) for sp in ("dev", "test")}
    return out
summary = {"kept": len(rows), "dropped": dict(drops), "official_split": agg("split"), "speaker_disjoint_dev_split": agg("split_v2"), "license": "research-only"}
json.dump(summary, open(os.path.join(DATA, "soapies_engzul_summary.json"), "w"), indent=1)
print(json.dumps(summary, indent=1))
