#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.model import (
    CATEGORIES,
    PRIMARY_MIN_PROJECT_N,
    category_summary,
    heterogeneity,
    project_contributions,
    project_table_from_rows,
    residuals,
)

URL = "https://zenodo.org/records/7078179/files/manual_labels.csv?download=1"
EXPECTED_MD5 = "a099d942098227a1fc8127759e55850e"
EXPECTED_SHA256 = "e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941"


def fetch():
    request = urllib.request.Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0 ResearchPackage/1.2"},
    )
    payload = urllib.request.urlopen(request, timeout=60).read()

    md5 = hashlib.md5(payload).hexdigest()
    sha256 = hashlib.sha256(payload).hexdigest()

    if md5 != EXPECTED_MD5:
        raise SystemExit(f"FAIL: Zenodo MD5 changed: {md5}")
    if sha256 != EXPECTED_SHA256:
        raise SystemExit(f"FAIL: Zenodo SHA-256 changed: {sha256}")

    rows = list(
        csv.DictReader(
            io.StringIO(payload.decode("utf-8-sig"))
        )
    )

    return rows, md5, sha256


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def close(a, b, tolerance=1e-6):
    return abs(float(a) - float(b)) <= tolerance


def check_project_table(calculated):
    packaged = read_csv(ROOT / "data/derived/project_composition.csv")

    if len(packaged) != len(calculated):
        raise SystemExit("FAIL: project table row count differs")

    for expected, actual in zip(packaged, calculated):
        if expected["project"] != actual["project"]:
            raise SystemExit("FAIL: project identity differs")
        if int(expected["n"]) != actual["n"]:
            raise SystemExit(f"FAIL: project sample size differs for {actual['project']}")

        for category in CATEGORIES:
            if int(expected[f"{category}_count"]) != actual[f"{category}_count"]:
                raise SystemExit(
                    f"FAIL: category count differs {actual['project']}/{category}"
                )

            for suffix in ("share", "ci_low", "ci_high"):
                key = f"{category}_{suffix}"
                if not close(expected[key], actual[key], 1.5e-6):
                    raise SystemExit(
                        f"FAIL: project estimate differs {actual['project']}/{key}"
                    )


def check_category_summary(projects):
    packaged = {
        row["category"]: row
        for row in read_csv(ROOT / "data/derived/category_summary.csv")
    }

    for calculated in category_summary(projects):
        row = packaged[calculated["category"]]
        if int(row["count"]) != calculated["count"]:
            raise SystemExit(
                f"FAIL: pooled count differs for {calculated['category']}"
            )
        for key in ("share", "ci_low", "ci_high"):
            if not close(row[key], calculated[key], 1.5e-6):
                raise SystemExit(
                    f"FAIL: pooled {key} differs for {calculated['category']}"
                )


def check_heterogeneity(projects):
    packaged = {
        int(row["min_project_n"]): row
        for row in read_csv(ROOT / "data/derived/heterogeneity_results.csv")
    }

    for cutoff in (10, 20, 30, 40, 50):
        calculated = heterogeneity(projects, cutoff)
        row = packaged[cutoff]

        for key in ("projects", "n_commits", "df", "cells_expected_lt5"):
            if int(row[key]) != calculated[key]:
                raise SystemExit(
                    f"FAIL: heterogeneity count differs {cutoff}/{key}"
                )

        for key in ("chi_square", "p_value", "cramers_v", "min_expected_count"):
            tolerance = max(1e-6, abs(calculated[key]) * 1e-6)
            if not close(row[key], calculated[key], tolerance):
                raise SystemExit(
                    f"FAIL: heterogeneity differs {cutoff}/{key}"
                )


def check_residual_file(path, calculated, expected_rows):
    packaged = read_csv(ROOT / path)

    if len(packaged) != expected_rows:
        raise SystemExit(f"FAIL: residual row count differs for {path}")

    for row, expected in zip(packaged, calculated):
        if row["project"] != expected["project"]:
            raise SystemExit(f"FAIL: residual project differs in {path}")
        if row["category"] != expected["category"]:
            raise SystemExit(f"FAIL: residual category differs in {path}")
        if int(row["observed"]) != expected["observed"]:
            raise SystemExit(f"FAIL: residual observed differs in {path}")

        for key in ("expected", "pearson_residual"):
            if not close(row[key], expected[key], 1.5e-6):
                raise SystemExit(f"FAIL: residual {key} differs in {path}")

        if "chi_square_contribution" in row:
            if not close(
                row["chi_square_contribution"],
                expected["chi_square_contribution"],
                1.5e-6,
            ):
                raise SystemExit(
                    f"FAIL: cell contribution differs in {path}"
                )


def check_project_contributions(projects):
    calculated = project_contributions(projects, PRIMARY_MIN_PROJECT_N)
    packaged = read_csv(
        ROOT / "data/derived/primary_project_contributions.csv"
    )

    if len(packaged) != len(calculated):
        raise SystemExit("FAIL: primary contribution row count differs")

    for row, expected in zip(packaged, calculated):
        if row["project"] != expected["project"]:
            raise SystemExit("FAIL: primary contribution project differs")
        if int(row["n"]) != expected["n"]:
            raise SystemExit("FAIL: primary contribution n differs")

        for key in (
            "chi_square_contribution",
            "share_of_primary_chi_square",
        ):
            if not close(row[key], expected[key], 1.5e-6):
                raise SystemExit(
                    f"FAIL: primary contribution {key} differs"
                )

    primary = heterogeneity(projects, PRIMARY_MIN_PROJECT_N)
    total = sum(row["chi_square_contribution"] for row in calculated)
    if not close(total, primary["chi_square"], 1e-9):
        raise SystemExit("FAIL: project contributions do not sum to primary chi square")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rows, md5, sha256 = fetch()

    print("zenodo_md5:", md5)
    print("zenodo_sha256:", sha256)
    print("rows:", len(rows))

    projects = project_table_from_rows(rows)

    if len(rows) != 2533 or len(projects) != 54:
        raise SystemExit("FAIL: source dimensions changed")

    if not args.check:
        print(
            json.dumps(
                {
                    "primary": heterogeneity(projects, PRIMARY_MIN_PROJECT_N),
                    "sensitivity_n30": heterogeneity(projects, 30),
                    "largest_primary_residuals": residuals(
                        projects,
                        PRIMARY_MIN_PROJECT_N,
                    )[:10],
                    "largest_project_contributions": project_contributions(
                        projects,
                        PRIMARY_MIN_PROJECT_N,
                    )[:10],
                },
                indent=2,
            )
        )
        return

    check_project_table(projects)
    check_category_summary(projects)
    check_heterogeneity(projects)

    check_residual_file(
        "data/derived/project_residuals.csv",
        residuals(projects, 0),
        162,
    )
    check_residual_file(
        "data/derived/primary_project_residuals.csv",
        residuals(projects, PRIMARY_MIN_PROJECT_N),
        129,
    )
    check_project_contributions(projects)

    summary = json.loads(
        (ROOT / "results/empirical_summary.json").read_text(encoding="utf-8")
    )
    headline = summary["headline_metrics"]

    if headline["perfective_count"] != 1022:
        raise SystemExit("FAIL: summary perfective count differs")
    if headline["corrective_count"] != 685:
        raise SystemExit("FAIL: summary corrective count differs")
    if headline["other_count"] != 826:
        raise SystemExit("FAIL: summary other count differs")
    if headline["top_primary_project_contributor"] != "phoenix":
        raise SystemExit("FAIL: summary top project contributor differs")

    print("zenodo_rebuild: PASS")


if __name__ == "__main__":
    main()
