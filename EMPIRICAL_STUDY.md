# Empirical Study Protocol

## Study
Quality-Oriented Engineering Change Dynamics in Apache Projects

## Research question
How frequently do observed engineering changes target internal versus external software quality, and how heterogeneous is that orientation across projects?

## Design and source
Secondary observational analysis of 2,533 manually coded commits from 54 Java Apache projects. Source: SmartSHARK commit-intent replication dataset (Trautsch et al.). Analysis/retrieval date: 2026-09-25.

## Hypotheses
1. H1: internal-quality changes constitute a substantial share of observed engineering work.
2. H2: project-level internal- and external-quality shares vary materially rather than following one portfolio-wide pattern.

## Operationalization and method
Parse the manually coded commit sample, classify each commit into internal-quality only, external-quality only, both, or neither, and compute overall and project-level shares. The packaged project table intentionally shows the ten projects with the largest sampled commit counts; portfolio extrema are computed over all 54 projects.

## Primary empirical result
Among 2,533 manually classified commits, 40.3% are internal-quality changes, 27.0% external-quality changes, and 32.6% neither. Project-level internal-quality shares range from 0.130 to 0.818, demonstrating strong heterogeneity in observed change orientation.

## Validity and claim boundary
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.

## Reproducibility status
The repository packages derived results, study-specific analysis functions, deterministic or seeded procedures where relevant, an internet-enabled source rebuild script, and tests for both computations and critical scientific invariants. The released analysis was documented after dataset selection and should not be represented as preregistered.
