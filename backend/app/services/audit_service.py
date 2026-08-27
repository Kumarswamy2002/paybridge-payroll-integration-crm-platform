from typing import Optional, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.audit import AuditLog

class AuditService:
    @staticmethod
    async def log_action(
        db: AsyncSession,
        tenant_id: str,
        action: str,
        entity_type: str,
        entity_id: Optional[str] = None,
        user_id: Optional[str] = None,
        user_email: Optional[str] = None,
        before_state: Optional[Dict[str, Any]] = None,
        after_state: Optional[Dict[str, Any]] = None,
        ip_address: Optional[str] = None,
        reason: Optional[str] = None,
    ) -> AuditLog:
        log_entry = AuditLog(
            tenant_id=tenant_id,
            user_id=user_id,
            user_email=user_email,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            before_state=before_state,
            after_state=after_state,
            ip_address=ip_address,
            reason=reason
        )
        db.add(log_entry)
        await db.commit()
        return log_entry
