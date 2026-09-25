from research.model import classify,aggregate,validate_bundle
def test_classification_states():
    assert classify(True,False)=='internal_only'; assert classify(False,True)=='external_only'; assert classify(False,False)=='neither'; assert classify(True,True)=='both'
def test_aggregation_fixture():
    rows=[{'project':'a','internal_quality':'True','external_quality':'False'},{'project':'a','internal_quality':'False','external_quality':'True'}]; c,p=aggregate(rows); assert c['internal_only']==1 and c['external_only']==1 and p['a']['n']==2
def test_packaged_invariants(): assert validate_bundle()
