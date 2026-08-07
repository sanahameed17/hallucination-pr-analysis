# Annotation Protocol

## Overview

This document describes the manual annotation protocol followed in the empirical study **"An Empirical Study of Hallucination-Induced Failures in LLM-Based Agent-Authored Pull Requests."**

The protocol was designed to ensure consistent identification and classification of hallucination behaviors in agent-authored pull requests.

---

# Annotation Workflow

Each pull request was analyzed using the following workflow.

```
Select Pull Request
        │
        ▼
Review PR Description
        │
        ▼
Inspect Code Changes
        │
        ▼
Review Commit History
        │
        ▼
Review Discussion Threads
        │
        ▼
Inspect Available CI/Test Results
        │
        ▼
Identify Hallucination
        │
        ▼
Assign Hallucination Category
        │
        ▼
Record Supporting Evidence
        │
        ▼
Finalize Annotation
```

---

# Annotation Procedure

For every pull request, the following steps were performed.

### Step 1

Review the pull request description to understand the development task.

### Step 2

Inspect the modified source code and implementation changes.

### Step 3

Review the complete commit history associated with the pull request.

### Step 4

Inspect pull request discussions and review comments.

### Step 5

Review available CI/Test execution results.

### Step 6

Determine whether hallucination behavior is present.

### Step 7

If hallucination is identified, assign one or more hallucination categories using the predefined taxonomy.

### Step 8

Record repository evidence supporting the annotation decision.

### Step 9

For hallucinated pull requests, compare the initial and final revisions to determine hallucination evolution.

### Step 10

Store the final annotation in the dataset.

---

# Hallucination Taxonomy

The annotation follows the taxonomy proposed by Liu et al. (2026).

The following hallucination categories were considered:

- Requirement-Conflicting
- Knowledge-Related
- Code-Inconsistency

Multiple hallucination categories may be assigned to the same pull request when supported by repository evidence.

---

# Hallucination Evolution

For hallucinated pull requests, hallucination evolution was analyzed using four predefined analytical outcomes.

- Persistence
- Correction
- Transformation
- Cannot be Determined

These categories were used only to describe observed evolution behavior and did not assume that every category would necessarily occur in the analyzed dataset.

---

# Annotation Principles

The annotation process followed four principles.

- Evidence-based annotation
- Context-aware analysis
- Consistent operational definitions
- Conservative labeling

---

# Quality Assurance

All annotations were performed manually using predefined operational definitions and consistent annotation criteria to improve labeling consistency throughout the study.
