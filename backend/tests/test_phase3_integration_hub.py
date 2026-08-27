import pytest
from httpx import AsyncClient
from integration_platform.adapters.factory import AdapterFactory
from integration_platform.mappings.engine import DataMappingEngine, MappingDefinition, FieldMappingRule

@pytest.mark.asyncio
async def test_provider_adapter_factory_and_connections(client: AsyncClient):
    # Test Gusto adapter creation & connection test
    gusto_adapter = AdapterFactory.get_adapter("GUSTO", {"api_key": "k1", "company_id": "c1"})
    assert await gusto_adapter.test_connection() is True
    gusto_emps = await gusto_adapter.get_employees()
    assert len(gusto_emps) >= 2
    assert gusto_emps[0].provider_name == "GUSTO"

    # Test ADP adapter creation & connection test
    adp_adapter = AdapterFactory.get_adapter("ADP", {"client_id": "c1", "client_secret": "s1"})
    assert await adp_adapter.test_connection() is True
    adp_emps = await adp_adapter.get_employees()
    assert len(adp_emps) >= 1
    assert adp_emps[0].provider_name == "ADP"

@pytest.mark.asyncio
async def test_data_mapping_engine():
    raw_payload = {
        "person": {
            "name": {"first": "Samantha", "last": "Carter"},
            "salary": "145000.50"
        },
        "dept": "Research"
    }

    mapping_def = MappingDefinition(
        provider_name="CUSTOM_HR",
        tenant_id="t1",
        rules=[
            FieldMappingRule(source_field="person.name.first", target_field="first_name"),
            FieldMappingRule(source_field="person.name.last", target_field="last_name"),
            FieldMappingRule(source_field="person.salary", target_field="base_salary", transform_type="FLOAT"),
            FieldMappingRule(source_field="dept", target_field="department_name"),
            FieldMappingRule(source_field="missing_field", target_field="currency", default_value="USD")
        ]
    )

    transformed = DataMappingEngine.transform(raw_payload, mapping_def)
    assert transformed["first_name"] == "Samantha"
    assert transformed["last_name"] == "Carter"
    assert transformed["base_salary"] == 145000.50
    assert transformed["department_name"] == "Research"
    assert transformed["currency"] == "USD"

@pytest.mark.asyncio
async def test_integration_sync_api_flow(client: AsyncClient):
    # Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Orion Corp", "slug": "orion"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "admin@orion.com",
        "password": "Password123!",
        "full_name": "Orion Admin",
        "tenant_id": tenant_id,
        "role": "PAYROLL_ADMIN"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'admin@orion.com', 'password': 'Password123!', 'tenant_slug': 'orion'})).json()['access_token']}"}

    # 1. Test Connection API
    conn_res = await client.post("/api/v1/integrations/connections/test", json={
        "provider_name": "GUSTO",
        "config": {"api_key": "k", "company_id": "c"}
    }, headers=headers)
    assert conn_res.status_code == 200
    assert conn_res.json()["connected"] is True

    # 2. Trigger Provider Synchronization API
    sync_res = await client.post("/api/v1/integrations/sync/trigger", json={
        "provider_name": "GUSTO",
        "config": {"api_key": "k", "company_id": "c"},
        "sync_type": "MANUAL_SYNC"
    }, headers=headers)
    assert sync_res.status_code == 200
    sync_data = sync_res.json()
    assert sync_data["status"] == "SUCCESS"
    assert sync_data["records_processed"] >= 2

    # 3. Verify Employees were automatically upserted into Employee CRM
    emps_res = await client.get("/api/v1/employees/", headers=headers)
    assert emps_res.status_code == 200
    emps = emps_res.json()
    assert len(emps) >= 2
    emails = [e["email"] for e in emps]
    assert "sarah.c@nexuscorp.com" in emails
