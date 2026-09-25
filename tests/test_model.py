from research.model import CATEGORIES,classify,heterogeneity,load_projects,residuals,validate_bundle,wilson_interval

def test_source_taxonomy():
    assert classify(True,False)=="perfective"
    assert classify(False,True)=="corrective"
    assert classify(False,False)=="other"

def test_both_flags_are_rejected():
    import pytest
    with pytest.raises(ValueError):classify(True,True)

def test_complete_54_project_evidence():
    ps=load_projects()
    assert len(ps)==54
    assert sum(int(p["n"]) for p in ps)==2533
    assert sum(int(p["perfective_count"]) for p in ps)==1022
    assert sum(int(p["corrective_count"]) for p in ps)==685
    assert sum(int(p["other_count"]) for p in ps)==826

def test_primary_heterogeneity():
    z=heterogeneity(load_projects(),20)
    assert z["projects"]==43 and z["n_commits"]==2374
    assert z["df"]==84 and z["cells_expected_lt5"]==0
    assert abs(z["chi_square"]-432.452175131331)<1e-8
    assert abs(z["cramers_v"]-0.3017961448456011)<1e-10
    assert z["p_value"]<1e-40

def test_sensitivity_effect_is_stable():
    ps=load_projects()
    for cut,expected in [(30,0.29979024396654913),(40,0.2927768791374733),(50,0.2929078094561519)]:
        assert abs(heterogeneity(ps,cut)["cramers_v"]-expected)<1e-10

def test_full_table_assumption_warning_is_encoded():
    z=heterogeneity(load_projects(),10)
    assert z["cells_expected_lt5"]==21
    assert z["min_expected_count"]<5

def test_residual_diagnostic():
    top=residuals(load_projects())[0]
    assert top["project"]=="phoenix" and top["category"]=="corrective"
    assert abs(top["pearson_residual"]-6.222033762768916)<1e-10

def test_wilson_interval_and_bundle():
    s,lo,hi=wilson_interval(1022,2533)
    assert lo<s<hi
    assert validate_bundle()
