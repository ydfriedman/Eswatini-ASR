"""End-to-end smoke test WITHOUT downloading model weights: tiny random SeamlessM4T-v2 speech-to-text + a tiny local sentencepiece
tokenizer, then train_lora.py (2 steps) -> transcribe.py (3 clips) -> score_cs.py. Checks plumbing, shapes and label handling only; the
numbers are meaningless. usage: python smoke_test.py [WORKDIR]   (needs data/manifest_soapies_engzul.jsonl and the config of UBC-NLP/Simba-S)"""
import json, os, subprocess, sys, tempfile
import sentencepiece as spm
from transformers import AutoConfig, SeamlessM4TFeatureExtractor, SeamlessM4TTokenizer, SeamlessM4TProcessor, SeamlessM4Tv2ForSpeechToText

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, "..", "data"); W = sys.argv[1] if len(sys.argv) > 1 else tempfile.mkdtemp()
man = os.path.join(DATA, "manifest_soapies_engzul.jsonl"); rows = [json.loads(l) for l in open(man)]
open(os.path.join(W, "text.txt"), "w").write("\n".join(r["ref"] for r in rows[:3000]))
spm.SentencePieceTrainer.train(input=os.path.join(W, "text.txt"), model_prefix=os.path.join(W, "sp"), vocab_size=300, model_type="bpe", pad_id=0, unk_id=1, bos_id=2, eos_id=3, character_coverage=1.0)
tok = SeamlessM4TTokenizer(vocab_file=os.path.join(W, "sp.model")); fe = SeamlessM4TFeatureExtractor()
proc = SeamlessM4TProcessor(feature_extractor=fe, tokenizer=tok)
cfg = AutoConfig.from_pretrained("UBC-NLP/Simba-S")
for k, v in dict(hidden_size=64, speech_encoder_layers=2, speech_encoder_attention_heads=4, speech_encoder_intermediate_size=128, decoder_layers=2, decoder_attention_heads=4,
                 decoder_ffn_dim=128, encoder_layers=1, encoder_attention_heads=4, encoder_ffn_dim=128, vocab_size=len(tok), adaptor_kernel_size=8, num_adapter_layers=1).items():
    if hasattr(cfg, k): setattr(cfg, k, v)
cfg.pad_token_id, cfg.eos_token_id, cfg.decoder_start_token_id = 0, 3, 3
m = SeamlessM4Tv2ForSpeechToText(cfg); m.generation_config.max_new_tokens = 20
tiny = os.path.join(W, "tiny"); m.save_pretrained(tiny); proc.save_pretrained(tiny)
sub = os.path.join(W, "sub.jsonl")                                   # 12 short train, 4 dev, 4 test clips, paths made absolute
short = [r for r in rows if r["duration"] < 4]
pick = [dict(r, split_v2=s, path=os.path.join(DATA, r["path"])) for s, g in (("train", [r for r in short if r["split_v2"] == "train"][:12]), ("dev", [r for r in short if r["split_v2"] == "dev"][:4]), ("test", [r for r in short if r["split_v2"] == "test"][:4])) for r in g]
open(sub, "w").write("\n".join(json.dumps(r) for r in pick))
py = sys.executable; env = dict(os.environ, PYTHONWARNINGS="ignore")
def run(*a): print("$", " ".join(a[1:])[:160], flush=True); subprocess.run(a, check=True, env=env)
run(py, os.path.join(HERE, "train_lora.py"), "--name", "smoke", "--base", tiny, "--soapies", sub, "--max_steps", "2", "--bs", "2", "--grad_accum", "1", "--eval_every", "1", "--dtype", "fp32", "--device", "cpu", "--out_root", W, "--no_ckpt", "--warmup", "1")
run(py, os.path.join(HERE, "transcribe.py"), "--manifest", sub, "--split", "test", "--tag", "smoke_base", "--base", tiny, "--dtype", "fp32", "--device", "cpu", "--out_dir", W)
run(py, os.path.join(HERE, "transcribe.py"), "--manifest", sub, "--split", "test", "--tag", "smoke_lora", "--base", tiny, "--adapter", os.path.join(W, "smoke", "adapter"), "--dtype", "fp32", "--device", "cpu", "--out_dir", W)
run(py, os.path.join(HERE, "score_cs.py"), "--manifest", sub, "--hyp", os.path.join(W, "ft_hyp_smoke_base.jsonl"), "--hyp", os.path.join(W, "ft_hyp_smoke_lora.jsonl"), "--boot", "50")
print("SMOKE TEST PASSED")
