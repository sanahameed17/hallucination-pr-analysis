# Hallucination Labels and Annotation Guidelines

## Overview

This document describes the annotation labels, hallucination taxonomy, and evolution categories used in the empirical study **"An Empirical Study of Hallucination-Induced Failures in LLM-Based Agent-Authored Pull Requests."**

The annotations were performed manually using predefined operational definitions to ensure consistency across all analyzed pull requests. Each pull request was inspected by reviewing its GitHub repository, pull request description, code changes, commit history, review discussions, and available CI/Test results.

---

# Hallucination Presence

Each pull request was first classified according to whether hallucination was present.

## Hallucination Present

The pull request contains one or more hallucination behaviors supported by repository evidence.

## No Hallucination

No observable hallucination behavior was identified in the pull request.

---

# Hallucination Taxonomy

Hallucination behaviors were classified using the taxonomy proposed by Liu et al. (2026). A pull request may contain more than one hallucination category.

## 1. Requirement-Conflicting Hallucination

The generated implementation contradicts the intended functionality or repository requirements.

Typical characteristics include:

- Incorrect implementation of requested functionality
- Violations of repository requirements
- Behavior inconsistent with the intended task
- Semantic conflicts with expected functionality

---

## 2. Knowledge-Related Hallucination

The generated implementation relies on incorrect assumptions regarding repository context, APIs, dependencies, libraries, or external knowledge.

Typical characteristics include:

- Non-existent APIs
- Incorrect dependency assumptions
- Fabricated functionality
- Unsupported framework or library usage
- Invalid repository assumptions

---

## 3. Code-Inconsistency Hallucination

The generated implementation conflicts with repository-specific conventions, architectural structures, or existing implementation logic.

Typical characteristics include:

- Repository convention violations
- Architectural inconsistencies
- Conflicting implementation logic
- Duplicate or inconsistent functionality
- Integration inconsistencies

---

# Hallucination Evolution

For hallucinated pull requests, hallucination evolution was analyzed by comparing the initial pull request version with the final observable revision.

The following evolution categories were used.

## Persistence

The hallucination remains present throughout subsequent pull request revisions.

The hallucination category does not change and remains observable in the final revision.

---

## Correction

The hallucination identified in the initial pull request is resolved during later revisions.

The final revision no longer exhibits the previously identified hallucination.

---

## Transformation

The hallucination changes from one hallucination category to another during the revision process.

No transformation cases were observed in the analyzed dataset; however, this category was included as a predefined analytical outcome.

---

## Cannot be Determined

The available revision history is insufficient to determine hallucination evolution.

Typical reasons include:

- Inaccessible repositories
- Missing revision history
- Deleted pull requests
- Insufficient repository evidence

---

# Annotation Procedure

Each pull request was analyzed using the following procedure.

1. Review the pull request description.
2. Examine the modified source code.
3. Inspect the commit history.
4. Review discussion threads and review comments.
5. Examine available CI/Test execution results.
6. Identify hallucination behaviors using predefined operational definitions.
7. Assign one or more hallucination taxonomy labels where appropriate.
8. Record supporting repository evidence.
9. Determine hallucination evolution for hallucinated pull requests.

---

# Annotation Principles

The annotation process followed four principles.

## Evidence-Based Annotation

Every annotation decision was supported by observable repository evidence rather than isolated code fragments.

## Context-Aware Analysis

Pull requests were interpreted within their repository context, including project architecture, existing implementation, and task requirements.

## Consistent Operational Definitions

The same operational definitions were applied throughout the entire annotation process to improve consistency.

## Conservative Labeling

Hallucination labels were assigned only when sufficient repository evidence supported the classification.

---

# Notes

- A single pull request may contain multiple hallucination categories.
- Hallucination categories are not mutually exclusive.
- Evolution analysis was performed only for pull requests in which hallucinations were identified.
- Annotation involves expert manual interpretation and may include limited subjectivity in complex repository contexts.
- The dataset and annotation guidelines are intended to support empirical research on hallucination-aware software engineering and enable replication of the reported analyses.
