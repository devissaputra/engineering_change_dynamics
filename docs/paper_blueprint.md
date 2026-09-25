# Paper Blueprint

## Working title

**Portfolio Averages Hide Project Differences: Cross-Project Heterogeneity in Manually Classified Software Maintenance Intent**

Alternative title:

**Cross-Project Heterogeneity in Perfective and Corrective Maintenance: Evidence from 2,533 Manually Classified Apache Commits**

## Paper identity

This should be written as a focused empirical software engineering and engineering management secondary analysis.

The paper is not a new commit classification paper.

Its contribution is the project level analysis of a manually labeled ground truth dataset that was originally collected mainly to support a different research objective.

## One sentence contribution

Using 2,533 manually classified commits from 54 Apache projects, the study shows that pooled maintenance intent proportions conceal stable and material cross project heterogeneity.

## Draft abstract

Portfolio level summaries of software maintenance activity can obscure differences between individual projects. This study reanalyzes 2,533 commits from 54 Java Apache projects that were manually classified by Trautsch, Erbel, Herbold, and Grabowski as perfective, corrective, or other maintenance. Across the full sample, 40.3% of commits are perfective, 27.0% corrective, and 32.6% other. To evaluate whether this composition is stable across projects, we construct project specific category profiles with 95% Wilson intervals and a project by category contingency analysis. Because the complete 54 project table contains 21 expected cells below five, the primary inferential analysis uses the 43 projects with at least 20 labeled commits. The resulting association is chi square(84) = 432.452, p = 2.46 × 10^-48, with Cramér's V = 0.302. Cramér's V remains between 0.293 and 0.305 when the minimum project sample threshold is varied from 10 to 50 commits. Project contribution and Pearson residual diagnostics show that Phoenix, PDFBox, Commons Math, Commons Lang, and Tez account for substantial portions of the observed departure from pooled composition. The findings indicate that a single portfolio maintenance profile is not representative of all sampled projects. The study contributes a transparent cross project view of maintenance intent heterogeneity while avoiding causal or project quality interpretations.

## Introduction logic

### Paragraph 1: management problem

Engineering managers often summarize maintenance portfolios with one aggregate distribution of work types.

### Paragraph 2: analytical problem

A pooled distribution can conceal large differences among individual projects, especially when project sample sizes differ.

### Paragraph 3: evidence opportunity

The Trautsch et al. ground truth contains manually classified commit intent across 54 projects, enabling direct project composition analysis without relying on keyword inferred labels.

### Paragraph 4: contribution

This study quantifies cross project heterogeneity, uncertainty, sensitivity to small samples, and project contributions to the omnibus pattern.

## Research questions

**RQ1.** What is the pooled maintenance intent composition?

**RQ2.** How heterogeneous is that composition across projects?

**RQ3.** How stable is the association after progressively excluding small project samples?

**RQ4.** Which project and category combinations contribute most strongly to the heterogeneity?

## Data section

Report:

- 2,533 manually classified commits;
- 54 Java Apache projects;
- Zenodo DOI 10.5281/zenodo.7078179;
- manual_labels.csv;
- approximately 2% random sample per project, rounded up;
- two researcher manual coding and disagreement resolution;
- three category taxonomy;
- derived aggregates stored locally while raw source is rebuilt from Zenodo.

## Taxonomy section

Explain clearly that the source flags are representations of a mutually exclusive three category taxonomy.

Do not return to the earlier phi coefficient framing.

## Descriptive analysis

Report pooled counts and Wilson intervals.

Then show project level compositions and uncertainty.

Do not interpret raw extreme shares from small projects without their intervals.

## Primary heterogeneity analysis

Explain why the full 54 project table is not the primary asymptotic test.

Use the n at least 20 subset:

- N = 2,374;
- projects = 43;
- chi square = 432.452175;
- df = 84;
- p = 2.46 × 10^-48;
- Cramér's V = 0.301796;
- minimum expected = 5.794019.

Avoid universal labels such as medium or large for Cramér's V.

## Sensitivity analysis

Show n at least 10, 20, 30, 40, and 50 together.

The key pattern is that V changes little despite substantial changes in the number of included projects.

## Contribution diagnostics

### Cell level

Use Pearson residuals to identify category specific departures.

### Project level

Decompose the primary chi square statistic into project contributions.

Highlight examples rather than ranking projects by quality.

## Results structure

### 1. Pooled composition

Perfective 40.3%, corrective 27.0%, other 32.6%.

### 2. Project composition

Use a ternary project profile figure with project sample size represented by point size and the pooled composition marked separately.

### 3. Primary heterogeneity

Present inferential result and effect size.

### 4. Sample size sensitivity

Show the stability of Cramér's V.

### 5. Contribution diagnostics

Discuss Phoenix, PDFBox, Commons Math, Commons Lang, Tez, and other major contributors.

## Discussion

### Portfolio interpretation

One pooled maintenance ratio is not an adequate description of all projects in the sample.

### Management interpretation

Project differences should trigger contextual investigation rather than project performance judgments.

### Methodological interpretation

Small project samples require visible uncertainty. A raw proportion without sample size is incomplete evidence.

### Source study relationship

The original paper studies software metrics associated with developer maintenance intent. This secondary analysis studies project composition heterogeneity in the manually coded ground truth.

## Limitations

Include at least:

1. Apache open source projects only;
2. Java projects only;
3. approximately 2% sample per project;
4. unequal project sample sizes;
5. commit message intent rather than direct observation of developer motivation;
6. classification guideline dependence;
7. no causal project variables;
8. no organizational context;
9. no cost or schedule outcomes;
10. no temporal or lifecycle modeling;
11. asymptotic inference requires a project sample restriction;
12. residual diagnostics are not multiplicity adjusted tests.

## Figures

**Figure 1. Cross project composition map.**  
Ternary plot of perfective, corrective, and other shares across all 54 projects. Point size represents labeled sample size. The pooled composition is shown as a reference marker.

**Figure 2. Empirical processing pipeline.**  
Zenodo source, taxonomy validation, project aggregation, uncertainty, heterogeneity, sensitivity, and diagnostic decomposition.

**Figure 3. Pooled composition.**  
Three category shares with Wilson intervals.

**Figure 4. Primary residual diagnostics.**  
Largest positive and negative project category residuals.

**Figure 5. Sample size sensitivity.**  
Cramér's V and retained project count across thresholds.

**Figure 6. Evidence boundary.**

## Tables

**Table 1.** Data and sampling description.  
**Table 2.** Pooled composition.  
**Table 3.** Heterogeneity sensitivity.  
**Table 4.** Largest project contributions and residuals.

## Writing rules

- Say **maintenance intent composition**, not project quality.
- Say **manually classified sample**, not all project commits.
- Distinguish perfective internal quality intent from corrective external quality intent.
- Do not use the earlier phi coefficient interpretation.
- Keep pooled composition separate from project level variation.
- Do not claim causal explanations for project differences.
- Do not claim temporal dynamics unless future work adds time explicitly.
- Describe residuals as diagnostics, not separate adjusted tests.

## Completion checklist

A manuscript draft is ready for external review when:

- every headline number maps to released evidence;
- the source taxonomy is described correctly;
- the sampling process is cited accurately;
- the n at least 20 decision is justified and sensitivity is shown;
- project uncertainty remains visible;
- contribution diagnostics are clearly distinguished from significance tests;
- limitations include external, sampling, construct, and causal boundaries;
- the repository release or commit is cited.
