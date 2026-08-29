import pytest
from integration_platform.adapters.diagnostics import ConnectorDiagnosticSuite

@pytest.mark.asyncio
async def test_single_connector_diagnostic():
    result = await ConnectorDiagnosticSuite.run_diagnostic("mock")
    assert result["provider"] == "mock"
    assert "latency_ms" in result
    assert result["capabilities"]["employee_sync"] is True

@pytest.mark.asyncio
async def test_all_connectors_diagnostic():
    results = await ConnectorDiagnosticSuite.run_all_diagnostics()
    assert len(results) >= 5
    providers = [r["provider"] for r in results]
    assert "adp" in providers
    assert "gusto" in providers
