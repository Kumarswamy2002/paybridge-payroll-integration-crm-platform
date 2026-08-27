import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Float, Text, JSON
from app.core.database import Base

class PayrollReconciliationRun(Base):
    __tablename__ = "payroll_reconciliation_runs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    payroll_provider = Column(String(100), nullable=False)
    payroll_run_id = Column(String(100), nullable=False)
    
    total_records_compared = Column(Float, default=0)
    matched_records_count = Column(Float, default=0)
    discrepancies_count = Column(Float, default=0)
    
    status = Column(String(50), default="COMPLETED")  # IN_PROGRESS, COMPLETED, FAILED
    created_at = Column(DateTime, default=datetime.utcnow)

class PayrollDiscrepancy(Base):
    __tablename__ = "payroll_discrepancies"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    reconciliation_run_id = Column(String(36), ForeignKey("payroll_reconciliation_runs.id"), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    
    discrepancy_type = Column(String(100), nullable=False)  # SALARY_MISMATCH, TAX_DISCREPANCY, DEDUCTION_MISMATCH, MISSING_EMPLOYEE
    severity = Column(String(50), default="HIGH")           # LOW, MEDIUM, HIGH, CRITICAL
    
    paybridge_value = Column(Float, nullable=True)
    provider_value = Column(Float, nullable=True)
    variance_amount = Column(Float, nullable=True)
    
    status = Column(String(50), default="UNRESOLVED")       # UNRESOLVED, CASE_CREATED, RESOLVED, IGNORED
    crm_case_id = Column(String(36), ForeignKey("crm_cases.id"), nullable=True)
    
    details = Column(JSON, default=dict)
    created_at = Column(DateTime, default=datetime.utcnow)
