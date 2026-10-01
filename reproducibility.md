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
3. Identify all annotated hallucination instances within the hallucinated pull requests.
4. Count the number of Requirement-Conflicting hallucination instances.
5. Count the number of Knowledge-Related hallucination instances.
6. Count the number of Code-Inconsistency hallucination instances.
7. Calculate frequencies and percentages using the total number of hallucination instances as the denominator.
8. Generate the hallucination distribution table and corresponding figure.

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
3. Analyze PR status across the four categories: Merged, Closed, Open, and Draft.
4. Perform Pearson's Chi-square test of independence for the 2×4 PR-status contingency table.
5. Because the PR-status table contains small expected frequencies, perform an exact test for the 2×4 contingency table.
6. For the binary comparison of merged versus non-merged pull requests, perform Fisher's exact test.
7. Compute Cramér's V for categorical associations.
8. Compute the odds ratio for the binary merged versus non-merged comparison.
9. Analyze available CI/test outcomes separately for hallucinated and non-hallucinated pull requests.
10. Perform Pearson's Chi-square test for the CI/test outcome comparison.
11. Compute Cramér's V for the CI/test outcome association.

---

# Reproducing RQ4

Research Question:

> Can hallucination indicators be identified in the initial version of a PR before formal validation activities such as code review and CI execution, without treating these indicators as evidence of predictive detection?

Procedure:

1. Review the initial version of hallucinated pull requests.
2. Examine annotation notes and supporting evidence.
3. Identify hallucination indicators observable before formal validation activities such as code review and CI execution.
4. Summarize the observable early hallucination characteristics.
5. Interpret the findings as qualitative observability rather than predictive detection.

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
- Exact Test for the 2×4 PR-status contingency table
- Fisher's Exact Test for the binary merged versus non-merged comparison
- Cramér's V
- Odds Ratio Analysis

---

# Reproducibility Notes

The datasets included in this repository allow researchers to reproduce the manual annotation process and empirical analyses reported in the paper.

Future researchers may extend the datasets with additional pull requests or apply alternative statistical analyses while following the same annotation protocol.
