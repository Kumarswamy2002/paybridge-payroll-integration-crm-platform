"""
Integration Platform - Connector Diagnostics Suite
Automated health checks, latency profiling, and schema compliance verification across adapters.
"""
from typing import Dict, Any, List
import time
from integration_platform.adapters.factory import AdapterFactory

class ConnectorDiagnosticSuite:
    SUPPORTED_PROVIDERS = [
        "adp", "gusto", "bamboohr", "paychex", "paylocity",
        "paycom", "namely", "zenefits", "personio", "sap_successfactors", "trunet", "mock"
    ]

    @classmethod
    async def run_diagnostic(cls, provider: str, config: Dict[str, Any] = None) -> Dict[str, Any]:
        config = config or {"api_key": "diag_test_key", "environment": "sandbox"}
        provider_lower = provider.lower()
        start_time = time.perf_counter()
        try:
            adapter = AdapterFactory.get_adapter(provider_lower, config)
            connected = await adapter.test_connection()
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            return {
                "provider": provider_lower,
                "status": "healthy" if connected else "unhealthy",
                "connected": connected,
                "latency_ms": elapsed_ms,
                "capabilities": {
                    "employee_sync": hasattr(adapter, "get_employees"),
                    "payroll_runs": hasattr(adapter, "get_payroll_runs"),
                    "webhook_ingestion": hasattr(adapter, "process_webhook")
                },
                "diagnostics_version": "2.1.0"
            }
        except Exception as e:
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            return {
                "provider": provider_lower,
                "status": "error",
                "connected": False,
                "latency_ms": elapsed_ms,
                "error": str(e),
                "diagnostics_version": "2.1.0"
            }

    @classmethod
    async def run_all_diagnostics(cls) -> List[Dict[str, Any]]:
        results = []
        for provider in cls.SUPPORTED_PROVIDERS:
            diag = await cls.run_diagnostic(provider)
            results.append(diag)
        return results
