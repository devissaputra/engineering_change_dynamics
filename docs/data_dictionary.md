# Data Dictionary

## `project_composition.csv`

Complete 54 project aggregate table.

Columns include:

- project name;
- manually labeled sample size;
- perfective count;
- corrective count;
- other count;
- project specific category shares;
- lower and upper 95% Wilson interval bounds for every category share.

## `category_summary.csv`

Pooled category summary across all 2,533 manually labeled commits.

Fields:

- category;
- count;
- share;
- Wilson interval lower bound;
- Wilson interval upper bound.

## `heterogeneity_results.csv`

One row per minimum project sample threshold:

- 10;
- 20;
- 30;
- 40;
- 50.

Fields:

- retained projects;
- retained commits;
- chi square;
- degrees of freedom;
- p value;
- Cramér's V;
- minimum expected count;
- number of expected cells below 5.

## `project_residuals.csv`

All 54 by 3 Pearson residual diagnostics relative to the full pooled composition.

This file is supplementary because the full table contains small expected counts.

## `primary_project_residuals.csv`

Pearson residuals for the primary n at least 20 subset.

Fields:

- project;
- category;
- observed count;
- expected count;
- Pearson residual;
- cell chi square contribution.

## `primary_project_contributions.csv`

One row per project retained in the primary n at least 20 analysis.

Fields:

- project;
- manually labeled sample size;
- project chi square contribution;
- share of the primary chi square statistic.

All project contributions sum to the primary chi square statistic.

## `results/empirical_summary.json`

Machine readable headline counts, primary inference, sensitivity values, and leading diagnostic results.

## Raw source

The 2,533 row Zenodo source is not redistributed because the Zenodo record does not display a specific dataset license value.

The online rebuild downloads and verifies it directly.
