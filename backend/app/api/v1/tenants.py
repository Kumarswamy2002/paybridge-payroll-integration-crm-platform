from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.tenant import TenantCreate, TenantResponse
from app.services.tenant_service import TenantService
from app.core.middleware import get_current_user, require_roles

router = APIRouter()

@router.post("/", response_model=TenantResponse)
async def create_tenant(tenant_in: TenantCreate, db: AsyncSession = Depends(get_db)):
    existing = await TenantService.get_by_slug(db, tenant_in.slug)
    if existing:
        raise HTTPException(status_code=400, detail="Tenant with slug already exists")
    return await TenantService.create_tenant(db, tenant_in)

@router.get("/", response_model=List[TenantResponse])
async def list_tenants(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_roles(["SUPER_ADMIN"]))
):
    return await TenantService.list_tenants(db)

@router.get("/slug/{slug}", response_model=TenantResponse)
async def get_tenant_by_slug(slug: str, db: AsyncSession = Depends(get_db)):
    tenant = await TenantService.get_by_slug(db, slug)
    if not tenant:
        raise HTTPException(status_code=404, detail="Tenant not found")
    return tenant
