"""Build 16 kHz mono wavs + data/manifest.jsonl for all evaluation sets."""
import io, json, os, glob, random
import numpy as np, pandas as pd, soundfile as sf, soxr, torch
from transformers import VitsModel, AutoTokenizer
from common import DATA, MANIFEST, normalize

RAW = os.path.join(DATA, "raw"); AUD = os.path.join(DATA, "audio")
rows = []

def save(set_name, uid, wav, sr, ref, lang, source, speaker="", synthetic=False):
    if wav.ndim > 1: wav = wav.mean(axis=1)
    if sr != 16000: wav = soxr.resample(wav, sr, 16000)
    os.makedirs(os.path.join(AUD, set_name), exist_ok=True)
    p = os.path.join(AUD, set_name, f"{uid}.wav"); sf.write(p, wav.astype(np.float32), 16000)
    rows.append(dict(set=set_name, id=uid, path=os.path.relpath(p, DATA), ref=ref, lang=lang, source=source,
                     speaker=speaker, synthetic=synthetic, duration=round(len(wav) / 16000, 2)))

# 1. Real siSwati: NCHLT test split (via SimbaBench)
nchlt = pd.read_parquet(os.path.join(RAW, "asr_test", "HF_test-ssw*NCHTL.parquet"))
for _, r in nchlt.iterrows():
    wav, sr = sf.read(io.BytesIO(r.audio["bytes"]))
    save("ssw_real_nchlt", r.benchmark_id, wav, sr, r.text, "ssw", "NCHLT siSwati test (SimbaBench)")

# 2. Real SiSwati-accented English: AfriSpeech-200 'siswati' accent, all splits (out-of-domain for both models)
af = pd.concat([pd.read_csv(os.path.join(RAW, "transcripts", "siswati", f"{s}.csv")) for s in ["train", "dev", "test"]])
wavs = {os.path.basename(p): p for p in glob.glob(os.path.join(RAW, "afrispeech_siswati", "**", "*.wav"), recursive=True)}
for _, r in af.iterrows():
    wav, sr = sf.read(wavs[os.path.basename(r.audio_paths)])
    save("eng_real_afrispeech_sswaccent", f"afr_{r.idx}", wav, sr, r.transcript.strip(), "eng",
         f"AfriSpeech-200 siswati accent ({r.split}, {r.domain})", r.user_ids)

# 3. Synthetic sets, all with the same Nguni (Xhosa) VITS voice so TTS effects are held constant
tok = AutoTokenizer.from_pretrained("UBC-NLP/Simba-TTS-xho"); tts = VitsModel.from_pretrained("UBC-NLP/Simba-TTS-xho").eval()
vocab = set("abcdefghijklmnopqrstuvwxyz '")
def synth(text, seed):
    torch.manual_seed(seed)
    with torch.no_grad(): w = tts(**tok(text, return_tensors="pt")).waveform[0].numpy()
    return w, tts.config.sampling_rate
random.seed(0)
cs = pd.read_csv(os.path.join(DATA, "codeswitch_sentences.tsv"), sep="\t")
for i, r in cs.iterrows():
    w, sr = synth(normalize(r.text), i); save("cs_tts", r.id, w, sr, r.text, "ssw+eng", "authored code-switched text, Simba-TTS-xho", "tts", True)
ctrl = nchlt.sample(40, random_state=0)   # same text as real set -> direct real-vs-TTS comparison
for i, (_, r) in enumerate(ctrl.iterrows()):
    w, sr = synth(normalize(r.text), 100 + i); save("ssw_tts_control", "tts_" + r.benchmark_id, w, sr, r.text, "ssw", "NCHLT test text, Simba-TTS-xho", "tts", True)
en = af[af.transcript.map(lambda t: set(normalize(t)) <= vocab and 4 <= len(normalize(t).split()) <= 20)].sample(40, random_state=0)
for i, (_, r) in enumerate(en.iterrows()):
    w, sr = synth(normalize(r.transcript), 200 + i); save("eng_tts_control", f"tts_afr_{r.idx}", w, sr, r.transcript.strip(), "eng", "AfriSpeech siswati text, Simba-TTS-xho", "tts", True)

with open(MANIFEST, "w") as f:
    for r in rows: f.write(json.dumps(r) + "\n")
df = pd.DataFrame(rows); print(df.groupby("set").agg(n=("id", "size"), minutes=("duration", lambda d: round(d.sum() / 60, 1))))
