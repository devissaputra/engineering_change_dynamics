# Reproducibility Guide

## Objective

The release supports two verification routes:

1. offline recomputation from the packaged project level evidence;
2. online reconstruction from the public Zenodo source.

## Environment

```bash
python -m pip install -r requirements.txt
```

## Offline verification

```bash
pytest -q
python run_demo.py
python scripts/generate_figures.py
```

The tests verify:

- 54 projects;
- 2,533 manually classified commits;
- exact pooled category counts;
- the mutually exclusive taxonomy;
- Wilson interval behavior;
- all released heterogeneity thresholds;
- the primary chi square and Cramér's V;
- expected cell diagnostics;
- primary residual diagnostics;
- project contribution decomposition;
- machine readable summary consistency;
- full bundle validation.

## Public source rebuild

```bash
python scripts/fetch_and_analyze.py --check
```

The rebuild:

1. downloads `manual_labels.csv` from Zenodo;
2. verifies MD5 `a099d942098227a1fc8127759e55850e`;
3. verifies SHA 256 `e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941`;
4. verifies the source taxonomy invariant;
5. reconstructs the complete 54 project composition table;
6. recomputes pooled composition and Wilson intervals;
7. recomputes all heterogeneity threshold analyses;
8. recomputes full and primary residual diagnostics;
9. recomputes primary project contributions;
10. compares the rebuilt evidence with the packaged release.

## Evidence map

| Claim | Primary evidence |
|---|---|
| 2,533 commits and 54 projects | `project_composition.csv` and source rebuild |
| Pooled composition | `category_summary.csv` |
| Primary heterogeneity | `heterogeneity_results.csv` |
| Sample threshold robustness | `heterogeneity_results.csv` |
| Cell departures | `project_residuals.csv` and source rebuild |
| Primary project contributions | `primary_project_contributions.csv` |
| Headline release values | `results/empirical_summary.json` |
| Source integrity | `data/source_manifest.json` |

## Failure policy

There is no synthetic fallback.

Checksum drift, source dimension changes, invalid taxonomy rows, aggregate mismatches, inference mismatches, or diagnostic mismatches cause the source verification to fail.

## Reproducibility boundary

Computational reproducibility confirms the released analysis for this source dataset. It does not establish external generalization or causal explanation.
