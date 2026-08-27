from typing import List, Dict, Any
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user, require_roles
from app.services.reconciliation_service import ReconciliationService
from integration_platform.canonical.models import CanonicalPayrollResult

router = APIRouter()

class ReconciliationRunRequest(BaseModel):
    payroll_provider: str
    payroll_run_id: str
    provider_results: List[CanonicalPayrollResult]
    tolerance_threshold: float = 1.00

@router.post("/run")
async def run_reconciliation(
    req: ReconciliationRunRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_roles(["TENANT_ADMIN", "PAYROLL_ADMIN", "SUPER_ADMIN"]))
):
    return await ReconciliationService.run_reconciliation(
        db,
        tenant_id=current_user["tenant_id"],
        payroll_provider=req.payroll_provider,
        payroll_run_id=req.payroll_run_id,
        provider_results=req.provider_results,
        tolerance_threshold=req.tolerance_threshold
    )

@router.get("/discrepancies")
async def list_discrepancies(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await ReconciliationService.list_discrepancies(db, current_user["tenant_id"])
