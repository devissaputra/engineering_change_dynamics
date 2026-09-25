# Final QA Report

**Research bundle status: PASS.**  
**Current CI status: PASS.**  
**Current Zenodo empirical rebuild status: PASS.**

## Scientific corrections completed
- replaced the incorrect four-state/phi framing with the source's **perfective / corrective / other** taxonomy;
- removed the phi coefficient from code, results, figures, and interpretation;
- packaged the complete **54-project** aggregate evidence rather than a top-10 display subset;
- added 95% Wilson intervals for every project-category share;
- added project×category chi-square heterogeneity analysis and Cramér's V;
- selected **n≥20** as the primary inferential subset because all expected cells then exceed 5;
- added n≥30/40/50 sample-size sensitivity analyses;
- added complete project-category Pearson residual diagnostics;
- removed stale references to the deleted `student_grade_regression` repository;
- added public-source integrity checks, CI, source rebuild CI, and reproducible figures;
- restored the complete MIT license;
- synchronized README, protocol, design, analysis plan, paper blueprint, references, provenance, citation metadata, results, and manifest.

## Verified source integrity
- Zenodo DOI: **10.5281/zenodo.7078179**
- source file: **manual_labels.csv**
- Zenodo MD5: **a099d942098227a1fc8127759e55850e**
- verified SHA-256: **e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941**
- source rows: **2,533**
- source projects: **54**
- raw source redistributed: **no**

## Verified empirical release
- perfective: **1,022 (40.3%)**
- corrective: **685 (27.0%)**
- other: **826 (32.6%)**
- primary n≥20 analysis: **43 projects / 2,374 commits**
- χ²(84): **432.452175**
- p: **2.46×10⁻⁴⁸**
- Cramér's V: **0.301796**
- minimum expected count: **5.794**
- expected cells below 5: **0**
- n≥30 sensitivity Cramér's V: **0.299790**
- full 54-project table Cramér's V: **0.305165**, with 21 expected cells below 5 and therefore retained as descriptive/sensitivity evidence rather than the primary asymptotic test.

## GitHub-hosted verification
- **CI:** PASS
- **Zenodo empirical rebuild:** PASS
- **source hash enforcement:** PASS
- **complete 54-project recomputation:** PASS
- **reproducible SVG generation:** PASS
- **full MIT license:** PASS

## Interpretation boundary
The study supports material heterogeneity in maintenance-intent composition across the sampled Apache projects. It does not measure requirements churn, design propagation, rework cost, schedule impact, causal project effects, or all software organizations.

No open scientific, source-provenance, data, code, test, CI, figure, reproducibility, licensing, or documentation defect remains in this QA release.
