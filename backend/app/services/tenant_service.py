import uuid
from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.tenant import Tenant
from app.schemas.tenant import TenantCreate

class TenantService:
    @staticmethod
    async def create_tenant(db: AsyncSession, tenant_in: TenantCreate) -> Tenant:
        tenant = Tenant(
            name=tenant_in.name,
            slug=tenant_in.slug,
            domain=tenant_in.domain,
            subscription_plan=tenant_in.subscription_plan,
            status="ACTIVE",
            settings={"default_currency": "USD", "timezone": "UTC"}
        )
        db.add(tenant)
        await db.commit()
        await db.refresh(tenant)
        return tenant

    @staticmethod
    async def get_by_slug(db: AsyncSession, slug: str) -> Optional[Tenant]:
        result = await db.execute(select(Tenant).where(Tenant.slug == slug))
        return result.scalars().first()

    @staticmethod
    async def get_by_id(db: AsyncSession, tenant_id: str) -> Optional[Tenant]:
        result = await db.execute(select(Tenant).where(Tenant.id == tenant_id))
        return result.scalars().first()

    @staticmethod
    async def list_tenants(db: AsyncSession) -> List[Tenant]:
        result = await db.execute(select(Tenant))
        return result.scalars().all()
