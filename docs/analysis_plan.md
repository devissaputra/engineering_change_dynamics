# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary estimand / descriptive target
How frequently do observed engineering changes target internal versus external software quality, and how heterogeneous is that orientation across projects?

## Analysis
Parse the manually coded commit sample, classify each commit into internal-quality only, external-quality only, both, or neither, and compute overall and project-level shares. The packaged project table intentionally shows the ten projects with the largest sampled commit counts; portfolio extrema are computed over all 54 projects.

## Specified outputs for this release
1. source/sample size and provenance;
2. primary derived metric(s);
3. comparator, cross-group, cross-time, or frontier contrast where applicable;
4. uncertainty, sensitivity, or error information supported by the source;
5. explicit construct and external-validity limitations.

## Missingness / exclusions

All 2,533 manually coded commits in the released SmartSHARK sample are retained. No commit labels are inferred or imputed. The top-10 project table is a display subset only; project-level extrema are calculated across all 54 projects.

## Interpretation boundary
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.
