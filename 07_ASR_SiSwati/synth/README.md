# synth/

- `grammar.py`, `make_corpus.py`: round-2 prototype (hard-coded prefixes, segment-wise Xhosa/MMS TTS).
- `morph.py`, `lexicon.py`, `textgen.py`, `test_textgen.py`: **morphotactic text generator** (no audio). Produces
  `../data/synth_text/cs_text.jsonl` with `text`, `tagged` (English in `[[ ]]`), `segments` (for TTS), `switch_type`, `split`.
  Regenerate: `python textgen.py --n 2000 --out ../data/synth_text --seed 0`; test: `python test_textgen.py`.

## What is modelled
Noun-class prefix from the loan's class (`i-/ema-`, `i-/ti-`, `bo-`), concord/possessive/demonstrative/`new` agreement from
that class, English verb stems under `ku-`/`u-`, and six logged switch types (insertion, dm_initial, conj_inter,
alternational, eng_first, tag). Train/val are split by clause, so no clause in val appears in train.

## What is NOT verified (read before training on it)
- **No native-speaker review of any siSwati.** Class assignments (`lexicon.py`, `conf: guess`), concord tables (`morph.py`),
  clause templates and day/duration/relative phrases are the author's best attempt. Review sheets are generated:
  `../data/synth_text/review_sample.tsv` (120 sentences) and `review_lexicon.tsv` (every class assignment).
  Apply corrections in `lexicon.py` / `morph.py`, regenerate, retrain.
- English share is ~50% of words overall because alternational/eng_first sentences contain whole English clauses; tune
  `MODES` weights toward `insertion` if real data shows less English.
- Spelling of the English stem is unchanged ("ema-pills"). A siSwati-ised spelling for TTS is not implemented.
- The TTS step is not run here (no GPU/torch in this environment). `segments[].glue_next` marks a prefix that must be
  voiced together with the following English stem; the old `make_corpus.py` voices segments separately and would not do this.
