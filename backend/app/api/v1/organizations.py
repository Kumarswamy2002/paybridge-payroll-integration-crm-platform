from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.org import (
    OrganizationCreate, OrganizationResponse,
    DepartmentCreate, DepartmentResponse,
    JobPositionCreate, JobPositionResponse
)
from app.services.org_service import OrgService
from app.core.middleware import get_current_user

router = APIRouter()

@router.post("/orgs", response_model=OrganizationResponse)
async def create_organization(
    org_in: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await OrgService.create_organization(db, current_user["tenant_id"], org_in)

@router.get("/orgs", response_model=List[OrganizationResponse])
async def list_organizations(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await OrgService.list_organizations(db, current_user["tenant_id"])

@router.post("/departments", response_model=DepartmentResponse)
async def create_department(
    dept_in: DepartmentCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await OrgService.create_department(db, current_user["tenant_id"], dept_in)

@router.get("/departments", response_model=List[DepartmentResponse])
async def list_departments(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await OrgService.list_departments(db, current_user["tenant_id"])

@router.post("/positions", response_model=JobPositionResponse)
async def create_position(
    pos_in: JobPositionCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await OrgService.create_job_position(db, current_user["tenant_id"], pos_in)

@router.get("/positions", response_model=List[JobPositionResponse])
async def list_positions(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await OrgService.list_job_positions(db, current_user["tenant_id"])
