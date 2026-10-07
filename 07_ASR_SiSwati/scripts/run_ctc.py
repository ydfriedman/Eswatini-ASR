"""Transcribe manifest clips with an MMS-style CTC model + language adapter. Resumable.
usage: run_ctc.py MODEL_ID ADAPTER TAG --sets a,b
CTC emits characters frame by frame, with no output-language decoder (so it cannot translate)."""
import argparse, json, os, time, torch, soundfile as sf
from transformers import AutoProcessor, Wav2Vec2ForCTC
from common import MANIFEST, DATA, RESULTS

ap = argparse.ArgumentParser(); ap.add_argument("model"); ap.add_argument("adapter"); ap.add_argument("tag"); ap.add_argument("--sets", required=True)
a = ap.parse_args()
rows = [json.loads(l) for l in open(MANIFEST) if json.loads(l)["set"] in a.sets.split(",")]
out = os.path.join(RESULTS, f"hyp_{a.tag}.jsonl")
done = {json.loads(l)["id"] for l in open(out)} if os.path.exists(out) else set()
todo = [r for r in rows if r["id"] not in done]
print(f"{a.tag}: {len(todo)} to do ({len(done)} done)", flush=True)
proc = AutoProcessor.from_pretrained(a.model, target_lang=a.adapter)
m = Wav2Vec2ForCTC.from_pretrained(a.model, target_lang=a.adapter, ignore_mismatched_sizes=True)
m.load_adapter(a.adapter); m = m.to("mps").eval()
t0 = time.time()
with open(out, "a") as f:
    for i, r in enumerate(todo):
        w, _ = sf.read(os.path.join(DATA, r["path"]))
        x = proc(w, sampling_rate=16000, return_tensors="pt").to("mps")
        with torch.no_grad(): ids = m(**x).logits.argmax(-1)[0]
        hyp = proc.decode(ids).strip()
        f.write(json.dumps(dict(id=r["id"], set=r["set"], model=a.model, tag=a.tag, tgt_lang=a.adapter, hyp=hyp)) + "\n"); f.flush()
        if (i + 1) % 100 == 0: print(f"{a.tag}: {i+1}/{len(todo)} ({time.time()-t0:.0f}s)", flush=True)
print(f"{a.tag}: DONE {len(todo)} in {time.time()-t0:.0f}s", flush=True)
