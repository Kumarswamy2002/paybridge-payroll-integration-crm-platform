from backend.app.services.tax_engine_service import TaxEngineService

def test_tax_withholding_calculation():
    res = TaxEngineService.calculate_statutory_withholding(
        gross_pay=5000.0,
        ytd_earnings=20000.0,
        federal_w4_rate=0.15,
        state_rate=0.05
    )
    assert res["gross_pay"] == 5000.0
    assert res["social_security_tax"] == 310.0
    assert res["medicare_tax"] == 72.5
    assert res["federal_income_tax"] == 750.0
    assert res["state_tax"] == 250.0
    assert res["net_pay"] == 3617.5
