from typing import List, Dict, Any, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.workflow import WorkflowRule, WorkflowExecution, ApprovalRequest
from app.models.crm import UnifiedTimelineEvent

class WorkflowService:
    """Generic Workflow & Multi-Stage Approval Engine."""

    @classmethod
    async def create_rule(
        cls,
        db: AsyncSession,
        tenant_id: str,
        name: str,
        event_trigger: str,
        conditions: Dict[str, Any],
        actions: List[Dict[str, Any]]
    ) -> WorkflowRule:
        rule = WorkflowRule(
            tenant_id=tenant_id,
            name=name,
            event_trigger=event_trigger,
            conditions=conditions,
            actions=actions,
            is_active="ACTIVE"
        )
        db.add(rule)
        await db.commit()
        await db.refresh(rule)
        return rule

    @classmethod
    async def trigger_event(
        cls,
        db: AsyncSession,
        tenant_id: str,
        event_trigger: str,
        entity_type: str,
        entity_id: str,
        payload: Dict[str, Any],
        requester_user_id: Optional[str] = None
    ) -> List[ApprovalRequest]:
        # Find active matching rules
        result = await db.execute(
            select(WorkflowRule).where(
                WorkflowRule.tenant_id == tenant_id,
                WorkflowRule.event_trigger == event_trigger,
                WorkflowRule.is_active == "ACTIVE"
            )
        )
        rules = result.scalars().all()
        created_approvals = []

        for rule in rules:
            execution = WorkflowExecution(
                tenant_id=tenant_id,
                workflow_rule_id=rule.id,
                event_trigger=event_trigger,
                event_payload=payload,
                status="COMPLETED"
            )
            db.add(execution)
            await db.commit()
            await db.refresh(execution)

            # Evaluate actions
            for action in rule.actions:
                if action.get("type") == "REQUEST_APPROVAL":
                    approver_role = action.get("role", "HR_MANAGER")
                    approval = ApprovalRequest(
                        tenant_id=tenant_id,
                        workflow_execution_id=execution.id,
                        entity_type=entity_type,
                        entity_id=entity_id,
                        requester_user_id=requester_user_id,
                        approver_role=approver_role,
                        status="PENDING",
                        reason_summary=f"Approval required by rule: {rule.name}"
                    )
                    db.add(approval)
                    await db.commit()
                    await db.refresh(approval)
                    created_approvals.append(approval)

        return created_approvals

    @classmethod
    async def respond_to_approval(
        cls,
        db: AsyncSession,
        tenant_id: str,
        approval_id: str,
        approver_user_id: str,
        decision: str,  # APPROVED or REJECTED
        notes: Optional[str] = None
    ) -> ApprovalRequest:
        if decision not in ["APPROVED", "REJECTED"]:
            raise HTTPException(status_code=400, detail="Decision must be APPROVED or REJECTED")

        result = await db.execute(
            select(ApprovalRequest).where(
                ApprovalRequest.id == approval_id,
                ApprovalRequest.tenant_id == tenant_id
            )
        )
        approval = result.scalars().first()
        if not approval:
            raise HTTPException(status_code=404, detail="Approval request not found")

        approval.status = decision
        approval.approver_user_id = approver_user_id
        approval.approval_notes = notes
        approval.resolved_at = datetime.utcnow()

        await db.commit()
        await db.refresh(approval)

        # Log timeline event
        event = UnifiedTimelineEvent(
            tenant_id=tenant_id,
            employee_id=approval.entity_id,
            event_type=f"APPROVAL_{decision}",
            summary=f"Approval request for {approval.entity_type} {decision.lower()}",
            details={"approval_id": approval_id, "notes": notes},
            actor_name="Workflow Engine"
        )
        db.add(event)
        await db.commit()

        return approval

    @classmethod
    async def list_pending_approvals(cls, db: AsyncSession, tenant_id: str, approver_role: Optional[str] = None) -> List[ApprovalRequest]:
        query = select(ApprovalRequest).where(
            ApprovalRequest.tenant_id == tenant_id,
            ApprovalRequest.status == "PENDING"
        )
        if approver_role:
            query = query.where(ApprovalRequest.approver_role == approver_role)
        result = await db.execute(query.order_by(ApprovalRequest.created_at.desc()))
        return result.scalars().all()

    @classmethod
    async def list_rules(cls, db: AsyncSession, tenant_id: str) -> List[WorkflowRule]:
        result = await db.execute(select(WorkflowRule).where(WorkflowRule.tenant_id == tenant_id))
        return result.scalars().all()
