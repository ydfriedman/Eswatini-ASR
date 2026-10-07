"""LoRA fine-tune Simba-S (SeamlessM4T-v2 speech-to-text, 1.5B) on code-switched speech, with optional synthetic and replay data.
Labels follow Simba-S inference (no language tag): decoder input = </s> + text, target = text + </s>.

Example (conditions used in the experiment, see README.md):
  B  python train_lora.py --name B_soapies                 --soapies ../data/manifest_soapies_engzul.jsonl
  C  python train_lora.py --name C_soapies_replay          --soapies ... --replay ../data/manifest_nchlt_train.jsonl --replay_n 1500
  D  python train_lora.py --name D_soapies_replay_synth    --soapies ... --replay ... --synth ../data/synth/manifest.jsonl --synth_n 1500
Defaults target a single 24 GB GPU or an M4 with >=24 GB (use --dtype bf16 on CUDA; fp32 may be needed on MPS). Smoke test: --max_steps 2 --bs 1.
Writes runs/<name>/{adapter/, config.json, log.csv}. Only decoder attention is adapted by default (--lora_encoder adds the speech encoder)."""
import argparse, csv, json, math, os, random, sys, time
import numpy as np, soundfile as sf, torch
from transformers import AutoProcessor, SeamlessM4Tv2ForSpeechToText
from peft import LoraConfig, get_peft_model
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
from common import normalize

ap = argparse.ArgumentParser()
ap.add_argument("--name", required=True); ap.add_argument("--base", default="UBC-NLP/Simba-S")
ap.add_argument("--soapies", required=True); ap.add_argument("--replay", default=None); ap.add_argument("--replay_n", type=int, default=0)
ap.add_argument("--synth", default=None); ap.add_argument("--synth_n", type=int, default=0)
ap.add_argument("--train_key", default="split_v2", help="soapies split field; training rows are those == train, dev rows == dev")
ap.add_argument("--epochs", type=float, default=3.0); ap.add_argument("--max_steps", type=int, default=0)
ap.add_argument("--bs", type=int, default=4); ap.add_argument("--grad_accum", type=int, default=4); ap.add_argument("--lr", type=float, default=1e-4)
ap.add_argument("--warmup", type=int, default=50); ap.add_argument("--lora_r", type=int, default=16); ap.add_argument("--lora_alpha", type=int, default=32)
ap.add_argument("--lora_dropout", type=float, default=0.05); ap.add_argument("--lora_encoder", action="store_true")
ap.add_argument("--dtype", default="auto", choices=["auto", "fp32", "bf16"]); ap.add_argument("--device", default="auto")
ap.add_argument("--eval_every", type=int, default=100); ap.add_argument("--dev_n", type=int, default=200); ap.add_argument("--seed", type=int, default=0)
ap.add_argument("--no_ckpt", action="store_true", help="disable gradient checkpointing"); ap.add_argument("--out_root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs"))
a = ap.parse_args()
random.seed(a.seed); np.random.seed(a.seed); torch.manual_seed(a.seed)
dev = a.device if a.device != "auto" else ("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
dt = torch.bfloat16 if (a.dtype == "bf16" or (a.dtype == "auto" and dev in ("cuda", "cpu"))) else torch.float32
out = os.path.join(a.out_root, a.name); os.makedirs(out, exist_ok=True)

def load(path, split=None, key=None, n=0, root=None):
    root = root or os.path.dirname(os.path.abspath(path)); rows = []
    for r in map(json.loads, open(path)):
        if split and r.get(key, r.get("split")) != split: continue
        rows.append(dict(path=os.path.join(root, r["path"]), text=normalize(r["ref"]), dur=r.get("duration", 0), src=r.get("set", os.path.basename(path))))
    rows = [r for r in rows if r["text"] and 0.3 <= r["dur"] <= 30]
    if n and n < len(rows): rows = random.Random(a.seed).sample(rows, n)
    return rows
train = load(a.soapies, "train", a.train_key)
if a.replay and a.replay_n: train += load(a.replay, n=a.replay_n)
if a.synth and a.synth_n: train += load(a.synth, "train", "split", a.synth_n)
devset = load(a.soapies, "dev", a.train_key); random.Random(1).shuffle(devset); devset = devset[:a.dev_n]
print(f"train {len(train)} clips ({sum(r['dur'] for r in train)/3600:.2f} h): " + str({s: sum(r['src'] == s for r in train) for s in {r['src'] for r in train}}) + f" | dev {len(devset)} | {dev}/{dt}", flush=True)

proc = AutoProcessor.from_pretrained(a.base); tok = proc.tokenizer
model = SeamlessM4Tv2ForSpeechToText.from_pretrained(a.base, dtype=dt)
pat = r".*text_decoder\.layers\.\d+\.(self_attn|cross_attention)\.(q_proj|v_proj)"
if a.lora_encoder: pat = f"({pat})|(.*speech_encoder\\.encoder\\.layers\\.\\d+\\.self_attn\\.(linear_q|linear_v))"
model = get_peft_model(model, LoraConfig(r=a.lora_r, lora_alpha=a.lora_alpha, lora_dropout=a.lora_dropout, target_modules=pat))
model.print_trainable_parameters()
if not a.no_ckpt: model.base_model.model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
model.to(dev)
EOS = model.base_model.model.config.eos_token_id

def batchify(rows):
    wavs = [sf.read(r["path"], dtype="float32")[0] for r in rows]
    x = proc.feature_extractor(wavs, sampling_rate=16000, return_tensors="pt", padding=True)   # works on transformers 4.x and 5.x (processor kwarg was renamed audios->audio)
    ids = [tok(r["text"], add_special_tokens=False).input_ids + [EOS] for r in rows]
    L = max(map(len, ids)); lab = torch.full((len(ids), L), -100, dtype=torch.long)
    for i, s in enumerate(ids): lab[i, :len(s)] = torch.tensor(s)
    return {"input_features": x["input_features"].to(dev, dt), "attention_mask": x["attention_mask"].to(dev), "labels": lab.to(dev)}

@torch.no_grad()
def dev_loss():
    model.eval(); tot, n = 0.0, 0
    for i in range(0, len(devset), a.bs):
        b = batchify(devset[i:i + a.bs]); tot += model(**b).loss.item() * len(devset[i:i + a.bs]); n += len(devset[i:i + a.bs])
    model.train(); return tot / max(1, n)

steps_per_epoch = math.ceil(len(train) / (a.bs * a.grad_accum)); total = a.max_steps or int(steps_per_epoch * a.epochs)
params = [p for p in model.parameters() if p.requires_grad]
opt = torch.optim.AdamW(params, lr=a.lr, weight_decay=0.0)
sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda s: min(1.0, (s + 1) / max(1, a.warmup)) * max(0.0, 0.5 * (1 + math.cos(math.pi * min(1.0, s / max(1, total))))))
json.dump({**vars(a), "n_train": len(train), "n_dev": len(devset), "total_steps": total, "device": dev, "dtype": str(dt)}, open(os.path.join(out, "config.json"), "w"), indent=1)
logf = open(os.path.join(out, "log.csv"), "w", newline=""); lw = csv.writer(logf); lw.writerow(["step", "train_loss", "dev_loss", "lr", "seconds"])
best, step, t0, run = 1e9, 0, time.time(), []
model.train(); order = []
while step < total:
    if len(order) < a.bs * a.grad_accum: order += random.sample(range(len(train)), len(train))
    for _ in range(a.grad_accum):
        idx, order = order[:a.bs], order[a.bs:]
        loss = model(**batchify([train[i] for i in idx])).loss / a.grad_accum; loss.backward(); run.append(loss.item() * a.grad_accum)
    torch.nn.utils.clip_grad_norm_(params, 1.0); opt.step(); sched.step(); opt.zero_grad(set_to_none=True); step += 1
    dl = ""
    if step % a.eval_every == 0 or step == total:
        dl = dev_loss()
        if dl < best: best = dl; model.save_pretrained(os.path.join(out, "adapter"))
    lw.writerow([step, round(float(np.mean(run)), 4), dl if dl == "" else round(dl, 4), f"{sched.get_last_lr()[0]:.2e}", round(time.time() - t0)]); logf.flush()
    if step % 10 == 0 or dl != "" or step <= 3: print(f"step {step}/{total} train {np.mean(run[-a.grad_accum*10:]):.3f} dev {dl} ({time.time()-t0:.0f}s)", flush=True)
if not os.path.exists(os.path.join(out, "adapter")): model.save_pretrained(os.path.join(out, "adapter"))
model.save_pretrained(os.path.join(out, "adapter_last")); print(f"DONE best dev loss {best:.4f}; adapter at {out}/adapter", flush=True)
