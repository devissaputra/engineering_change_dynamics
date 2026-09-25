# Cross-Project Heterogeneity in Quality-Oriented Engineering Change

[![CI](https://github.com/devissaputra/engineering_change_dynamics/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/engineering_change_dynamics/actions/workflows/ci.yml)
[![Zenodo source rebuild](https://github.com/devissaputra/engineering_change_dynamics/actions/workflows/empirical-rebuild.yml/badge.svg)](https://github.com/devissaputra/engineering_change_dynamics/actions/workflows/empirical-rebuild.yml)

> **System Engineering Research Package** · Engineering Management Research · Software Intensive Systems · Maintenance Intent

A reproducible secondary study of **2,533 manually classified commits across 54 Java Apache projects**. The analysis asks whether the observed mix of perfective, corrective, and other maintenance intent is similar across projects or whether pooled averages hide materially different local profiles.

![Cross project composition](assets/architecture.svg)

## Start here

- [Scientific report](REPORT.md)
- [Empirical study protocol](EMPIRICAL_STUDY.md)
- [Paper blueprint](docs/paper_blueprint.md)
- [Analysis plan](docs/analysis_plan.md)
- [Research design](docs/research_design.md)
- [Reproducibility guide](REPRODUCIBILITY.md)
- [Data provenance](data/README.md)
- [Final QA evidence](QA_REPORT.md)

## Research questions

1. What is the pooled composition of perfective, corrective, and other commits?
2. Does maintenance intent composition vary across projects?
3. Is the estimated heterogeneity robust when small project samples are removed?
4. Which projects and category combinations contribute most strongly to the heterogeneity?

## Source

| Item | Value |
|---|---|
| Dataset | Trautsch et al. replication dataset |
| Zenodo DOI | 10.5281/zenodo.7078179 |
| Source file | `manual_labels.csv` |
| Commits | 2,533 |
| Projects | 54 Java Apache projects |
| Manual coding | Two researchers with disagreement resolution |
| Source sample | Approximately 2% of eligible commits per project, rounded up |
| Raw source redistributed | No |

The peer reviewed source study classifies commit intent as **perfective, corrective, or other**. Perfective corresponds to internal quality improvement intent and corrective to external quality improvement intent.

## Why the taxonomy matters

An earlier prototype treated the source internal quality and external quality fields as independent binary variables.

That was incorrect for this dataset.

The source study defines a three category ground truth. The released package therefore reconstructs:

```text
perfective | corrective | other
```

and rejects any impossible row in which both quality flags are true.

## Pooled composition

| Category | Count | Share | 95% Wilson interval |
|---|---:|---:|---:|
| Perfective | 1,022 | 40.3% | 38.5% to 42.3% |
| Corrective | 685 | 27.0% | 25.3% to 28.8% |
| Other | 826 | 32.6% | 30.8% to 34.5% |

![Pooled composition](assets/category_composition.svg)

The pooled sample is useful as a portfolio summary, but it is not representative of every project.

## Primary cross project result

The complete 54 project table contains 21 expected cells below 5. The primary inferential analysis therefore uses projects with at least 20 manually labeled commits.

For **43 projects and 2,374 commits**:

| Statistic | Result |
|---|---:|
| Chi square | 432.452175 |
| Degrees of freedom | 84 |
| p value | 2.46 × 10^-48 |
| Cramér's V | 0.301796 |
| Minimum expected count | 5.794019 |
| Expected cells below 5 | 0 |

The result shows that maintenance intent composition differs across the sampled projects.

![Project heterogeneity](assets/project_heterogeneity.svg)

## What the heterogeneity looks like

The project profiles are not minor variations around one common mix.

Examples:

- **Phoenix:** 14.6% perfective, 52.9% corrective, 32.5% other
- **Commons Lang:** 75.8% perfective, 9.1% corrective, 15.2% other
- **Commons Math:** 70.2% perfective, 10.6% corrective, 19.1% other
- **PDFBox:** 48.8% perfective, 41.6% corrective, only 9.6% other
- **NiFi:** 18.2% perfective, 27.3% corrective, 54.5% other

These are descriptive maintenance profiles, not project quality rankings.

## Sensitivity to project sample size

| Minimum project n | Projects | Commits | Cramér's V |
|---:|---:|---:|---:|
| 10 | 54 | 2,533 | 0.305165 |
| 20 | 43 | 2,374 | 0.301796 |
| 30 | 34 | 2,159 | 0.299790 |
| 40 | 25 | 1,864 | 0.292777 |
| 50 | 17 | 1,506 | 0.292908 |

![Sensitivity](assets/sensitivity.svg)

The effect remains near 0.30 even as smaller project samples are progressively removed.

## Which projects drive the result?

For the primary n at least 20 analysis, the largest project level contributions to the chi square statistic include:

| Project | Contribution | Share of primary chi square |
|---|---:|---:|
| Phoenix | 61.145 | 14.1% |
| PDFBox | 42.270 | 9.8% |
| Commons Math | 37.173 | 8.6% |
| Commons Lang | 36.067 | 8.3% |
| Tez | 21.164 | 4.9% |

The largest cell level Pearson residual is Phoenix corrective at approximately **+6.03** in the primary subset.

These diagnostics explain the omnibus result. They are not separate adjusted significance tests.

## Engineering management interpretation

The result does **not** mean that projects with different maintenance profiles are better or worse.

It means a portfolio average can conceal large differences in local engineering work.

Project level maintenance ratios should therefore be interpreted with:

- local project context;
- sample size;
- uncertainty;
- the project's actual development and maintenance conditions.

## What this study contributes

The source publication focuses mainly on how developer maintenance intent relates to software metrics and static analysis warnings.

This repository asks a different secondary question:

> How heterogeneous is the manually observed maintenance intent composition across projects?

The contribution is the combination of complete project composition evidence, uncertainty intervals, an omnibus heterogeneity test, sample size sensitivity, and project level contribution diagnostics.

## Claim boundary

**Supported:** maintenance intent composition is materially heterogeneous across the sampled Apache projects and this pattern is stable under progressively stricter project sample thresholds.

**Not supported:** causal project effects, project quality rankings, requirements churn, rework cost, schedule impact, change propagation, or generalization to every software organization.

![Evidence boundary](assets/evaluation.svg)

## Reproduce

Offline:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/generate_figures.py
```

Public source rebuild:

```bash
python scripts/fetch_and_analyze.py --check
```

The rebuild verifies the Zenodo MD5 and release pinned SHA 256 before reconstructing and checking the empirical evidence.

## Repository map

- `REPORT.md`: scientific report
- `EMPIRICAL_STUDY.md`: released protocol and claim boundaries
- `docs/paper_blueprint.md`: manuscript plan and draft abstract
- `docs/analysis_plan.md`: estimands and inferential logic
- `docs/research_design.md`: study design and validity scope
- `docs/data_dictionary.md`: derived evidence definitions
- `data/source_manifest.json`: source identity and integrity metadata
- `data/derived/project_composition.csv`: complete 54 project composition evidence
- `data/derived/category_summary.csv`: pooled composition
- `data/derived/heterogeneity_results.csv`: sample threshold sensitivity
- `data/derived/project_residuals.csv`: full table cell diagnostics
- `data/derived/primary_project_contributions.csv`: project contributions for the primary subset
- `research/model.py`: taxonomy, intervals, heterogeneity, residuals, validation
- `scripts/`: source reconstruction and scientific figure generation
- `tests/`: scientific invariants and release checks
- `QA_REPORT.md`: release consistency evidence

## Research integrity

This is not a preregistered analysis.

The n at least 20 primary restriction is explicitly documented, and results from the full table plus stricter thresholds are retained so the sensitivity of the finding remains visible.
