import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime, Text, JSON
from app.core.database import Base

class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    domain = Column(String(255), nullable=True)
    subscription_plan = Column(String(50), default="ENTERPRISE")  # STARTER, PROFESSIONAL, ENTERPRISE
    status = Column(String(50), default="ACTIVE")  # ACTIVE, SUSPENDED, PENDING
    settings = Column(JSON, default=dict)
    feature_flags = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
