# Hallucination Labels and Categories

This document describes the annotation labels and hallucination categories used in the dataset.

## 1. Hallucination Label

Each pull request (PR) is assigned a hallucination label indicating whether hallucination is present:

- **Yes**  
  The PR contains clear hallucination behavior, such as incorrect assumptions, flawed logic, or invalid implementation.

- **No**  
  The PR does not contain hallucination and correctly implements the intended functionality.

- **Borderline**  
  The PR contains ambiguous or partially problematic behavior that cannot be confidently classified as hallucination. These cases may require deeper contextual understanding.

---

## 2. Hallucination Types

For PRs labeled as hallucinations or borderline cases, a hallucination type is assigned based on predefined categories.

### 2.1 Knowledge-related Hallucination
- The code is based on incorrect or unsupported assumptions about the system, APIs, or dependencies.
- Example:
  - Using a non-existent API
  - Misunderstanding library behavior
  - Incorrect configuration assumptions

---

### 2.2 Code-inconsistency Hallucination
- The implementation contains logical inconsistencies or flawed reasoning.
- Example:
  - Incorrect control flow
  - Invalid conditional logic
  - Inconsistent variable usage

---

### 2.3 Borderline Cases
- These cases do not clearly fall into hallucination categories but exhibit suspicious or suboptimal behavior.
- Example:
  - Overly complex implementation (over-generation)
  - Unnecessary code changes
  - Potential integration risks

---

### 2.4 None
- No hallucination is present.
- This is used when the hallucination label is **No**.

---

## 3. Annotation Guidelines

The annotation process follows these principles:

1. **Context-aware analysis**  
   Each PR is evaluated based on its repository context, code changes, and intended functionality.

2. **Conservative labeling**  
   Only clear cases are labeled as hallucinations. Ambiguous cases are marked as **Borderline**.

3. **Consistency with taxonomy**  
   All annotations align with predefined hallucination categories derived from prior research.

---

## 4. Notes

- The classification may involve subjective judgment, especially for borderline cases.
- The labels are designed to support empirical analysis of hallucination behavior in real-world software development workflows.
