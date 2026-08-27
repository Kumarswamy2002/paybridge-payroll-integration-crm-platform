from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.org import Organization, Department, JobPosition
from app.schemas.org import OrganizationCreate, DepartmentCreate, JobPositionCreate

class OrgService:
    @staticmethod
    async def create_organization(db: AsyncSession, tenant_id: str, org_in: OrganizationCreate) -> Organization:
        org = Organization(
            tenant_id=tenant_id,
            name=org_in.name,
            code=org_in.code,
            currency=org_in.currency,
            timezone=org_in.timezone
        )
        db.add(org)
        await db.commit()
        await db.refresh(org)
        return org

    @staticmethod
    async def list_organizations(db: AsyncSession, tenant_id: str) -> List[Organization]:
        result = await db.execute(select(Organization).where(Organization.tenant_id == tenant_id))
        return result.scalars().all()

    @staticmethod
    async def create_department(db: AsyncSession, tenant_id: str, dept_in: DepartmentCreate) -> Department:
        dept = Department(
            tenant_id=tenant_id,
            organization_id=dept_in.organization_id,
            name=dept_in.name,
            code=dept_in.code,
            parent_id=dept_in.parent_id
        )
        db.add(dept)
        await db.commit()
        await db.refresh(dept)
        return dept

    @staticmethod
    async def list_departments(db: AsyncSession, tenant_id: str) -> List[Department]:
        result = await db.execute(select(Department).where(Department.tenant_id == tenant_id))
        return result.scalars().all()

    @staticmethod
    async def create_job_position(db: AsyncSession, tenant_id: str, pos_in: JobPositionCreate) -> JobPosition:
        pos = JobPosition(
            tenant_id=tenant_id,
            department_id=pos_in.department_id,
            title=pos_in.title,
            code=pos_in.code,
            level=pos_in.level
        )
        db.add(pos)
        await db.commit()
        await db.refresh(pos)
        return pos

    @staticmethod
    async def list_job_positions(db: AsyncSession, tenant_id: str) -> List[JobPosition]:
        result = await db.execute(select(JobPosition).where(JobPosition.tenant_id == tenant_id))
        return result.scalars().all()
