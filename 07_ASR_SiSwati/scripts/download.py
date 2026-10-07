"""Download source data + models. Large model weights go to the HF cache."""
from huggingface_hub import hf_hub_download, snapshot_download
import os, tarfile
D = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
os.makedirs(D, exist_ok=True)
for f in ["asr_test/HF_test-ssw*NCHTL.parquet", "asr_test/HF_test-ssw*Lwazi.parquet"]:
    p = hf_hub_download("UBC-NLP/SimbaBench_dataset", f, repo_type="dataset", local_dir=D); print(p)
for split in ["train", "dev", "test"]:
    t = hf_hub_download("intronhealth/afrispeech-200", f"audio/siswati/{split}/{split}_siswati_0.tar.gz", repo_type="dataset", local_dir=D)
    c = hf_hub_download("intronhealth/afrispeech-200", f"transcripts/siswati/{split}.csv", repo_type="dataset", local_dir=D)
    out = os.path.join(D, "afrispeech_siswati", split); os.makedirs(out, exist_ok=True)
    with tarfile.open(t) as tf: tf.extractall(out)
    print(t, c)
snapshot_download("UBC-NLP/Simba-TTS-xho"); print("tts ok")
