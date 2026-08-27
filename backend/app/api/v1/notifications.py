from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user
from app.services.notification_service import NotificationService

router = APIRouter()

class SendNotificationRequest(BaseModel):
    user_id: str
    title: str
    template_name: Optional[str] = None
    context: Dict[str, Any] = {}
    channel: str = "IN_APP"

class AddCaseMessageRequest(BaseModel):
    content: str
    message_type: str = "PUBLIC"

@router.get("/")
async def get_my_notifications(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await NotificationService.list_user_notifications(
        db, 
        tenant_id=current_user["tenant_id"], 
        user_id=current_user["user_id"]
    )

@router.post("/send")
async def send_notification(
    req: SendNotificationRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await NotificationService.send_notification(
        db,
        tenant_id=current_user["tenant_id"],
        user_id=req.user_id,
        title=req.title,
        template_name=req.template_name,
        context=req.context,
        channel=req.channel
    )

@router.post("/{notification_id}/read")
async def mark_notification_read(
    notification_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await NotificationService.mark_read(db, tenant_id=current_user["tenant_id"], notification_id=notification_id)

@router.post("/cases/{case_id}/messages")
async def add_case_message(
    case_id: str,
    req: AddCaseMessageRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await NotificationService.add_case_message(
        db,
        tenant_id=current_user["tenant_id"],
        case_id=case_id,
        sender_user_id=current_user["user_id"],
        sender_name=current_user.get("user_id", "Staff User"),
        content=req.content,
        message_type=req.message_type
    )

@router.get("/cases/{case_id}/messages")
async def get_case_messages(
    case_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await NotificationService.list_case_messages(db, tenant_id=current_user["tenant_id"], case_id=case_id)
