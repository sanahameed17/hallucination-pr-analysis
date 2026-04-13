# Replication Package: Hallucination Analysis in Agent-Authored Pull Requests

## Overview
This repository provides the replication package for the empirical study on hallucination-induced failures in agent-authored pull requests (PRs). The goal of this study is to analyze how hallucinations occur, evolve, and impact software development workflows in real-world repositories.

## Dataset Description
The dataset used in this study is derived from the AIDev dataset, a large-scale collection of agent-authored pull requests from GitHub. From this dataset, we selected and manually analyzed approximately 95 pull requests.

Each pull request was examined to determine:
- Whether hallucination is present
- The type of hallucination (if any)
- Its impact on development workflow outcomes (e.g., CI results, PR status)

## Repository Structure
This replication package contains the following files:

- `pr_dataset.csv`  
  The main dataset containing annotated pull requests and their associated metadata.

- `labels_description.md`  
  Detailed explanation of hallucination labels and categories used in the study.

## Dataset Fields
The dataset includes the following columns:

- `pr_id`: Unique identifier for each pull request  
- `pr_url`: URL of the pull request  
- `repo_name`: Name of the GitHub repository  
- `agent`: AI agent responsible for generating the PR (e.g., OpenAI Codex, Copilot, Devin AI)  
- `pr_state`: Final state of the pull request (e.g., Merged, Closed, Open)  
- `task_type`: Type of development task (e.g., Bug Fix, Feature, Refactor)  
- `ci_result`: CI/CD outcome (Passed, Failed, Not Available)  
- `hallucination_label`: Indicates whether hallucination is present (Yes, No, Borderline)  
- `hallucination_type`: Type of hallucination (Knowledge-related, Code-inconsistency, Borderline, None)  
- `notes`: Additional observations about each pull request  

## Annotation Process
Each pull request was manually analyzed based on a predefined taxonomy of hallucinations derived from prior research. The annotation process involved:

1. Reviewing the PR description, code changes, and context
2. Identifying inconsistencies, incorrect assumptions, or over-generation behavior
3. Classifying each case into one of the following categories:
   - **Knowledge-related hallucination**: Incorrect assumptions about system behavior or dependencies  
   - **Code-inconsistency hallucination**: Logical errors or flawed implementation  
   - **Borderline cases**: Ambiguous cases requiring deeper interpretation  
   - **No hallucination**: Correct and valid implementation  

## Reproducibility
This replication package enables other researchers to reproduce the analysis and validate the findings presented in the study. All annotated data used in the results section is included in this repository.

## Source Dataset
The original dataset is based on the AIDev dataset:

Li, Hao et al.  
*The Rise of AI Teammates in Software Engineering (SE 3.0): How Autonomous Coding Agents Are Reshaping Software Engineering*  
arXiv preprint, 2025.

## Limitations
- The dataset is a subset (~95 PRs) and may not fully represent all agent-authored pull requests.
- Annotation involves manual judgment and may include subjective interpretation in borderline cases.


Sana Hameed
