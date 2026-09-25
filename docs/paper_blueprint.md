# Paper Blueprint

## Working title
**Cross-Project Heterogeneity in Quality-Oriented Engineering Change: Evidence from 2,533 Manually Classified Apache Commits**

## Motivation
Engineering managers see different mixes of internal-quality improvement, corrective work, and other development activity. A manually coded multi-project dataset permits direct comparison without inferring intent from commit-message keywords.

## Contribution
The source publication primarily studies software metrics associated with maintenance intent. This secondary analysis focuses instead on **between-project composition**, uncertainty, and the stability of heterogeneity after small-sample filtering.

## Data
2,533 manually classified commits from 54 Java Apache projects.

## Method
Three-category composition; 95% Wilson intervals; project×category chi-square; Cramér's V; sample-size sensitivity; Pearson residual diagnostics.

## Main result
In the primary n≥20 analysis, χ²(84)=432.452175, p≈2.46×10⁻⁴⁸, Cramér's V=0.301796. At n≥30, V=0.29979. The stable effect size supports material project-to-project differences in maintenance-intent composition.

## Interpretation
The result is about the observed Apache sample, not all organizations and not causal determinants of engineering-change behavior.

## Follow-on work
A stronger longitudinal study would merge these labels with timestamps and project lifecycle information. That would justify a true temporal “dynamics” claim; this release intentionally does not pretend the current CSV contains time.
