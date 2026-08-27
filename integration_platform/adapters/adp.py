from typing import List, Dict, Any, Optional
from datetime import date
from integration_platform.adapters.base import BasePayrollAdapter
from integration_platform.canonical.models import (
    CanonicalEmployee, CanonicalCompensation, CanonicalPayrollRun, CanonicalPayrollResult
)

class ADPWorkforceAdapter(BasePayrollAdapter):
    """ADP Workforce Now Payroll Provider Adapter."""

    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.client_id = config.get("client_id", "adp_client_demo")
        self.client_secret = config.get("client_secret", "adp_secret_demo")

    async def test_connection(self) -> bool:
        return bool(self.client_id and self.client_secret)

    async def get_employees(self) -> List[CanonicalEmployee]:
        raw_adp_workers = [
            {
                "associateOID": "ADP-OID-9901",
                "workerID": {"idValue": "EMP-002"},
                "person": {
                    "legalName": {"givenName": "John", "familyName1": "Reese"},
                    "communication": {"emails": [{"emailUri": "john.r@nexuscorp.com"}]}
                },
                "workAssignment": {
                    "departmentName": "Operations",
                    "jobTitle": "Director of Operations",
                    "hireDate": "2025-03-01"
                }
            }
        ]

        canonical_list = []
        for raw in raw_adp_workers:
            given_name = raw["person"]["legalName"]["givenName"]
            family_name = raw["person"]["legalName"]["familyName1"]
            email = raw["person"]["communication"]["emails"][0]["emailUri"]
            work = raw["workAssignment"]
            hire_dt = date.fromisoformat(work["hireDate"]) if work.get("hireDate") else None

            canonical_list.append(
                CanonicalEmployee(
                    provider_name="ADP",
                    external_id=raw["associateOID"],
                    employee_code=raw["workerID"]["idValue"],
                    first_name=given_name,
                    last_name=family_name,
                    email=email,
                    employment_type="FULL_TIME",
                    status="ACTIVE",
                    hire_date=hire_dt,
                    department_name=work.get("departmentName"),
                    job_title=work.get("jobTitle"),
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
                provider_name="ADP",
                payroll_run_id="ADP-RUN-2026-01",
                period_start=date(2026, 1, 1),
                period_end=date(2026, 1, 31),
                payment_date=date(2026, 1, 31),
                status="PROCESSED",
                total_gross_pay=185000.00 / 12,
                total_net_pay=11500.00,
                total_tax=2900.00,
                total_deductions=1016.66,
                records_count=1
            )
        ]

    async def get_payroll_results(self, payroll_run_id: str) -> List[CanonicalPayrollResult]:
        return [
            CanonicalPayrollResult(
                payroll_run_id=payroll_run_id,
                external_employee_id="ADP-OID-9901",
                gross_pay=15416.66,
                net_pay=11500.00,
                tax_withheld=2900.00,
                deductions=1016.66,
                direct_deposit_amount=11500.00
            )
        ]

    async def process_webhook(self, payload: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        return {"status": "success", "provider": "ADP", "event": "worker.change"}
