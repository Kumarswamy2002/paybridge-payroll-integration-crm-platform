from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.payroll import PayrollProfile, Compensation
from app.models.crm import UnifiedTimelineEvent
from app.schemas.payroll import PayrollProfileCreate, CompensationCreate

class PayrollService:
    @staticmethod
    async def create_payroll_profile(db: AsyncSession, tenant_id: str, profile_in: PayrollProfileCreate) -> PayrollProfile:
        profile = PayrollProfile(
            tenant_id=tenant_id,
            employee_id=profile_in.employee_id,
            payroll_provider=profile_in.payroll_provider,
            external_provider_employee_id=profile_in.external_provider_employee_id,
            payment_method=profile_in.payment_method,
            sync_status="IN_SYNC"
        )
        db.add(profile)
        await db.commit()
        await db.refresh(profile)

        # Log event
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=profile.employee_id,
            event_type="PAYROLL_PROFILE_CREATED",
            summary=f"Payroll profile configured with provider {profile.payroll_provider}",
            actor_name="Payroll Administrator"
        )
        db.add(event)
        await db.commit()

        return profile

    @staticmethod
    async def get_profile_by_employee_id(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[PayrollProfile]:
        result = await db.execute(
            select(PayrollProfile).where(PayrollProfile.employee_id == employee_id, PayrollProfile.tenant_id == tenant_id)
        )
        return result.scalars().first()

    @staticmethod
    async def create_compensation(db: AsyncSession, tenant_id: str, comp_in: CompensationCreate) -> Compensation:
        # Supersede old active compensations
        existing_res = await db.execute(
            select(Compensation).where(Compensation.employee_id == comp_in.employee_id, Compensation.tenant_id == tenant_id)
        )
        for old_comp in existing_res.scalars().all():
            old_comp.status = "SUPERSEDED"

        comp = Compensation(
            tenant_id=tenant_id,
            employee_id=comp_in.employee_id,
            pay_frequency=comp_in.pay_frequency,
            currency=comp_in.currency,
            base_salary=comp_in.base_salary,
            hourly_rate=comp_in.hourly_rate,
            effective_date=comp_in.effective_date,
            status="ACTIVE"
        )
        db.add(comp)
        await db.commit()
        await db.refresh(comp)

        # Log timeline event
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=comp.employee_id,
            event_type="SALARY_UPDATED",
            summary=f"Base salary revised to {comp.currency} {comp.base_salary:,.2f}",
            details={"base_salary": comp.base_salary, "currency": comp.currency},
            actor_name="HR Manager"
        )
        db.add(event)
        await db.commit()

        return comp
