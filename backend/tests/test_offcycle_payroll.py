from backend.app.services.offcycle_payroll_service import OffCyclePayrollProcessor

def test_termination_paycheck():
    res = OffCyclePayrollProcessor.process_termination_paycheck(40.0, 40.0, 20.0, 2000.0)
    assert res["regular_earnings"] == 1600.0
    assert res["pto_payout"] == 800.0
    assert res["total_gross_pay"] == 4400.0
