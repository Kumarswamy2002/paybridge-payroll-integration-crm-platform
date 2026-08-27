import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, JSON
from app.core.database import Base

class CRMCase(Base):
    __tablename__ = "crm_cases"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    ticket_number = Column(String(50), nullable=False, index=True)
    
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    assigned_to_user_id = Column(String(36), ForeignKey("users.id"), nullable=True)
    
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    category = Column(String(100), default="SALARY_QUERY")  # SALARY_QUERY, PAYSLIP_ISSUE, DISCREPANCY, TAX_QUERY, SYNC_ERROR
    
    priority = Column(String(50), default="MEDIUM")  # LOW, MEDIUM, HIGH, URGENT
    status = Column(String(50), default="OPEN")      # OPEN, TRIAGED, ASSIGNED, INVESTIGATING, WAITING, RESOLVED, CLOSED
    
    resolution_notes = Column(Text, nullable=True)
    resolved_at = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CRMActivity(Base):
    __tablename__ = "crm_activities"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    case_id = Column(String(36), ForeignKey("crm_cases.id"), nullable=True)
    
    activity_type = Column(String(50), nullable=False)  # NOTE, CALL, EMAIL, PROFILE_UPDATE, SYNC_EVENT
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)
    actor_user_id = Column(String(36), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class UnifiedTimelineEvent(Base):
    __tablename__ = "unified_timeline_events"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    
    event_type = Column(String(100), nullable=False)  # EMPLOYEE_CREATED, SALARY_UPDATED, SYNC_COMPLETED, CASE_OPENED, CASE_RESOLVED
    summary = Column(String(255), nullable=False)
    details = Column(JSON, default=dict)
    actor_name = Column(String(255), default="System")
    
    created_at = Column(DateTime, default=datetime.utcnow)
