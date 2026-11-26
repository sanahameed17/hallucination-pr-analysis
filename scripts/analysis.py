"""Reproduces all numbers reported in the paper from the released data.

Usage (from the repository root):
    python scripts/analysis.py            # writes results/results.json and prints a summary

Inputs:  data/annotations.csv, data/pr_size.csv, data/pilot_agreement.csv
Requires: Python 3.10+, numpy, scipy
"""
import collections
import csv
import json
import math
import random
from pathlib import Path

import numpy as np
from scipy.stats import chi2_contingency, fisher_exact, mannwhitneyu, norm

ROOT = Path(__file__).resolve().parents[1]
TYPES = ['Requirement-Conflicting', 'Knowledge-Related', 'Code-Inconsistency']
STATES = ['Merged', 'Closed', 'Open', 'Draft']
AUDIT = {'A': 'Single agent version', 'B': 'Persisted across a relevant later agent revision',
         'C': 'Later commits did not touch the hallucinated artifact', 'D': 'Corrected by the agent',
         'E': 'Fixed or changed only by the repository owner', 'F': 'Introduced in a later agent commit',
         'T': 'Transformed into another category', 'U': 'First version not determinable'}


def load():
    ann = list(csv.DictReader(open(ROOT / 'data' / 'annotations.csv', encoding='utf-8')))
    size = {r['pr_id']: r for r in csv.DictReader(open(ROOT / 'data' / 'pr_size.csv', encoding='utf-8'))}
    for r in ann:
        r['H'] = r['hallucination'] == 'Hallucinated'
        r['types'] = [t for t in r['hallucination_types'].split('; ') if t]
        s = size[r['pr_id']]
        r['size'] = None if s['commits'] == '' else {k: int(v) for k, v in s.items() if k != 'pr_id'}
    return ann


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(c - h, 4), round(c + h, 4)


def cramers_v(t):
    chi, p, dof, _ = chi2_contingency(t, correction=False)
    return chi, p, dof, math.sqrt(chi / (t.sum() * (min(t.shape) - 1)))


def freeman_halton_mc(t, sims=100000, seed=1):
    """Monte Carlo estimate of the Freeman-Halton exact test (permutation of the chi-square statistic)."""
    obs = chi2_contingency(t, correction=False)[0]
    groups = np.repeat(np.arange(t.shape[0]), t.sum(axis=1))
    cats = np.concatenate([np.repeat(j, t[:, j].sum()) for j in range(t.shape[1])])
    rng = np.random.default_rng(seed)
    hits = 0
    for _ in range(sims):
        rng.shuffle(cats)
        tt = np.zeros_like(t)
        np.add.at(tt, (groups, cats), 1)
        hits += chi2_contingency(tt, correction=False)[0] >= obs - 1e-9
    return (hits + 1) / (sims + 1)


def status_tests(R, sims=0):
    t = np.array([[sum(r['pr_state'] == s and r['H'] == g for r in R) for s in STATES] for g in (True, False)])
    tk = t[:, t.sum(axis=0) > 0]
    chi, p, dof, v = cramers_v(tk)
    m = np.array([[t[0, 0], t[0, 1:].sum()], [t[1, 0], t[1, 1:].sum()]])
    orr, pf = fisher_exact(m)
    se = math.sqrt((1 / m).sum())
    out = {'n': len(R), 'table': {'Hallucinated': dict(zip(STATES, map(int, t[0]))),
                                  'Non-Hallucinated': dict(zip(STATES, map(int, t[1])))},
           'chi2': round(chi, 2), 'dof': int(dof), 'p': p, 'cramers_v': round(v, 3),
           'merge_fisher_p': pf, 'merge_OR': round(orr, 2),
           'merge_OR_CI95': [round(math.exp(math.log(orr) - 1.96 * se), 2), round(math.exp(math.log(orr) + 1.96 * se), 2)]}
    if sims:
        out['freeman_halton_p_mc'] = freeman_halton_mc(tk, sims)
    return out


# ------------------------------------------------------------------ logistic regression (RQ3)
TASK_MAP = {'Feature': 'Feature', 'Bug Fix': 'Bug Fix', 'Documentation': 'Documentation', 'Refactor': 'Refactor',
            'UI Change': 'UI Change', 'Testing': 'Testing', 'Configuration': 'Config/DevOps', 'DevOps': 'Config/DevOps'}
AGENTS = ['GitHub Copilot', 'Devin AI', 'Cursor AI', 'Claude Code']  # reference level: OpenAI Codex
TASKS = ['Bug Fix', 'Documentation', 'Refactor', 'UI Change', 'Testing', 'Config/DevOps', 'Other']  # reference: Feature


def design(R):
    names, cols = ['Intercept', 'Hallucinated'], [np.ones(len(R)), np.array([r['H'] for r in R], float)]
    for a in AGENTS:
        names.append('Agent: ' + a); cols.append(np.array([r['agent'] == a for r in R], float))
    for t in TASKS:
        names.append('Task: ' + t); cols.append(np.array([TASK_MAP.get(r['task_type'], 'Other') == t for r in R], float))
    for nm, f in [('log(lines changed + 1)', lambda s: math.log1p(s['lines_added'] + s['lines_deleted'])),
                  ('log(files changed + 1)', lambda s: math.log1p(s['files_changed'])),
                  ('log(commits)', lambda s: math.log(max(1, s['commits']))),
                  ('log(description words + 1)', lambda s: math.log1p(s['description_words']))]:
        x = np.array([f(r['size']) for r in R]); names.append(nm); cols.append((x - x.mean()) / x.std())
    return names, np.column_stack(cols)


def logit_cluster(X, y, clusters):
    """Logistic regression by IRLS with cluster-robust (CR1) standard errors."""
    b = np.zeros(X.shape[1])
    for _ in range(100):
        p = 1 / (1 + np.exp(-X @ b))
        step = np.linalg.solve(X.T @ (X * (p * (1 - p))[:, None]), X.T @ (y - p))
        b += step
        if np.max(np.abs(step)) < 1e-10:
            break
    p = 1 / (1 + np.exp(-X @ b))
    Hinv = np.linalg.inv(X.T @ (X * (p * (1 - p))[:, None]))
    S = X * (y - p)[:, None]
    G = collections.defaultdict(lambda: np.zeros(X.shape[1]))
    for i, c in enumerate(clusters):
        G[c] += S[i]
    meat = sum(np.outer(v, v) for v in G.values())
    nC, n, k = len(G), len(y), X.shape[1]
    V = (nC / (nC - 1)) * ((n - 1) / (n - k)) * Hinv @ meat @ Hinv
    order = np.argsort(p); ranks = np.empty(n); ranks[order] = np.arange(1, n + 1)
    n1 = y.sum(); auc = (ranks[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * (n - n1))
    return b, np.sqrt(np.diag(V)), auc


def vif(X, names):
    out = {}
    for j in range(1, X.shape[1]):
        others = np.delete(X, j, axis=1)
        beta, *_ = np.linalg.lstsq(others, X[:, j], rcond=None)
        r2 = 1 - (X[:, j] - others @ beta).var() / X[:, j].var()
        out[names[j]] = round(1 / (1 - r2), 2)
    return out


def main():
    ann = load()
    H = [r for r in ann if r['H']]
    res = {}

    # Pilot inter-rater agreement (Cohen's kappa, PABAK)
    pil = list(csv.DictReader(open(ROOT / 'data' / 'pilot_agreement.csv', encoding='utf-8')))
    pv = [(r['coder1_label'], r['coder2_label']) for r in pil if 'Cannot' not in r['coder1_label'] + r['coder2_label']]
    n = len(pv); po = sum(a == b for a, b in pv) / n
    p1 = sum(a == 'Hallucinated' for a, _ in pv) / n; p2 = sum(b == 'Hallucinated' for _, b in pv) / n
    pe = p1 * p2 + (1 - p1) * (1 - p2); kap = (po - pe) / (1 - pe)
    se = math.sqrt(po * (1 - po) / (n * (1 - pe) ** 2))
    res['pilot_agreement'] = {'n': n, 'observed_agreement': round(po, 3), 'cohens_kappa': round(kap, 2),
                              'kappa_CI95': [round(kap - 1.96 * se, 2), round(kap + 1.96 * se, 2)], 'PABAK': round(2 * po - 1, 2)}

    # RQ1
    lab = collections.Counter(r['hallucination'] for r in ann)
    res['rq1_labels'] = dict(lab)
    res['rq1_rate'] = round(lab['Hallucinated'] / len(ann), 4)
    res['rq1_rate_CI95_wilson'] = wilson(lab['Hallucinated'], len(ann))
    inst = collections.Counter(t for r in H for t in r['types'])
    tot = sum(inst.values())
    res['table1'] = {t: {'instances': inst[t], 'pct_instances': round(100 * inst[t] / tot, 1),
                         'pct_hallucinated_prs': round(100 * inst[t] / len(H), 1)} for t in TYPES}
    res['table1_total_instances'] = tot
    R = [r for r in ann if r['hallucination'] != 'Cannot Determine']
    for key, col in (('agent', 'agent'), ('task', 'task_type')):
        groups = sorted({r[col] for r in R})
        t = np.array([[sum(r[col] == g and r['H'] for r in R), sum(r[col] == g and not r['H'] for r in R)] for g in groups])
        chi, p, dof, v = cramers_v(t)
        res[f'rq1_by_{key}'] = {'chi2': round(chi, 2), 'dof': dof, 'p': p, 'cramers_v': round(v, 2),
                                'groups': {g: {'H': int(a), 'n': int(a + b), 'pct': round(100 * a / (a + b), 1)} for g, (a, b) in zip(groups, t)}}
    cod = [r for r in R if r['agent'] == 'OpenAI Codex']; oth = [r for r in R if r['agent'] != 'OpenAI Codex']
    orr, p = fisher_exact([[sum(r['H'] for r in oth), sum(not r['H'] for r in oth)],
                           [sum(r['H'] for r in cod), sum(not r['H'] for r in cod)]])
    res['rq1_other_agents_vs_codex'] = {'OR': round(orr, 2), 'p': p}
    st = collections.Counter(s for r in H for s in r['sub_types'].split('; ') if s)
    res['rq1_subtypes'] = dict(sorted(st.items()))
    res['rq1_prs_with_C1_or_C2'] = sum(any(s in ('C1', 'C2') for s in r['sub_types'].split('; ')) for r in H)

    # RQ2
    res['rq2_outcomes'] = dict(collections.Counter(r['rq2_outcome'] for r in H))
    res['rq2_revision_audit'] = {f'{k} ({AUDIT[k]})': v for k, v in
                                 sorted(collections.Counter(r['revision_audit_category'] for r in H).items())}

    # RQ3
    res['rq3_all'] = status_tests(R, sims=100000)
    res['rq3_excluding_borderline'] = status_tests([r for r in R if r['borderline'] != 'Yes'])
    by_repo = collections.defaultdict(list)
    for r in R:
        by_repo[r['repository'].lower()].append(r)
    rnd = random.Random(42)
    res['rq3_one_pr_per_repository'] = status_tests([rnd.choice(v) for v in by_repo.values()])
    res['n_repositories'] = len({r['repository'].lower() for r in ann})
    res['rq3_codex_only'] = status_tests(cod)
    S = [r for r in R if r['size']]
    for k in ('lines', 'files_changed', 'description_words'):
        f = (lambda r: r['size']['lines_added'] + r['size']['lines_deleted']) if k == 'lines' else (lambda r, k=k: r['size'][k])
        a = [f(r) for r in S if r['H']]; b = [f(r) for r in S if not r['H']]
        res[f'rq3_size_{k}'] = {'median_H': float(np.median(a)), 'median_NH': float(np.median(b)),
                                'mann_whitney_p': mannwhitneyu(a, b).pvalue}
    names, X = design(S)
    y = np.array([r['pr_state'] == 'Merged' for r in S], float)
    b, se, auc = logit_cluster(X, y, [r['repository'].lower() for r in S])
    pv = 2 * norm.sf(np.abs(b / se))
    res['rq3_regression'] = {'n': len(S), 'clusters': len({r['repository'].lower() for r in S}), 'auc': round(auc, 2),
                             'max_vif': max(vif(X, names).values()),
                             'odds_ratios': {n: {'OR': round(math.exp(bb), 2), 'CI95': [round(math.exp(bb - 1.96 * s), 2),
                                                 round(math.exp(bb + 1.96 * s), 2)], 'p': round(float(pp), 3)}
                                             for n, bb, s, pp in zip(names[1:], b[1:], se[1:], pv[1:])}}

    # RQ4
    first = collections.Counter(r['present_in_first_agent_version'] for r in H)
    res['rq4_first_version'] = dict(first)
    res['rq4_first_version_pct'] = round(100 * first['Yes'] / len(H), 1)
    res['rq4_by_initial_type'] = {t: {'present': sum(t in r['rq2_initial_type'] and r['present_in_first_agent_version'] == 'Yes' for r in H),
                                      'n': sum(t in r['rq2_initial_type'] for r in H)} for t in TYPES}

    (ROOT / 'results').mkdir(exist_ok=True)
    json.dump(res, open(ROOT / 'results' / 'results.json', 'w'), indent=1, default=float)
    print(json.dumps(res, indent=1, default=float))


if __name__ == '__main__':
    main()
