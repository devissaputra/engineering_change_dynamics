# Final QA Report

**Release status: PASS after correction.**

## Checks completed
- provenance and source identity reviewed;
- licensing/reuse note recorded;
- derived CSV structure checked against the stated sample and estimand;
- `results/empirical_summary.json` reconciled with packaged evidence;
- README/report language reconciled with the numerical results;
- study-specific methods moved into `research/model.py`;
- tests exercise scientific logic and invariants;
- internet rebuild script has no synthetic fallback;
- four SVG assets regenerated as study-specific figures and XML-validated;
- local Markdown links checked;
- citation metadata points to the final repository slug;
- no preregistration claim is made.

## Final empirical finding
Among 2,533 manually classified commits, 40.3% are internal-quality changes, 27.0% external-quality changes, and 32.6% neither. Project-level internal-quality shares range from 0.130 to 0.818, demonstrating strong heterogeneity in observed change orientation.

## Required interpretation boundary
Commit intent is not equivalent to requirement change, design rework, or downstream cost/schedule impact. The empirical title is intentionally narrower: claims concern coded change orientation in this sample of Apache projects.
