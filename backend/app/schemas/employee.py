from typing import Optional, Dict, Any
from datetime import date, datetime
from pydantic import BaseModel, EmailStr, ConfigDict

class EmployeeCreate(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    department_id: Optional[str] = None
    job_position_id: Optional[str] = None
    manager_id: Optional[str] = None
    employment_type: str = "FULL_TIME"
    status: str = "ACTIVE"
    date_of_joining: Optional[date] = None
    work_location: Optional[str] = None

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    department_id: Optional[str] = None
    job_position_id: Optional[str] = None
    manager_id: Optional[str] = None
    status: Optional[str] = None

class EmployeeResponse(BaseModel):
    id: str
    tenant_id: str
    employee_code: str
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    department_id: Optional[str] = None
    job_position_id: Optional[str] = None
    manager_id: Optional[str] = None
    employment_type: str
    status: str
    date_of_joining: Optional[date] = None
    work_location: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class Employee360Response(BaseModel):
    employee: EmployeeResponse
    department_name: Optional[str] = None
    position_title: Optional[str] = None
    manager_name: Optional[str] = None
    payroll_provider: Optional[str] = None
    sync_status: Optional[str] = None
    base_salary: Optional[float] = None
    open_cases_count: int = 0
