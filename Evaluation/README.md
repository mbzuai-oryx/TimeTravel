# Evaluation Scripts for Vision-Language Model (VLM)

This repository contains Python scripts for evaluating Vision-Language Model (VLM) generated descriptions using various NLP metrics.

## Installation
Install required dependencies:
```bash
pip install nltk torch bert-score tqdm pycocoevalcap pandas openai
```

## Usage

### BLEU, ROUGE, SPICE, BERTScore Evaluation
Run:
```bash
python bleu-Rouge-spice-bert-evaluation.py
```
**Inputs:**
- `ground_truth_description.json`
- `vlm_response.json`

**Outputs:**
- `test.txt` (evaluation scores)

### Judge LLM Evaluation
Run:
```bash
python judge-llm-evaluation.py
```
**Inputs:**
- `ground_truth_description.json`
- `vlm_response.json`

**Outputs:**
- `results.json` (GPT-4 similarity scores)

### METEOR Evaluation
Run:
```bash
python meteor-evaluation.py
```
**Inputs:**
- `ground_truth_description.json`
- `response.json`

**Outputs:**
- `scores.csv` (METEOR scores)


