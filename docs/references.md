# References and Data Sources

## Canonical dataset

Trautsch, A., Erbel, J., Herbold, S., & Grabowski, J. (2022). *What really changes when developers intend to improve their source code: A commit-level study of static metric value and static analysis warning changes* [Dataset, version 2]. Zenodo. https://doi.org/10.5281/zenodo.7078179

The Zenodo record documents a random sample of 2,533 commits from 54 Java Apache open source projects classified as perfective, corrective, or other.

## Peer reviewed source study

Trautsch, A., Erbel, J., Herbold, S., & Grabowski, J. (2023). What really changes when developers intend to improve their source code: a commit-level study of static metric value and static analysis warning changes. *Empirical Software Engineering, 28*, Article 30. https://doi.org/10.1007/s10664-022-10257-9

The article reports the project sampling procedure, manual classification process, maintenance taxonomy, and the broader software metric analyses for which the manual labels were originally collected.

## Maintenance taxonomy context

Swanson, E. B. (1976). The dimensions of maintenance. *Proceedings of the 2nd International Conference on Software Engineering*, 492 to 497.

## Statistical interval reference

Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. *Journal of the American Statistical Association, 22*(158), 209 to 212.

## How these sources are used

The Trautsch et al. dataset supplies the empirical ground truth.

The peer reviewed article supplies the study design and taxonomy context.

The present repository performs a distinct secondary analysis focused on cross project composition heterogeneity. It does not claim to reproduce the source article's complete software metric study.

## Source integrity

Zenodo reports the MD5 for `manual_labels.csv` as:

`a099d942098227a1fc8127759e55850e`

The release also pins SHA 256:

`e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941`

Both are verified during the public source rebuild.

## Rights note

The peer reviewed article is licensed CC BY 4.0.

The Zenodo dataset record is open but does not display a specific dataset license value in its rights field. This repository therefore stores only derived aggregate evidence and does not redistribute `manual_labels.csv`.
