from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, Request, Header, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user, require_roles
from app.services.developer_service import DeveloperService

router = APIRouter()

class CreateApiKeyRequest(BaseModel):
    name: str
    scopes: List[str] = ["employees:read", "payroll:read"]

@router.post("/api-keys")
async def create_api_key(
    req: CreateApiKeyRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_roles(["TENANT_ADMIN", "SUPER_ADMIN"]))
):
    return await DeveloperService.create_api_key(
        db,
        tenant_id=current_user["tenant_id"],
        name=req.name,
        scopes=req.scopes
    )

@router.get("/api-keys")
async def list_api_keys(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_roles(["TENANT_ADMIN", "SUPER_ADMIN"]))
):
    return await DeveloperService.list_api_keys(db, current_user["tenant_id"])

@router.post("/webhooks/incoming/{provider_name}")
async def incoming_webhook_gateway(
    provider_name: str,
    payload: Dict[str, Any],
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    headers_dict = dict(request.headers)
    return await DeveloperService.process_incoming_webhook(
        db,
        provider_name=provider_name,
        payload=payload,
        headers=headers_dict
    )
