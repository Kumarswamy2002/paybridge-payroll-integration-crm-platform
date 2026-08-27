from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.reconciliation import PayrollReconciliationRun, PayrollDiscrepancy
from app.models.employee import Employee
from app.models.payroll import Compensation, PayrollProfile
from app.models.crm import UnifiedTimelineEvent
from app.schemas.crm import CRMCaseCreate
from app.services.crm_service import CRMService
from integration_platform.canonical.models import CanonicalPayrollResult

class ReconciliationService:
    """Intelligent Reconciliation Comparator & Exception-to-CRM Pipeline."""

    @classmethod
    async def run_reconciliation(
        cls,
        db: AsyncSession,
        tenant_id: str,
        payroll_provider: str,
        payroll_run_id: str,
        provider_results: List[CanonicalPayrollResult],
        tolerance_threshold: float = 1.00
    ) -> Dict[str, Any]:
        recon_run = PayrollReconciliationRun(
            tenant_id=tenant_id,
            payroll_provider=payroll_provider,
            payroll_run_id=payroll_run_id,
            status="IN_PROGRESS"
        )
        db.add(recon_run)
        await db.commit()
        await db.refresh(recon_run)

        compared_count = 0
        matched_count = 0
        discrepancies_count = 0
        discrepancies_list = []

        for result in provider_results:
            compared_count += 1
            # Find matching profile in PayBridge
            profile_res = await db.execute(
                select(PayrollProfile).where(
                    PayrollProfile.external_provider_employee_id == result.external_employee_id,
                    PayrollProfile.tenant_id == tenant_id
                )
            )
            profile = profile_res.scalars().first()
            if not profile:
                # Discrepancy: MISSING_EMPLOYEE in PayBridge
                discrepancy = PayrollDiscrepancy(
                    tenant_id=tenant_id,
                    reconciliation_run_id=recon_run.id,
                    employee_id=tenant_id, # Fallback ID
                    discrepancy_type="MISSING_EMPLOYEE",
                    severity="CRITICAL",
                    provider_value=result.gross_pay,
                    details={"external_employee_id": result.external_employee_id}
                )
                db.add(discrepancy)
                discrepancies_count += 1
                continue

            # Fetch active compensation in PayBridge
            comp_res = await db.execute(
                select(Compensation).where(
                    Compensation.employee_id == profile.employee_id,
                    Compensation.tenant_id == tenant_id,
                    Compensation.status == "ACTIVE"
                )
            )
            comp = comp_res.scalars().first()
            expected_gross = (comp.base_salary / 12) if comp else 0.0
            actual_gross = result.gross_pay
            variance = abs(expected_gross - actual_gross)

            if variance > tolerance_threshold:
                discrepancies_count += 1
                discrepancy = PayrollDiscrepancy(
                    tenant_id=tenant_id,
                    reconciliation_run_id=recon_run.id,
                    employee_id=profile.employee_id,
                    discrepancy_type="SALARY_MISMATCH",
                    severity="HIGH" if variance > 500 else "MEDIUM",
                    paybridge_value=expected_gross,
                    provider_value=actual_gross,
                    variance_amount=variance,
                    details={
                        "expected_monthly_gross": expected_gross,
                        "actual_provider_gross": actual_gross,
                        "payroll_run_id": payroll_run_id
                    }
                )
                db.add(discrepancy)
                await db.commit()
                await db.refresh(discrepancy)

                # Exception-to-CRM Pipeline: Automatically create CRM Case
                case_in = CRMCaseCreate(
                    employee_id=profile.employee_id,
                    title=f"Reconciliation Mismatch: {payroll_provider} Pay Run {payroll_run_id}",
                    description=(
                        f"Automated Reconciliation Engine detected a salary variance of ${variance:,.2f}.\n"
                        f"PayBridge Expected: ${expected_gross:,.2f} | Provider Gross: ${actual_gross:,.2f}"
                    ),
                    category="DISCREPANCY",
                    priority="HIGH"
                )
                crm_case = await CRMService.create_case(db, tenant_id, case_in)
                discrepancy.crm_case_id = crm_case.id
                discrepancy.status = "CASE_CREATED"

                discrepancies_list.append(discrepancy)
            else:
                matched_count += 1

        recon_run.total_records_compared = compared_count
        recon_run.matched_records_count = matched_count
        recon_run.discrepancies_count = discrepancies_count
        recon_run.status = "COMPLETED"
        await db.commit()

        # Log timeline event
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=tenant_id,
            event_type="RECONCILIATION_COMPLETED",
            summary=f"Payroll Reconciliation completed for {payroll_provider} ({discrepancies_count} mismatches detected)",
            details={
                "reconciliation_run_id": recon_run.id,
                "discrepancies_count": discrepancies_count,
                "matched_count": matched_count
            },
            actor_name="Intelligent Reconciliation Engine"
        )
        db.add(event)
        await db.commit()

        return {
            "reconciliation_run_id": recon_run.id,
            "payroll_provider": payroll_provider,
            "payroll_run_id": payroll_run_id,
            "total_compared": compared_count,
            "matched": matched_count,
            "discrepancies_count": discrepancies_count,
            "status": "COMPLETED"
        }

    @classmethod
    async def list_discrepancies(cls, db: AsyncSession, tenant_id: str) -> List[PayrollDiscrepancy]:
        result = await db.execute(
            select(PayrollDiscrepancy)
            .where(PayrollDiscrepancy.tenant_id == tenant_id)
            .order_by(PayrollDiscrepancy.created_at.desc())
        )
        return result.scalars().all()
