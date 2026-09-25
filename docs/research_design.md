# Research Design

## Research question
How frequently do observed engineering changes target internal versus external software quality, and how heterogeneous is that orientation across projects?

## Design
Secondary observational analysis of 2,533 manually coded commits from 54 Java Apache projects.

## Source and unit of analysis
Source: SmartSHARK commit-intent replication dataset (Trautsch et al.). The operational unit follows the public dataset and is documented in `data/source_manifest.json` and `docs/data_dictionary.md`.

## Hypotheses
1. H1: internal-quality changes constitute a substantial share of observed engineering work.
2. H2: project-level internal- and external-quality shares vary materially rather than following one portfolio-wide pattern.

## Method
Parse the manually coded commit sample, classify each commit into internal-quality only, external-quality only, both, or neither, and compute overall and project-level shares. The packaged project table intentionally shows the ten projects with the largest sampled commit counts; portfolio extrema are computed over all 54 projects.

## Validity boundary
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.
