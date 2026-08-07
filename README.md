# Replication Package: An Empirical Study of Hallucination-Induced Failures in LLM-Based Agent-Authored Pull Requests

## Overview

This repository contains the replication package for the paper **"An Empirical Study of Hallucination-Induced Failures in LLM-Based Agent-Authored Pull Requests."**

The study presents a large-scale empirical investigation of hallucination behaviors in AI-generated pull requests created by autonomous coding agents. Using a manually annotated dataset of **500 agent-authored pull requests** selected from the **AIDev dataset**, the study investigates how hallucinations occur, evolve across pull request revision cycles, relate to workflow outcomes, and whether hallucination indicators can be identified before formal validation activities.

This replication package provides the annotated datasets, annotation guidelines, and supporting materials required to reproduce the empirical analyses presented in the paper and to facilitate future research on hallucination-aware software engineering.

---

# Research Questions

This study addresses the following research questions:

- **RQ1:** What hallucination types occur in agent-authored pull requests?

- **RQ2:** How do hallucinations evolve across pull request revision cycles?

- **RQ3:** What is the relationship between hallucination presence and measurable pull request outcomes, including integration success, CI/test outcomes, and pull request rejection?

- **RQ4:** Can hallucination indicators be identified in the initial version of a pull request before formal validation activities such as code review and CI execution?

---

# Repository Structure

```
hallucination-pr-analysis/
│
├── README.md
├── labels_description.md
├── pr_annotation_dataset.csv
├── hallucination_evolution_dataset.csv
```

This repository contains two manually annotated datasets together with the annotation guideline used throughout the empirical study.

---

# Datasets

The replication package contains two complementary datasets.

## 1. PR Annotation Dataset

**File:** `pr_annotation_dataset.csv`

This dataset contains the manual annotations of all analyzed pull requests used throughout the empirical study.

The dataset includes:

- Pull request metadata
- AI coding agent
- Pull request state
- Task category
- CI/Test outcome
- Hallucination presence
- Hallucination category
- Annotation notes

This dataset is used to answer:

- RQ1
- RQ3
- RQ4

---

## 2. Hallucination Evolution Dataset

**File:** `hallucination_evolution_dataset.csv`

This dataset contains the detailed revision-history analysis performed for hallucinated pull requests.

Each record includes:

- Initial hallucination type
- Final hallucination type
- Evolution type
- Final pull request status
- Supporting evidence

This dataset is used to answer:

- RQ2

---

# Annotation Methodology

Each pull request was manually analyzed using a structured annotation protocol.

The annotation process consisted of the following steps:

1. Reviewing the pull request description.
2. Inspecting the modified source code.
3. Examining the commit history.
4. Reviewing discussion threads and review comments.
5. Inspecting available CI/Test execution results.
6. Identifying hallucination behaviors using predefined operational definitions.
7. Assigning hallucination taxonomy labels.
8. Recording supporting evidence and annotation notes.

All annotations were performed manually using consistent operational definitions to improve labeling consistency throughout the dataset.

---

# Hallucination Taxonomy

The annotation follows the taxonomy proposed by Liu et al. (2026).

Three hallucination categories are considered.

## Requirement-Conflicting Hallucination

Generated code contradicts the intended functionality or repository requirements.

Examples include:

- Incorrect implementation of requested functionality
- Violations of repository-specific requirements
- Behavior inconsistent with intended task objectives

---

## Knowledge-Related Hallucination

Generated code relies on incorrect assumptions regarding repository context, APIs, libraries, dependencies, or external knowledge.

Examples include:

- Non-existent APIs
- Incorrect dependency assumptions
- Fabricated functionality
- Unsupported library usage

---

## Code-Inconsistency Hallucination

Generated code conflicts with repository-specific implementation logic, architectural structures, or coding conventions.

Examples include:

- Repository convention violations
- Architectural inconsistencies
- Conflicting implementation logic
- Inconsistent code integration

---

# Hallucination Evolution

Hallucination evolution was analyzed across pull request revision cycles using the following categories.

## Persistence

The hallucination remains present throughout subsequent pull request revisions.

## Correction

The hallucination is resolved during later revisions.

## Transformation

The hallucination changes from one taxonomy category to another during revision.

## Cannot be Determined

Revision history is unavailable or insufficient to determine hallucination evolution.

---

# Statistical Analysis

The empirical analysis combines qualitative manual analysis with quantitative statistical analysis.

The following statistical techniques were used:

- Descriptive Statistics
- Pearson's Chi-square Test
- Fisher's Exact Test
- Cramér's V
- Odds Ratio Analysis

The statistical analyses were performed using Python with:

- pandas
- NumPy
- SciPy

---

# Reproducibility

This repository contains the annotated datasets and annotation guidelines used to reproduce the empirical analyses reported in the paper.

Researchers can use these materials to:

- Reproduce the manual annotation process.
- Replicate the empirical analyses.
- Validate the reported findings.
- Extend the dataset with additional pull requests.
- Develop automated hallucination detection techniques.

---

# Source Dataset

The analyzed pull requests were selected from the **AIDev dataset**:

> Li, Hao, Zhang, Haoxiang, and Hassan, Ahmed E.

> **AIDev: Studying AI Coding Agents on GitHub.**

> Proceedings of the International Conference on Mining Software Repositories (MSR), 2026.

---

# Citation

If you use this replication package in your research, please cite:

```bibtex
@misc{sanahameed2026dataset,
  author = {Sana Hameed and Ruiyin Li and Peng Liang and Amjed Tahir and Mojtaba Shahin and Zengyang Li and Arif Ali Khan},
  title = {Replication Package for the Paper: An Empirical Study of Hallucination-Induced Failures in LLM-Based Agent-Authored Pull Requests},
  year = {2026},
  howpublished = {GitHub Repository},
  url = {https://github.com/sanahameed17/hallucination-pr-analysis}
}
```

---

# License

This replication package is released for academic and research purposes.

Please cite the associated paper when using the dataset or annotation guidelines in your research.

---

# Contact

**Sana Hameed**

School of Computer Science

Wuhan University, China

GitHub:
https://github.com/sanahameed17
