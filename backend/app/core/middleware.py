from typing import Optional, List
from fastapi import Request, HTTPException, status, Depends
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.security import oauth2_scheme, decode_token

class TenantContext:
    _tenant_id: Optional[str] = None
    _user_id: Optional[str] = None
    _role: Optional[str] = None

    @classmethod
    def set(cls, tenant_id: str, user_id: str, role: str):
        cls._tenant_id = tenant_id
        cls._user_id = user_id
        cls._role = role

    @classmethod
    def get_tenant_id(cls) -> Optional[str]:
        return cls._tenant_id

    @classmethod
    def get_user_id(cls) -> Optional[str]:
        return cls._user_id

    @classmethod
    def get_role(cls) -> Optional[str]:
        return cls._role

    @classmethod
    def clear(cls):
        cls._tenant_id = None
        cls._user_id = None
        cls._role = None

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    payload = decode_token(token)
    user_id = payload.get("sub")
    tenant_id = payload.get("tenant_id")
    role = payload.get("role")
    
    if not user_id or not tenant_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token payload"
        )
    
    TenantContext.set(tenant_id, user_id, role or "EMPLOYEE")
    return {
        "user_id": user_id,
        "tenant_id": tenant_id,
        "role": role or "EMPLOYEE",
    }

def require_roles(allowed_roles: List[str]):
    def role_checker(current_user: dict = Depends(get_current_user)):
        user_role = current_user.get("role")
        if user_role not in allowed_roles and "SUPER_ADMIN" not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Operation not permitted for role: {user_role}"
            )
        return current_user
    return role_checker
