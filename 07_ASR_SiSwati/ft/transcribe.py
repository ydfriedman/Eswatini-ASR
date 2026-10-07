"""Transcribe a manifest split with Simba-S (or a LoRA-adapted copy). Greedy decoding, no language tag (as the Simba-S card). Resumable.
usage: python transcribe.py --manifest ../data/manifest_soapies_engzul.jsonl --split test --tag base [--adapter runs/B/adapter] [--subset 120]
Output: ../results/ft_hyp_<tag>.jsonl  ({id, hyp, tag})   device: cuda > mps > cpu"""
import argparse, json, os, random, sys, time
import soundfile as sf, torch
from transformers import AutoProcessor, SeamlessM4Tv2ForSpeechToText

ap = argparse.ArgumentParser()
ap.add_argument("--manifest", required=True); ap.add_argument("--data_root", default=None, help="dir that manifest paths are relative to (default: the manifest's own dir)")
ap.add_argument("--split", default="test", help="split value to keep, or 'all'"); ap.add_argument("--split_key", default="split_v2")
ap.add_argument("--sets", default=None, help="comma list of manifest `set` values to keep (for ../data/manifest.jsonl)")
ap.add_argument("--legacy", action="store_true", help="write results/hyp_<tag>.jsonl with set/tag fields so ../scripts/score.py picks it up")
ap.add_argument("--tag", required=True); ap.add_argument("--base", default="UBC-NLP/Simba-S"); ap.add_argument("--adapter", default=None)
ap.add_argument("--subset", type=int, default=0, help="stratified (by cs_type) subset size; 0 = all"); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--dtype", default="auto", choices=["auto", "fp32", "fp16", "bf16"]); ap.add_argument("--device", default="auto")
ap.add_argument("--out_dir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "results"))
a = ap.parse_args()

dev = a.device if a.device != "auto" else ("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
dt = {"fp32": torch.float32, "fp16": torch.float16, "bf16": torch.bfloat16}[a.dtype if a.dtype != "auto" else ("fp16" if dev in ("cuda", "mps") else "bf16")]
root = a.data_root or os.path.dirname(os.path.abspath(a.manifest))      # manifest paths are relative to its own directory (data/)
rows = [r for r in map(json.loads, open(a.manifest)) if a.split == "all" or r.get(a.split_key, r.get("split")) == a.split]
if a.sets: rows = [r for r in rows if r.get("set") in a.sets.split(",")]
if a.subset and a.subset < len(rows):      # stratified by cs_type so mixed/mono proportions are preserved; same subset for every condition (seeded)
    rng = random.Random(a.seed); by = {}
    for r in rows: by.setdefault(r.get("cs_type", ""), []).append(r)
    rows = [r for g in by.values() for r in rng.sample(g, max(1, round(a.subset * len(g) / len(rows))))]
    rows.sort(key=lambda r: r["id"])
os.makedirs(a.out_dir, exist_ok=True); out = os.path.join(a.out_dir, f"{'hyp' if a.legacy else 'ft_hyp'}_{a.tag}.jsonl")
done = {json.loads(l)["id"] for l in open(out)} if os.path.exists(out) else set()
todo = [r for r in rows if r["id"] not in done]
print(f"{a.tag}: {len(todo)} to do ({len(done)} done) on {dev}/{dt}", flush=True)

proc = AutoProcessor.from_pretrained(a.base)
m = SeamlessM4Tv2ForSpeechToText.from_pretrained(a.base, dtype=dt)
if a.adapter:
    from peft import PeftModel
    m = PeftModel.from_pretrained(m, a.adapter).merge_and_unload()
m = m.to(dev).eval(); t0 = time.time()
with open(out, "a") as f:
    for i, r in enumerate(todo):
        w, sr = sf.read(os.path.join(root, r["path"]), dtype="float32")
        x = proc.feature_extractor(w, sampling_rate=16000, return_tensors="pt").to(dev); x["input_features"] = x["input_features"].to(dt)   # 4.x/5.x-safe
        with torch.no_grad(): seq = m.generate(**x, num_beams=1, max_new_tokens=int(r["duration"] * 10) + 20)[0]
        f.write(json.dumps({"id": r["id"], "set": r.get("set"), "hyp": proc.tokenizer.decode(seq, skip_special_tokens=True).strip(), "tag": a.tag}, ensure_ascii=False) + "\n"); f.flush()
        if (i + 1) % 10 == 0: print(f"{a.tag}: {i+1}/{len(todo)} ({time.time()-t0:.0f}s)", flush=True)
print(f"{a.tag}: DONE {len(todo)} in {time.time()-t0:.0f}s", flush=True)
