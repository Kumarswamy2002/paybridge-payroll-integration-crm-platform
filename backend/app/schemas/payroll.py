from typing import Optional, List
from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

class PayrollProfileCreate(BaseModel):
    employee_id: str
    payroll_provider: str = "GUSTO"
    external_provider_employee_id: Optional[str] = None
    payment_method: str = "DIRECT_DEPOSIT"
    tax_identifier: Optional[str] = None
    bank_account: Optional[str] = None

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

class PIIDecryptedResponse(BaseModel):
    employee_id: str
    tax_identifier: Optional[str] = None
    bank_account: Optional[str] = None

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
    status: str
    effective_date: date
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
