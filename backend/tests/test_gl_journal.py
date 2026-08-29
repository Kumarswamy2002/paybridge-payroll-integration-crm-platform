from backend.app.services.gl_journal_service import GLJournalService

def test_gl_journal_balance():
    res = GLJournalService.create_journal_batch(
        gross_wages=10000.0,
        employer_taxes=800.0,
        employee_withholdings=2500.0,
        net_pay=7500.0
    )
    assert res["is_balanced"] is True
    assert res["total_debit"] == 10800.0
    assert res["total_credit"] == 10800.0
