import random
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.crm import CRMCase, CRMActivity, UnifiedTimelineEvent
from app.schemas.crm import CRMCaseCreate

class CRMService:
    @staticmethod
    async def create_case(db: AsyncSession, tenant_id: str, case_in: CRMCaseCreate) -> CRMCase:
        ticket_number = f"PAY-{random.randint(10000, 99999)}"
        case = CRMCase(
            tenant_id=tenant_id,
            ticket_number=ticket_number,
            employee_id=case_in.employee_id,
            title=case_in.title,
            description=case_in.description,
            category=case_in.category,
            priority=case_in.priority,
            assigned_to_user_id=case_in.assigned_to_user_id,
            status="OPEN"
        )
        db.add(case)
        await db.commit()
        await db.refresh(case)

        # Log timeline event
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=case.employee_id,
            event_type="CASE_OPENED",
            summary=f"Payroll Case [{ticket_number}] opened: {case.title}",
            details={"ticket_number": ticket_number, "priority": case.priority},
            actor_name="Employee Support"
        )
        db.add(event)
        await db.commit()

        return case

    @staticmethod
    async def list_cases(db: AsyncSession, tenant_id: str, employee_id: Optional[str] = None) -> List[CRMCase]:
        query = select(CRMCase).where(CRMCase.tenant_id == tenant_id)
        if employee_id:
            query = query.where(CRMCase.employee_id == employee_id)
        result = await db.execute(query.order_by(CRMCase.created_at.desc()))
        return result.scalars().all()

    @staticmethod
    async def get_employee_timeline(db: AsyncSession, tenant_id: str, employee_id: str) -> List[UnifiedTimelineEvent]:
        result = await db.execute(
            select(UnifiedTimelineEvent)
            .where(UnifiedTimelineEvent.employee_id == employee_id, UnifiedTimelineEvent.tenant_id == tenant_id)
            .order_by(UnifiedTimelineEvent.created_at.desc())
        )
        return result.scalars().all()
