"""Add AfriSpeech-200 'zulu' + 'isizulu' accent English (all splits) to the manifest as a larger Nguni-accent proxy set.
Downloads tarballs, writes 16 kHz copies, then removes the raw downloads to save disk."""
import glob, json, os, shutil, tarfile
import numpy as np, pandas as pd, soundfile as sf, soxr
from huggingface_hub import hf_hub_download
from common import DATA, MANIFEST

RAW = os.path.join(DATA, "raw"); SET = "eng_real_afrispeech_zuluaccent"; OUT = os.path.join(DATA, "audio", SET)
os.makedirs(OUT, exist_ok=True)
existing = [json.loads(l) for l in open(MANIFEST)]
rows = [r for r in existing if r["set"] != SET]
new = []
for acc in ["zulu", "isizulu"]:
    for split in ["train", "dev", "test"]:
        csv = hf_hub_download("intronhealth/afrispeech-200", f"transcripts/{acc}/{split}.csv", repo_type="dataset", local_dir=RAW)
        tgz = hf_hub_download("intronhealth/afrispeech-200", f"audio/{acc}/{split}/{split}_{acc}_0.tar.gz", repo_type="dataset", local_dir=RAW)
        tmp = os.path.join(RAW, f"tmp_{acc}_{split}")
        with tarfile.open(tgz) as tf: tf.extractall(tmp)
        wavs = {os.path.basename(p): p for p in glob.glob(os.path.join(tmp, "**", "*.wav"), recursive=True)}
        df = pd.read_csv(csv); miss = 0
        for _, r in df.iterrows():
            p = wavs.get(os.path.basename(r.audio_paths))
            if p is None: miss += 1; continue
            w, sr = sf.read(p)
            if w.ndim > 1: w = w.mean(axis=1)
            if sr != 16000: w = soxr.resample(w, sr, 16000)
            dst = os.path.join(OUT, f"afr_{r.idx}.wav"); sf.write(dst, w.astype(np.float32), 16000)
            new.append(dict(set=SET, id=f"afr_{r.idx}", path=os.path.relpath(dst, DATA), ref=str(r.transcript).strip(), lang="eng",
                            source=f"AfriSpeech-200 {acc} accent ({r.split}, {r.domain})", speaker=r.user_ids, synthetic=False,
                            duration=round(len(w) / 16000, 2), domain=r.domain, accent=acc))
        shutil.rmtree(tmp); os.remove(tgz)
        print(acc, split, len(df), "rows,", miss, "missing audio", flush=True)
with open(MANIFEST, "w") as f:
    for r in rows + new: f.write(json.dumps(r) + "\n")
d = pd.DataFrame(new)
print(len(d), "clips,", round(d.duration.sum() / 3600, 2), "h,", d.speaker.nunique(), "speakers; max dur", d.duration.max())
print(d.groupby(["accent", "domain"]).size())
