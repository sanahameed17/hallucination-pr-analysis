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

This repository contains the replication datasets and analysis scripts for the empirical study of hallucination behaviors in LLM-based agent-authored pull requests. The study analyzes 1,066 randomly selected agent-authored pull requests with publicly accessible repositories from the AIDev dataset. A brief description of each file is provided below.

## 1. data/annotations.csv

This file contains the manually annotated dataset of the 1,066 analyzed agent-authored pull requests. Each record provides the pull request URL, repository, coding agent, task type, final pull request status, hallucination presence (Hallucinated, Non-Hallucinated, or Cannot Determine), and hallucination categories (Requirement-Conflicting, Knowledge-Related, and Code-Inconsistency). For hallucinated pull requests, it also records the initial and final hallucination types and the evolution outcome (Persistence, Correction, or Transformation) used in RQ2.

## 2. data/subtypes.csv

This file assigns each of the 537 hallucination instances to one of ten fine-grained sub-types: C1 unsupported claims in description or documentation, C2 unsupported verification claims, C3 conflict with existing repository code or configuration, C4 internal inconsistency within the change, K1 non-existent API, option, endpoint, resource, or fact, K2 non-existent or incompatible dependency version, K3 incorrect assumption about language, library, or platform behavior, K4 outdated or removed API or knowledge, R1 requirement not met although claimed as done, and R2 change that contradicts the requirement or adds unrequested scope.

## 3. data/revision_audit.csv

This file contains the commit-level audit of the 429 hallucinated pull requests, which was used to confirm the evolution outcomes in RQ2 and the first-version observability in RQ4. Each record provides the number of commits, the audit category (A: single agent version; B: persisted across a relevant later agent revision; C: later commits did not touch the hallucinated artifact; D: corrected by the agent; E: fixed or changed only by the repository owner; F: introduced in a later agent commit; T: transformed into another category; U: first version not determinable), and whether the hallucination was present in the first agent version.

## 4. data/pr_size.csv

This file contains the size measures of each pull request (number of commits, lines added and deleted, files changed, description length in words, and number of comments), which were used as control variables in the logistic regression for RQ3.

## 5. data/pilot_agreement.csv

This file contains the labels independently assigned by two coders to the 50 pull requests of the pilot sample, which were used to compute the inter-rater agreement (Cohen's kappa = 0.58 on 49 pull requests; PABAK = 0.71).

## 6. scripts/ and results/

`scripts/analysis.py` reproduces all results reported in the paper for RQ1–RQ4 and the pilot agreement, and writes them to `results/results.json`. `scripts/figures.py` regenerates the data figures of the paper. To run them:

```
pip install numpy scipy matplotlib
python scripts/analysis.py
python scripts/figures.py
```

## 📝 Citation

```bibtex
@article{sanahameed2026dataset,
  author = {Hameed, Sana and Li, Ruiyin and Liang, Peng and Tahir, Amjed and Shahin, Mojtaba and Li, Zengyang and Khan, Arif Ali},
  title = {An Empirical Study of Hallucination Behaviors in LLM-based Agent-Authored Pull Requests},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year = {2026},
}
