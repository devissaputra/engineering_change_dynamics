# Empirical Study Protocol

## Study title

**Cross-Project Heterogeneity in Quality-Oriented Engineering Change**

## Study type

Secondary observational analysis of manually classified maintenance intent across Java Apache projects.

This document records the released analysis and is not a preregistration.

## Research questions

**RQ1.** What is the pooled composition of perfective, corrective, and other commits?

**RQ2.** Does maintenance intent composition vary across projects beyond sampling variation?

**RQ3.** Is the estimated cross project association stable after removing increasingly small project samples?

**RQ4.** Which projects and category cells contribute most strongly to the omnibus heterogeneity?

## Source

Trautsch, Erbel, Herbold, and Grabowski replication dataset.

Zenodo DOI:

`10.5281/zenodo.7078179`

Source file:

`manual_labels.csv`

Released source dimensions:

- 2,533 commits
- 54 Java Apache projects

## Classification

The source labels are reconstructed as three mutually exclusive categories:

- **perfective**: internal quality improvement intent;
- **corrective**: external quality improvement intent;
- **other**: neither of the above under the source coding scheme.

Rows in which both quality flags are true are treated as invalid because they violate the source taxonomy invariant.

## Sampling

The source paper reports a random sample of approximately 2% of eligible commits per project, rounded up, for manual classification.

## Pooled estimand

For each category:

- count;
- share of all 2,533 manually classified commits;
- 95% Wilson interval.

## Project estimand

For each project and category:

- count;
- project specific share;
- 95% Wilson interval.

## Primary heterogeneity analysis

Construct the project by category contingency table.

The full 54 project table contains 21 expected cells below 5.

The primary inferential subset therefore includes projects with at least 20 labeled commits.

Released primary result:

- 43 projects;
- 2,374 commits;
- chi square(84) = 432.452175;
- p = 2.4645853238931284e-48;
- Cramér's V = 0.301796;
- minimum expected count = 5.794019;
- zero expected cells below 5.

## Sensitivity

Repeat the same analysis at minimum project sizes:

- 10;
- 20;
- 30;
- 40;
- 50.

The full 54 project table is retained as descriptive and sensitivity evidence rather than treated as the primary asymptotic test.

## Cell diagnostics

Compute Pearson residuals:

```text
(observed - expected) / sqrt(expected)
```

Residuals describe which project and category cells contribute strongly to the omnibus difference.

They are not separately multiplicity adjusted hypothesis tests.

## Project contribution diagnostic

For every project in the primary subset, sum its three cell chi square contributions:

```text
sum((observed - expected)^2 / expected)
```

The sum of all project contributions equals the primary chi square statistic.

This diagnostic provides a project level decomposition without converting the result into a quality ranking.

## Validity boundary

The analysis describes maintenance intent composition in a manually sampled Apache dataset.

It does not estimate requirements churn, engineering change cost, schedule impact, project quality, productivity, or causal project effects.

The current analysis is cross project rather than longitudinal and does not support a temporal dynamics claim.
