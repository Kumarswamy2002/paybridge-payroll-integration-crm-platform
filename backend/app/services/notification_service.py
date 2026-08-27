from typing import List, Dict, Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.notification import Notification, CaseMessage
from app.models.crm import CRMCase

class NotificationService:
    """Multi-channel Notification & Case Threading Service."""

    TEMPLATES = {
        "PAYSLIP_AVAILABLE": "Hello {name}, your payslip for {period} is now ready to view.",
        "CASE_UPDATED": "Hello {name}, your payroll ticket [{ticket_number}] has been updated to status: {status}.",
        "APPROVAL_REQUESTED": "Action Required: Approval requested for {entity_type} revision.",
        "SYNC_FAILURE_ALERT": "Alert: {provider} synchronization encountered {error_count} errors."
    }

    @classmethod
    async def send_notification(
        cls,
        db: AsyncSession,
        tenant_id: str,
        user_id: str,
        title: str,
        template_name: Optional[str] = None,
        context: Dict[str, Any] = None,
        channel: str = "IN_APP"
    ) -> Notification:
        context = context or {}
        message_body = title

        if template_name and template_name in cls.TEMPLATES:
            template_str = cls.TEMPLATES[template_name]
            try:
                message_body = template_str.format(**context)
            except KeyError:
                message_body = template_str

        notif = Notification(
            tenant_id=tenant_id,
            user_id=user_id,
            channel=channel,
            title=title,
            message=message_body,
            template_name=template_name,
            data=context,
            is_read=False
        )
        db.add(notif)
        await db.commit()
        await db.refresh(notif)
        return notif

    @classmethod
    async def list_user_notifications(cls, db: AsyncSession, tenant_id: str, user_id: str) -> List[Notification]:
        result = await db.execute(
            select(Notification)
            .where(Notification.tenant_id == tenant_id, Notification.user_id == user_id)
            .order_by(Notification.created_at.desc())
        )
        return result.scalars().all()

    @classmethod
    async def mark_read(cls, db: AsyncSession, tenant_id: str, notification_id: str) -> Notification:
        result = await db.execute(
            select(Notification).where(Notification.id == notification_id, Notification.tenant_id == tenant_id)
        )
        notif = result.scalars().first()
        if not notif:
            raise HTTPException(status_code=404, detail="Notification not found")
        notif.is_read = True
        await db.commit()
        await db.refresh(notif)
        return notif

    @classmethod
    async def add_case_message(
        cls,
        db: AsyncSession,
        tenant_id: str,
        case_id: str,
        sender_user_id: str,
        sender_name: str,
        content: str,
        message_type: str = "PUBLIC"
    ) -> CaseMessage:
        # Check case exists
        case_res = await db.execute(
            select(CRMCase).where(CRMCase.id == case_id, CRMCase.tenant_id == tenant_id)
        )
        case = case_res.scalars().first()
        if not case:
            raise HTTPException(status_code=404, detail="CRM case not found")

        msg = CaseMessage(
            tenant_id=tenant_id,
            case_id=case_id,
            sender_user_id=sender_user_id,
            sender_name=sender_name,
            content=content,
            message_type=message_type
        )
        db.add(msg)
        await db.commit()
        await db.refresh(msg)
        return msg

    @classmethod
    async def list_case_messages(cls, db: AsyncSession, tenant_id: str, case_id: str) -> List[CaseMessage]:
        result = await db.execute(
            select(CaseMessage)
            .where(CaseMessage.case_id == case_id, CaseMessage.tenant_id == tenant_id)
            .order_by(CaseMessage.created_at.asc())
        )
        return result.scalars().all()
