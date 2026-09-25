# Analysis Plan

## Status

This document records the released secondary analysis. It is not a preregistration.

## RQ1: pooled maintenance intent

Count perfective, corrective, and other commits across the complete manually classified sample.

Report:

- count;
- share;
- 95% Wilson interval.

## RQ2: cross project heterogeneity

Construct a project by category contingency table.

The complete 54 project table contains 21 expected cells below 5. It is retained descriptively and in the sensitivity series.

The primary asymptotic analysis uses projects with at least 20 labeled commits, where every expected cell exceeds 5.

Report:

- number of retained projects;
- retained commit count;
- chi square;
- degrees of freedom;
- p value;
- Cramér's V;
- minimum expected cell count;
- count of expected cells below 5.

## RQ3: sample size sensitivity

Repeat the same heterogeneity calculation at minimum project sample sizes:

- 10;
- 20;
- 30;
- 40;
- 50.

The principal robustness question is whether Cramér's V changes materially as progressively smaller projects are removed.

## RQ4: contribution diagnostics

Use two complementary diagnostics.

### Cell level residuals

Compute Pearson residuals for every project and category cell.

Use the primary n at least 20 residuals for the main interpretation.

Retain the full 54 project residual table as supplementary descriptive evidence.

Residuals are not interpreted as individually multiplicity adjusted hypothesis tests.

### Project level contributions

For each project in the primary subset, sum its three cell contributions to the chi square statistic.

Verify that all project contributions sum exactly to the primary chi square result.

## Confidence intervals

Use 95% Wilson intervals for every project and category proportion.

Intervals are descriptive component intervals within a multinomial composition.

## Taxonomy rule

Do not compute or interpret phi between source quality flags.

The source labels represent a mutually exclusive three category taxonomy:

- perfective;
- corrective;
- other.

## Exclusions

No source commit is removed from the pooled descriptive results.

Only project sample size thresholds are used for inferential sensitivity analyses.

## Interpretation constraints

Do not convert maintenance intent composition into:

- project quality rankings;
- productivity rankings;
- causal explanations;
- cost estimates;
- requirements churn;
- temporal dynamics.
