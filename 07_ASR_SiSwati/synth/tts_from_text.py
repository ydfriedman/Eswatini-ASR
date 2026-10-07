"""Voice the morphotactic text (data/synth_text/cs_text.jsonl) with MMS-TTS-eng (English spans) and Simba-TTS-xho (siSwati spans; there is
NO siSwati TTS, Xhosa is the nearest Nguni voice and mispronounces siSwati - see the round-1 report). Augmentations are those of make_corpus.py.
usage: python tts_from_text.py --n 1500 --out ../data/synth [--glue split|merge] [--device cuda]
glue: a siSwati prefix glued to an English stem ('ema-' + 'pills'): `split` voices them as two segments with no gap (default); `merge` voices
      prefix+stem together with the Xhosa voice (English stem then read with Xhosa phonology).
Output: <out>/audio/*.wav (16 kHz) and <out>/manifest.jsonl (fields: id, path, ref, split, duration, synthetic, switch_type, segments). NOT yet run:
needs the TTS weights from huggingface.co (CDN hosts must be reachable)."""
import argparse, json, os, random, re, sys, time
import numpy as np, soundfile as sf, torch, torchaudio
from transformers import AutoTokenizer, VitsModel

ap = argparse.ArgumentParser(); ap.add_argument("--text", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "synth_text", "cs_text.jsonl"))
ap.add_argument("--n", type=int, default=1500); ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "synth"))
ap.add_argument("--glue", default="split", choices=["split", "merge"]); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--device", default="cpu"); ap.add_argument("--types", default=None, help="comma list of switch_type to keep (default: all)")
a = ap.parse_args()
rng = random.Random(a.seed); torch.manual_seed(a.seed); SR = 16000
os.makedirs(os.path.join(a.out, "audio"), exist_ok=True)
MODELS = {"ssw": "UBC-NLP/Simba-TTS-xho", "eng": "facebook/mms-tts-eng"}
if os.environ.get("TTS_STUB"):        # plumbing test without model weights: a tone whose length follows the text length
    class _M:
        config = type("c", (), {"sampling_rate": SR})()
        def __call__(self, input_ids=None, **k):
            n = int(SR * 0.06 * input_ids.shape[1]); t = torch.arange(n) / SR
            return type("o", (), {"waveform": (torch.sin(2 * torch.pi * 180 * t) * torch.hann_window(n))[None]})()
    class _T:
        def __call__(self, text, return_tensors=None): return type("b", (dict,), {"to": lambda s, d: s, "__getattr__": lambda s, k: s[k]})({"input_ids": torch.zeros(1, len(text), dtype=torch.long)})
    tts = {k: (_T(), _M()) for k in MODELS}
else:
    tts = {k: (AutoTokenizer.from_pretrained(v), VitsModel.from_pretrained(v).eval().to(a.device)) for k, v in MODELS.items()}
for k, (_, m) in tts.items(): assert m.config.sampling_rate == SR, (k, m.config.sampling_rate)

def clean(t): return re.sub(r"[^a-z' ]", " ", t.lower()).strip()
def say(text, lang, rate, ns):
    tok, m = tts[lang]; m.speaking_rate = rate; m.noise_scale = ns
    ids = tok(clean(text) or "a", return_tensors="pt").to(a.device)
    with torch.no_grad(): w = m(**ids).waveform[0].cpu().numpy()
    return w / (np.abs(w).max() + 1e-6) * 0.5
def trim(w, thr=0.01, pad=int(0.03 * SR)):
    idx = np.where(np.abs(w) > thr)[0]; return w[max(idx[0] - pad, 0): idx[-1] + pad] if len(idx) else w
def rir(rt60):
    n = int(SR * rt60); t = np.arange(n) / SR; h = np.random.randn(n) * np.exp(-6.9 * t / rt60); h[0] = 1.0; return h / np.linalg.norm(h)
def augment(w, r):
    p = {}; n = r.choice([-2, -1, 0, 0, 1, 2]) + r.uniform(-0.4, 0.4); p["pitch_semitones"] = round(n, 2)
    if abs(n) > 0.3: w = torchaudio.functional.resample(torch.from_numpy(w).float(), int(round(100 * 2 ** (n / 12))), 100).numpy()   # coarse rational ratio: fast, same pitch+tempo shift
    if r.random() < 0.5:
        rt = r.uniform(0.2, 0.7); p["reverb_rt60"] = round(rt, 2); np.random.seed(r.randrange(1 << 30)); w = torchaudio.functional.fftconvolve(torch.from_numpy(w).float(), torch.from_numpy(rir(rt)).float()).numpy()[: len(w) + int(0.1 * SR)]
    if r.random() < 0.25:
        p["telephone"] = True; w = torchaudio.functional.highpass_biquad(torch.from_numpy(w).float(), SR, 300)
        w = torchaudio.functional.resample(torchaudio.functional.resample(w, SR, 8000), 8000, SR); w = torchaudio.functional.lowpass_biquad(w, SR, 3400).numpy()
    snr = r.uniform(8, 30); beta = r.choice([0.0, 1.0, 2.0]); p["snr_db"] = round(snr, 1); p["noise_beta"] = beta
    spec = np.fft.rfft(np.random.randn(len(w))); nz = np.fft.irfft(spec / (np.arange(len(spec)) + 1.0) ** (beta / 2), len(w))
    nz *= np.sqrt((w ** 2).mean() / (10 ** (snr / 10) * (nz ** 2).mean() + 1e-12)); w = w + nz
    p["gain_db"] = round(r.uniform(-12, -2), 1); return (w / (np.abs(w).max() + 1e-6) * 10 ** (p["gain_db"] / 20)).astype(np.float32), p

def plan(segs):
    """-> list of (lang, text, gap_before). A segment that follows a glue_next prefix gets NO gap (prefix + stem are one word).
    With glue=merge a glued ssw prefix and the following English stem are voiced as one ssw string."""
    out, i, prev_glue = [], 0, False
    while i < len(segs):
        s = segs[i]
        if a.glue == "merge" and s.get("glue_next") and i + 1 < len(segs):
            out.append(("ssw", s["text"] + segs[i + 1]["text"], 0.0 if prev_glue else rng.uniform(0.02, 0.15))); prev_glue = bool(segs[i + 1].get("glue_next")); i += 2; continue
        out.append((s["lang"], s["text"], 0.0 if prev_glue else rng.uniform(0.02, 0.15))); prev_glue = bool(s.get("glue_next")); i += 1
    return out

rows = [json.loads(l) for l in open(a.text)]
if a.types: rows = [r for r in rows if r["switch_type"] in a.types.split(",")]
rng.shuffle(rows); man, t0, tot = [], time.time(), 0.0
for r in rows[: a.n]:
    rate, ns = rng.uniform(0.85, 1.15), rng.uniform(0.5, 0.9); parts, spans, cur = [], [], 0.0
    for j, (lang, text, gap) in enumerate(plan(r["segments"])):
        w = trim(say(text, lang, 1.0 / rate, ns)); g = np.zeros(int(SR * (0.0 if j == 0 else gap)), dtype=np.float32)
        parts += [g, w]; cur += len(g) / SR; spans.append({"lang": lang, "text": text, "start": round(cur, 3), "end": round(cur + len(w) / SR, 3)}); cur += len(w) / SR
    wav, p = augment(np.concatenate(parts).astype(np.float32), rng)
    sf.write(os.path.join(a.out, "audio", r["id"] + ".wav"), wav, SR, subtype="PCM_16"); tot += len(wav) / SR
    man.append({"set": "synth_cs", "id": r["id"], "path": f"audio/{r['id']}.wav", "ref": r["text"], "split": r["split"], "duration": round(len(wav) / SR, 2),
                "synthetic": True, "switch_type": r["switch_type"], "segments": spans, "aug": p, "glue": a.glue, "tts": MODELS})
    if len(man) % 100 == 0: print(f"{len(man)} utts, {tot/3600:.2f} h, {time.time()-t0:.0f}s", flush=True)
with open(os.path.join(a.out, "manifest.jsonl"), "w") as f:
    for m in man: f.write(json.dumps(m, ensure_ascii=False) + "\n")
print(f"DONE {len(man)} utts, {tot/3600:.2f} h")
