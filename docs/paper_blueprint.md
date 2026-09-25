# Paper Blueprint

## Working title
Quality-Oriented Engineering Change Dynamics in Apache Projects

## Motivation
Engineering-management portfolios contain different mixes of maintenance, externally visible change, and internal-quality work. A manually coded multi-project sample makes it possible to quantify that orientation without inferring intent from commit-message keywords alone.

## Research question
How frequently do observed engineering changes target internal versus external software quality, and how heterogeneous is that orientation across projects?

## Data and method
Parse the manually coded commit sample, classify each commit into internal-quality only, external-quality only, both, or neither, and compute overall and project-level shares. The packaged project table intentionally shows the ten projects with the largest sampled commit counts; portfolio extrema are computed over all 54 projects.

## Results to report
Among 2,533 manually classified commits, 40.3% are internal-quality changes, 27.0% external-quality changes, and 32.6% neither. Project-level internal-quality shares range from 0.130 to 0.818, demonstrating strong heterogeneity in observed change orientation. Report the packaged headline metrics and the full relevant derived table; do not cherry-pick only the strongest contrast.

## Robustness / sensitivity
The release checks portfolio totals across all 2,533 labeled commits and computes project-level shares across all 54 projects. The displayed CSV intentionally contains only the ten projects with the largest labeled samples, while reported minima and maxima are calculated over the complete 54-project set. No claim is made that the sample is representative of all software organizations.

## Limitations
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.

## Publication integrity
Do not describe this repository as peer reviewed, preregistered, or externally validated unless those events actually occur. Distinguish analysis of public data from original data collection.
