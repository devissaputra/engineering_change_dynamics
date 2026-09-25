# Final QA Report

**Release status: PENDING GITHUB-HOSTED VERIFICATION AFTER SCIENTIFIC REPAIR.**

## Scientific repairs completed
- replaced the incorrect four-state/phi framing with the source's perfective/corrective/other taxonomy;
- removed the phi coefficient from results and interpretation;
- packaged the complete 54-project aggregate table rather than a top-10 subset;
- added 95% Wilson intervals for every project-category share;
- added project×category chi-square heterogeneity analysis and Cramér's V;
- selected n≥20 as the primary inferential subset because all expected cells then exceed 5;
- added n≥30/40/50 sample-size sensitivity analyses;
- added complete project-category Pearson residual diagnostics;
- removed stale deleted-repository references;
- added source MD5 enforcement, public-source rebuild, regular CI, and reproducible figures;
- restored the complete MIT license;
- synchronized README, protocol, design, analysis plan, paper blueprint, references, provenance, citation metadata, and manifest.

## Verified packaged headline
- commits: **2,533**
- projects: **54**
- perfective: **1,022 (40.3%)**
- corrective: **685 (27.0%)**
- other: **826 (32.6%)**
- primary n≥20: **43 projects / 2,374 commits**
- χ²(84): **432.452175**
- p: **≈2.46×10⁻⁴⁸**
- Cramér's V: **0.301796**
- n≥30 sensitivity Cramér's V: **0.29979**

## Release condition
Mark PASS only after regular CI and the Zenodo empirical rebuild both succeed on the final release commit.
