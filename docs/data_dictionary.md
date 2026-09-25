# Data Dictionary

## Provenance
See `data/source_manifest.json`. Raw source observations are not silently republished.

## `data/derived/primary_results.csv`
Ten projects with the largest sampled commit counts; portfolio-wide counts and extrema use all 54 projects.

## `data/derived/secondary_results.csv`
When present and non-empty, this contains a second derived table needed to reproduce a reported comparison. If empty, no second packaged table is required.

## `results/empirical_summary.json`
Machine-readable headline sample sizes, estimates, and the release finding. Values must agree with README text and the derived CSVs.

## Construct boundary
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.
