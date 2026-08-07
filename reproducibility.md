# Reproducibility Guide

## Overview

This document explains how the empirical analyses reported in the paper can be reproduced using the datasets provided in this repository.

The replication package contains all manually annotated data required to reproduce the reported empirical findings.

---

# Required Files

The following files are required.

- pr_annotation_dataset.csv
- hallucination_evolution_dataset.csv
- labels_description.md

---

# Reproducing RQ1

Research Question:

> What hallucination types occur in agent-authored pull requests?

Procedure:

1. Open `pr_annotation_dataset.csv`.
2. Filter pull requests where hallucination is present.
3. Count the number of Requirement-Conflicting hallucinations.
4. Count the number of Knowledge-Related hallucinations.
5. Count the number of Code-Inconsistency hallucinations.
6. Calculate frequencies and percentages.
7. Generate the hallucination distribution table and corresponding figure.

---

# Reproducing RQ2

Research Question:

> How do hallucinations evolve across pull request revision cycles?

Procedure:

1. Open `hallucination_evolution_dataset.csv`.
2. Review the Initial Hallucination Type and Final Hallucination Type.
3. Count the number of Persistence cases.
4. Count the number of Correction cases.
5. Count the number of Transformation cases.
6. Count the number of Cannot be Determined cases.
7. Summarize the observed evolution patterns.

---

# Reproducing RQ3

Research Question:

> What is the relationship between hallucination presence and pull request outcomes?

Procedure:

1. Open `pr_annotation_dataset.csv`.
2. Compare hallucinated and non-hallucinated pull requests.
3. Analyze PR status.
4. Analyze available CI/Test outcomes.
5. Perform Pearson's Chi-square test.
6. Compute Fisher's Exact Test where appropriate.
7. Compute Cramér's V.
8. Compute Odds Ratios.

---

# Reproducing RQ4

Research Question:

> Can hallucination indicators be identified before formal validation?

Procedure:

1. Review the initial version of hallucinated pull requests.
2. Examine annotation notes and supporting evidence.
3. Identify observable hallucination indicators before code review and CI execution.
4. Summarize common early hallucination characteristics.

---

# Statistical Analysis

The statistical analyses were performed using Python.

Libraries used:

- pandas
- NumPy
- SciPy

Statistical techniques:

- Descriptive Statistics
- Pearson's Chi-square Test
- Fisher's Exact Test
- Cramér's V
- Odds Ratio Analysis

---

# Reproducibility Notes

The datasets included in this repository allow researchers to reproduce the manual annotation process and empirical analyses reported in the paper.

Future researchers may extend the datasets with additional pull requests or apply alternative statistical analyses while following the same annotation protocol.
