import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from integration_platform.adapters.factory import AdapterFactory
from app.models.employee import Employee
from app.models.payroll import PayrollProfile, Compensation
from app.models.crm import UnifiedTimelineEvent
from app.services.employee_service import EmployeeService
from app.services.payroll_service import PayrollService
from app.schemas.employee import EmployeeCreate
from app.schemas.payroll import PayrollProfileCreate, CompensationCreate

class SyncResult(BaseModel := type("SyncResult", (), {})):
    job_id: str
    tenant_id: str
    provider_name: str
    status: str
    records_processed: int
    records_failed: int
    errors: List[str]

class SynchronizationEngine:
    """Orchestrates sync execution between external payroll providers and PayBridge DB."""

    @classmethod
    async def run_sync_job(
        cls,
        db: AsyncSession,
        tenant_id: str,
        provider_name: str,
        provider_config: Dict[str, Any],
        sync_type: str = "MANUAL_SYNC"
    ) -> Dict[str, Any]:
        job_id = f"SYNC-{uuid.uuid4().hex[:8].upper()}"
        adapter = AdapterFactory.get_adapter(provider_name, provider_config)

        records_processed = 0
        records_failed = 0
        errors = []

        try:
            # Fetch canonical employees from provider adapter
            canonical_employees = await adapter.get_employees()

            for canonical_emp in canonical_employees:
                try:
                    # Idempotency check: Find existing employee by email or provider external ID
                    existing = await db.execute(
                        select(Employee).where(
                            Employee.tenant_id == tenant_id,
                            Employee.email == canonical_emp.email
                        )
                    )
                    emp = existing.scalars().first()

                    if not emp:
                        # Create new employee record
                        emp_code = canonical_emp.employee_code or f"EMP-{uuid.uuid4().hex[:4].upper()}"
                        emp_create = EmployeeCreate(
                            employee_code=emp_code,
                            first_name=canonical_emp.first_name,
                            last_name=canonical_emp.last_name,
                            email=canonical_emp.email,
                            phone=canonical_emp.phone,
                            employment_type=canonical_emp.employment_type,
                            status=canonical_emp.status,
                            date_of_joining=canonical_emp.hire_date
                        )
                        emp = await EmployeeService.create_employee(db, tenant_id, emp_create)

                    # Upsert Payroll Profile
                    prof_existing = await db.execute(
                        select(PayrollProfile).where(
                            PayrollProfile.employee_id == emp.id,
                            PayrollProfile.tenant_id == tenant_id
                        )
                    )
                    profile = prof_existing.scalars().first()
                    if not profile:
                        prof_in = PayrollProfileCreate(
                            employee_id=emp.id,
                            payroll_provider=provider_name,
                            external_provider_employee_id=canonical_emp.external_id,
                            payment_method="DIRECT_DEPOSIT"
                        )
                        await PayrollService.create_payroll_profile(db, tenant_id, prof_in)
                    else:
                        profile.sync_status = "IN_SYNC"
                        profile.last_synced_at = datetime.utcnow()
                        await db.commit()

                    records_processed += 1
                except Exception as ex:
                    records_failed += 1
                    errors.append(f"Failed to sync employee {canonical_emp.email}: {str(ex)}")

            # Log overall sync job completion event in timeline
            status_str = "SUCCESS" if records_failed == 0 else "PARTIAL_SUCCESS"
            event = UnifiedTimelineEvent(
                tenant_id=tenant_id,
                employee_id=emp.id if 'emp' in locals() and emp else tenant_id,
                event_type="SYNC_COMPLETED",
                summary=f"{provider_name} Synchronization completed ({records_processed} processed, {records_failed} failed)",
                details={
                    "job_id": job_id,
                    "sync_type": sync_type,
                    "records_processed": records_processed,
                    "records_failed": records_failed,
                    "errors": errors
                },
                actor_name=f"{provider_name} Adapter"
            )
            db.add(event)
            await db.commit()

            return {
                "job_id": job_id,
                "tenant_id": tenant_id,
                "provider_name": provider_name,
                "status": status_str,
                "records_processed": records_processed,
                "records_failed": records_failed,
                "errors": errors
            }

        except Exception as global_ex:
            return {
                "job_id": job_id,
                "tenant_id": tenant_id,
                "provider_name": provider_name,
                "status": "FAILED",
                "records_processed": records_processed,
                "records_failed": records_failed,
                "errors": [str(global_ex)]
            }
