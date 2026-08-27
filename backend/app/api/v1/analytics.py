from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user
from app.services.analytics_service import AnalyticsService

router = APIRouter()

@router.get("/overview")
async def get_analytics_overview(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await AnalyticsService.get_overview_metrics(db, current_user["tenant_id"])

@router.get("/sync-performance")
async def get_sync_performance(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await AnalyticsService.get_sync_performance_metrics(db, current_user["tenant_id"])

@router.get("/cases-sla")
async def get_cases_sla(
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await AnalyticsService.get_cases_sla_metrics(db, current_user["tenant_id"])
