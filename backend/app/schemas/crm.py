from typing import Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CRMCaseCreate(BaseModel):
    employee_id: str
    title: str
    description: Optional[str] = None
    category: str = "SALARY_QUERY"
    priority: str = "MEDIUM"
    assigned_to_user_id: Optional[str] = None

class CRMCaseResponse(BaseModel):
    id: str
    tenant_id: str
    ticket_number: str
    employee_id: str
    title: str
    category: str
    priority: str
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TimelineEventResponse(BaseModel):
    id: str
    tenant_id: str
    employee_id: str
    event_type: str
    summary: str
    details: Dict[str, Any] = {}
    actor_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
