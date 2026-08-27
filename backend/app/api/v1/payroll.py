from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.payroll import (
    PayrollProfileCreate, PayrollProfileResponse,
    CompensationCreate, CompensationResponse
)
from app.services.payroll_service import PayrollService
from app.core.middleware import get_current_user

router = APIRouter()

@router.post("/profiles", response_model=PayrollProfileResponse)
async def create_payroll_profile(
    profile_in: PayrollProfileCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await PayrollService.create_payroll_profile(db, current_user["tenant_id"], profile_in)

@router.get("/profiles/employee/{employee_id}", response_model=PayrollProfileResponse)
async def get_payroll_profile(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    profile = await PayrollService.get_profile_by_employee_id(db, current_user["tenant_id"], employee_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Payroll profile not found")
    return profile

@router.post("/compensation", response_model=CompensationResponse)
async def create_compensation(
    comp_in: CompensationCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await PayrollService.create_compensation(db, current_user["tenant_id"], comp_in)
