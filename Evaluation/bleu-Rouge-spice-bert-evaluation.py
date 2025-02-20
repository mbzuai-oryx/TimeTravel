# ============================
# This file contains the code to evaluate the generated descriptions using BLEU, ROUGE, SPICE, and BERTScore.
# The code is written in Python and uses the following libraries:
# - nltk
# - torch
# - pycocoevalcap
# - bert_score
# - tqdm
# - os
# - sys
# ============================



import json
import nltk
from nltk.tokenize import sent_tokenize
import torch
from pycocoevalcap.bleu.bleu import Bleu
from pycocoevalcap.rouge.rouge import Rouge
from pycocoevalcap.spice.spice import Spice
from bert_score import score
from tqdm import tqdm
import os
import sys  # in case we want sys.exit()

# ============================
# 1. Download nltk data and Load & Process Ground Truth Data
# ============================
nltk.download('punkt')

ground_truth_path = "/data2/ketan/history_project_subset_v2/datatset/ground_truth_description.json"
with open(ground_truth_path, "r", encoding="utf-8") as f:
    ground_truth_data = json.load(f)

# Sort by ID to ensure consistent ordering
ground_truth_data = sorted(ground_truth_data, key=lambda x: x["id"])

# Optionally split into sentences if you want each sentence as a separate reference
references = []
for item in ground_truth_data:
    if "description" in item and item["description"]:
        sentences = sent_tokenize(item["description"])
        references.append(sentences)
    else:
        # If no description is available, append an empty list
        references.append([])

# ============================
# 2. Load VLM-generated Descriptions
# ============================
vlm_response_path = "/data2/ketan/history_project_subset_v2/desciption_generation/response.json"
with open(vlm_response_path, "r", encoding="utf-8") as f:
    vlm_response_data = json.load(f)

vlm_response_data = sorted(vlm_response_data, key=lambda x: x["id"])

generated = []
for item in vlm_response_data:
    # Here we store the entire generated description as a single string
    # (unlike references which are split into sentences).
    if "description" in item and item["description"]:
        generated.append(item["description"])
    else:
        # If no description is available, store an empty string
        generated.append("")

# Ensure data consistency in length
assert len(references) == len(generated), (
    f"Mismatch between references ({len(references)}) and generated ({len(generated)}) descriptions!"
)

# Check if both datasets have the same IDs
gt_ids = {item["id"] for item in ground_truth_data}
vlm_ids = {item["id"] for item in vlm_response_data}

if gt_ids == vlm_ids:
    print("Both datasets have the exact same IDs.")
else:
    print("Mismatch in IDs between the datasets.")
    missing_in_gt = vlm_ids - gt_ids
    missing_in_vlm = gt_ids - vlm_ids
    print(f"IDs missing in ground truth dataset: {missing_in_gt}")
    print(f"IDs missing in VLM response dataset: {missing_in_vlm}")
    sys.exit(1)  # or exit()

# ============================
# 3. Prepare Data for COCO Evaluators
# ============================
gts = {}
res = {}
for i, (refs, hypo) in enumerate(zip(references, generated)):
    # refs is a list of reference strings (sentences)
    # Pycocoevalcap expects a list of reference strings per image
    gts[i] = refs
    # Single hypothesis for each image
    res[i] = [hypo]

# ============================
# 4. Evaluate Using COCO-based Metrics
# ============================
scorers = [
    (Bleu(1),     ["Bleu"]),
    (Rouge(),     "ROUGE_L"),
    (Spice(),     "SPICE"),
]

final_scores = {}

# Specify the path for the output text file.
output_file = "test.txt"

# Open the file once, and write partial results as you go.
with open(output_file, "w", encoding="utf-8") as f_out:
    # Optional: Write a header
    f_out.write("===== Partial Evaluation Scores =====\n\n")
    
    # Evaluate COCO-based metrics with a progress bar
    for scorer, method in tqdm(scorers, desc="Evaluating Metrics", unit="metric"):
        score_val, _ = scorer.compute_score(gts, res)
        
        # Some metrics like BLEU return a list of multiple sub-metrics (e.g. BLEU-1..BLEU-4)
        if isinstance(score_val, list):
            for m, s in zip(method, score_val):
                final_scores[m] = s
                # Write partial score to file
                f_out.write(f"{m}: {s:.4f}\n")
        else:
            final_scores[method] = score_val
            f_out.write(f"{method}: {score_val:.4f}\n")
        
        f_out.write("\n")
        f_out.flush()  # Ensure it's written to disk immediately
    
    # ============================
    # 5. Compute BERTScore (Multi-Reference Handling)
    # ============================
    flat_hyps = []
    flat_refs = []
    for refs, hypo in tqdm(zip(references, generated), total=len(generated), desc="Preparing BERTScore data"):
        # For each reference sentence, we replicate the hypothesis
        for r in refs:
            flat_hyps.append(hypo)
            flat_refs.append(r)
    
    # If you have a GPU, you can specify "cuda:0" or "cuda:3" etc.
    P, R, F1 = score(flat_hyps, flat_refs, lang="en", 
                     # rescale_with_baseline=True,
                     device="cuda:3", 
                     batch_size=32)
    
    bert_score = float(torch.mean(F1))
    final_scores["BERTScore"] = bert_score
    
    # Write BERTScore on the fly
    f_out.write("BERTScore: {:.4f}\n".format(bert_score))
    f_out.write("\n===== Final Evaluation Scores =====\n")

    # ============================
    # 6. Print and Store Final Evaluation Scores
    # ============================
    for metric_name, metric_value in final_scores.items():
        f_out.write(f"{metric_name}: {metric_value:.4f}\n")
    
    print("\n===== Final Evaluation Scores =====")
    for metric_name, metric_value in final_scores.items():
        print(f"{metric_name}: {metric_value:.4f}")

print(f"\nIntermediate and final evaluation scores have been written to '{output_file}'.")
