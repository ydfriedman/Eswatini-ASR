"""Build a small NCHLT siSwati TRAIN replay set (keeps the fine-tune from forgetting siSwati). CC BY 3.0. Downloads ONE train shard (~430 MB)
from the Hugging Face dataset danielshaps/nchlt_speech_ssw, keeps clean rows (no typos/disfluency), samples N spread over speakers, writes 16 kHz wavs
and data/manifest_nchlt_train.jsonl. NCHLT train/test speakers are disjoint, so the existing ssw_real_nchlt eval set stays clean.
usage: python prep_nchlt_replay.py --n 1500 [--shard 0]   (NOT yet run here: needs the HF CDN hosts reachable)"""
import argparse, io, json, os, random
import numpy as np, pandas as pd, soundfile as sf, soxr
from huggingface_hub import hf_hub_download
from common import DATA

ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=1500); ap.add_argument("--shard", type=int, default=0); ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args()
p = hf_hub_download("danielshaps/nchlt_speech_ssw", f"data/train-{a.shard:05d}-of-00007.parquet", repo_type="dataset", local_dir=os.path.join(DATA, "raw", "nchlt_ssw"))
df = pd.read_parquet(p); df = df[~df.typos & ~df.disfluency & df.text.str.strip().astype(bool)]
rng = random.Random(a.seed); per = {}
for i, r in df.iterrows(): per.setdefault(r.speaker_id, []).append(i)
for v in per.values(): rng.shuffle(v)
picked = []
while len(picked) < a.n and any(per.values()):                    # round-robin over speakers
    for s in list(per):
        if per[s] and len(picked) < a.n: picked.append(per[s].pop())
out = os.path.join(DATA, "audio", "nchlt_ssw_train"); os.makedirs(out, exist_ok=True); rows = []
for i in picked:
    r = df.loc[i]; wav, sr = sf.read(io.BytesIO(r.audio["bytes"]), dtype="float32")
    if wav.ndim > 1: wav = wav.mean(axis=1)
    if sr != 16000: wav = soxr.resample(wav, sr, 16000)
    uid = f"nchlt_{r.utterance_id}"; sf.write(os.path.join(out, uid + ".wav"), wav, 16000, subtype="PCM_16")
    rows.append({"set": "nchlt_ssw_train", "id": uid, "path": f"audio/nchlt_ssw_train/{uid}.wav", "ref": r.text.strip(), "lang": "ssw", "speaker": r.speaker_id,
                 "duration": round(len(wav) / 16000, 2), "synthetic": False, "split": "train", "source": "NCHLT siSwati train (CC BY 3.0)"})
with open(os.path.join(DATA, "manifest_nchlt_train.jsonl"), "w") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
print(len(rows), "clips,", round(sum(r["duration"] for r in rows) / 3600, 2), "h,", len({r["speaker"] for r in rows}), "speakers")
