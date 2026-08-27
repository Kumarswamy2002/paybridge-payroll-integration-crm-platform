"""
PayBridge Canonical Model Specification: DeductionRules
Unified data contract isolating provider schema differences.
"""

import uuid
from typing import List, Dict, Any, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict

class CanonicalDeductionRulesModel1(BaseModel):
    """Canonical Model contract 1 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel2(BaseModel):
    """Canonical Model contract 2 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel3(BaseModel):
    """Canonical Model contract 3 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel4(BaseModel):
    """Canonical Model contract 4 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel5(BaseModel):
    """Canonical Model contract 5 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel6(BaseModel):
    """Canonical Model contract 6 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel7(BaseModel):
    """Canonical Model contract 7 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel8(BaseModel):
    """Canonical Model contract 8 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel9(BaseModel):
    """Canonical Model contract 9 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel10(BaseModel):
    """Canonical Model contract 10 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel11(BaseModel):
    """Canonical Model contract 11 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel12(BaseModel):
    """Canonical Model contract 12 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel13(BaseModel):
    """Canonical Model contract 13 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel14(BaseModel):
    """Canonical Model contract 14 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel15(BaseModel):
    """Canonical Model contract 15 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel16(BaseModel):
    """Canonical Model contract 16 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel17(BaseModel):
    """Canonical Model contract 17 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel18(BaseModel):
    """Canonical Model contract 18 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel19(BaseModel):
    """Canonical Model contract 19 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel20(BaseModel):
    """Canonical Model contract 20 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel21(BaseModel):
    """Canonical Model contract 21 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel22(BaseModel):
    """Canonical Model contract 22 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel23(BaseModel):
    """Canonical Model contract 23 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel24(BaseModel):
    """Canonical Model contract 24 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel25(BaseModel):
    """Canonical Model contract 25 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel26(BaseModel):
    """Canonical Model contract 26 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel27(BaseModel):
    """Canonical Model contract 27 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel28(BaseModel):
    """Canonical Model contract 28 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel29(BaseModel):
    """Canonical Model contract 29 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel30(BaseModel):
    """Canonical Model contract 30 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel31(BaseModel):
    """Canonical Model contract 31 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel32(BaseModel):
    """Canonical Model contract 32 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel33(BaseModel):
    """Canonical Model contract 33 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel34(BaseModel):
    """Canonical Model contract 34 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel35(BaseModel):
    """Canonical Model contract 35 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel36(BaseModel):
    """Canonical Model contract 36 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel37(BaseModel):
    """Canonical Model contract 37 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel38(BaseModel):
    """Canonical Model contract 38 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel39(BaseModel):
    """Canonical Model contract 39 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel40(BaseModel):
    """Canonical Model contract 40 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel41(BaseModel):
    """Canonical Model contract 41 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel42(BaseModel):
    """Canonical Model contract 42 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel43(BaseModel):
    """Canonical Model contract 43 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)

class CanonicalDeductionRulesModel44(BaseModel):
    """Canonical Model contract 44 for DeductionRules."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    provider_name: str = Field(..., description="Payroll Provider Identifier")
    external_id: str = Field(..., description="External Provider Entity ID")
    code: Optional[str] = Field(None, description="Canonical Code")
    amount: float = Field(0.0, description="Financial Value")
    currency: str = Field("USD", description="Currency Code")
    effective_date: Optional[date] = Field(None, description="Effective Date")
    status: str = Field("ACTIVE", description="Record Status")
    attributes: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = ConfigDict(from_attributes=True)
