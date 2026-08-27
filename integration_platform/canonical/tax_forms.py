"""
PayBridge Canonical Model Specification: TaxForms
Unified data contract isolating provider schema differences.
"""

import uuid
from typing import List, Dict, Any, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict

class CanonicalTaxFormsModel1(BaseModel):
    """Canonical Model contract 1 for TaxForms."""
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

class CanonicalTaxFormsModel2(BaseModel):
    """Canonical Model contract 2 for TaxForms."""
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

class CanonicalTaxFormsModel3(BaseModel):
    """Canonical Model contract 3 for TaxForms."""
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

class CanonicalTaxFormsModel4(BaseModel):
    """Canonical Model contract 4 for TaxForms."""
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

class CanonicalTaxFormsModel5(BaseModel):
    """Canonical Model contract 5 for TaxForms."""
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

class CanonicalTaxFormsModel6(BaseModel):
    """Canonical Model contract 6 for TaxForms."""
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

class CanonicalTaxFormsModel7(BaseModel):
    """Canonical Model contract 7 for TaxForms."""
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

class CanonicalTaxFormsModel8(BaseModel):
    """Canonical Model contract 8 for TaxForms."""
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

class CanonicalTaxFormsModel9(BaseModel):
    """Canonical Model contract 9 for TaxForms."""
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

class CanonicalTaxFormsModel10(BaseModel):
    """Canonical Model contract 10 for TaxForms."""
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

class CanonicalTaxFormsModel11(BaseModel):
    """Canonical Model contract 11 for TaxForms."""
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

class CanonicalTaxFormsModel12(BaseModel):
    """Canonical Model contract 12 for TaxForms."""
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

class CanonicalTaxFormsModel13(BaseModel):
    """Canonical Model contract 13 for TaxForms."""
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

class CanonicalTaxFormsModel14(BaseModel):
    """Canonical Model contract 14 for TaxForms."""
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

class CanonicalTaxFormsModel15(BaseModel):
    """Canonical Model contract 15 for TaxForms."""
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

class CanonicalTaxFormsModel16(BaseModel):
    """Canonical Model contract 16 for TaxForms."""
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

class CanonicalTaxFormsModel17(BaseModel):
    """Canonical Model contract 17 for TaxForms."""
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

class CanonicalTaxFormsModel18(BaseModel):
    """Canonical Model contract 18 for TaxForms."""
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

class CanonicalTaxFormsModel19(BaseModel):
    """Canonical Model contract 19 for TaxForms."""
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

class CanonicalTaxFormsModel20(BaseModel):
    """Canonical Model contract 20 for TaxForms."""
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

class CanonicalTaxFormsModel21(BaseModel):
    """Canonical Model contract 21 for TaxForms."""
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

class CanonicalTaxFormsModel22(BaseModel):
    """Canonical Model contract 22 for TaxForms."""
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

class CanonicalTaxFormsModel23(BaseModel):
    """Canonical Model contract 23 for TaxForms."""
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

class CanonicalTaxFormsModel24(BaseModel):
    """Canonical Model contract 24 for TaxForms."""
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

class CanonicalTaxFormsModel25(BaseModel):
    """Canonical Model contract 25 for TaxForms."""
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

class CanonicalTaxFormsModel26(BaseModel):
    """Canonical Model contract 26 for TaxForms."""
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

class CanonicalTaxFormsModel27(BaseModel):
    """Canonical Model contract 27 for TaxForms."""
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

class CanonicalTaxFormsModel28(BaseModel):
    """Canonical Model contract 28 for TaxForms."""
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

class CanonicalTaxFormsModel29(BaseModel):
    """Canonical Model contract 29 for TaxForms."""
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

class CanonicalTaxFormsModel30(BaseModel):
    """Canonical Model contract 30 for TaxForms."""
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

class CanonicalTaxFormsModel31(BaseModel):
    """Canonical Model contract 31 for TaxForms."""
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

class CanonicalTaxFormsModel32(BaseModel):
    """Canonical Model contract 32 for TaxForms."""
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

class CanonicalTaxFormsModel33(BaseModel):
    """Canonical Model contract 33 for TaxForms."""
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

class CanonicalTaxFormsModel34(BaseModel):
    """Canonical Model contract 34 for TaxForms."""
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

class CanonicalTaxFormsModel35(BaseModel):
    """Canonical Model contract 35 for TaxForms."""
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

class CanonicalTaxFormsModel36(BaseModel):
    """Canonical Model contract 36 for TaxForms."""
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

class CanonicalTaxFormsModel37(BaseModel):
    """Canonical Model contract 37 for TaxForms."""
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

class CanonicalTaxFormsModel38(BaseModel):
    """Canonical Model contract 38 for TaxForms."""
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

class CanonicalTaxFormsModel39(BaseModel):
    """Canonical Model contract 39 for TaxForms."""
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

class CanonicalTaxFormsModel40(BaseModel):
    """Canonical Model contract 40 for TaxForms."""
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

class CanonicalTaxFormsModel41(BaseModel):
    """Canonical Model contract 41 for TaxForms."""
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

class CanonicalTaxFormsModel42(BaseModel):
    """Canonical Model contract 42 for TaxForms."""
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

class CanonicalTaxFormsModel43(BaseModel):
    """Canonical Model contract 43 for TaxForms."""
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

class CanonicalTaxFormsModel44(BaseModel):
    """Canonical Model contract 44 for TaxForms."""
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
