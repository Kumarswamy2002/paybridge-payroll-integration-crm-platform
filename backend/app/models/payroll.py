import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, JSON, Float, Date
from app.core.database import Base

class PayrollProfile(Base):
    __tablename__ = "payroll_profiles"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), ForeignKey("tenants.id"), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, unique=True, index=True)
    
    payroll_provider = Column(String(100), default="GUSTO")  # GUSTO, ADP, RIPPLING, WORKDAY, MANUAL
    external_provider_employee_id = Column(String(100), nullable=True, index=True)
    
    sync_status = Column(String(50), default="NOT_SYNCED")  # IN_SYNC, OUT_OF_SYNC, ERROR, NOT_SYNCED
    last_synced_at = Column(DateTime, nullable=True)
    
    payment_method = Column(String(50), default="DIRECT_DEPOSIT")  # DIRECT_DEPOSIT, CHECK, WIRE
    tax_identifier_encrypted = Column(Text, nullable=True)  # AES-256 Encrypted SSN/PAN
    bank_account_encrypted = Column(Text, nullable=True)    # AES-256 Encrypted IBAN/Account
    
    status = Column(String(50), default="ACTIVE")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Compensation(Base):
    __tablename__ = "compensations"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    
    pay_frequency = Column(String(50), default="MONTHLY")  # WEEKLY, BIWEEKLY, MONTHLY, ANNUAL
    currency = Column(String(10), default="USD")
    
    base_salary = Column(Float, nullable=False, default=0.0)
    hourly_rate = Column(Float, default=0.0)
    bonus_amount = Column(Float, default=0.0)
    allowance_amount = Column(Float, default=0.0)
    
    effective_date = Column(Date, nullable=False)
    status = Column(String(50), default="ACTIVE")  # ACTIVE, SUPERSEDED
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
