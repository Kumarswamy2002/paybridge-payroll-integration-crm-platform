"""
General Ledger (GL) Journal Entry Export Engine
"""
from decimal import Decimal
from typing import List, Dict, Any

class GLJournalService:
    @staticmethod
    def create_journal_batch(gross_wages: float, employer_taxes: float, employee_withholdings: float, net_pay: float) -> Dict[str, Any]:
        wages = Decimal(str(gross_wages))
        er_tax = Decimal(str(employer_taxes))
        ee_withhold = Decimal(str(employee_withholdings))
        net = Decimal(str(net_pay))

        # Debits
        debits = [
            {"account": "5000 - Payroll Expense (Gross)", "amount": float(wages)},
            {"account": "5010 - Employer Payroll Taxes", "amount": float(er_tax)}
        ]

        # Credits
        credits = [
            {"account": "2000 - Payroll Taxes Payable", "amount": float(ee_withhold + er_tax)},
            {"account": "1000 - Cash Operating (Net Pay)", "amount": float(net)}
        ]

        total_debit = wages + er_tax
        total_credit = (ee_withhold + er_tax) + net

        return {
            "batch_id": "GL_PAY_2026",
            "is_balanced": total_debit == total_credit,
            "total_debit": float(round(total_debit, 2)),
            "total_credit": float(round(total_credit, 2)),
            "entries": {"debits": debits, "credits": credits}
        }
