from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user, require_roles
from app.services.workflow_service import WorkflowService

router = APIRouter()

class CreateRuleRequest(BaseModel):
    name: str
    event_trigger: str
    conditions: Dict[str, Any] = {}
    actions: List[Dict[str, Any]]

class TriggerEventRequest(BaseModel):
    event_trigger: str
    entity_type: str
    entity_id: str
    payload: Dict[str, Any] = {}

class RespondApprovalRequest(BaseModel):
    decision: str  # APPROVED or REJECTED
    notes: Optional[str] = None

@router.post("/rules")
async def create_workflow_rule(
    req: CreateRuleRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_roles(["TENANT_ADMIN", "SUPER_ADMIN"]))
):
    return await WorkflowService.create_rule(
        db,
        tenant_id=current_user["tenant_id"],
        name=req.name,
        event_trigger=req.event_trigger,
        conditions=req.conditions,
        actions=req.actions
    )

@router.get("/rules")
async def list_workflow_rules(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await WorkflowService.list_rules(db, current_user["tenant_id"])

@router.post("/events/trigger")
async def trigger_workflow_event(
    req: TriggerEventRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    approvals = await WorkflowService.trigger_event(
        db,
        tenant_id=current_user["tenant_id"],
        event_trigger=req.event_trigger,
        entity_type=req.entity_type,
        entity_id=req.entity_id,
        payload=req.payload,
        requester_user_id=current_user["user_id"]
    )
    return {
        "event_trigger": req.event_trigger,
        "approvals_created_count": len(approvals),
        "approvals": approvals
    }

@router.get("/approvals/pending")
async def list_pending_approvals(
    role: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await WorkflowService.list_pending_approvals(db, current_user["tenant_id"], approver_role=role)

@router.post("/approvals/{approval_id}/respond")
async def respond_to_approval(
    approval_id: str,
    req: RespondApprovalRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await WorkflowService.respond_to_approval(
        db,
        tenant_id=current_user["tenant_id"],
        approval_id=approval_id,
        approver_user_id=current_user["user_id"],
        decision=req.decision,
        notes=req.notes
    )
