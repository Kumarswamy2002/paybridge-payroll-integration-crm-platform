from typing import Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.core.middleware import get_current_user, require_roles
from integration_platform.adapters.factory import AdapterFactory
from integration_platform.mappings.engine import DataMappingEngine, MappingDefinition
from integration_platform.synchronization.engine import SynchronizationEngine

router = APIRouter()

class ConnectionTestRequest(BaseModel):
    provider_name: str
    config: Dict[str, Any]

class SyncTriggerRequest(BaseModel):
    provider_name: str
    config: Dict[str, Any] = {}
    sync_type: str = "MANUAL_SYNC"

class TransformPayloadRequest(BaseModel):
    raw_data: Dict[str, Any]
    mapping_definition: MappingDefinition

@router.post("/connections/test")
async def test_provider_connection(
    req: ConnectionTestRequest,
    current_user: dict = Depends(get_current_user)
):
    adapter = AdapterFactory.get_adapter(req.provider_name, req.config)
    is_connected = await adapter.test_connection()
    return {
        "provider_name": req.provider_name,
        "connected": is_connected,
        "status": "ONLINE" if is_connected else "OFFLINE"
    }

@router.post("/sync/trigger")
async def trigger_sync_job(
    req: SyncTriggerRequest,
    db: AsyncSession = Depends(get_db),
    current_user: dict = Depends(require_roles(["TENANT_ADMIN", "PAYROLL_ADMIN", "SUPER_ADMIN"]))
):
    result = await SynchronizationEngine.run_sync_job(
        db,
        tenant_id=current_user["tenant_id"],
        provider_name=req.provider_name,
        provider_config=req.config,
        sync_type=req.sync_type
    )
    return result

@router.post("/mappings/transform")
async def transform_provider_schema(
    req: TransformPayloadRequest,
    current_user: dict = Depends(get_current_user)
):
    result = DataMappingEngine.transform(req.raw_data, req.mapping_definition)
    return {
        "provider_name": req.mapping_definition.provider_name,
        "transformed_data": result
    }
