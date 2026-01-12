# Optical Digest Bot

A fully local, open-source pipeline that collects optical communications
industry news, filters for relevance, summarizes using an open LLM,
and produces a weekly digest automatically.

## Features
- RSS-based data collection
- Semantic relevance filtering
- Local LLM summarization (Mistral 7B via llama.cpp)
- Weekly digest generation
- Windows Task Scheduler compatible

## Stack
- Python
- SQLite
- sentence-transformers
- llama.cpp
- Mistral-7B-Instruct (GGUF)

## Usage
Run the full pipeline:

```bash
python run_weekly_pipeline.py


## Repository Notes

Model files, virtual environments, and local databases are excluded from
version control by design.

These artifacts are large, machine-specific, or runtime-generated and
should be recreated locally when running the pipeline.
