from typing import Optional, List, Dict, Any
from datetime import date, datetime
from pydantic import BaseModel

class CanonicalTaxWithholding(BaseModel):
    tax_name: str  # Federal Income Tax, State Income Tax, Social Security, Medicare
    amount: float
    tax_code: Optional[str] = None
    tax_authority: Optional[str] = None

class CanonicalDeduction(BaseModel):
    deduction_name: str  # 401k, Health Insurance, Dental, FSA, HSA
    amount: float
    is_pre_tax: bool = True
    employer_match_amount: float = 0.0

class CanonicalEmployee(BaseModel):
    provider_name: str
    external_id: str
    employee_code: Optional[str] = None
    first_name: str
    last_name: str
    email: str
    phone: Optional[str] = None
    employment_type: str  # FULL_TIME, PART_TIME, CONTRACTOR
    status: str           # ACTIVE, TERMINATED, LEAVE
    hire_date: Optional[date] = None
    department_name: Optional[str] = None
    job_title: Optional[str] = None
    raw_provider_data: Dict[str, Any] = {}

class CanonicalCompensation(BaseModel):
    provider_name: str
    external_employee_id: str
    pay_frequency: str  # MONTHLY, BIWEEKLY, WEEKLY, ANNUAL
    currency: str = "USD"
    base_pay: float
    hourly_rate: float = 0.0
    effective_date: Optional[date] = None

class CanonicalPayrollRun(BaseModel):
    provider_name: str
    payroll_run_id: str
    period_start: date
    period_end: date
    payment_date: date
    status: str  # DRAFT, APPROVED, PROCESSED, FAILED
    total_gross_pay: float
    total_net_pay: float
    total_tax: float
    total_deductions: float
    records_count: int

class CanonicalPayrollResult(BaseModel):
    payroll_run_id: str
    external_employee_id: str
    gross_pay: float
    net_pay: float
    tax_withheld: float
    deductions: float
    direct_deposit_amount: float
    taxes_breakdown: List[CanonicalTaxWithholding] = []
    deductions_breakdown: List[CanonicalDeduction] = []
    payslip_url: Optional[str] = None
