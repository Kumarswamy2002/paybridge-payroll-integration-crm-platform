from typing import Dict, Any, List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user
from app.services.ai_service import AIService

router = APIRouter()

class CaseSummarizeRequest(BaseModel):
    case_id: str

class AnomalyDetectRequest(BaseModel):
    payroll_run_data: List[Dict[str, Any]]

class AIQueryRequest(BaseModel):
    prompt: str

@router.post("/summarize-case")
async def summarize_case(
    req: CaseSummarizeRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await AIService.summarize_case(db, current_user["tenant_id"], req.case_id)

@router.post("/detect-anomalies")
async def detect_anomalies(
    req: AnomalyDetectRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    anomalies = await AIService.detect_anomalies(db, current_user["tenant_id"], req.payroll_run_data)
    return {
        "anomalies_detected_count": len(anomalies),
        "anomalies": anomalies
    }

@router.post("/query")
async def natural_language_query(
    req: AIQueryRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return await AIService.natural_language_query(db, current_user["tenant_id"], req.prompt)
