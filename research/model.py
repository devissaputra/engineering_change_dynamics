from __future__ import annotations

import csv
import json
import math
from pathlib import Path

from scipy.stats import chi2

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ("perfective", "corrective", "other")
PRIMARY_MIN_PROJECT_N = 20


def classify(internal, external):
    internal_quality = str(internal).lower() == "true"
    external_quality = str(external).lower() == "true"

    if internal_quality and external_quality:
        raise ValueError("Source taxonomy is expected to be mutually exclusive")

    if internal_quality:
        return "perfective"
    if external_quality:
        return "corrective"
    return "other"


def wilson_interval(k, n, z=1.959963984540054):
    if n <= 0:
        raise ValueError("n must be positive")

    p = k / n
    denominator = 1 + z * z / n
    center = (p + z * z / (2 * n)) / denominator
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denominator
    return p, center - half, center + half


def project_table_from_rows(rows):
    projects = {}

    for row in rows:
        category = classify(row["internal_quality"], row["external_quality"])
        project = projects.setdefault(
            row["project"],
            {
                "project": row["project"],
                "n": 0,
                "perfective_count": 0,
                "corrective_count": 0,
                "other_count": 0,
            },
        )
        project["n"] += 1
        project[f"{category}_count"] += 1

    output = []
    for project in sorted(projects.values(), key=lambda x: x["project"]):
        item = dict(project)
        for category in CATEGORIES:
            share, lower, upper = wilson_interval(
                project[f"{category}_count"],
                project["n"],
            )
            item[f"{category}_share"] = share
            item[f"{category}_ci_low"] = lower
            item[f"{category}_ci_high"] = upper
        output.append(item)

    return output


def category_summary(projects):
    n = sum(int(p["n"]) for p in projects)
    output = []

    for category in CATEGORIES:
        count = sum(int(p[f"{category}_count"]) for p in projects)
        share, lower, upper = wilson_interval(count, n)
        output.append(
            {
                "category": category,
                "count": count,
                "share": share,
                "ci_low": lower,
                "ci_high": upper,
            }
        )

    return output


def heterogeneity(projects, min_project_n=PRIMARY_MIN_PROJECT_N):
    selected = [p for p in projects if int(p["n"]) >= min_project_n]
    if len(selected) < 2:
        raise ValueError("At least two projects are required")

    n = sum(int(p["n"]) for p in selected)
    column_totals = {
        category: sum(int(p[f"{category}_count"]) for p in selected)
        for category in CATEGORIES
    }

    statistic = 0.0
    min_expected = float("inf")
    expected_lt5 = 0

    for project in selected:
        for category in CATEGORIES:
            expected = int(project["n"]) * column_totals[category] / n
            observed = int(project[f"{category}_count"])
            statistic += (observed - expected) ** 2 / expected
            min_expected = min(min_expected, expected)
            expected_lt5 += expected < 5

    df = (len(selected) - 1) * (len(CATEGORIES) - 1)
    cramers_v = math.sqrt(
        statistic
        / (n * min(len(selected) - 1, len(CATEGORIES) - 1))
    )

    return {
        "min_project_n": min_project_n,
        "projects": len(selected),
        "n_commits": n,
        "chi_square": statistic,
        "df": df,
        "p_value": float(chi2.sf(statistic, df)),
        "cramers_v": cramers_v,
        "min_expected_count": min_expected,
        "cells_expected_lt5": int(expected_lt5),
    }


def residuals(projects, min_project_n=0):
    selected = [p for p in projects if int(p["n"]) >= min_project_n]
    n = sum(int(p["n"]) for p in selected)
    column_totals = {
        category: sum(int(p[f"{category}_count"]) for p in selected)
        for category in CATEGORIES
    }

    output = []

    for project in selected:
        for category in CATEGORIES:
            expected = int(project["n"]) * column_totals[category] / n
            observed = int(project[f"{category}_count"])
            residual = (observed - expected) / math.sqrt(expected)
            contribution = (observed - expected) ** 2 / expected
            output.append(
                {
                    "project": project["project"],
                    "category": category,
                    "observed": observed,
                    "expected": expected,
                    "pearson_residual": residual,
                    "chi_square_contribution": contribution,
                }
            )

    return sorted(
        output,
        key=lambda row: (
            -abs(row["pearson_residual"]),
            row["project"],
            row["category"],
        ),
    )


def project_contributions(projects, min_project_n=PRIMARY_MIN_PROJECT_N):
    cells = residuals(projects, min_project_n)
    by_project = {}

    for row in cells:
        item = by_project.setdefault(
            row["project"],
            {
                "project": row["project"],
                "n": next(
                    int(p["n"])
                    for p in projects
                    if p["project"] == row["project"]
                ),
                "chi_square_contribution": 0.0,
            },
        )
        item["chi_square_contribution"] += row["chi_square_contribution"]

    total = sum(item["chi_square_contribution"] for item in by_project.values())
    output = []

    for item in by_project.values():
        output.append(
            {
                **item,
                "share_of_primary_chi_square": item["chi_square_contribution"] / total,
            }
        )

    return sorted(
        output,
        key=lambda row: (-row["chi_square_contribution"], row["project"]),
    )


def _read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_projects():
    return _read_csv(ROOT / "data/derived/project_composition.csv")


def load_category_summary():
    return _read_csv(ROOT / "data/derived/category_summary.csv")


def load_heterogeneity():
    return _read_csv(ROOT / "data/derived/heterogeneity_results.csv")


def load_full_residuals():
    return _read_csv(ROOT / "data/derived/project_residuals.csv")


def load_primary_residuals():
    return _read_csv(ROOT / "data/derived/primary_project_residuals.csv")


def load_primary_contributions():
    return _read_csv(ROOT / "data/derived/primary_project_contributions.csv")


def load_summary():
    return json.loads(
        (ROOT / "results/empirical_summary.json").read_text(encoding="utf-8")
    )


def _close(a, b, tolerance=1e-6):
    return abs(float(a) - float(b)) <= tolerance


def validate_bundle():
    projects = load_projects()

    if len(projects) != 54:
        return False
    if sum(int(p["n"]) for p in projects) != 2533:
        return False

    expected_counts = {
        "perfective": 1022,
        "corrective": 685,
        "other": 826,
    }
    for category, expected in expected_counts.items():
        if sum(int(p[f"{category}_count"]) for p in projects) != expected:
            return False

    packed_summary = {row["category"]: row for row in load_category_summary()}
    for row in category_summary(projects):
        packed = packed_summary[row["category"]]
        if int(packed["count"]) != row["count"]:
            return False
        for key in ("share", "ci_low", "ci_high"):
            if not _close(packed[key], row[key], 1.5e-6):
                return False

    packed_heterogeneity = {
        int(row["min_project_n"]): row for row in load_heterogeneity()
    }
    for cutoff in (10, 20, 30, 40, 50):
        calculated = heterogeneity(projects, cutoff)
        packed = packed_heterogeneity[cutoff]

        if int(packed["projects"]) != calculated["projects"]:
            return False
        if int(packed["n_commits"]) != calculated["n_commits"]:
            return False
        if int(packed["df"]) != calculated["df"]:
            return False
        if int(packed["cells_expected_lt5"]) != calculated["cells_expected_lt5"]:
            return False

        for key in (
            "chi_square",
            "p_value",
            "cramers_v",
            "min_expected_count",
        ):
            tolerance = max(1e-6, abs(calculated[key]) * 1e-6)
            if not _close(packed[key], calculated[key], tolerance):
                return False

    full_residuals = residuals(projects, 0)
    packed_full = load_full_residuals()
    if len(packed_full) != 162:
        return False
    if packed_full[0]["project"] != "phoenix":
        return False
    if packed_full[0]["category"] != "corrective":
        return False
    if not _close(
        packed_full[0]["pearson_residual"],
        full_residuals[0]["pearson_residual"],
        1e-5,
    ):
        return False

    primary_residuals = residuals(projects, PRIMARY_MIN_PROJECT_N)
    packed_primary = load_primary_residuals()
    if len(packed_primary) != 129:
        return False

    for packed, calculated in zip(packed_primary, primary_residuals):
        if packed["project"] != calculated["project"]:
            return False
        if packed["category"] != calculated["category"]:
            return False
        if int(packed["observed"]) != calculated["observed"]:
            return False
        for key in ("expected", "pearson_residual", "chi_square_contribution"):
            if not _close(packed[key], calculated[key], 1.5e-6):
                return False

    primary_contributions = project_contributions(
        projects,
        PRIMARY_MIN_PROJECT_N,
    )
    packed_contributions = load_primary_contributions()

    if len(packed_contributions) != 43:
        return False

    for packed, calculated in zip(packed_contributions, primary_contributions):
        if packed["project"] != calculated["project"]:
            return False
        if int(packed["n"]) != calculated["n"]:
            return False
        if not _close(
            packed["chi_square_contribution"],
            calculated["chi_square_contribution"],
            1.5e-6,
        ):
            return False
        if not _close(
            packed["share_of_primary_chi_square"],
            calculated["share_of_primary_chi_square"],
            1.5e-6,
        ):
            return False

    if not _close(
        sum(row["chi_square_contribution"] for row in primary_contributions),
        heterogeneity(projects, PRIMARY_MIN_PROJECT_N)["chi_square"],
        1e-9,
    ):
        return False

    headline = load_summary()["headline_metrics"]

    return (
        headline["n_commits"] == 2533
        and headline["n_projects"] == 54
        and headline["primary_min_project_n"] == 20
        and _close(headline["primary_cramers_v"], 0.301796, 1e-6)
        and headline["source_categories_mutually_exclusive"] is True
        and headline["top_primary_project_contributor"] == "phoenix"
    )
