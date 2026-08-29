from backend.app.services.benefits_engine_service import BenefitsEngineService

def test_401k_matching():
    res = BenefitsEngineService.calculate_401k_match(5000.0, 6.0, 100.0, 4.0)
    assert res["employee_contribution"] == 300.0
    assert res["employer_match"] == 200.0
    assert res["total_401k_deposit"] == 500.0
