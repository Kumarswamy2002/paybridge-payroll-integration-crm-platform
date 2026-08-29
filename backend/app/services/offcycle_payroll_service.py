"""
Off-Cycle & Final Termination Paycheck Processor
"""
from decimal import Decimal
from typing import Dict, Any

class OffCyclePayrollProcessor:
    @staticmethod
    def process_termination_paycheck(base_hourly_rate: float, hours_worked_current_period: float, accrued_pto_hours: float, severance_amount: float = 0.0) -> Dict[str, Any]:
        rate = Decimal(str(base_hourly_rate))
        regular_pay = Decimal(str(hours_worked_current_period)) * rate
        pto_payout = Decimal(str(accrued_pto_hours)) * rate
        severance = Decimal(str(severance_amount))
        gross = regular_pay + pto_payout + severance

        return {
            "regular_earnings": float(round(regular_pay, 2)),
            "pto_payout": float(round(pto_payout, 2)),
            "severance_amount": float(round(severance, 2)),
            "total_gross_pay": float(round(gross, 2)),
            "run_type": "FINAL_TERMINATION_PAYCHECK"
        }
