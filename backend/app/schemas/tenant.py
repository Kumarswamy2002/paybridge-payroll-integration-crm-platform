from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TenantCreate(BaseModel):
    name: str
    slug: str
    domain: Optional[str] = None
    subscription_plan: str = "ENTERPRISE"

class TenantResponse(BaseModel):
    id: str
    name: str
    slug: str
    domain: Optional[str] = None
    subscription_plan: str
    status: str
    settings: Dict[str, Any] = {}
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
