$ErrorActionPreference = 'Stop'
Write-Host 'Starting guideline chat at http://127.0.0.1:8000 (Ollama defaults: http://localhost:11434, llama3.1:8b, bge-m3:latest embeddings)'
Write-Host 'Questions, recent conversation and retrieved passages are sent to the ML server model.'
python "$PSScriptRoot/app.py"
