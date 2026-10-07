#!/bin/zsh
# Follow-up: Simba-W with English forced (no auto language-ID) on siSwati-accent set + random 300 Zulu-accent clips.
set -e
PY=../../.venv_asr/bin/python; HUB=~/.cache/huggingface/hub
until grep -q "MMS DONE" ../results/run_mms.log || grep -qE "^exit [1-9]" ../results/run_mms.log; do sleep 30; done
$PY run_asr.py UBC-NLP/Simba-W simba_w_en --tgt_lang en --sets eng_real_afrispeech_sswaccent,eng_real_afrispeech_zuluaccent --ids ../data/simba_w_en_subset.txt
rm -rf $HUB/models--UBC-NLP--Simba-W; echo "deleted simba-w"
echo "SIMBAW_EN DONE"
