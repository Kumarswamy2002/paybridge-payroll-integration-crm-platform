from typing import Optional
from pydantic import BaseModel, EmailStr, ConfigDict

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None
    user_id: str
    tenant_id: str
    role: str

class TokenPayload(BaseModel):
    sub: Optional[str] = None
    tenant_id: Optional[str] = None
    role: Optional[str] = None

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    tenant_slug: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    tenant_id: str
    role: str = "EMPLOYEE"

class UserResponse(BaseModel):
    id: str
    tenant_id: str
    email: str
    full_name: str
    role: str
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
