 <img src='asset/logo.png' align="left" width="11%" />
 <div style="margin-top:50px;">
      <h1 style="font-size: 30px; margin: 0;"> TimeTravel: A Comprehensive Benchmark to Evaluate LMMs on Historical and Cultural Artifacts</h1>
 </div>
   
 <div  align="center" style="margin-top:10px;"> 
    
  [Sara Ghaboura](https://huggingface.co/SLMLAH) <sup> * </sup> &nbsp;
  [Ketan More](https://huggingface.co/SLMLAH) <sup> * </sup> &nbsp;
  [Retish Thawkar](https://huggingface.co/SLMLAH) <sup> * </sup> &nbsp;
  [Wafa Alghallabi](https://huggingface.co/SLMLAH) <sup> * </sup> &nbsp;
  [Omkar Thawakar](https://omkarthawakar.github.io) <sup> * </sup> &nbsp;
  <br>
  [Fahad Shahbaz Khan](https://scholar.google.com/citations?hl=en&user=zvaeYnUAAAAJ) &nbsp;
  [Hisham Cholakkal](https://scholar.google.com/citations?hl=en&user=bZ3YBRcAAAAJ) &nbsp;
  [Salman Khan](https://scholar.google.com/citations?hl=en&user=M59O9lkAAAAJ) &nbsp;
  [Rao M. Anwer](https://scholar.google.com/citations?hl=en&user=_KlvMVoAAAAJ)
  <br>
  <br>
  [![arXiv](https://img.shields.io/badge/arXiv-2502.0094-F6D769)](https://arxiv.org/abs/2502.00094)
  [![Our Page](https://img.shields.io/badge/Visit-Our%20Page-E7DAB7?style=flat)](https://mbzuai-oryx.github.io/AIN/)
  [![GitHub issues](https://img.shields.io/github/issues/mbzuai-oryx/Camel-Bench?color=E5D5C1&label=issues&style=flat)](https://github.com/mbzuai-oryx/AIN/issues)
  [![GitHub stars](https://img.shields.io/github/stars/mbzuai-oryx/AIN?color=FAF1D9&style=flat)](https://github.com/mbzuai-oryx/AIN/stargazers)
  [![GitHub license](https://img.shields.io/github/license/mbzuai-oryx/Camel-Bench?color=F1E9E3)](https://github.com/mbzuai-oryx/AIN/blob/main/LICENSE)
  <br>
  <em> <sup> *Equal Contribution  </sup> </em>
  <br>
  <br>
</div>



<p align="center">
    <img src="asset/line.png"  height="9px">
</p> 

 
<div align="center">
 <b> If you like our project, please give us a star ⭐ on GitHub for the latest update. </b><br>
</div>
<br>
<p align="center">
    <img src="asset/line.png" height="9px">
</p> 
<br>
<br>

##  <img src="https://github.com/user-attachments/assets/1abcf195-ad44-4500-a14b-f1a4bef9b748" width="40" height="40" />Latest Updates

 🤗 **[18 Feb 2025]** TimeTravel dataset available on HuggingFace.<br>
 🔥 **[19 Feb 2025]** TimeTravel the **1<sup>st</sup>** comprehensive open-source benchmark on Historical and Cultural Artifacts is released.<br>
<br>
<br>


## <img src="asset/hour_g_1.png" width="40" height="40" alt="hourg_logo"> Overview
<p style="text-align: justify">
TimeTravel is the <b>first comprehensive</b> benchmark for AI-driven historical artifact analysis, designed to identify artifacts within their <b>historical era and cultural context</b>. Spanning <b>266 cultural groups across 10 regions</b>, it prioritizes <b>historical knowledge, contextual reasoning, and cultural preservation</b>, unlike generic object recognition benchmarks. With <b>over 10,000 expert-verified samples</b>, TimeTravel sets a new standard for evaluating multimodal models in historical research, cross-civilizational analysis, and AI-powered cultural heritage preservation.
<br>
<br>
<div style="display: flex; justify-content: space-between; align="center;">
    <figure style="width: 40%;">
      &emsp;&emsp;
     <img src="asset/Taxonomy.png" alt="Figure 1" style="width: 40%; height: auto;"> &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
     <img src="asset/Samples_Distribution.png" alt="Figure 2" style="width: 40%; height: auto;">
    </figure>
</div>
<br>
<h6><em>  <b>Figure 1.</b> Left: TimeTravel Taxonomy maps artifacts from 10 civilizations, 266 cultures, and 10k+ verified samples for AI-driven historical analysis. Right: Regional dataset distribution by archaeological provenance, with Greece holding the largest share (18%) and balanced regional coverage.
</em> 
</h6>
<br>
<br>
</p> 

 ## 🌟 Key Features
 - The **first Arabic-centric inclusive Large Multimodal Model (LMM)** trained on **3.6M samples**.
 - Includes **35% authentic Arabic data** within its Arabic data subset.
 - Achieves **superior performance compared to open- and closed-source models** (e.g., GPT-4o) and open-source models (e.g., Qwen2-VL-7B) across tasks such as OCR and specialized domains.
 - Demonstrates **robust bilingual capabilities** (Arabic/English), **validated** through **comprehensive testing** and **human evaluation** across 17 Arab countries.
 - Exhibits **advanced cultural understanding** and domain expertise in fields such as **medical imaging**, **agriculture**, and **scientific visualization**.

<p align="center">
   <img src="images/intro_bar.png" width="70%" alt="intro_bar"  style="margin-right: 2px";/>
   <h6>
       <em>  <b>Figure 2.</b> Comparative performance of AIN-7B against other models across key domains, including OCR & Document Understanding, Remote Sensing, Agricultural Understanding, and overall performance across all domains. </em>
   </h6>
</p> 
<br>

---
## ⚖️ Quantitative Evaluation and Results
AIN demonstrates state-of-the-art performance across diverse domains, surpassing both open- and closed-source models. Notably, it achieves an aggregate performance score of 63.77%, with significant gains in OCR, remote sensing, and agricultural image understanding.



## 🎯 Qualitative Evaluation
The qualitative evaluation showcases AIN's advanced capabilities in handling diverse, complex tasks, including OCR, medical imaging, remote sensing, and cultural-specific understanding, with remarkable precision and contextual relevance. Unlike GPT-4o and LLaVA, AIN demonstrates superior performance in identifying intricate details and maintaining accuracy across varied query formats and multi-domain challenges.

<div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-top: 20px;">
  <p align="center" >
  <img src="images/contre.png" width="50%" alt="contre" />
  <img src="images/qualitative.png" width="40%" alt="qualitative" />
     <h6>
       <em>  <b>Figure 3.</b> Left: Comparison of AIN-7B’s qualitative performance against other models across multiple domains. Right: Qualitative examples showcasing AIN-7B’s capabilities across various domains, including general VQA, OCR & Document Understanding, Remote Sensing, Medical Imaging, Agricultural Understanding, and Cultural-Specific tasks. </em>
    </h6>
  </p> 
</div>
<br>

---
## 🧐 Data Verification and Toxicity Filtering
A multi-step verification pipeline was implemented to ensure high-quality translations and safe visual data. Translation accuracy was assessed through human evaluation, where native Arabic speakers rated outputs against reference translations, and semantic similarity checks were conducted using **LaBSE**. Additionally, translated samples were reverse-translated and validated using **BLEU, METEOR, and ROUGE scores** to measure correctness, correlation, and overlap. For visual data, toxicity filtering was applied using **LLavaGuard’s safety policies and GPT-4o**, identifying and removing unsafe content related to violence, substance abuse, and harmful imagery, ensuring compliance with ethical AI standards.

<p align="center">
   <img src="images/verify_pipeline.png" width="75%" alt="verify"  style="margin-right: 2px";/>
    <h6>
       <em>  <b>Figure 4.</b> Data verification and filtering pipeline for textual and visual data, ensuring high-quality training data through semantic similarity checks, translation quality evaluations, and toxicity screening for safety compliance. </em>
    </h6>
</p> 
<br>
<br>
<p align="center">
   <img src="images/toxicity.png" width=50%" alt="verify"  style="margin-right: 2px";/>
    <h6>
       <em>  <b>Figure 5.</b> Distribution of visual data toxicity filtering results, showing that 95% of the data is classified as safe, while 5% is identified as unsafe due to categories like weapons or substance abuse, violence, and animal cruelty. </em>
   </h6>
</p> 
<br>
<br>

---
## 🔒 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
<br>
<br>

## 💬 Contact us
For questions or suggestions, feel free to reach out to us on [GitHub Discussions](https://github.com/mbzuai-oryx/AIN/discussions).

---

## 📚 Citation

If you use AIN LMM in your research, please consider citing:

```bibtex

```
<br>

---


<p align="center">
   <img src="asset/IVAL_logo.png" width="18%" style="display: inline-block; margin: 0 10px;" />
   <img src="asset/Oryx_logo.png" width="10%" style="display: inline-block; margin: 0 10px;" />
   <img src="asset/MBZUAI_logo.png" width="50%" style="display: inline-block; margin: 0 10px;" />
</p>
