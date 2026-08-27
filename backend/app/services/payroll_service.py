from typing import Optional, List
from datetime import date, datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.payroll import PayrollProfile, Compensation
from app.models.crm import UnifiedTimelineEvent
from app.schemas.payroll import PayrollProfileCreate, CompensationCreate
from app.core.crypto import encrypt_field, decrypt_field

class PayrollService:
    @staticmethod
    async def create_payroll_profile(
        db: AsyncSession, 
        tenant_id: str, 
        profile_in: PayrollProfileCreate,
        tax_identifier: Optional[str] = None,
        bank_account: Optional[str] = None
    ) -> PayrollProfile:
        # Check if profile exists for employee
        existing = await db.execute(
            select(PayrollProfile).where(
                PayrollProfile.employee_id == profile_in.employee_id, 
                PayrollProfile.tenant_id == tenant_id
            )
        )
        if existing.scalars().first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Payroll profile already exists for this employee"
            )

        encrypted_tax = encrypt_field(tax_identifier) if tax_identifier else None
        encrypted_bank = encrypt_field(bank_account) if bank_account else None

        profile = PayrollProfile(
            tenant_id=tenant_id,
            employee_id=profile_in.employee_id,
            payroll_provider=profile_in.payroll_provider,
            external_provider_employee_id=profile_in.external_provider_employee_id,
            payment_method=profile_in.payment_method,
            tax_identifier_encrypted=encrypted_tax,
            bank_account_encrypted=encrypted_bank,
            sync_status="IN_SYNC",
            last_synced_at=datetime.utcnow()
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
            details={"provider": profile.payroll_provider, "payment_method": profile.payment_method},
            actor_name="Payroll Administrator"
        )
        db.add(event)
        await db.commit()

        return profile

    @staticmethod
    async def get_profile_by_employee_id(db: AsyncSession, tenant_id: str, employee_id: str) -> Optional[PayrollProfile]:
        result = await db.execute(
            select(PayrollProfile).where(
                PayrollProfile.employee_id == employee_id, 
                PayrollProfile.tenant_id == tenant_id
            )
        )
        return result.scalars().first()

    @staticmethod
    async def get_decrypted_pii(db: AsyncSession, tenant_id: str, employee_id: str) -> dict:
        profile = await PayrollService.get_profile_by_employee_id(db, tenant_id, employee_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Payroll profile not found")
        
        return {
            "employee_id": employee_id,
            "tax_identifier": decrypt_field(profile.tax_identifier_encrypted) if profile.tax_identifier_encrypted else None,
            "bank_account": decrypt_field(profile.bank_account_encrypted) if profile.bank_account_encrypted else None,
        }

    @staticmethod
    async def create_compensation(db: AsyncSession, tenant_id: str, comp_in: CompensationCreate) -> Compensation:
        # Supersede all prior active compensation records for this employee
        existing_res = await db.execute(
            select(Compensation).where(
                Compensation.employee_id == comp_in.employee_id, 
                Compensation.tenant_id == tenant_id,
                Compensation.status == "ACTIVE"
            )
        )
        prior_comp = existing_res.scalars().first()
        old_salary = prior_comp.base_salary if prior_comp else 0.0

        if prior_comp:
            prior_comp.status = "SUPERSEDED"

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

        # Log timeline event with salary change delta
        summary = (
            f"Base salary revised from {comp.currency} {old_salary:,.2f} to {comp.currency} {comp.base_salary:,.2f}"
            if old_salary > 0 else
            f"Initial compensation established: {comp.currency} {comp.base_salary:,.2f} / {comp.pay_frequency}"
        )

        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=comp.employee_id,
            event_type="SALARY_UPDATED",
            summary=summary,
            details={
                "previous_salary": old_salary,
                "new_salary": comp.base_salary,
                "currency": comp.currency,
                "effective_date": str(comp.effective_date)
            },
            actor_name="HR Compensation Lead"
        )
        db.add(event)
        await db.commit()

        return comp

    @staticmethod
    async def get_compensation_history(db: AsyncSession, tenant_id: str, employee_id: str) -> List[Compensation]:
        result = await db.execute(
            select(Compensation)
            .where(Compensation.employee_id == employee_id, Compensation.tenant_id == tenant_id)
            .order_by(Compensation.effective_date.desc(), Compensation.created_at.desc())
        )
        return result.scalars().all()
