# Final QA Report

## Release verdict

**Status: PASS after the current full research package rebuild.**

This file verifies release consistency. The scientific narrative is in [REPORT.md](REPORT.md).

## Source verification

Verified against the Trautsch et al. Zenodo source:

- DOI: 10.5281/zenodo.7078179
- source file: manual_labels.csv
- Zenodo MD5: a099d942098227a1fc8127759e55850e
- release SHA 256: e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941
- source commits: 2,533
- source projects: 54
- raw source redistributed: no

The peer reviewed source paper confirms the manual random sample, approximately 2% per project rounded up, and the perfective, corrective, other coding scheme.

## Scientific corrections retained

The repository no longer treats internal quality and external quality as independent binary constructs.

The release follows the source taxonomy directly:

- perfective;
- corrective;
- other.

No phi coefficient is used.

## Released empirical results

| Check | Result | Status |
|---|---:|---|
| Projects | 54 | PASS |
| Commits | 2,533 | PASS |
| Perfective | 1,022 | PASS |
| Corrective | 685 | PASS |
| Other | 826 | PASS |
| Primary minimum n | 20 | PASS |
| Primary projects | 43 | PASS |
| Primary commits | 2,374 | PASS |
| Primary chi square | 432.452175 | PASS |
| Primary df | 84 | PASS |
| Primary Cramér's V | 0.301796 | PASS |
| Minimum expected count | 5.794019 | PASS |
| Expected cells below 5 | 0 | PASS |

## Sensitivity verification

Cramér's V:

- n at least 10: 0.305165
- n at least 20: 0.301796
- n at least 30: 0.299790
- n at least 40: 0.292777
- n at least 50: 0.292908

The effect remains stable after progressively excluding small project samples.

## Diagnostic verification

The release checks:

- full 54 project residual evidence;
- primary n at least 20 residual diagnostics;
- primary project chi square contributions;
- agreement between the sum of project contributions and the primary chi square statistic.

The primary diagnostic pattern includes Phoenix corrective as the largest positive residual and PDFBox other as the largest negative residual.

## Presentation repairs

The current rebuild:

- adds a real `REPORT.md`;
- expands the paper blueprint into a manuscript ready structure;
- replaces the generic first image with a scientific cross project composition visualization;
- rebuilds the method, composition, residual, sensitivity, and evidence figures with semantic color;
- updates the figure generator so future regeneration preserves the new visual system;
- updates the public portfolio summary and points Report MD to the scientific report;
- distinguishes project level heterogeneity from project quality judgments;
- makes the absence of temporal dynamics explicit.

## Reproducibility

PASS requires:

- offline tests;
- complete bundle validation;
- reproducible SVG generation;
- Zenodo checksum verification;
- complete source reconstruction;
- exact released result agreement.

## Interpretation boundary

A PASS indicates that the repository is internally consistent and reproducible for the stated secondary analysis.

It does not establish causal project effects, organization wide generalization, engineering change cost, schedule impact, or project performance rankings.
