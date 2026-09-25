# Research Bundle Definition

This repository is treated as a research bundle because it links one explicit research question to a named empirical source, a documented operationalization, executable analysis code, derived evidence, reproducibility checks, visual evidence, validity boundaries, and a paper-ready interpretation path.

## Question
How frequently do observed engineering changes target internal versus external software quality, and how heterogeneous is that orientation across projects?

## Empirical core
Manual-label aggregation and cross-project heterogeneity.

## Main result
Among 2,533 manually classified commits, 40.3% are internal-quality changes, 27.0% external-quality changes, and 32.6% neither. Project-level internal-quality shares range from 0.130 to 0.818, demonstrating strong heterogeneity in observed change orientation.

## Boundary
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.

## Release criterion
A release passes only if source provenance, code, derived tables, JSON summary, README claims, figures, and tests agree numerically and semantically.
