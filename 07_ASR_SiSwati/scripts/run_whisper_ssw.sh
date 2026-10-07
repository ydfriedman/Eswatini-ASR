#!/bin/zsh
# Follow-up: Whisper large-v3 (no siSwati support) on the siSwati + code-switched sets. Starts after run_chain.sh finishes.
set -e
PY=../../.venv_asr/bin/python; HUB=~/.cache/huggingface/hub
until grep -q "CHAIN DONE" ../results/run_chain.log || grep -qE "^exit [1-9]" ../results/run_chain.log; do sleep 30; done
SSW=ssw_real_nchlt,ssw_tts_control,cs_tts
$PY run_asr.py openai/whisper-large-v3 whisper_v3_auto --tgt_lang auto --sets $SSW
$PY run_asr.py openai/whisper-large-v3 whisper_v3_sw --tgt_lang sw --sets $SSW
rm -rf $HUB/models--openai--whisper-large-v3; echo "deleted whisper"
echo "SSW DONE"
