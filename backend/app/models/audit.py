import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, JSON
from app.core.database import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    user_id = Column(String(36), nullable=True)
    user_email = Column(String(255), nullable=True)
    
    action = Column(String(100), nullable=False)  # CREATE, UPDATE, DELETE, VIEW_PII, LOGIN, SYNC
    entity_type = Column(String(100), nullable=False)  # Employee, Compensation, User, Tenant, Case
    entity_id = Column(String(36), nullable=True)
    
    before_state = Column(JSON, nullable=True)
    after_state = Column(JSON, nullable=True)
    
    ip_address = Column(String(50), nullable=True)
    user_agent = Column(String(255), nullable=True)
    reason = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
