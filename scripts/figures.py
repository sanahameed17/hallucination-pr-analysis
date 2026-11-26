"""Regenerates the data figures of the paper (Fig. 3, Fig. 4, and Fig. 5) from the released data.

Usage (from the repository root):
    python scripts/figures.py            # writes PDFs to figures/

Requires: Python 3.10+, numpy, matplotlib
"""
import collections
import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 9.5, 'pdf.fonttype': 42})
BLUE, ORANGE = '#2E5A88', '#E07B1A'
TYPES = ['Requirement-Conflicting', 'Knowledge-Related', 'Code-Inconsistency']

ann = list(csv.DictReader(open(ROOT / 'data' / 'annotations.csv', encoding='utf-8')))
R = [r for r in ann if r['hallucination'] != 'Cannot Determine']
for r in R:
    r['H'] = r['hallucination'] == 'Hallucinated'


def wilson(k, n, z=1.96):
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h


# ---- Fig. 3: hallucination rates by agent and task type (groups with at least 20 PRs)
fig, axs = plt.subplots(1, 2, figsize=(7.4, 3.1), gridspec_kw={'width_ratios': [1, 1.2]})
overall = sum(r['H'] for r in R) / len(R)
for ax, col, title in [(axs[0], 'agent', '(a) By agent'), (axs[1], 'task_type', '(b) By task type')]:
    groups = collections.Counter(r[col] for r in R)
    G = [(g, sum(r['H'] for r in R if r[col] == g), n) for g, n in groups.items() if n >= 20]
    G.sort(key=lambda z: z[1] / z[2])
    for i, (g, k, n) in enumerate(G):
        lo, hi = wilson(k, n)
        ax.plot([100 * lo, 100 * hi], [i, i], color=BLUE, lw=1.6)
        ax.plot(100 * k / n, i, 'o', color=BLUE, ms=6)
        ax.text(103, i, f'{100 * k / n:.1f}% ({k}/{n})', va='center', fontsize=7.5)
    ax.set_yticks(range(len(G))); ax.set_yticklabels([g for g, _, _ in G])
    ax.axvline(100 * overall, color=ORANGE, ls='--', lw=1); ax.set_xlim(0, 100)
    ax.set_xlabel('Hallucinated PRs (%)', fontsize=8.5); ax.set_title(title, fontsize=9.5, loc='left')
    ax.tick_params(labelsize=8)
    for s in ['top', 'right']:
        ax.spines[s].set_visible(False)
fig.tight_layout(); fig.subplots_adjust(wspace=0.95, right=0.86)
fig.savefig(OUT / 'Fig3_Rates_by_Agent_and_Task.pdf'); plt.close(fig)

# ---- Fig. 4: hallucination categories by agent (% of each agent's hallucinated PRs)
agents = [a for a, _ in collections.Counter(r['agent'] for r in R).most_common()]
M = np.array([[100 * sum(t in r['hallucination_types'] for r in R if r['agent'] == a and r['H'])
               / max(1, sum(r['H'] for r in R if r['agent'] == a)) for t in TYPES] for a in agents])
N = [sum(r['H'] for r in R if r['agent'] == a) for a in agents]
fig, ax = plt.subplots(figsize=(5.6, 2.9))
im = ax.imshow(M, cmap='Blues', vmin=0, vmax=100, aspect='auto')
for i in range(len(agents)):
    for j in range(3):
        ax.text(j, i, f'{M[i, j]:.0f}%', ha='center', va='center', color='white' if M[i, j] > 55 else '#222', fontsize=9)
ax.set_xticks(range(3)); ax.set_xticklabels(['Requirement-\nConflicting', 'Knowledge-\nRelated', 'Code-\nInconsistency'])
ax.set_yticks(range(len(agents))); ax.set_yticklabels([f'{a} (n={n})' for a, n in zip(agents, N)])
cb = fig.colorbar(im, ax=ax, fraction=0.04); cb.set_label('% of hallucinated PRs', fontsize=8)
fig.tight_layout(); fig.savefig(OUT / 'Fig4_Categories_by_Agent.pdf'); plt.close(fig)

# ---- Fig. 5: initial-to-final outcomes of hallucinated PRs (RQ2)
H = [r for r in R if r['H']]
q = collections.Counter(r['rq2_outcome'] for r in H)
labs = [o for o in ['Persistence', 'Correction', 'Transformation'] if o in q]
v = [q[o] for o in labs]
fig, ax = plt.subplots(figsize=(7, 2.2))
ax.barh(labs[::-1], v[::-1], color=BLUE, height=0.6)
for i, x in enumerate(v[::-1]):
    ax.text(x + len(H) * 0.01, i, f'{x} ({100 * x / len(H):.1f}%)', va='center')
ax.set_xlabel('Number of Hallucinated Pull Requests'); ax.set_xlim(0, max(v) * 1.22)
for s in ['top', 'right']:
    ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(OUT / 'Fig5_RQ2_Outcomes.pdf'); plt.close(fig)
print('Figures written to', OUT)
