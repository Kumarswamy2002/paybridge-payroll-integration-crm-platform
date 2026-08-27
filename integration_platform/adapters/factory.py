from typing import Dict, Any
from fastapi import HTTPException, status
from integration_platform.adapters.base import BasePayrollAdapter
from integration_platform.adapters.gusto import GustoAdapter
from integration_platform.adapters.adp import ADPWorkforceAdapter
from integration_platform.adapters.mock import MockPayrollAdapter

class AdapterFactory:
    """Registry and Factory for Payroll Provider Adapters."""

    _adapters = {
        "GUSTO": GustoAdapter,
        "ADP": ADPWorkforceAdapter,
        "RIPPLING": MockPayrollAdapter,
        "WORKDAY": MockPayrollAdapter,
        "MOCK_PAYROLL": MockPayrollAdapter,
    }

    @classmethod
    def get_adapter(cls, provider_name: str, config: Dict[str, Any]) -> BasePayrollAdapter:
        provider_key = provider_name.upper()
        adapter_cls = cls._adapters.get(provider_key)
        if not adapter_cls:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported payroll provider adapter: {provider_name}. Supported: {list(cls._adapters.keys())}"
            )
        return adapter_cls(config)
