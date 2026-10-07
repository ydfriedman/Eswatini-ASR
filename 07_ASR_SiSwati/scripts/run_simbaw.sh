#!/bin/zsh
# Follow-up: Simba-W (Whisper large-v3 fine-tuned on SimbaBench incl. siSwati), language auto-detect, all sets.
set -e
PY=../../.venv_asr/bin/python; HUB=~/.cache/huggingface/hub
until grep -q "SSW DONE" ../results/run_whisper_ssw.log || grep -qE "^exit [1-9]" ../results/run_whisper_ssw.log; do sleep 30; done
$PY run_asr.py UBC-NLP/Simba-W simba_w --tgt_lang auto --sets ssw_real_nchlt,ssw_tts_control,cs_tts,eng_real_afrispeech_sswaccent,eng_tts_control,eng_real_afrispeech_zuluaccent
rm -rf $HUB/models--UBC-NLP--Simba-W; echo "deleted simba-w"
echo "SIMBAW DONE"
