# Analysis Plan

## Status
This documents the corrected released analysis. It is **not a preregistration**.

## RQ1 — pooled composition
Count perfective, corrective, and other commits and report pooled shares with 95% Wilson intervals.

## RQ2 — project heterogeneity
Construct the complete project×category contingency table.

Because the full 54-project table contains 21 expected cells below 5, use projects with n≥20 as the primary Pearson chi-square analysis. Report χ², df, p-value, Cramér's V, minimum expected count, and number of expected cells below 5.

## RQ3 — small-sample sensitivity
Repeat at minimum project sizes of 30, 40, and 50. The full n≥10 table is retained as a descriptive/sensitivity result rather than relied upon as the primary asymptotic test.

## RQ4 — contribution diagnostics
Compute Pearson residuals for every project-category cell against pooled proportions. Use them to describe which cells contribute strongly to the omnibus heterogeneity, without treating them as multiplicity-adjusted individual tests.

## Confidence intervals
Use 95% Wilson intervals for each project-category proportion.

## No phi coefficient
Do not compute or interpret phi between the two source flags. The source ground truth is a three-category maintenance taxonomy, not two independent binary constructs.

## Exclusions
No source commit is dropped from pooled descriptive counts. Only the inferential sensitivity subsets apply project-level sample-size thresholds.
