# Scientific Report

## Cross-Project Heterogeneity in Quality-Oriented Engineering Change

### Executive summary

Software maintenance activity is often summarized at portfolio level, but a pooled average can hide large differences between projects. This study uses 2,533 manually classified commits from 54 Java Apache projects to examine how the composition of perfective, corrective, and other maintenance intent varies across projects.

The source dataset comes from Trautsch, Erbel, Herbold, and Grabowski and is distributed through Zenodo under DOI 10.5281/zenodo.7078179. The source authors manually classified commit messages into three mutually exclusive categories. Perfective changes represent internal quality improvement intent, corrective changes represent external quality improvement intent, and the remaining commits are classified as other.

Across all 2,533 commits, 1,022 are perfective, 685 are corrective, and 826 are other. The pooled shares are therefore 40.3%, 27.0%, and 32.6%.

The core question is whether that pooled composition is representative of individual projects. The complete 54 by 3 contingency table contains 21 cells with expected counts below 5, so the release does not rely on that asymptotic test as the primary inferential result. The primary analysis uses the 43 projects with at least 20 manually labeled commits. This subset contains 2,374 commits and has no expected cell below 5.

For the primary subset:

- chi square(84) = 432.452175
- p = 2.46 × 10^-48
- Cramér's V = 0.301796
- minimum expected count = 5.794019

The effect size remains close to 0.30 when the minimum project sample threshold is raised to 30, 40, and 50 commits. This indicates that the observed heterogeneity is not explained only by the smallest project samples.

The project level pattern is also concrete rather than abstract. Phoenix contains 52.9% corrective and only 14.6% perfective commits, while Commons Lang contains 75.8% perfective and 9.1% corrective commits. PDFBox contains only 9.6% other commits, compared with a pooled other share of 32.6%. These differences create large Pearson residuals and make clear why a portfolio average is insufficient.

The strongest contribution of this repository is therefore not a new commit classifier. It is a reproducible cross project analysis showing that maintenance intent composition differs materially across sampled software systems and that engineering managers should be cautious about treating one pooled maintenance profile as representative of every project.

### Research questions

1. What is the pooled composition of perfective, corrective, and other manually classified commits?
2. Does maintenance intent composition vary across projects beyond ordinary sampling variation?
3. Is the estimated heterogeneity robust when increasingly small project samples are removed?
4. Which project and category combinations contribute most strongly to the observed heterogeneity?

### Source study and provenance

Canonical dataset:

**Trautsch, Erbel, Herbold, and Grabowski replication dataset**  
Zenodo DOI: **10.5281/zenodo.7078179**

Source file:

`manual_labels.csv`

Verified release dimensions:

- 2,533 manually classified commits
- 54 Java Apache projects
- three mutually exclusive maintenance intent categories

The original paper reports that approximately 2% of eligible commits were randomly sampled per project, rounded up, for manual classification.

Each sampled commit message was independently classified by two researchers. Disagreements were resolved jointly.

The repository does not redistribute the source CSV because the Zenodo record is open but does not display a specific dataset license value. Instead, the release stores derived aggregate evidence and verifies it against the public source during the rebuild workflow.

### Unit of analysis

One manually classified commit nested within one Apache Java project.

### Source taxonomy

The source ground truth distinguishes three categories:

| Category | Interpretation in source study |
|---|---|
| Perfective | Internal quality improvement intent |
| Corrective | External quality improvement intent |
| Other | Neither perfective nor corrective under the released coding scheme |

The source CSV exposes internal quality and external quality flags, but these are not treated as two independent binary constructs. No source row has both flags true.

The repository therefore reconstructs the source taxonomy directly instead of interpreting the flags as four possible independent states.

### Pooled composition

| Category | Count | Share | 95% Wilson interval |
|---|---:|---:|---:|
| Perfective | 1,022 | 40.3% | 38.5% to 42.3% |
| Corrective | 685 | 27.0% | 25.3% to 28.8% |
| Other | 826 | 32.6% | 30.8% to 34.5% |

These pooled values describe the sample as a whole. They should not be interpreted as the expected maintenance profile of every Apache project.

### Project level uncertainty

Each project and category share is accompanied by a 95% Wilson interval.

This matters because the project sample sizes vary substantially. Small samples can produce apparently extreme proportions with wide uncertainty.

For example, Commons RDF contains only 11 labeled commits and has an observed perfective share of 81.8%, but its Wilson interval is much wider than the corresponding interval for large projects such as Jena or PDFBox.

### Primary heterogeneity analysis

The full 54 project contingency table is useful descriptively, but it contains 21 expected cells below 5.

The released primary inferential analysis therefore uses projects with at least 20 manually classified commits.

Primary subset:

- projects: 43
- commits: 2,374
- chi square: 432.452175
- degrees of freedom: 84
- p value: 2.4646 × 10^-48
- Cramér's V: 0.301796
- minimum expected count: 5.794019
- expected cells below 5: 0

The result provides strong evidence that the observed perfective, corrective, and other composition differs across the sampled projects.

Cramér's V is reported as an effect size. The repository avoids assigning a universal small, medium, or large label because interpretation depends on context and table dimensions.

### Sample size sensitivity

| Minimum project n | Projects | Commits | Cramér's V | Minimum expected |
|---:|---:|---:|---:|---:|
| 10 | 54 | 2,533 | 0.305165 | 2.704303 |
| 20 | 43 | 2,374 | 0.301796 | 5.794019 |
| 30 | 34 | 2,159 | 0.299790 | 8.364984 |
| 40 | 25 | 1,864 | 0.292777 | 11.630901 |
| 50 | 17 | 1,506 | 0.292908 | 13.977424 |

The estimated association remains between approximately 0.293 and 0.305 across all released thresholds.

The stability matters more than any one cutoff. It shows that the cross project composition differences remain visible even when progressively smaller project samples are removed.

### Concrete project differences

Several projects illustrate the heterogeneity clearly.

| Project | n | Perfective | Corrective | Other |
|---|---:|---:|---:|---:|
| Phoenix | 157 | 14.6% | 52.9% | 32.5% |
| PDFBox | 166 | 48.8% | 41.6% | 9.6% |
| Commons Math | 94 | 70.2% | 10.6% | 19.1% |
| Commons Lang | 66 | 75.8% | 9.1% | 15.2% |
| Tez | 48 | 16.7% | 56.3% | 27.1% |
| NiFi | 66 | 18.2% | 27.3% | 54.5% |

These are descriptive examples, not ranked project quality scores.

### Residual diagnostics

Pearson residuals identify project and category cells that depart strongly from the pooled composition.

For the primary n at least 20 subset, the largest absolute residuals include:

| Project | Category | Pearson residual |
|---|---|---:|
| Phoenix | Corrective | +6.03 |
| PDFBox | Other | -5.20 |
| Phoenix | Perfective | -4.98 |
| Commons Math | Perfective | +4.70 |
| Commons Lang | Perfective | +4.65 |
| Tez | Corrective | +3.78 |

A positive residual means that more commits were observed in that project and category than expected under the pooled composition. A negative residual means fewer were observed.

These residuals are diagnostic contributions to the omnibus pattern. They are not treated as separately multiplicity adjusted hypothesis tests.

### Project contributions to heterogeneity

The chi square statistic can also be decomposed into project level contributions.

In the primary subset, the largest project contributions are:

| Project | Chi square contribution | Share of primary chi square |
|---|---:|---:|
| Phoenix | 61.145 | 14.1% |
| PDFBox | 42.270 | 9.8% |
| Commons Math | 37.173 | 8.6% |
| Commons Lang | 36.067 | 8.3% |
| Tez | 21.164 | 4.9% |

This provides a more interpretable project level view of the omnibus result while preserving the fact that the primary statistical test concerns the complete contingency table.

### Engineering management interpretation

The main management implication is not that one project is better than another.

The evidence shows that the observed mix of maintenance intents differs substantially between software projects in the sample. A pooled portfolio average can therefore hide very different local maintenance profiles.

For engineering management, that suggests at least three cautions:

1. portfolio level maintenance ratios should not automatically be used as project level expectations;
2. unusually high or low category shares should be interpreted together with project sample size and uncertainty;
3. differences in maintenance intent should motivate further investigation of project context rather than immediate performance judgments.

The present dataset does not explain why the projects differ.

### Relation to the source publication

The source publication uses the manually classified sample as ground truth for commit intent classification and then investigates how perfective and corrective changes relate to static source code metrics and warnings.

This repository asks a narrower secondary question that is not the main focus of the source article:

**How heterogeneous is the manually observed maintenance intent composition across projects?**

The contribution is therefore a secondary cross project composition analysis built on the source ground truth, not a reproduction of the complete original study.

### What this study supports

The release supports these statements:

- the source sample contains 2,533 manually classified commits from 54 Java Apache projects;
- the pooled sample contains 1,022 perfective, 685 corrective, and 826 other commits;
- project maintenance intent composition is heterogeneous in the released sample;
- the estimated Cramér's V remains near 0.30 after increasingly strict project sample thresholds;
- several projects and categories contribute strongly to the omnibus heterogeneity;
- project level uncertainty is substantial for small samples.

### What this study does not support

The release does not establish:

- causal reasons for the project differences;
- whether a project is well managed or poorly managed;
- requirements churn;
- engineering change propagation;
- rework cost;
- schedule impact;
- product quality;
- developer productivity;
- generalization to all software organizations;
- temporal change dynamics within projects.

The repository name uses engineering change in the context of software intensive maintenance work. The released data are cross sectional with respect to the current analysis and do not justify a temporal dynamics claim.

### Threats to validity

**Construct validity.** Commit message intent is a proxy for maintenance intent and depends on the source study's classification guidelines.

**Sampling validity.** Approximately 2% of eligible commits were sampled per project. Project level sample sizes therefore vary.

**Statistical validity.** The full table contains small expected counts. The primary n at least 20 restriction and sensitivity analyses are used to reduce reliance on weak asymptotic cells.

**Diagnostic multiplicity.** Pearson residuals are descriptive diagnostics and are not individually adjusted hypothesis tests.

**External validity.** The source projects are Java open source projects under the Apache Software Foundation.

**Causal validity.** No project characteristic is manipulated or modeled as a cause of maintenance intent.

**Temporal validity.** The current analysis aggregates projects and does not model time, project age, release cycles, or lifecycle phases.

### Reproducibility

Offline verification:

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

The rebuild downloads `manual_labels.csv` from Zenodo, verifies the published MD5 and release pinned SHA 256 values, reconstructs the source taxonomy, rebuilds all 54 project aggregates, recomputes the sensitivity analyses and diagnostic evidence, and compares the results with the packaged release.

### Research integrity statement

This is a secondary analysis of public research data.

The analysis is not preregistered. The n at least 20 primary restriction is a released analysis decision selected to avoid expected cell counts below 5. Results for the full table and stricter thresholds are retained so the effect of that decision is transparent.

The repository should be interpreted as evidence of cross project heterogeneity in the sampled maintenance intent labels, not as evidence of causal engineering performance differences.
