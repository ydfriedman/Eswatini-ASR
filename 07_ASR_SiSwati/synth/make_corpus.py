"""Prototype: expand grammar -> segment-wise TTS (siSwati: Simba-TTS-xho placeholder, English: MMS-TTS-eng) -> augment -> manifest.
Usage: ../../.venv_asr/bin/python make_corpus.py --n 1400 --out ../data/synth --seed 0
"""
import argparse, json, os, random, re, time, hashlib
import numpy as np, soundfile as sf, torch, torchaudio
from transformers import AutoTokenizer, VitsModel
import grammar

ap = argparse.ArgumentParser()
ap.add_argument("--n", type=int, default=1400); ap.add_argument("--out", default="../data/synth"); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--val_frac", type=float, default=0.1)
a = ap.parse_args()
rng = random.Random(a.seed); torch.manual_seed(a.seed)
SR = 16000
os.makedirs(os.path.join(a.out, "audio"), exist_ok=True)

MODELS = {"ssw": "UBC-NLP/Simba-TTS-xho", "eng": "facebook/mms-tts-eng"}
tts = {k: (AutoTokenizer.from_pretrained(v), VitsModel.from_pretrained(v).eval()) for k, v in MODELS.items()}
for k, (_, m) in tts.items(): assert m.config.sampling_rate == SR, (k, m.config.sampling_rate)

def clean(t, lang):
    t = t.lower(); t = t.replace("ngelisontfo", "ngelisontfo")
    return re.sub(r"[^a-z' ]", " ", t).strip() if lang == "eng" else re.sub(r"[^a-z' ]", " ", t).strip()

def say(text, lang, rate, ns):
    tok, m = tts[lang]
    m.speaking_rate = rate; m.noise_scale = ns
    ids = tok(clean(text, lang), return_tensors="pt")
    with torch.no_grad(): w = m(**ids).waveform[0].numpy()
    return w / (np.abs(w).max() + 1e-6) * 0.5   # per-segment peak norm so languages sit at the same level

def trim(w, thr=0.01, pad=int(0.03 * SR)):
    idx = np.where(np.abs(w) > thr)[0]
    return w[max(idx[0] - pad, 0): idx[-1] + pad] if len(idx) else w

def rir(rt60):
    n = int(SR * rt60); t = np.arange(n) / SR
    h = np.random.randn(n) * np.exp(-6.9 * t / rt60); h[0] = 1.0
    return h / np.linalg.norm(h)

def augment(w, r):
    p = {}
    n = r.choice([-2, -1, 0, 0, 1, 2]) + r.uniform(-0.4, 0.4); p["pitch_semitones"] = round(n, 2)
    if abs(n) > 0.3:   # resampling shifts pitch AND tempo together (cheap; tempo is randomised anyway)
        f = 2 ** (n / 12); w = torchaudio.functional.resample(torch.from_numpy(w).float(), int(SR * f), SR).numpy()
    if r.random() < 0.5:
        rt = r.uniform(0.2, 0.7); p["reverb_rt60"] = round(rt, 2)
        np.random.seed(r.randrange(1 << 30)); w = np.convolve(w, rir(rt))[: len(w) + int(0.1 * SR)]
    if r.random() < 0.25:
        p["telephone"] = True
        w = torchaudio.functional.resample(torchaudio.functional.highpass_biquad(torch.from_numpy(w).float(), SR, 300), SR, 8000)
        w = torchaudio.functional.resample(torchaudio.functional.lowpass_biquad(w, 8000, 3400), 8000, SR).numpy()
    # coloured noise as a stand-in for clinic ambience (replace with real recorded ambience when available)
    snr = r.uniform(8, 30); p["snr_db"] = round(snr, 1)
    beta = r.choice([0.0, 1.0, 2.0]); p["noise_beta"] = beta
    spec = np.fft.rfft(np.random.randn(len(w))); f = np.arange(len(spec)) + 1.0
    nz = np.fft.irfft(spec / f ** (beta / 2), len(w))
    nz *= np.sqrt((w ** 2).mean() / (10 ** (snr / 10) * (nz ** 2).mean() + 1e-12))
    w = w + nz
    p["gain_db"] = round(r.uniform(-12, -2), 1); w = w / (np.abs(w).max() + 1e-6) * 10 ** (p["gain_db"] / 20)
    return w.astype(np.float32), p

frames = list(range(len(grammar.FRAMES)))
rng.shuffle(frames)
n_val = max(1, int(len(frames) * a.val_frac))
val_frames = set(frames[:n_val])    # held-out TEMPLATES: validation never shares a frame with training
man, seen, t0 = [], set(), time.time()
tot = 0.0
while len(man) < a.n:
    fi = rng.randrange(len(grammar.FRAMES))
    segs = grammar.expand(grammar.FRAMES[fi], rng)
    key = tuple(segs)
    if key in seen: continue
    seen.add(key)
    rate, ns = rng.uniform(0.85, 1.15), rng.uniform(0.5, 0.9)
    parts, spans, cur = [], [], 0.0
    for j, (lang, t) in enumerate(segs):
        w = trim(say(t, lang, 1.0 / rate, ns))
        gap = np.zeros(int(SR * (0.0 if j == 0 else rng.uniform(0.02, 0.15))), dtype=np.float32)
        parts += [gap, w]; cur += len(gap) / SR
        spans.append({"lang": lang, "text": t, "start": round(cur, 3), "end": round(cur + len(w) / SR, 3)}); cur += len(w) / SR
    wav, p = augment(np.concatenate(parts).astype(np.float32), rng)
    uid = f"cs{len(man):06d}"
    sf.write(os.path.join(a.out, "audio", uid + ".wav"), wav, SR, subtype="PCM_16")
    text = " ".join(t for _, t in segs); tot += len(wav) / SR
    man.append({"id": uid, "path": f"audio/{uid}.wav", "text": text, "segments": spans, "frame": fi,
                "split": "val" if fi in val_frames else "train", "duration": round(len(wav) / SR, 2),
                "synthetic": True, "tts": MODELS, "aug": p, "speaking_rate": round(rate, 2)})
    if len(man) % 100 == 0: print(f"{len(man)} utts, {tot/3600:.2f} h, {time.time()-t0:.0f}s", flush=True)

with open(os.path.join(a.out, "manifest.jsonl"), "w") as f:
    for m in man: f.write(json.dumps(m, ensure_ascii=False) + "\n")
ew = sum(len(s["text"].split()) for m in man for s in m["segments"] if s["lang"] == "eng"); aw = sum(len(m["text"].split()) for m in man)
print(f"DONE {len(man)} utts, {tot/3600:.2f} h; English word share {ew/aw:.0%}; train {sum(m['split']=='train' for m in man)} val {sum(m['split']=='val' for m in man)}; "
      f"unique texts {len({m['text'] for m in man})}")
