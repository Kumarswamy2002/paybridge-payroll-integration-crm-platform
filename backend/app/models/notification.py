import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Boolean, JSON
from app.core.database import Base

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False, index=True)
    
    channel = Column(String(50), default="IN_APP")  # IN_APP, EMAIL, WEBHOOK
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    template_name = Column(String(100), nullable=True)
    
    is_read = Column(Boolean, default=False)
    data = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class CaseMessage(Base):
    __tablename__ = "case_messages"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    case_id = Column(String(36), ForeignKey("crm_cases.id"), nullable=False, index=True)
    sender_user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    
    message_type = Column(String(50), default="PUBLIC")  # PUBLIC (visible to employee), INTERNAL_NOTE (staff only)
    sender_name = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    attachments = Column(JSON, default=list)
    
    created_at = Column(DateTime, default=datetime.utcnow)
