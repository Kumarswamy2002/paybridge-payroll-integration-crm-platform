"""
Section 125 Pre-Tax Benefits & 401(k) Matching Engine
"""
from decimal import Decimal
from typing import Dict, Any

class BenefitsEngineService:
    ANNUAL_401K_LIMIT = Decimal("23000.00")

    @classmethod
    def calculate_401k_match(cls, gross_pay: float, employee_contrib_pct: float, employer_match_pct: float, employer_match_cap_pct: float) -> Dict[str, Any]:
        gross = Decimal(str(gross_pay))
        ee_pct = Decimal(str(employee_contrib_pct))
        er_match = Decimal(str(employer_match_pct))
        er_cap = Decimal(str(employer_match_cap_pct))

        ee_contrib = gross * (ee_pct / Decimal("100"))
        matched_pct = min(ee_pct, er_cap)
        er_contrib = gross * (matched_pct / Decimal("100")) * (er_match / Decimal("100"))

        return {
            "gross_pay": float(gross),
            "employee_contribution": float(round(ee_contrib, 2)),
            "employer_match": float(round(er_contrib, 2)),
            "total_401k_deposit": float(round(ee_contrib + er_contrib, 2))
        }
