from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.crm import (
    CRMCaseCreate, CRMCaseResponse, CRMCaseTransitionRequest,
    CRMActivityCreate, CRMActivityResponse, TimelineEventResponse
)
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

@router.get("/cases/{case_id}", response_model=CRMCaseResponse)
async def get_case(
    case_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    case = await CRMService.get_case_by_id(db, current_user["tenant_id"], case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found")
    return case

@router.post("/cases/{case_id}/transition", response_model=CRMCaseResponse)
async def transition_case(
    case_id: str,
    trans_in: CRMCaseTransitionRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.transition_case_status(
        db,
        current_user["tenant_id"],
        case_id,
        new_status=trans_in.new_status,
        resolution_notes=trans_in.resolution_notes,
        assigned_to_user_id=trans_in.assigned_to_user_id,
        actor_name=current_user.get("user_id", "System User")
    )

@router.post("/cases/{case_id}/activities", response_model=CRMActivityResponse)
async def add_case_activity(
    case_id: str,
    act_in: CRMActivityCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.add_case_activity(
        db,
        current_user["tenant_id"],
        case_id,
        activity_type=act_in.activity_type,
        title=act_in.title,
        content=act_in.content,
        actor_user_id=current_user["user_id"]
    )

@router.get("/cases/{case_id}/activities", response_model=List[CRMActivityResponse])
async def get_case_activities(
    case_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.get_case_activities(db, current_user["tenant_id"], case_id)

@router.get("/timeline/{employee_id}", response_model=List[TimelineEventResponse])
async def get_employee_timeline(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await CRMService.get_employee_timeline(db, current_user["tenant_id"], employee_id)
