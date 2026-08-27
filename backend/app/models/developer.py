import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Boolean, JSON
from app.core.database import Base

class ApiKey(Base):
    __tablename__ = "api_keys"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    key_prefix = Column(String(10), nullable=False, index=True)
    hashed_key = Column(String(255), nullable=False)
    
    scopes = Column(JSON, default=list)  # ["employees:read", "payroll:write", "reconciliation:read"]
    is_active = Column(Boolean, default=True)
    expires_at = Column(DateTime, nullable=True)
    last_used_at = Column(DateTime, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class WebhookEventLog(Base):
    __tablename__ = "webhook_event_logs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=True, index=True)
    provider_name = Column(String(100), nullable=False, index=True)
    event_type = Column(String(100), nullable=False)
    
    idempotency_key = Column(String(255), nullable=True, index=True)
    signature_header = Column(String(255), nullable=True)
    payload = Column(JSON, default=dict)
    
    status = Column(String(50), default="PROCESSED")  # PROCESSED, FAILED, DUPLICATE_IGNORED
    error_message = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)
