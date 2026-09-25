import pytest

from research.model import (
    CATEGORIES,
    PRIMARY_MIN_PROJECT_N,
    category_summary,
    classify,
    heterogeneity,
    load_primary_contributions,
    load_primary_residuals,
    load_projects,
    project_contributions,
    residuals,
    validate_bundle,
    wilson_interval,
)


def test_source_taxonomy():
    assert classify(True, False) == "perfective"
    assert classify(False, True) == "corrective"
    assert classify(False, False) == "other"


def test_both_flags_are_rejected():
    with pytest.raises(ValueError):
        classify(True, True)


def test_complete_54_project_evidence():
    projects = load_projects()

    assert len(projects) == 54
    assert sum(int(p["n"]) for p in projects) == 2533
    assert sum(int(p["perfective_count"]) for p in projects) == 1022
    assert sum(int(p["corrective_count"]) for p in projects) == 685
    assert sum(int(p["other_count"]) for p in projects) == 826


def test_pooled_category_summary():
    rows = {row["category"]: row for row in category_summary(load_projects())}

    assert rows["perfective"]["count"] == 1022
    assert rows["corrective"]["count"] == 685
    assert rows["other"]["count"] == 826
    assert abs(rows["perfective"]["share"] - 1022 / 2533) < 1e-12


def test_primary_heterogeneity():
    result = heterogeneity(load_projects(), PRIMARY_MIN_PROJECT_N)

    assert result["projects"] == 43
    assert result["n_commits"] == 2374
    assert result["df"] == 84
    assert result["cells_expected_lt5"] == 0
    assert abs(result["chi_square"] - 432.452175131331) < 1e-9
    assert abs(result["cramers_v"] - 0.3017961448456011) < 1e-10
    assert result["p_value"] < 1e-40


def test_full_table_assumption_warning_is_encoded():
    result = heterogeneity(load_projects(), 10)

    assert result["projects"] == 54
    assert result["cells_expected_lt5"] == 21
    assert result["min_expected_count"] < 5


def test_sensitivity_effect_is_stable():
    projects = load_projects()
    expected = {
        30: 0.29979024396654913,
        40: 0.2927768791374733,
        50: 0.2929078094561519,
    }

    for cutoff, value in expected.items():
        assert abs(heterogeneity(projects, cutoff)["cramers_v"] - value) < 1e-10


def test_primary_residual_diagnostics():
    calculated = residuals(load_projects(), PRIMARY_MIN_PROJECT_N)
    packaged = load_primary_residuals()

    assert len(calculated) == 129
    assert len(packaged) == 129

    assert calculated[0]["project"] == "phoenix"
    assert calculated[0]["category"] == "corrective"
    assert abs(calculated[0]["pearson_residual"] - 6.029375619597332) < 1e-10

    assert packaged[0]["project"] == "phoenix"
    assert packaged[0]["category"] == "corrective"


def test_project_contribution_decomposition():
    projects = load_projects()
    contributions = project_contributions(projects, PRIMARY_MIN_PROJECT_N)
    packaged = load_primary_contributions()
    primary = heterogeneity(projects, PRIMARY_MIN_PROJECT_N)

    assert len(contributions) == 43
    assert len(packaged) == 43
    assert contributions[0]["project"] == "phoenix"
    assert abs(contributions[0]["chi_square_contribution"] - 61.14517740352014) < 1e-10
    assert abs(sum(r["chi_square_contribution"] for r in contributions) - primary["chi_square"]) < 1e-9


def test_wilson_interval():
    share, lower, upper = wilson_interval(1022, 2533)

    assert lower < share < upper
    assert 0 <= lower <= 1
    assert 0 <= upper <= 1


def test_bundle_validation():
    assert validate_bundle()
