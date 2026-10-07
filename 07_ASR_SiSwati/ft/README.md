# Fine-tuning experiment: does code-switched fine-tuning of Simba-S help? (exploratory)

**Purpose.** A cheap first look at whether the code-switching work so far justifies a more rigorous study. It is *not* a siSwati-English
result: the only real code-switched audio we have is **isiZulu-English** (soap operas, research-only licence). It can show whether Simba-S can
learn code-switched acoustics from a few hours of real data, whether it keeps its siSwati, and whether our synthetic data adds anything.

## What exists and what has been run
| Piece | File | Status |
|---|---|---|
| LoRA fine-tune (decoder attention; `--lora_encoder` optional) | `train_lora.py` | plumbing tested on a tiny random model (loss/lr/adapter save OK). **Not run on real weights.** |
| Transcribe base / adapter, greedy, no lang tag | `transcribe.py` | plumbing tested the same way. Not run on real weights. |
| Scorer: WER, English-vs-isiZulu word errors, speaker-bootstrap CIs, paired diffs | `score_cs.py` | tested on the tiny model's output. |
| Soap-opera data | `../scripts/prep_soapies.py` | **run**: 8,953 clips, 5.4 h |
| Synthetic audio | `../synth/tts_from_text.py` | plumbing tested with a stub TTS (glue/gap/manifest logic). Real TTS not run. |
| siSwati replay set | `../scripts/prep_nchlt_replay.py` | written, not run |
| Whole chain with random weights | `smoke_test.py` | passes |

Blocker: this sandbox can reach `huggingface.co` but not the CDN hosts that serve model/audio files (`cdn-lfs.hf.co`, `us.aws.cdn.hf.co`,
`cas-server.xethub.hf.co`, possibly `*.hf.co`). Weights (Simba-S 6 GB, TTS models) therefore could not be downloaded here, and there is no GPU
(4 CPUs, 15 GB RAM) - run the steps below on your M4 / a rented GPU, or allow those hosts and the CPU baseline (A) can run here.

## Conditions
| | Training data | Question it answers |
|---|---|---|
| A | none (zero-shot Simba-S) | baseline on soap-opera test, NCHLT test, cs_tts, AfriSpeech |
| B | soap-opera train (4.5 h, real isiZulu-English) | can real code-switched data move the needle? |
| C | B + 1,500 NCHLT siSwati clips (replay) | does replay prevent forgetting siSwati? |
| D | C + 1,500 synthetic utterances (morphotactic text -> TTS) | does our synthetic data add anything on top of real data? |

Evaluate every condition on: **soap-opera test** (765 clips, 17 held-out speakers, `score_cs.py`), **NCHLT test** (existing `ssw_real_nchlt`, 500 clips:
forgetting check; A = 19.1% WER), the earlier **cs_tts** set (40 synthetic siSwati-English clips: weak siSwati-side signal) and **AfriSpeech siSwati-accent English** (96 clips).

## Commands
```
pip install torch transformers peft accelerate sentencepiece jiwer soundfile soxr pandas   # transformers 4.57 and 5.x both work
python ../scripts/prep_soapies.py            # needs data/raw/soapies_engzul (see synth/README.md)
python ../scripts/prep_nchlt_replay.py --n 1500
python ../synth/tts_from_text.py --n 1500 --out ../data/synth --device cuda
python transcribe.py --manifest ../data/manifest_soapies_engzul.jsonl --split test --tag A_base            # add --subset 150 for a quick look
python train_lora.py --name B --soapies ../data/manifest_soapies_engzul.jsonl
python train_lora.py --name C --soapies ../data/manifest_soapies_engzul.jsonl --replay ../data/manifest_nchlt_train.jsonl --replay_n 1500
python train_lora.py --name D --soapies ../data/manifest_soapies_engzul.jsonl --replay ../data/manifest_nchlt_train.jsonl --replay_n 1500 --synth ../data/synth/manifest.jsonl --synth_n 1500
for c in B C D; do python transcribe.py --manifest ../data/manifest_soapies_engzul.jsonl --split test --tag $c --adapter runs/$c/adapter; done
python score_cs.py --manifest ../data/manifest_soapies_engzul.jsonl --hyp ../results/ft_hyp_A_base.jsonl --hyp ../results/ft_hyp_B.jsonl --hyp ../results/ft_hyp_C.jsonl --hyp ../results/ft_hyp_D.jsonl --out ../results/ft_scores.csv
```
For NCHLT / AfriSpeech / cs_tts (the earlier eval sets, scored by `../scripts/score.py`):
`python transcribe.py --manifest ../data/manifest.jsonl --split all --sets ssw_real_nchlt,cs_tts,eng_real_afrispeech_sswaccent --tag C --adapter runs/C/adapter --legacy && python ../scripts/score.py`
Cost (unmeasured estimate): one LoRA run is roughly an hour on a 24 GB GPU; the CPU baseline over 765 clips is a few hours on 4 cores.

## Decision rules (fixed before looking at results)
The work "suggests a more rigorous approach is worthwhile" if:
1. **B beats A** on soap-opera test by >=20% relative WER, paired speaker-bootstrap CI excluding 0 (real CS data helps at all);
2. **C stays within 2 absolute WER points of A on NCHLT test** (siSwati not forgotten);
3. **D beats C** on soap-opera test, paired CI excluding 0. If not, synthetic audio is not yet earning its keep and the investment should go to real siSwati-English recordings instead.
Also read the English-word and isiZulu-word error rates separately: gains confined to one language side mean something different from overall gains.

## Caveats you must carry into any write-up
- isiZulu-English is not siSwati-English; there is **no real siSwati-English test set**. The decisive test is a small set of real siSwati-English recordings (e.g. EBIS, with permission, native-speaker transcribed).
- Soap-opera data is research-only: adapters trained on it must not be released or shipped; keep them internal.
- Synthetic siSwati audio uses a Xhosa voice; the earlier round showed this voice dominates error (115% WER on TTS vs 19% on real speech). Condition D may therefore teach TTS artifacts.
- Only 17 test speakers: CIs are wide; resampling is by speaker. Single training seed per condition.
- All siSwati in the synthetic text is unreviewed by a native speaker.
