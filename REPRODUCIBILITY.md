# Reproducibility

## Offline
```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/generate_figures.py --out-dir /tmp/change_figures
```

Offline tests recompute all pooled counts, confidence intervals, contingency statistics, effect sizes, and residuals from the complete 54-project derived table.

## Public source
```bash
python scripts/fetch_and_analyze.py --check
```

The rebuild:
1. downloads `manual_labels.csv` from Zenodo;
2. verifies MD5 `a099d942098227a1fc8127759e55850e`;
3. verifies release-pinned SHA-256 `e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941`;
4. verifies the mutually exclusive three-category source invariant;
5. reconstructs the 54-project aggregate table;
6. checks all released heterogeneity and summary results.

There is no synthetic fallback.
