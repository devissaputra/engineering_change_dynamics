# Data Provenance and Derived Evidence

## Canonical public source

Trautsch, Erbel, Herbold, and Grabowski replication dataset.

Zenodo DOI:

`10.5281/zenodo.7078179`

Source file:

`manual_labels.csv`

## Source integrity

Zenodo reported MD5:

`a099d942098227a1fc8127759e55850e`

Release verified SHA 256:

`e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941`

## Source dimensions

- 2,533 manually classified commits
- 54 Java Apache projects
- perfective, corrective, other taxonomy

## Raw file policy

The raw source CSV is not republished in this repository.

The Zenodo record is open but does not display a specific dataset license value. The release therefore stores derived aggregates and rebuilds them from Zenodo during verification.

## Packaged evidence

- `derived/project_composition.csv`: all 54 project profiles and Wilson intervals
- `derived/category_summary.csv`: pooled category composition
- `derived/heterogeneity_results.csv`: sample threshold sensitivity
- `derived/project_residuals.csv`: full table residual diagnostics
- `derived/primary_project_residuals.csv`: primary subset cell diagnostics
- `derived/primary_project_contributions.csv`: primary subset project contributions

## Rebuild

Run:

```bash
python scripts/fetch_and_analyze.py --check
```

The rebuild verifies both source checksums before reconstructing and checking the complete released evidence.

There is no synthetic fallback.
