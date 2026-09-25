# Empirical Study Protocol

## Study
Cross-Project Heterogeneity in Quality-Oriented Engineering Change

## Design
Secondary observational analysis of 2,533 manually coded commits from 54 Java Apache projects.

## Source taxonomy
The source study manually classifies commits into three mutually exclusive categories:
- **perfective** — internal-quality improvement intent;
- **corrective** — external-quality improvement intent;
- **other** — neither perfective nor corrective in the released coding scheme.

The source CSV stores these as `internal_quality` and `external_quality` flags. No released row has both flags true. This is treated as a taxonomy property, not as an empirical negative association.

## Primary estimand
Project-level composition of perfective, corrective, and other commits.

## Uncertainty
Each project-category share receives a 95% Wilson binomial interval. These intervals are descriptive and do not imply independent multinomial categories.

## Heterogeneity test
The complete 54×3 table is reported descriptively, but 21 expected cells are below 5. Primary inferential analysis therefore uses projects with at least 20 labeled commits, where every expected cell exceeds 5.

Primary result:
χ²(84) = 432.452175, p ≈ 2.46×10⁻⁴⁸, Cramér's V = 0.301796, N = 2374, 43 projects.

## Sensitivity
At n≥30: χ²(66) = 388.076754, p ≈ 3.98×10⁻⁴⁷, Cramér's V = 0.29979, N = 2159, 34 projects.

Additional n≥40 and n≥50 results are packaged.

## Diagnostic residuals
Pearson residuals identify project-category cells that contribute strongly to the omnibus heterogeneity statistic. They are not reported as separately adjusted significance tests.

## Validity boundary
This study describes maintenance-intent composition in a manually sampled Apache dataset. It does not estimate requirement churn, design propagation, cost, schedule impact, or causal project effects.
