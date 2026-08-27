from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

class PayrollProfileCreate(BaseModel):
    employee_id: str
    payroll_provider: str = "GUSTO"
    external_provider_employee_id: Optional[str] = None
    payment_method: str = "DIRECT_DEPOSIT"

class PayrollProfileResponse(BaseModel):
    id: str
    tenant_id: str
    employee_id: str
    payroll_provider: str
    external_provider_employee_id: Optional[str] = None
    sync_status: str
    payment_method: str
    status: str

    model_config = ConfigDict(from_attributes=True)

class CompensationCreate(BaseModel):
    employee_id: str
    pay_frequency: str = "MONTHLY"
    currency: str = "USD"
    base_salary: float
    hourly_rate: float = 0.0
    effective_date: date

class CompensationResponse(BaseModel):
    id: str
    tenant_id: str
    employee_id: str
    pay_frequency: str
    currency: str
    base_salary: float
    effective_date: date

    model_config = ConfigDict(from_attributes=True)
