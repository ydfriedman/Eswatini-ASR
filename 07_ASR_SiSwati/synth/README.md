# synth/

- `grammar.py`, `make_corpus.py`: round-2 prototype (hard-coded prefixes, segment-wise Xhosa/MMS TTS).
- `morph.py`, `lexicon.py`, `textgen.py`, `test_textgen.py`: **morphotactic text generator** (no audio). Produces
  `../data/synth_text/cs_text.jsonl` with `text`, `tagged` (English in `[[ ]]`), `segments` (for TTS), `switch_type`, `split`.
  Regenerate: `python textgen.py --n 2000 --out ../data/synth_text --seed 0`; test: `python test_textgen.py`.

## What is modelled
Noun-class prefix from the loan's class (`i-/ema-`), concord/possessive/demonstrative/`new` agreement from that class, English verb
stems under `ku-`/`u-`, function prefixes on English stems (`ne-`, `nge-`, `ku-`, `kwe-`, `se-`), and nine logged sentence types:
`mono_ssw`, `mono_eng`, `insertion`, `dm_initial`, `conj_inter`, `multi` (3+ segments), `alternational`, `eng_first`, `tag`.
Train/val are split by clause / source sentence, so nothing in val appears in train.

## Evidence used (all aggregate; raw data is gitignored under `data/raw/`)
- **Real siSwati text** (SADiLaR Autshumato Monolingual + Bilingual EN-SS corpora, CC BY 4.0; 2.2M tokens). `scripts/mine_loans.py` ->
  `data/synth_text/loan_evidence.tsv`, `loan_prefix_totals.json`. Findings: loans take `i-`/`ema-` (5,419 / 916 prefixed forms) and
  almost never `ti-` (2), so the earlier 9/10 guesses were dropped; hyphenation (`i-form`, `ku-website`, `se-asthma`) is the dominant
  convention; only 26 of 75 generator stems appear at all (the corpus is formal/government text, thin on clinical vocabulary); real
  writers also respell many loans (`ajenda`, `akhawunti`, `inthanethi`) - **not modelled yet**.
- **Soap-opera English-isiZulu transcripts** (SADiLaR, licence "Research only"; see below). `scripts/cs_stats.py` ->
  `data/synth_text/soap_engzul_stats.json` (aggregates only): 40% of utterances mixed, 47% isiZulu-only, 13% English-only; 48% of mixed
  utterances have 3+ language segments; 55% of English segments are one word, 23% two to three; most frequent English words are
  `and so right but sure no okay if or`. `MODES` weights and the DM/conjunction lists were set from this. Caveat: that subset is
  *balanced* by construction (equal English and Bantu), so its English share overstates natural speech.
- `mono_ssw` / `mono_eng` utterances are real short sentences from the CC BY 4.0 corpora (formal register).

## Respelling and real-sentence swaps
- **Nativised forms** (`lexicon.NATIVISED`, probability `P_NATIVE`=0.5): for doctor/hospital/condom/cancel the real text overwhelmingly prefers the
  siSwati-spelled loan (`dokotela` 269 vs English 2; `sibhedlela`/`tibhedlela`/`esibhedlela` 329 vs `hospital` 6). Evidence in
  `data/synth_text/native_evidence.tsv`. Written text is formal; spoken clinic speech likely uses more English, hence 0.5, not 1.0.
  `scripts/mine_respell.py` -> `data/synth_text/respell_pairs.tsv` mines 138 further nativised pairs (English word <-> aligned siSwati form) from the
  aligned corpus, but they are mostly government terms and place names and include errors: **candidates for review, not used by the generator**.
- **Real-sentence swaps** (`realswitch.py` -> `data/synth_text/real_swaps.jsonl`, 984 sentences, 109 distinct nouns): a real siSwati sentence, one noun
  replaced by English when (a) the Autshumato dictionary (CC BY 2.5 ZA) maps that siSwati noun to exactly one English word and (b) that word is
  in the aligned English sentence at a similar relative position. Concords are untouched (the writer's own); the English noun takes the replaced
  noun's prefix (`i-`, `ema-`, `bo-`). Ambiguous classes (`um-`, `imi-`, `si-`, `tin-`) are skipped. Limits: formal government register, mostly
  singular `i-` nouns (973 of 984), dictionary sense errors still slip through (e.g. check `real_swaps.jsonl` `swapped` column), and real speakers
  do not necessarily switch on nouns like "policy" or "waste". Use as extra siSwati-side realism, not as a model of switching behaviour.

## Licence note: soap-opera corpus
SADiLaR record `20.500.12185/545` carries only `Research only.` (the bundled license.txt is the depositor's grant to SADiLaR, not user
terms). Use is therefore limited to research; do not release weights or a product trained on it without written permission from the
corpus owners (contact: Thomas Niesler, Stellenbosch). Audio for the English-isiZulu subset (5.45 h, 9,371 clips, 32 kHz) is downloaded
to `data/raw/soapies_engzul/` (gitignored). Do not commit it.

## What is NOT verified (read before training on it)
- **No native-speaker review of any siSwati.** Person-noun class (`1a/2a`), the concord table, clause templates and day/duration phrases
  are unreviewed. Review sheets: `../data/synth_text/review_sample.tsv` and `review_lexicon.tsv`. `loan_evidence.tsv` shows which stems
  have corpus support.
- The generator's English vocabulary is clinic-flavoured; the real soap-opera English is conversational. Switch statistics come from
  an isiZulu drama corpus, not siSwati clinic speech.
- The TTS step is not run here (no GPU/torch). `segments[].glue_next` marks a prefix that must be voiced with the following English stem.
