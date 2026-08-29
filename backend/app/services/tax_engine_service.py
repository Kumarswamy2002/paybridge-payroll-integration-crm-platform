"""
Multi-Jurisdiction Payroll Statutory Tax Engine
"""
from decimal import Decimal
from typing import Dict, Any

class TaxEngineService:
    FICA_SS_RATE = Decimal("0.062")
    FICA_MEDICARE_RATE = Decimal("0.0145")
    FICA_SS_WAGE_BASE_CAP = Decimal("168600.00")

    @classmethod
    def calculate_statutory_withholding(cls, gross_pay: float, ytd_earnings: float, federal_w4_rate: float, state_rate: float) -> Dict[str, Any]:
        gross = Decimal(str(gross_pay))
        ytd = Decimal(str(ytd_earnings))
        ss_taxable = max(Decimal("0.0"), min(gross, cls.FICA_SS_WAGE_BASE_CAP - ytd))
        ss_tax = ss_taxable * cls.FICA_SS_RATE
        medicare_tax = gross * cls.FICA_MEDICARE_RATE
        fed_income_tax = gross * Decimal(str(federal_w4_rate))
        state_tax = gross * Decimal(str(state_rate))
        total_tax = ss_tax + medicare_tax + fed_income_tax + state_tax
        net_pay = gross - total_tax

        return {
            "gross_pay": float(gross),
            "social_security_tax": float(round(ss_tax, 2)),
            "medicare_tax": float(round(medicare_tax, 2)),
            "federal_income_tax": float(round(fed_income_tax, 2)),
            "state_tax": float(round(state_tax, 2)),
            "total_withholding": float(round(total_tax, 2)),
            "net_pay": float(round(net_pay, 2))
        }
