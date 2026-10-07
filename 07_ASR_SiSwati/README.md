# SiSwati ASR evaluation: Simba-S vs SeamlessM4T-v2

> **Superseded by the round-2 report:** `report/SiSwati_ASR_Evaluation.docx` (adds Whisper-large-v3, Simba-W, Simba-M, MMS, a 2,835-clip Zulu-accent English set, and a proposed Eswatini clinic test set for evaluating Intron Health). Rebuild with `scripts/report_tables.py`, `scripts/figures.py`, then `node report/build_report.js`. The round-1 notes below remain accurate for the models they cover.

Run 2026-09-25 on an Apple M4 (MPS, fp16, greedy decoding for every condition).

## Question

How well do two open ASR models transcribe (1) SiSwati-accented English, (2) siSwati, and (3) siSwati–English code-switched speech?

- **UBC-NLP/Simba-S**: SeamlessM4T-v2 speech-to-text fine-tuned on SimbaBench, which covers 43 African languages including siSwati (`ssw`). It was not fine-tuned on English. It is called with no language tag, as its model card does.
- **facebook/seamless-m4t-v2-large**: has **no siSwati support**. For siSwati and code-switched audio it runs with `tgt_lang="zul"` (Zulu, the closest supported language). For English audio it runs with `tgt_lang="eng"`. The code-switched set is also run with `tgt_lang="eng"`.

## Evaluation sets

| Set | Audio | n | Minutes | Notes |
|---|---|---|---|---|
| `ssw_real_nchlt` | **Real** siSwati: NCHLT test split (via SimbaBench) | 500 | 34.8 | Read prompts, about 3 words each. Simba-S was trained on the NCHLT *train* split. Speakers are disjoint, but NCHLT reuses prompts, so this set favours Simba-S. |
| `eng_real_afrispeech_sswaccent` | **Real** SiSwati-accented English: AfriSpeech-200 `siswati` accent (all splits) | 96 | 22.8 | 5 speakers, one of whom accounts for 58 clips. Mostly clinical text. Out-of-domain for both models. |
| `cs_tts` | **Synthetic** code-switched: 40 authored siSwati-matrix sentences with English insertions (clinic domain), voiced by Simba-TTS-xho | 40 | 2.4 | No real siSwati–English code-switched corpus and no siSwati TTS exist; Xhosa is the nearest Nguni voice available. **Sentences were written by Claude and have not been checked by a native speaker.** |
| `ssw_tts_control` | Same Xhosa TTS voice reading 40 NCHLT test sentences | 40 | 1.8 | Same text as real clips, so real vs synthetic can be compared directly |
| `eng_tts_control` | Same Xhosa TTS voice reading 40 AfriSpeech English sentences | 40 | 4.4 | Control for TTS voice on English |

Excluded: SimbaBench's `HF_test-ssw*Lwazi.parquet` is **mislabelled — its content is Afrikaans**, not siSwati.

## Results

WER and CER are corpus-level, with 95% bootstrap CIs over utterances. Normalisation: lowercase, punctuation stripped, hyphens split, NCHLT `[s]` noise tags removed.

| Set | Model (target) | WER [95% CI] | CER | Exact match | Empty output |
|---|---|---|---|---|---|
| **siSwati (real)** | Simba-S | **19.1%** [17.0–21.3] | **3.0%** | 57% | 0% |
| | Seamless (zul) | 88.0% [83.7–92.4] | 23.5% | 5% | 0% |
| **SiSwati-accented English (real)** | Simba-S | 43.9% [37.4–51.0] | 26.6% | 2% | **8.3%** |
| | Seamless (eng) | **37.7%** [31.8–44.4] | **22.7%** | 3% | 0% |
| **Code-switched (TTS)** | Simba-S | 94.3% [85.8–102] | **39.3%** | 0% | 0% |
| | Seamless (zul) | **85.7%** [75.2–96.1] | 42.3% | 5% | 0% |
| | Seamless (eng) | 141% | 80.8% | 0% | 0% |
| siSwati TTS control | Simba-S | 115% | 27.6% | 5% | 0% |
| | Seamless (zul) | 124% | 37.8% | 5% | 0% |
| English TTS control | Simba-S | 83.2% | 51.5% | 0% | 0% |
| | Seamless (eng) | 83.0% | 45.4% | 0% | 0% |

**Paired differences** (Simba-S minus Seamless on the same clips; negative means Simba-S is better; CIs from bootstrap):
- Real siSwati: WER −68.8 pts [−73.4, −64.6]; CER −20.5 pts. Clear win for Simba-S.
- Real accented English: WER +6.2 pts [−1.1, +14.4]. Seamless is better, but not significantly with 96 clips from 5 speakers.
- Code-switched: WER +8.6 pts [−1.7, +20.0]; CER −3.0 pts [−8.3, +2.2]. Neither model is reliably better; both fail.

**Code-switched set, by word language** (share of reference words not recovered exactly):

| Model | English words (n=67) | siSwati words (n=177) |
|---|---|---|
| Simba-S | 97% | 81% |
| Seamless (zul) | 91% | 73% |
| Seamless (eng) | 93% | 99% |

A lenient English score (spoken "comma"/"full stop" removed, and the 21 references containing digits dropped) gives Simba-S 40.4% vs Seamless 30.7%.

## Findings

1. **For siSwati itself, Simba-S is far better.** On read NCHLT speech it gets 19% WER and 3% CER. Most of its errors are single letters within otherwise correct words, e.g. *batekelwa → badekelwa*. This is an upper bound: the text is short read prompts that Simba-S has probably seen in training. Expect worse on spontaneous clinic speech.
2. **SeamlessM4T-v2 does not transcribe siSwati; it translates it into Zulu.** Examples: *utsite ngitsatse → uthi ngithathe*, *le medication → imithi*. Its CER is moderate (23%), but that is because siSwati and Zulu are closely related, not because it is producing siSwati text.
3. **On SiSwati-accented English, Seamless is modestly better, and Simba-S sometimes outputs nothing.** Simba-S returned an empty transcript for 8 of 96 clips (8%), consistently across fp16/fp32 and greedy/beam decoding. It was not fine-tuned on English. Both models struggle with medical vocabulary (e.g. *phyllodes tumour, fibroadenoma*), which accounts for much of the roughly 40% WER.
4. **Neither model handles code-switching.** English words inside siSwati sentences are almost never recovered (91–97% error). Simba-S turns them into siSwati-sounding strings (*blood test → haibolo tesɛ*). Seamless-zul translates or drops them. Seamless-eng translates the whole utterance into English. Occasionally both models hallucinate unrelated English.
5. **The synthetic-audio results need a large caveat.** On *identical text*, Simba-S gets 19% WER on real speech and 115% on TTS (CER 3% vs 28%). The Xhosa voice's mispronunciation of siSwati dominates the synthetic sets. Code-switched CER (39–42%) is only modestly worse than the siSwati TTS control (28–38%). So the code-switching penalty cannot be cleanly separated from TTS artifacts. This set is useful only as a qualitative check of failure modes. **Real code-switched recordings are needed for a quantitative answer.**
6. Simba-S sometimes outputs non-Latin letters (ɛ, ɔ), apparently carried over from other African languages in its training data. A post-filter or constrained vocabulary would help in production.

## Limitations

- Small English (96 clips, 5 speakers, one dominant) and code-switched (40) sets; CIs are wide.
- The code-switched text was authored without native-speaker review, and the TTS voice is Xhosa, not siSwati.
- NCHLT is read speech. Some AfriSpeech references have fused words (e.g. "theinfluence"), and readers voiced digits and punctuation.
- Greedy decoding only. Other Simba variants (W/X/M/H), Whisper, and Meta's Omnilingual ASR (which lists `ssw`) were not tested.

## Suggested next steps

1. **Record real code-switched audio**: 30–60 minutes of clinic-style siSwati–English from a few Eswatini speakers, ideally reading, then paraphrasing, the `data/codeswitch_sentences.tsv` prompts after a native speaker corrects them. That is the only way to get a trustworthy code-switching number.
2. Add Omnilingual ASR and Simba-W/M as further baselines.
3. If code-switched ASR matters for the product, the strongest option is probably to fine-tune Simba-S on a small real code-switched set plus English (to fix the empty outputs).

## Reproduce

```
../.venv_asr/bin/python scripts/download.py
cd scripts
../../.venv_asr/bin/python prep_data.py                      # -> data/manifest.jsonl, data/audio/
../../.venv_asr/bin/python run_asr.py UBC-NLP/Simba-S simba_s
../../.venv_asr/bin/python run_asr.py facebook/seamless-m4t-v2-large seamless_zul --tgt_lang zul --sets ssw_real_nchlt,ssw_tts_control,cs_tts
../../.venv_asr/bin/python run_asr.py facebook/seamless-m4t-v2-large seamless_eng --tgt_lang eng --sets eng_real_afrispeech_sswaccent,eng_tts_control,cs_tts
../../.venv_asr/bin/python score.py
```

Outputs are in `results/`:
- `hyp_*.jsonl`: raw transcripts
- `per_utt.csv`
- `scores.csv`
- `paired_differences.csv`
- `cs_by_language.csv`
- `afrispeech_by_speaker.csv`

Environment: `.venv_asr` (Python 3.9, torch 2.8, transformers 4.57.6).

Data licences: NCHLT (CC-BY 3.0), AfriSpeech-200 (CC-BY-NC-SA 4.0), SimbaBench / Simba models (CC-BY 4.0).
