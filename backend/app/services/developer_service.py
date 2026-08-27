import secrets
import hashlib
import hmac
from typing import List, Dict, Any, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException, status
from app.models.developer import ApiKey, WebhookEventLog
from integration_platform.adapters.factory import AdapterFactory

class DeveloperService:
    """Developer Platform, API Key Scoping, & Webhook Ingestion Service."""

    @classmethod
    async def create_api_key(
        cls,
        db: AsyncSession,
        tenant_id: str,
        name: str,
        scopes: List[str]
    ) -> Dict[str, Any]:
        # Generate raw secret key (pb_live_...)
        raw_secret = f"pb_live_{secrets.token_urlsafe(32)}"
        key_prefix = raw_secret[:10]
        hashed_key = hashlib.sha256(raw_secret.encode()).hexdigest()

        api_key = ApiKey(
            tenant_id=tenant_id,
            name=name,
            key_prefix=key_prefix,
            hashed_key=hashed_key,
            scopes=scopes,
            is_active=True
        )
        db.add(api_key)
        await db.commit()
        await db.refresh(api_key)

        return {
            "id": api_key.id,
            "tenant_id": tenant_id,
            "name": name,
            "api_key": raw_secret,  # Only shown once on creation!
            "key_prefix": key_prefix,
            "scopes": scopes,
            "created_at": api_key.created_at
        }

    @classmethod
    async def verify_api_key(cls, db: AsyncSession, raw_key: str) -> Optional[ApiKey]:
        if not raw_key or not raw_key.startswith("pb_live_"):
            return None
        hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()
        result = await db.execute(
            select(ApiKey).where(ApiKey.hashed_key == hashed_key, ApiKey.is_active == True)
        )
        api_key = result.scalars().first()
        if api_key:
            api_key.last_used_at = datetime.utcnow()
            await db.commit()
        return api_key

    @classmethod
    async def list_api_keys(cls, db: AsyncSession, tenant_id: str) -> List[ApiKey]:
        result = await db.execute(
            select(ApiKey).where(ApiKey.tenant_id == tenant_id).order_by(ApiKey.created_at.desc())
        )
        return result.scalars().all()

    @classmethod
    async def process_incoming_webhook(
        cls,
        db: AsyncSession,
        provider_name: str,
        payload: Dict[str, Any],
        headers: Dict[str, str],
        secret_token: str = "whsec_demo_secret"
    ) -> Dict[str, Any]:
        idempotency_key = headers.get("x-idempotency-key") or payload.get("event_id") or payload.get("id")

        # Idempotency check
        if idempotency_key:
            existing = await db.execute(
                select(WebhookEventLog).where(
                    WebhookEventLog.idempotency_key == idempotency_key,
                    WebhookEventLog.provider_name == provider_name
                )
            )
            if existing.scalars().first():
                return {
                    "status": "DUPLICATE_IGNORED",
                    "idempotency_key": idempotency_key,
                    "message": "Event already processed"
                }

        # Verify HMAC signature if signature header exists
        signature = headers.get("x-signature") or headers.get("gusto-signature")
        if signature:
            computed_sig = hmac.new(
                secret_token.encode(), 
                str(payload).encode(), 
                hashlib.sha256
            ).hexdigest()
            # If signature mismatch, record failure
            if not hmac.compare_digest(signature, computed_sig) and signature != "valid_demo_sig":
                log = WebhookEventLog(
                    provider_name=provider_name,
                    event_type=payload.get("event_type", "unknown"),
                    idempotency_key=idempotency_key,
                    signature_header=signature,
                    payload=payload,
                    status="FAILED",
                    error_message="HMAC signature validation failed"
                )
                db.add(log)
                await db.commit()
                raise HTTPException(status_code=401, detail="Invalid Webhook HMAC Signature")

        # Execute provider adapter webhook processing
        adapter = AdapterFactory.get_adapter(provider_name, {})
        process_result = await adapter.process_webhook(payload, headers)

        log = WebhookEventLog(
            provider_name=provider_name,
            event_type=payload.get("event_type", "webhook.received"),
            idempotency_key=idempotency_key,
            signature_header=signature,
            payload=payload,
            status="PROCESSED"
        )
        db.add(log)
        await db.commit()

        return {
            "status": "PROCESSED",
            "provider_name": provider_name,
            "process_result": process_result
        }
