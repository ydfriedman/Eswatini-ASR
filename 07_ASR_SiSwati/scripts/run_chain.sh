#!/bin/zsh
# Whisper (plain + clinical prompt) on both accent sets, then Seamless + Simba-S on the Zulu-accent set.
# Each model's HF cache is deleted after its runs (disk is tight).
set -e
PY=../../.venv_asr/bin/python; HUB=~/.cache/huggingface/hub
ENG=eng_real_afrispeech_sswaccent,eng_real_afrispeech_zuluaccent
PROMPT="Clinical notes: The patient presented with hypertension, tachycardia and dyspnoea. Histology showed carcinoma with a lymphocytic infiltrate; treated with antibiotics and analgesics."
$PY run_asr.py openai/whisper-large-v3 whisper_v3 --tgt_lang en --sets $ENG
$PY run_asr.py openai/whisper-large-v3 whisper_v3_prompt --tgt_lang en --sets $ENG --prompt "$PROMPT"
rm -rf $HUB/models--openai--whisper-large-v3; echo "deleted whisper"
$PY -c "from huggingface_hub import snapshot_download as s; s('facebook/seamless-m4t-v2-large', allow_patterns=['*.json','*.safetensors','sentencepiece.bpe.model','tokenizer.model'])"
$PY run_asr.py facebook/seamless-m4t-v2-large seamless_eng --tgt_lang eng --sets eng_real_afrispeech_zuluaccent
rm -rf $HUB/models--facebook--seamless-m4t-v2-large; echo "deleted seamless"
$PY run_asr.py UBC-NLP/Simba-S simba_s --sets eng_real_afrispeech_zuluaccent
rm -rf $HUB/models--UBC-NLP--Simba-S; echo "deleted simba"
echo "CHAIN DONE"
