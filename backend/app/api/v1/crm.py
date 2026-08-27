from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.crm import CRMCaseCreate, CRMCaseResponse, TimelineEventResponse
from app.services.crm_service import CRMService
from app.core.middleware import get_current_user

router = APIRouter()

@router.post("/cases", response_model=CRMCaseResponse)
async def create_case(
    case_in: CRMCaseCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.create_case(db, current_user["tenant_id"], case_in)

@router.get("/cases", response_model=List[CRMCaseResponse])
async def list_cases(
    employee_id: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.list_cases(db, current_user["tenant_id"], employee_id)

@router.get("/timeline/{employee_id}", response_model=List[TimelineEventResponse])
async def get_employee_timeline(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.get_employee_timeline(db, current_user["tenant_id"], employee_id)
