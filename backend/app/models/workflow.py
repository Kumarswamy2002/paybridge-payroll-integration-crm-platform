import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, JSON
from app.core.database import Base

class WorkflowRule(Base):
    __tablename__ = "workflow_rules"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    event_trigger = Column(String(100), nullable=False, index=True)  # SalaryChanged, SyncFailed, ReconciliationMismatch, EmployeeHired
    
    conditions = Column(JSON, default=dict)  # e.g., {"min_salary_increase": 10000}
    actions = Column(JSON, default=list)     # e.g., [{"type": "REQUEST_APPROVAL", "role": "HR_MANAGER"}]
    
    is_active = Column(String(50), default="ACTIVE")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class WorkflowExecution(Base):
    __tablename__ = "workflow_executions"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    workflow_rule_id = Column(String(36), ForeignKey("workflow_rules.id"), nullable=False, index=True)
    
    event_trigger = Column(String(100), nullable=False)
    status = Column(String(50), default="COMPLETED")  # PENDING_APPROVAL, COMPLETED, FAILED
    
    event_payload = Column(JSON, default=dict)
    execution_log = Column(JSON, default=list)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class ApprovalRequest(Base):
    __tablename__ = "approval_requests"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    workflow_execution_id = Column(String(36), ForeignKey("workflow_executions.id"), nullable=True)
    
    entity_type = Column(String(100), nullable=False)  # Compensation, PayrollProfile, Case
    entity_id = Column(String(36), nullable=False, index=True)
    
    requester_user_id = Column(String(36), nullable=True)
    approver_role = Column(String(50), nullable=False)  # HR_MANAGER, PAYROLL_ADMIN, TENANT_ADMIN
    approver_user_id = Column(String(36), nullable=True)
    
    status = Column(String(50), default="PENDING")  # PENDING, APPROVED, REJECTED, EXPIRED
    reason_summary = Column(String(255), nullable=False)
    approval_notes = Column(Text, nullable=True)
    
    resolved_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
