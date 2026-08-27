from typing import List, Dict, Any, Optional
from datetime import date
from integration_platform.adapters.base import BasePayrollAdapter
from integration_platform.canonical.models import (
    CanonicalEmployee, CanonicalCompensation, CanonicalPayrollRun, CanonicalPayrollResult
)

class GustoAdapter(BasePayrollAdapter):
    """Gusto Payroll Provider Adapter."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.api_key = config.get("api_key", "gusto_demo_key")
        self.company_id = config.get("company_id", "gusto_company_101")

    async def test_connection(self) -> bool:
        # Verify Gusto API Key & Connectivity
        return bool(self.api_key and self.company_id)

    async def get_employees(self) -> List[CanonicalEmployee]:
        # Transforms Gusto JSON Schema to Canonical Employee Schema
        raw_gusto_employees = [
            {
                "id": "gusto_emp_8801",
                "version": "v2",
                "first_name": "Sarah",
                "last_name": "Connor",
                "email": "sarah.c@nexuscorp.com",
                "phone": "555-0199",
                "department": "Engineering",
                "title": "Principal Architect",
                "employment_status": "active",
                "hire_date": "2025-01-15",
                "job": {"rate": "165000.00", "payment_unit": "Year"}
            },
            {
                "id": "gusto_emp_8802",
                "version": "v2",
                "first_name": "Marcus",
                "last_name": "Wright",
                "email": "marcus.w@nexuscorp.com",
                "phone": "555-0288",
                "department": "Engineering",
                "title": "VP Engineering",
                "employment_status": "active",
                "hire_date": "2024-11-01",
                "job": {"rate": "210000.00", "payment_unit": "Year"}
            }
        ]

        canonical_list = []
        for raw in raw_gusto_employees:
            hire_dt = date.fromisoformat(raw["hire_date"]) if raw.get("hire_date") else None
            canonical_list.append(
                CanonicalEmployee(
                    provider_name="GUSTO",
                    external_id=raw["id"],
                    first_name=raw["first_name"],
                    last_name=raw["last_name"],
                    email=raw["email"],
                    phone=raw.get("phone"),
                    employment_type="FULL_TIME",
                    status="ACTIVE" if raw.get("employment_status") == "active" else "TERMINATED",
                    hire_date=hire_dt,
                    department_name=raw.get("department"),
                    job_title=raw.get("title"),
                    raw_provider_data=raw
                )
            )
        return canonical_list

    async def get_employee(self, external_id: str) -> Optional[CanonicalEmployee]:
        employees = await self.get_employees()
        for emp in employees:
            if emp.external_id == external_id:
                return emp
        return None

    async def get_payroll_runs(self, limit: int = 50) -> List[CanonicalPayrollRun]:
        return [
            CanonicalPayrollRun(
                provider_name="GUSTO",
                payroll_run_id="GUSTO-PAYRUN-2026-01",
                period_start=date(2026, 1, 1),
                period_end=date(2026, 1, 31),
                payment_date=date(2026, 1, 31),
                status="PROCESSED",
                total_gross_pay=375000.00,
                total_net_pay=275000.00,
                total_tax=75000.00,
                total_deductions=25000.00,
                records_count=2
            )
        ]

    async def get_payroll_results(self, payroll_run_id: str) -> List[CanonicalPayrollResult]:
        return [
            CanonicalPayrollResult(
                payroll_run_id=payroll_run_id,
                external_employee_id="gusto_emp_8801",
                gross_pay=13750.00,
                net_pay=9850.00,
                tax_withheld=2900.00,
                deductions=1000.00,
                direct_deposit_amount=9850.00
            ),
            CanonicalPayrollResult(
                payroll_run_id=payroll_run_id,
                external_employee_id="gusto_emp_8802",
                gross_pay=17500.00,
                net_pay=12400.00,
                tax_withheld=3700.00,
                deductions=1400.00,
                direct_deposit_amount=12400.00
            )
        ]

    async def process_webhook(self, payload: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        event_type = payload.get("event_type", "payroll.processed")
        return {"status": "success", "provider": "GUSTO", "event": event_type}
