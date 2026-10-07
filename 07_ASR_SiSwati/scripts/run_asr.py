"""Transcribe manifest clips with a SeamlessM4T-v2-architecture or Whisper model. Resumable.
usage: run_asr.py MODEL_ID TAG [--tgt_lang LANG] [--sets a,b] [--prompt TEXT]
For Whisper, --tgt_lang is the transcription language and --prompt an optional initial prompt.
Greedy decoding (num_beams=1) for every model/condition so comparisons are like-for-like."""
import argparse, json, os, time, torch, soundfile as sf
from transformers import AutoConfig, AutoProcessor, SeamlessM4Tv2ForSpeechToText, WhisperForConditionalGeneration
from common import MANIFEST, DATA, RESULTS

ap = argparse.ArgumentParser(); ap.add_argument("model"); ap.add_argument("tag")
ap.add_argument("--tgt_lang", default=None); ap.add_argument("--sets", default=None); ap.add_argument("--prompt", default=None)
ap.add_argument("--ids", default=None, help="file with one clip id per line (subset)")
a = ap.parse_args()
rows = [json.loads(l) for l in open(MANIFEST)]
if a.sets: rows = [r for r in rows if r["set"] in a.sets.split(",")]
if a.ids: keep = set(open(a.ids).read().split()); rows = [r for r in rows if r["id"] in keep]
out = os.path.join(RESULTS, f"hyp_{a.tag}.jsonl")
done = {json.loads(l)["id"] for l in open(out)} if os.path.exists(out) else set()
todo = [r for r in rows if r["id"] not in done]
print(f"{a.tag}: {len(todo)} to do ({len(done)} done)", flush=True)
proc = AutoProcessor.from_pretrained(a.model)
WHISPER = AutoConfig.from_pretrained(a.model).model_type == "whisper"   # also catches fine-tunes like Simba-W
M = WhisperForConditionalGeneration if WHISPER else SeamlessM4Tv2ForSpeechToText
# eager attention: MPS SDPA yields "!!!!" garbage for Whisper in fp16/bf16
m = M.from_pretrained(a.model, dtype=torch.float16, **({"attn_implementation": "eager"} if WHISPER else {})).to("mps").eval()
prompt_ids = proc.get_prompt_ids(a.prompt, return_tensors="pt").to("mps") if (WHISPER and a.prompt) else None
t0 = time.time()
with open(out, "a") as f:
    for i, r in enumerate(todo):
        w, _ = sf.read(os.path.join(DATA, r["path"]))
        if WHISPER:
            x = proc(w, sampling_rate=16000, return_tensors="pt").to("mps")
            kw = dict(num_beams=1, max_new_tokens=min(440 - (0 if prompt_ids is None else len(prompt_ids)), int(r["duration"] * 10) + 20), task="transcribe")
            if a.tgt_lang != "auto": kw["language"] = a.tgt_lang or "en"   # "auto" = Whisper language detection
            if prompt_ids is not None: kw["prompt_ids"] = prompt_ids
        else:
            x = proc(audios=w, sampling_rate=16000, return_tensors="pt").to("mps")
            kw = dict(num_beams=1, max_new_tokens=int(r["duration"] * 10) + 20)
            if a.tgt_lang: kw["tgt_lang"] = a.tgt_lang
        x["input_features"] = x["input_features"].half()
        with torch.no_grad(): seq = m.generate(**x, **kw)[0]
        hyp = proc.tokenizer.decode(seq, skip_special_tokens=True).strip()
        if WHISPER and a.prompt and hyp.startswith(a.prompt.strip()): hyp = hyp[len(a.prompt.strip()):].strip()
        f.write(json.dumps(dict(id=r["id"], set=r["set"], model=a.model, tag=a.tag, tgt_lang=a.tgt_lang, prompt=a.prompt, hyp=hyp)) + "\n"); f.flush()
        if (i + 1) % 50 == 0: print(f"{a.tag}: {i+1}/{len(todo)} ({time.time()-t0:.0f}s)", flush=True)
print(f"{a.tag}: DONE {len(todo)} in {time.time()-t0:.0f}s", flush=True)
