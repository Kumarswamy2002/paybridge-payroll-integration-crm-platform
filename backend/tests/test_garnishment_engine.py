from backend.app.services.garnishment_service import GarnishmentEngine

def test_child_support_garnishment():
    res = GarnishmentEngine.calculate_garnishment(4000.0, "CHILD_SUPPORT", 1500.0)
    assert res["actual_deduction"] == 1500.0
    assert res["fully_satisfied"] is True

def test_garnishment_cap_enforcement():
    res = GarnishmentEngine.calculate_garnishment(4000.0, "CREDITOR_GARNISHMENT", 2000.0)
    assert res["actual_deduction"] == 1000.0 # 25% max
    assert res["fully_satisfied"] is False
