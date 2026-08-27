from typing import List, Dict, Any, Optional
from datetime import date
from integration_platform.adapters.base import BasePayrollAdapter
from integration_platform.canonical.models import (
    CanonicalEmployee, CanonicalCompensation, CanonicalPayrollRun, CanonicalPayrollResult
)

class MockPayrollAdapter(BasePayrollAdapter):
    """Mock Payroll Adapter serving standardized payroll test data."""

    async def test_connection(self) -> bool:
        return True

    async def get_employees(self) -> List[CanonicalEmployee]:
        return [
            CanonicalEmployee(
                provider_name="MOCK_PAYROLL",
                external_id="MOCK-EMP-101",
                employee_code="EMP-001",
                first_name="Sarah",
                last_name="Connor",
                email="sarah.c@nexus.com",
                employment_type="FULL_TIME",
                status="ACTIVE",
                hire_date=date(2025, 1, 15),
                department_name="Engineering",
                job_title="Lead Architect",
                raw_provider_data={"vendor": "MockProvider", "id": "101"}
            ),
            CanonicalEmployee(
                provider_name="MOCK_PAYROLL",
                external_id="MOCK-EMP-102",
                employee_code="EMP-002",
                first_name="John",
                last_name="Reese",
                email="john.r@nexus.com",
                employment_type="FULL_TIME",
                status="ACTIVE",
                hire_date=date(2025, 3, 1),
                department_name="Operations",
                job_title="Security Lead",
                raw_provider_data={"vendor": "MockProvider", "id": "102"}
            ),
        ]

    async def get_employee(self, external_id: str) -> Optional[CanonicalEmployee]:
        employees = await self.get_employees()
        for emp in employees:
            if emp.external_id == external_id:
                return emp
        return None

    async def get_payroll_runs(self, limit: int = 50) -> List[CanonicalPayrollRun]:
        return [
            CanonicalPayrollRun(
                provider_name="MOCK_PAYROLL",
                payroll_run_id="RUN-2026-01",
                period_start=date(2026, 1, 1),
                period_end=date(2026, 1, 31),
                payment_date=date(2026, 1, 31),
                status="PROCESSED",
                total_gross_pay=240000.00,
                total_net_pay=180000.00,
                total_tax=45000.00,
                total_deductions=15000.00,
                records_count=2
            )
        ]

    async def get_payroll_results(self, payroll_run_id: str) -> List[CanonicalPayrollResult]:
        return [
            CanonicalPayrollResult(
                payroll_run_id=payroll_run_id,
                external_employee_id="MOCK-EMP-101",
                gross_pay=125000.00 / 12,
                net_pay=7800.00,
                tax_withheld=2000.00,
                deductions=616.66,
                direct_deposit_amount=7800.00
            ),
            CanonicalPayrollResult(
                payroll_run_id=payroll_run_id,
                external_employee_id="MOCK-EMP-102",
                gross_pay=115000.00 / 12,
                net_pay=7200.00,
                tax_withheld=1800.00,
                deductions=583.33,
                direct_deposit_amount=7200.00
            )
        ]

    async def process_webhook(self, payload: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        return {"status": "processed", "event_type": payload.get("event_type", "unknown")}
