# Data Dictionary

## `project_composition.csv`
Complete 54-project aggregate table:
- project name;
- manually labeled sample size;
- perfective/corrective/other counts;
- category shares;
- 95% Wilson interval bounds for each share.

This table is sufficient for offline reproduction of pooled counts and project×category heterogeneity tests.

## `category_summary.csv`
Pooled category counts, shares, and 95% Wilson intervals.

## `heterogeneity_results.csv`
Omnibus project×category results at minimum project sample sizes 10, 20, 30, 40, and 50.

## `project_residuals.csv`
All 54×3 Pearson residuals relative to pooled category proportions.

## `results/empirical_summary.json`
Headline counts and the primary/sensitivity heterogeneity results.

## Raw source
The 2,533-row Zenodo source is not redistributed because the Zenodo record does not display a specific dataset-license value. The online rebuild downloads and verifies it directly.
