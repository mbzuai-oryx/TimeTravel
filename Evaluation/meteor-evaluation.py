# ============================
# This file contains the code to evaluate the generated descriptions using Meteor.
# The code reads the ground truth and generated descriptions from the JSON files and computes the METEOR score.
# The METEOR score is computed using the nltk library.
# The METEOR score is saved in a CSV file.
# ============================
# Input:
# - Ground truth description JSON file
# - Generated description JSON file
# Output:
# - CSV file with METEOR scores
# ============================


from nltk.translate.meteor_score import meteor_score
from nltk.tokenize import word_tokenize
import pandas as pd
from tqdm import tqdm
import nltk
import json

ground_truth_file = "/data2/ketan/history_project_subset_v2/datatset/ground_truth_description.json"
vlm_reponse_file = "/data2/ketan/history_project_subset_v2/desciption_generation/response.json"
# output_path = "/data2/ketan/history_project_subset_v2/judge_llm_evaluation/results/llava_next-judge-llm-results.json"

with open(ground_truth_file) as flp :
    ground_truth_dataset = json.load(flp)


with open(vlm_reponse_file) as flp :
    vlm_resposnse_dataset = json.load(flp)


ground_truth_dataset = sorted(ground_truth_dataset, key=lambda x: x["id"])
vlm_resposnse_dataset = sorted(vlm_resposnse_dataset, key=lambda x: x["id"])

# Check if both datasets have the same ids
gt_ids = {item["id"] for item in ground_truth_dataset}
vlm_ids = {item["id"] for item in vlm_resposnse_dataset}

if gt_ids == vlm_ids:
    print("Both datasets have the exact same IDs.")
else:
    print("Mismatch in IDs between the datasets.")
    missing_in_gt = vlm_ids - gt_ids
    missing_in_vlm = gt_ids - vlm_ids
    print(f"IDs missing in ground truth dataset: {missing_in_gt}")
    print(f"IDs missing in VLM response dataset: {missing_in_vlm}")
    exit()




references = [
    [word_tokenize(item["description"])] if isinstance(item["description"], str) 
    else [word_tokenize(ref) for ref in item["description"]] 
    for item in ground_truth_dataset
]


# Extract and tokenize hypotheses
hypotheses = [word_tokenize(item["description"]) for item in vlm_resposnse_dataset]

# Compute METEOR scores with a progress bar
meteor_scores = [meteor_score(ref, hyp) for ref, hyp in tqdm(zip(references, hypotheses), total=len(hypotheses))]

# Convert results into a DataFrame
df = pd.DataFrame({
    "ID": [item["id"] for item in ground_truth_dataset],
    "Reference": [" ".join(ref[0]) if len(ref) == 1 else " | ".join([" ".join(r) for r in ref]) for ref in references],  # Join tokens back for readability
    "Hypothesis": [" ".join(hyp) for hyp in hypotheses],
    "METEOR Score": meteor_scores
})

# Optionally, save to CSV
df.to_csv("scores.csv", index=False)

print(df["METEOR Score"].mean())
