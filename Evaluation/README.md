# Evaluation Scripts for TimeTravel

This repository contains Python scripts for evaluating TimeTravel.

## Description Generation Process
We used metadata in JSON format as input to GPT-4o to generate refined captions. Below is the system prompt used for description generation:

```
You are an expert in historical artifact documentation. Your task is to generate a refined and sophisticated description using all available details from the provided metadata while ensuring clarity and conciseness. The description should be structured as a single, well-crafted paragraph that seamlessly integrates key details.  

Begin by introducing the artifact, including its type, cultural origin, and production date. Provide a brief yet vivid physical description, mentioning its material, notable inscriptions, and distinctive features. If relevant, incorporate historical and cultural context, highlighting associated figures, events, or symbolic significance. Conclude with provenance details, including its findspot and any relevant excavation notes. Ensure the description flows naturally and remains scholarly yet accessible. Any missing or null values should be excluded without disrupting coherence. Keep the description informative yet concise, maintaining richness in detail while avoiding unnecessary elaboration.  
```

### Example:

#### Metadata Input:
```json
{
    "id":1,
    "Image":"..../media/Repository/Document/2014_10/15_10/preview_00926319_001.jpg",
    "Description":"Alloy coin.; Crude laureate ?draped and ?cuirassed bust of Gallienus viewed from back.; Triumphal arch with three portals. The two side portals each have a window above.",
    "Production date":"253-268",
    "Find spot":"Excavated/Findspot: Balkans (Probably - deduced by associated material.)",
    "Materials":"alloy",
    "Inscription":"Inscription type: inscription Inscription position: obverse Inscription language: Latin Inscription quoted: IMP LIC...AINNC Inscription note: garbled legend; Inscription type: inscription Inscription position: reverse exergue Inscription language: Latin Inscription quoted: (CGIHP) Inscription note: not fully visible - possibly retrograde?",
    "Subjects":"emperor/empress; arch/gateway",
    "Assoc name":"Named in inscription & portrayed: Gallienus",
    "Culture":"Roman Provincial",
    "Section":"roman",
    "Place":"roman empire",
    "image_path":"1.jpg"
}
```



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
- `vlm_response.json`

**Outputs:**
- `scores.csv` (METEOR scores)

