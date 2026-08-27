"""
PayBridge Canonical Model Specification: TimeOff
Unified data contract isolating provider schema differences.
"""

import uuid
from typing import List, Dict, Any, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, ConfigDict

class CanonicalTimeOffModel1(BaseModel):
    """Canonical Model contract 1 for TimeOff."""
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

class CanonicalTimeOffModel2(BaseModel):
    """Canonical Model contract 2 for TimeOff."""
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

class CanonicalTimeOffModel3(BaseModel):
    """Canonical Model contract 3 for TimeOff."""
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

class CanonicalTimeOffModel4(BaseModel):
    """Canonical Model contract 4 for TimeOff."""
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

class CanonicalTimeOffModel5(BaseModel):
    """Canonical Model contract 5 for TimeOff."""
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

class CanonicalTimeOffModel6(BaseModel):
    """Canonical Model contract 6 for TimeOff."""
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

class CanonicalTimeOffModel7(BaseModel):
    """Canonical Model contract 7 for TimeOff."""
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

class CanonicalTimeOffModel8(BaseModel):
    """Canonical Model contract 8 for TimeOff."""
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

class CanonicalTimeOffModel9(BaseModel):
    """Canonical Model contract 9 for TimeOff."""
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

class CanonicalTimeOffModel10(BaseModel):
    """Canonical Model contract 10 for TimeOff."""
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

class CanonicalTimeOffModel11(BaseModel):
    """Canonical Model contract 11 for TimeOff."""
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

class CanonicalTimeOffModel12(BaseModel):
    """Canonical Model contract 12 for TimeOff."""
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

class CanonicalTimeOffModel13(BaseModel):
    """Canonical Model contract 13 for TimeOff."""
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

class CanonicalTimeOffModel14(BaseModel):
    """Canonical Model contract 14 for TimeOff."""
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

class CanonicalTimeOffModel15(BaseModel):
    """Canonical Model contract 15 for TimeOff."""
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

class CanonicalTimeOffModel16(BaseModel):
    """Canonical Model contract 16 for TimeOff."""
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

class CanonicalTimeOffModel17(BaseModel):
    """Canonical Model contract 17 for TimeOff."""
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

class CanonicalTimeOffModel18(BaseModel):
    """Canonical Model contract 18 for TimeOff."""
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

class CanonicalTimeOffModel19(BaseModel):
    """Canonical Model contract 19 for TimeOff."""
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

class CanonicalTimeOffModel20(BaseModel):
    """Canonical Model contract 20 for TimeOff."""
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

class CanonicalTimeOffModel21(BaseModel):
    """Canonical Model contract 21 for TimeOff."""
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

class CanonicalTimeOffModel22(BaseModel):
    """Canonical Model contract 22 for TimeOff."""
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

class CanonicalTimeOffModel23(BaseModel):
    """Canonical Model contract 23 for TimeOff."""
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

class CanonicalTimeOffModel24(BaseModel):
    """Canonical Model contract 24 for TimeOff."""
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

class CanonicalTimeOffModel25(BaseModel):
    """Canonical Model contract 25 for TimeOff."""
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

class CanonicalTimeOffModel26(BaseModel):
    """Canonical Model contract 26 for TimeOff."""
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

class CanonicalTimeOffModel27(BaseModel):
    """Canonical Model contract 27 for TimeOff."""
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

class CanonicalTimeOffModel28(BaseModel):
    """Canonical Model contract 28 for TimeOff."""
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

class CanonicalTimeOffModel29(BaseModel):
    """Canonical Model contract 29 for TimeOff."""
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

class CanonicalTimeOffModel30(BaseModel):
    """Canonical Model contract 30 for TimeOff."""
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

class CanonicalTimeOffModel31(BaseModel):
    """Canonical Model contract 31 for TimeOff."""
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

class CanonicalTimeOffModel32(BaseModel):
    """Canonical Model contract 32 for TimeOff."""
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

class CanonicalTimeOffModel33(BaseModel):
    """Canonical Model contract 33 for TimeOff."""
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

class CanonicalTimeOffModel34(BaseModel):
    """Canonical Model contract 34 for TimeOff."""
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

class CanonicalTimeOffModel35(BaseModel):
    """Canonical Model contract 35 for TimeOff."""
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

class CanonicalTimeOffModel36(BaseModel):
    """Canonical Model contract 36 for TimeOff."""
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

class CanonicalTimeOffModel37(BaseModel):
    """Canonical Model contract 37 for TimeOff."""
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

class CanonicalTimeOffModel38(BaseModel):
    """Canonical Model contract 38 for TimeOff."""
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

class CanonicalTimeOffModel39(BaseModel):
    """Canonical Model contract 39 for TimeOff."""
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

class CanonicalTimeOffModel40(BaseModel):
    """Canonical Model contract 40 for TimeOff."""
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

class CanonicalTimeOffModel41(BaseModel):
    """Canonical Model contract 41 for TimeOff."""
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

class CanonicalTimeOffModel42(BaseModel):
    """Canonical Model contract 42 for TimeOff."""
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

class CanonicalTimeOffModel43(BaseModel):
    """Canonical Model contract 43 for TimeOff."""
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

class CanonicalTimeOffModel44(BaseModel):
    """Canonical Model contract 44 for TimeOff."""
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
