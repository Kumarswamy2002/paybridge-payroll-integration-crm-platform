import random
from datetime import datetime
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.crm import CRMCase, CRMActivity, UnifiedTimelineEvent
from app.schemas.crm import CRMCaseCreate

VALID_CASE_STATUSES = ["OPEN", "TRIAGED", "ASSIGNED", "INVESTIGATING", "WAITING", "RESOLVED", "CLOSED"]
VALID_PRIORITIES = ["LOW", "MEDIUM", "HIGH", "URGENT"]

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
            priority=case_in.priority if case_in.priority in VALID_PRIORITIES else "MEDIUM",
            assigned_to_user_id=case_in.assigned_to_user_id,
            status="OPEN"
        )
        db.add(case)
        await db.commit()
        await db.refresh(case)

        # Log initial activity note
        activity = CRMActivity(
            tenant_id=tenant_id,
            employee_id=case.employee_id,
            case_id=case.id,
            activity_type="SYSTEM",
            title=f"Case [{ticket_number}] Created",
            content=f"Category: {case.category} | Priority: {case.priority}\nDescription: {case.description or 'N/A'}"
        )
        db.add(activity)

        # Log timeline event
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=case.employee_id,
            event_type="CASE_OPENED",
            summary=f"Payroll Case [{ticket_number}] opened: {case.title}",
            details={"ticket_number": ticket_number, "priority": case.priority, "category": case.category},
            actor_name="Employee Support"
        )
        db.add(event)
        await db.commit()

        return case

    @staticmethod
    async def transition_case_status(
        db: AsyncSession, 
        tenant_id: str, 
        case_id: str, 
        new_status: str,
        resolution_notes: Optional[str] = None,
        assigned_to_user_id: Optional[str] = None,
        actor_name: str = "HR Specialist"
    ) -> CRMCase:
        if new_status not in VALID_CASE_STATUSES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status: {new_status}. Allowed: {VALID_CASE_STATUSES}"
            )

        result = await db.execute(
            select(CRMCase).where(CRMCase.id == case_id, CRMCase.tenant_id == tenant_id)
        )
        case = result.scalars().first()
        if not case:
            raise HTTPException(status_code=404, detail="Payroll case not found")

        old_status = case.status
        case.status = new_status

        if assigned_to_user_id:
            case.assigned_to_user_id = assigned_to_user_id

        if new_status in ["RESOLVED", "CLOSED"]:
            case.resolution_notes = resolution_notes
            case.resolved_at = datetime.utcnow()

        await db.commit()
        await db.refresh(case)

        # Record Activity Log
        activity = CRMActivity(
            tenant_id=tenant_id,
            employee_id=case.employee_id,
            case_id=case.id,
            activity_type="STATUS_CHANGE",
            title=f"Case Status Updated: {old_status} -> {new_status}",
            content=f"Resolution Notes: {resolution_notes}" if resolution_notes else f"Transitioned by {actor_name}"
        )
        db.add(activity)

        # Log Timeline Event
        event_type = "CASE_RESOLVED" if new_status in ["RESOLVED", "CLOSED"] else "CASE_UPDATED"
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=case.employee_id,
            event_type=event_type,
            summary=f"Payroll Case [{case.ticket_number}] status changed to {new_status}",
            details={"old_status": old_status, "new_status": new_status, "notes": resolution_notes},
            actor_name=actor_name
        )
        db.add(event)
        await db.commit()

        return case

    @staticmethod
    async def add_case_activity(
        db: AsyncSession,
        tenant_id: str,
        case_id: str,
        activity_type: str,
        title: str,
        content: str,
        actor_user_id: Optional[str] = None
    ) -> CRMActivity:
        result = await db.execute(
            select(CRMCase).where(CRMCase.id == case_id, CRMCase.tenant_id == tenant_id)
        )
        case = result.scalars().first()
        if not case:
            raise HTTPException(status_code=404, detail="Case not found")

        activity = CRMActivity(
            tenant_id=tenant_id,
            employee_id=case.employee_id,
            case_id=case.id,
            activity_type=activity_type,
            title=title,
            content=content,
            actor_user_id=actor_user_id
        )
        db.add(activity)
        await db.commit()
        await db.refresh(activity)
        return activity

    @staticmethod
    async def list_cases(db: AsyncSession, tenant_id: str, employee_id: Optional[str] = None) -> List[CRMCase]:
        query = select(CRMCase).where(CRMCase.tenant_id == tenant_id)
        if employee_id:
            query = query.where(CRMCase.employee_id == employee_id)
        result = await db.execute(query.order_by(CRMCase.created_at.desc()))
        return result.scalars().all()

    @staticmethod
    async def get_case_by_id(db: AsyncSession, tenant_id: str, case_id: str) -> Optional[CRMCase]:
        result = await db.execute(
            select(CRMCase).where(CRMCase.id == case_id, CRMCase.tenant_id == tenant_id)
        )
        return result.scalars().first()

    @staticmethod
    async def get_case_activities(db: AsyncSession, tenant_id: str, case_id: str) -> List[CRMActivity]:
        result = await db.execute(
            select(CRMActivity)
            .where(CRMActivity.case_id == case_id, CRMActivity.tenant_id == tenant_id)
            .order_by(CRMActivity.created_at.desc())
        )
        return result.scalars().all()

    @staticmethod
    async def get_employee_timeline(db: AsyncSession, tenant_id: str, employee_id: str) -> List[UnifiedTimelineEvent]:
        result = await db.execute(
            select(UnifiedTimelineEvent)
            .where(UnifiedTimelineEvent.employee_id == employee_id, UnifiedTimelineEvent.tenant_id == tenant_id)
            .order_by(UnifiedTimelineEvent.created_at.desc())
        )
        return result.scalars().all()
