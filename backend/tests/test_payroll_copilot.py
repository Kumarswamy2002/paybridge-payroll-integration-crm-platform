from backend.app.services.payroll_copilot_service import PayrollCopilotService

def test_flsa_compliance_valid():
    res = PayrollCopilotService.evaluate_flsa_compliance("emp-101", 18.50, 45000.0, True)
    assert res["compliant"] is True
    assert len(res["violations"]) == 0

def test_variance_advisory():
    res = PayrollCopilotService.generate_variance_advisory("disc-1", 1000.0, 1600.0, "GROSS_PAY")
    assert res["severity"] == "HIGH"
    assert res["variance_amount"] == 600.0
