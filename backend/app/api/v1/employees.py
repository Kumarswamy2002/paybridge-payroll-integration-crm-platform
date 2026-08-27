from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.schemas.employee import EmployeeCreate, EmployeeResponse, Employee360Response
from app.services.employee_service import EmployeeService
from app.core.middleware import get_current_user

router = APIRouter()

@router.post("/", response_model=EmployeeResponse)
async def create_employee(
    emp_in: EmployeeCreate,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await EmployeeService.create_employee(db, current_user["tenant_id"], emp_in)

@router.get("/", response_model=List[EmployeeResponse])
async def list_employees(
    department_id: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await EmployeeService.list_employees(db, current_user["tenant_id"], department_id, status)

@router.get("/{employee_id}", response_model=EmployeeResponse)
async def get_employee(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    employee = await EmployeeService.get_employee_by_id(db, current_user["tenant_id"], employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.get("/{employee_id}/360", response_model=Employee360Response)
async def get_employee_360(
    employee_id: str,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    emp_360 = await EmployeeService.get_employee_360(db, current_user["tenant_id"], employee_id)
    if not emp_360:
        raise HTTPException(status_code=404, detail="Employee 360 profile not found")
    return emp_360
