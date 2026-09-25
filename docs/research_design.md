# Research Design

## Research problem

How much does manually observed software maintenance intent composition differ across projects, and how robust is that difference to unequal project sample sizes?

## Unit of analysis

One manually classified commit nested within one Java Apache project.

## Source sampling

The source study reports a random sample of approximately 2% of eligible commits per project, rounded up.

This produces unequal project sample sizes and motivates explicit project level uncertainty.

## Classification

The source taxonomy contains three mutually exclusive categories:

- perfective;
- corrective;
- other.

Perfective is mapped by the source authors to internal quality improvement intent.

Corrective is mapped to external quality improvement intent.

## Evidence layers

The release separates four layers:

1. pooled category composition;
2. project specific composition with Wilson intervals;
3. omnibus cross project heterogeneity;
4. residual and project contribution diagnostics.

## Primary inference

The complete 54 project contingency table contains 21 expected cells below 5.

The primary inferential subset therefore uses projects with at least 20 manually labeled commits.

All expected cells in that subset exceed 5.

## Robustness

The same effect size is recomputed at minimum project sample sizes of 10, 20, 30, 40, and 50.

The purpose is not to identify one uniquely correct cutoff. The purpose is to show whether the estimated association is sensitive to the smallest project samples.

## Diagnostic decomposition

Pearson residuals identify category specific departures.

Project contributions sum the three cell chi square contributions for each retained project.

These diagnostics explain the omnibus result without turning projects into quality rankings.

## Construct boundary

The study measures manually classified maintenance intent in commit messages.

It does not directly measure requirements change, change propagation, engineering rework, cost, schedule, productivity, or delivered product quality.

## Temporal boundary

The present analysis aggregates commits within projects.

It does not model when commits occurred and therefore does not support a temporal dynamics claim.
