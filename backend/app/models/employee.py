import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Text, JSON, Date, Float
from app.core.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), ForeignKey("tenants.id"), nullable=False, index=True)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=True, index=True)
    employee_code = Column(String(50), nullable=False, index=True)
    
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False, index=True)
    phone = Column(String(50), nullable=True)
    
    department_id = Column(String(36), ForeignKey("departments.id"), nullable=True)
    job_position_id = Column(String(36), ForeignKey("job_positions.id"), nullable=True)
    cost_center_id = Column(String(36), ForeignKey("cost_centers.id"), nullable=True)
    manager_id = Column(String(36), ForeignKey("employees.id"), nullable=True)
    
    employment_type = Column(String(50), default="FULL_TIME")  # FULL_TIME, PART_TIME, CONTRACTOR, INTERN
    status = Column(String(50), default="ACTIVE")  # ACTIVE, ON_LEAVE, TERMINATED, PROBATION
    
    date_of_joining = Column(Date, nullable=True)
    date_of_birth = Column(Date, nullable=True)
    work_location = Column(String(255), nullable=True)
    
    address = Column(Text, nullable=True)
    metadata_fields = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class EmploymentHistory(Base):
    __tablename__ = "employment_histories"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    change_type = Column(String(50), nullable=False)  # PROMOTION, DEPT_TRANSFER, SALARY_REVISION, STATUS_CHANGE
    previous_value = Column(Text, nullable=True)
    new_value = Column(Text, nullable=True)
    effective_date = Column(Date, nullable=False)
    reason = Column(Text, nullable=True)
    created_by_user_id = Column(String(36), nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow)

class EmployeeRelationship(Base):
    __tablename__ = "employee_relationships"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    tenant_id = Column(String(36), nullable=False, index=True)
    source_employee_id = Column(String(36), ForeignKey("employees.id"), nullable=False, index=True)
    target_entity_type = Column(String(50), nullable=False)  # MANAGER, DEPARTMENT, PROVIDER, CASE
    target_entity_id = Column(String(36), nullable=False, index=True)
    relationship_type = Column(String(50), nullable=False)  # REPORTS_TO, BELONGS_TO, HAS_PAYROLL, HAS_CASE
    created_at = Column(DateTime, default=datetime.utcnow)
