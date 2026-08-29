"""
Court-Ordered Wage Garnishment & CCPA Compliance Engine
"""
from decimal import Decimal
from typing import Dict, Any, List

class GarnishmentEngine:
    CCPA_CHILD_SUPPORT_MAX_RATE = Decimal("0.50")
    CCPA_GENERAL_MAX_RATE = Decimal("0.25")

    @classmethod
    def calculate_garnishment(cls, disposable_earnings: float, garnishment_type: str, requested_amount: float) -> Dict[str, Any]:
        disp = Decimal(str(disposable_earnings))
        req = Decimal(str(requested_amount))
        
        max_rate = cls.CCPA_CHILD_SUPPORT_MAX_RATE if garnishment_type == "CHILD_SUPPORT" else cls.CCPA_GENERAL_MAX_RATE
        max_allowable = disp * max_rate
        actual_deduction = min(req, max_allowable)

        return {
            "disposable_earnings": float(disp),
            "garnishment_type": garnishment_type,
            "requested_amount": float(req),
            "max_allowable_deduction": float(round(max_allowable, 2)),
            "actual_deduction": float(round(actual_deduction, 2)),
            "remaining_net_pay": float(round(disp - actual_deduction, 2)),
            "fully_satisfied": actual_deduction == req
        }
