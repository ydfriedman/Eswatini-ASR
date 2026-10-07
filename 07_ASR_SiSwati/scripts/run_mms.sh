#!/bin/zsh
# Follow-up: CTC models (no output-language decoder). Simba-M = MMS-1b-all fine-tuned incl. siSwati; MMS zul = stock MMS (no ssw adapter exists).
set -e
PY=../../.venv_asr/bin/python; HUB=~/.cache/huggingface/hub
until grep -q "SIMBAW DONE" ../results/run_simbaw.log || grep -qE "^exit [1-9]" ../results/run_simbaw.log; do sleep 30; done
SSW=ssw_real_nchlt,ssw_tts_control,cs_tts
$PY run_ctc.py UBC-NLP/Simba-M multilingual_african simba_m --sets $SSW
rm -rf $HUB/models--UBC-NLP--Simba-M; echo "deleted simba-m"
$PY run_ctc.py facebook/mms-1b-all zul mms_zul --sets $SSW
rm -rf $HUB/models--facebook--mms-1b-all; echo "deleted mms"
echo "MMS DONE"
