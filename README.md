<div align="center">
  <h1 align="center">An Empirical Study of Hallucination Behaviors in LLM-based Agent-Authored Pull Requests</h1>
</div>

<div align="center">
    <a href="https://github.com/sanahameed17/hallucination-pr-analysis/">
      <img src="https://img.shields.io/badge/Dataset-GitHub-2d333b?style=flat-square&logo=github" alt="github">
    </a>
    <a href="https://arxiv.org/abs/xxxx.xxxxx">
      <img src="https://img.shields.io/badge/Paper-arXiv-b31b1b?style=flat-square&logo=arxiv&logoColor=white" alt="arXiv">
    </a>
    <hr>
</div>

This repository contains the replication datasets for the empirical study of hallucination behaviors in LLM-based agent-authored pull requests. A brief description of each dataset is provided below.

## 1. pr_annotation_dataset.csv

This file contains the manually annotated dataset of the analyzed agent-authored pull requests. Each record provides information about the pull request, including its URL, AI coding agent, pull request state, task category, CI/test outcome, hallucination presence, hallucination category, and annotation notes. The dataset provides the main annotated records used to examine hallucination behaviors and their relationship with pull request and CI/test outcomes.

## 2. hallucination_evolution_dataset.csv

This file contains the revision-level data used to examine the evolution of hallucination behaviors in hallucinated pull requests. It records the initial and final hallucination types, the observed evolution category, final pull request status, and supporting evidence used for the evolution analysis. The dataset supports the analysis of how hallucination behaviors change or persist across pull request revisions.

## 📝 Citation

```bibtex
@article{sanahameed2026dataset,
  author = {Hameed, Sana and Li, Ruiyin and Liang, Peng and Tahir, Amjed and Shahin, Mojtaba and Li, Zengyang and Khan, Arif Ali},
  title = {An Empirical Study of Hallucination Behaviors in LLM-based Agent-Authored Pull Requests},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year = {2026},
}
