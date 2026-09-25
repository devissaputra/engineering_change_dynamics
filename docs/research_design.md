# Research Design

## Research question
How heterogeneous is manually classified maintenance-intent composition across Apache projects?

## Unit of analysis
One manually classified commit nested within one Apache Java project.

## Source sampling
The original study randomly sampled approximately 2% of eligible commits per project, rounded up, for manual classification.

## Classification
Perfective, corrective, or other. The source authors map perfective to internal-quality improvement intent and corrective to external-quality improvement intent.

## Project-level uncertainty
Small project samples can generate extreme raw proportions. The released bundle therefore reports Wilson intervals and does not use min/max proportions alone as evidence.

## Omnibus inference
Primary heterogeneity analysis is restricted to projects with n≥20 so all expected contingency-table counts exceed 5. Effect-size stability is checked at n≥30, 40, and 50.

## Construct boundary
This is software-maintenance intent, not a direct measure of requirements change, engineering-change propagation, rework cost, or schedule risk.
