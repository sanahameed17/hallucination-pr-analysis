# An Empirical Study of Hallucination Behaviors in LLM-based Agent-Authored Pull Requests

---

This repository contains the replication datasets for the empirical study of hallucination behaviors in LLM-based agent-authored pull requests. A brief description of each dataset is provided below.

## 1. pr_annotation_dataset.csv

This file contains the manually annotated dataset of the analyzed agent-authored pull requests. Each record provides information about the pull request, including its URL, AI coding agent, pull request state, task category, CI/test outcome, hallucination presence, hallucination category, and annotation notes. The dataset provides the main annotated records used to examine hallucination behaviors and their relationship with pull request and CI/test outcomes.

## 2. hallucination_evolution_dataset.csv

This file contains the revision-level data used to examine the evolution of hallucination behaviors in hallucinated pull requests. It records the initial and final hallucination types, the observed evolution category, final pull request status, and supporting evidence used for the evolution analysis. The dataset supports the analysis of how hallucination behaviors change or persist across pull request revisions.

## 📁 Repository Structure

```text
├── pr_annotation_dataset.csv
├── hallucination_evolution_dataset.csv
└── README.md
```


## 📝 Citation

```bibtex
@misc{sanahameed2026dataset,
  author = {Sana Hameed and Ruiyin Li and Peng Liang and Amjed Tahir and Mojtaba Shahin and Zengyang Li and Arif Ali Khan},
  title = {Replication Package for the Paper: An Empirical Study of Hallucination Behaviors in LLM-based Agent-Authored Pull Requests},
  year = {2026},
  howpublished = {GitHub Repository},
  url = {https://github.com/sanahameed17/hallucination-pr-analysis}
}