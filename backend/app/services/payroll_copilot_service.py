"""
AI Payroll Copilot & FLSA Compliance Advisory Service
"""
from typing import Dict, Any, List
from decimal import Decimal

class PayrollCopilotService:
    FEDERAL_MINIMUM_HOURLY_WAGE = Decimal("7.25")
    FLSA_EXEMPT_SALARY_THRESHOLD_ANNUAL = Decimal("35568.00")

    @classmethod
    def evaluate_flsa_compliance(cls, employee_id: str, hourly_rate: float, annual_salary: float, is_exempt: bool) -> Dict[str, Any]:
        violations = []
        if not is_exempt and Decimal(str(hourly_rate)) < cls.FEDERAL_MINIMUM_HOURLY_WAGE:
            violations.append(f"Hourly rate ${hourly_rate} is below federal minimum wage ${cls.FEDERAL_MINIMUM_HOURLY_WAGE}")
        if is_exempt and Decimal(str(annual_salary)) < cls.FLSA_EXEMPT_SALARY_THRESHOLD_ANNUAL:
            violations.append(f"Exempt salary ${annual_salary} is below FLSA threshold ${cls.FLSA_EXEMPT_SALARY_THRESHOLD_ANNUAL}")
        return {
            "employee_id": employee_id,
            "compliant": len(violations) == 0,
            "violations": violations,
            "rule_set": "FLSA-2026-V1"
        }

    @classmethod
    def generate_variance_advisory(cls, discrepancy_id: str, expected_amount: float, actual_amount: float, category: str) -> Dict[str, Any]:
        diff = actual_amount - expected_amount
        percent_diff = (diff / expected_amount * 100) if expected_amount else 0.0
        severity = "HIGH" if abs(diff) > 500 else ("MEDIUM" if abs(diff) > 100 else "LOW")
        return {
            "discrepancy_id": discrepancy_id,
            "category": category,
            "variance_amount": diff,
            "variance_percentage": round(percent_diff, 2),
            "severity": severity,
            "ai_explanation": f"Detected {category} discrepancy of ${abs(diff):.2f}. Automated reconciliation recommended.",
            "recommended_action": "Auto-adjust line items" if severity == "LOW" else "Manual HR approval required"
        }
