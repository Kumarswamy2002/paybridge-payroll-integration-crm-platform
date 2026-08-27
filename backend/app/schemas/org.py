from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class OrganizationCreate(BaseModel):
    name: str
    code: Optional[str] = None
    currency: str = "USD"
    timezone: str = "UTC"

class OrganizationResponse(BaseModel):
    id: str
    tenant_id: str
    name: str
    code: Optional[str] = None
    currency: str
    timezone: str

    model_config = ConfigDict(from_attributes=True)

class DepartmentCreate(BaseModel):
    organization_id: str
    name: str
    code: Optional[str] = None
    parent_id: Optional[str] = None

class DepartmentResponse(BaseModel):
    id: str
    tenant_id: str
    organization_id: str
    name: str
    code: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

class JobPositionCreate(BaseModel):
    title: str
    code: Optional[str] = None
    level: Optional[str] = None
    department_id: Optional[str] = None

class JobPositionResponse(BaseModel):
    id: str
    tenant_id: str
    title: str
    code: Optional[str] = None
    level: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
