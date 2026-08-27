import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_payroll_profile_pii_encryption_and_decryption(client: AsyncClient):
    # 1. Tenant & User Setup
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Aether Inc", "slug": "aether"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "payroll_admin@aether.com",
        "password": "Password123!",
        "full_name": "Payroll Lead",
        "tenant_id": tenant_id,
        "role": "PAYROLL_ADMIN"
    })

    login_res = await client.post("/api/v1/auth/login", json={
        "email": "payroll_admin@aether.com",
        "password": "Password123!",
        "tenant_slug": "aether"
    })
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create Employee
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-909",
        "first_name": "David",
        "last_name": "Miller",
        "email": "david.m@aether.com",
        "employment_type": "FULL_TIME"
    }, headers=headers)
    emp_id = emp_res.json()["id"]

    # 3. Create Payroll Profile with PII Data (SSN & Bank Account)
    profile_res = await client.post("/api/v1/payroll/profiles", json={
        "employee_id": emp_id,
        "payroll_provider": "ADP",
        "external_provider_employee_id": "ADP-8812",
        "payment_method": "DIRECT_DEPOSIT",
        "tax_identifier": "SSN-999-88-7766",
        "bank_account": "US8937000111222333"
    }, headers=headers)
    assert profile_res.status_code == 200
    profile_data = profile_res.json()
    assert profile_data["payroll_provider"] == "ADP"

    # 4. Fetch Decrypted PII (Requires PAYROLL_ADMIN role)
    pii_res = await client.get(f"/api/v1/payroll/profiles/pii/{emp_id}", headers=headers)
    assert pii_res.status_code == 200
    pii_data = pii_res.json()
    assert pii_data["tax_identifier"] == "SSN-999-88-7766"
    assert pii_data["bank_account"] == "US8937000111222333"

@pytest.mark.asyncio
async def test_compensation_history_superseding(client: AsyncClient):
    # Setup
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Vortex", "slug": "vortex"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "hr@vortex.com",
        "password": "Password123!",
        "full_name": "HR Manager",
        "tenant_id": tenant_id,
        "role": "HR_MANAGER"
    })

    login_res = await client.post("/api/v1/auth/login", json={
        "email": "hr@vortex.com",
        "password": "Password123!",
        "tenant_slug": "vortex"
    })
    headers = {"Authorization": f"Bearer {login_res.json()['access_token']}"}

    # Create Employee
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-303",
        "first_name": "Alice",
        "last_name": "Vane",
        "email": "alice.v@vortex.com"
    }, headers=headers)
    emp_id = emp_res.json()["id"]

    # Initial Compensation ($100,000)
    comp1_res = await client.post("/api/v1/payroll/compensation", json={
        "employee_id": emp_id,
        "pay_frequency": "MONTHLY",
        "currency": "USD",
        "base_salary": 100000.0,
        "effective_date": "2025-01-01"
    }, headers=headers)
    assert comp1_res.status_code == 200
    assert comp1_res.json()["status"] == "ACTIVE"

    # Revised Compensation ($120,000)
    comp2_res = await client.post("/api/v1/payroll/compensation", json={
        "employee_id": emp_id,
        "pay_frequency": "MONTHLY",
        "currency": "USD",
        "base_salary": 120000.0,
        "effective_date": "2026-01-01"
    }, headers=headers)
    assert comp2_res.status_code == 200
    assert comp2_res.json()["status"] == "ACTIVE"

    # Fetch History
    history_res = await client.get(f"/api/v1/payroll/compensation/history/{emp_id}", headers=headers)
    assert history_res.status_code == 200
    history = history_res.json()
    assert len(history) == 2
    # Latest should be active
    assert history[0]["base_salary"] == 120000.0
    assert history[0]["status"] == "ACTIVE"
    # Older should be superseded
    assert history[1]["base_salary"] == 100000.0
    assert history[1]["status"] == "SUPERSEDED"

@pytest.mark.asyncio
async def test_case_lifecycle_state_machine(client: AsyncClient):
    # Setup
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Starlight", "slug": "starlight"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "support@starlight.com",
        "password": "Password123!",
        "full_name": "Support Officer",
        "tenant_id": tenant_id,
        "role": "EMPLOYEE"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'support@starlight.com', 'password': 'Password123!', 'tenant_slug': 'starlight'})).json()['access_token']}"}

    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "EMP-777",
        "first_name": "Bob",
        "last_name": "Builder",
        "email": "bob.b@starlight.com"
    }, headers=headers)
    emp_id = emp_res.json()["id"]

    # 1. Create Case
    case_res = await client.post("/api/v1/crm/cases", json={
        "employee_id": emp_id,
        "title": "Payslip Deduction Error",
        "category": "DEDUCTION_QUERY",
        "priority": "HIGH",
        "description": "401k contribution deducted twice in January"
    }, headers=headers)
    assert case_res.status_code == 200
    case_data = case_res.json()
    case_id = case_data["id"]
    assert case_data["status"] == "OPEN"
    assert "PAY-" in case_data["ticket_number"]

    # 2. Transition to INVESTIGATING
    trans1_res = await client.post(f"/api/v1/crm/cases/{case_id}/transition", json={
        "new_status": "INVESTIGATING"
    }, headers=headers)
    assert trans1_res.status_code == 200
    assert trans1_res.json()["status"] == "INVESTIGATING"

    # 3. Add Activity note
    act_res = await client.post(f"/api/v1/crm/cases/{case_id}/activities", json={
        "activity_type": "NOTE",
        "title": "Contacted Rippling Support",
        "content": "Awaiting provider credit memo for duplicate deduction."
    }, headers=headers)
    assert act_res.status_code == 200

    # 4. Resolve Case
    trans2_res = await client.post(f"/api/v1/crm/cases/{case_id}/transition", json={
        "new_status": "RESOLVED",
        "resolution_notes": "Credit memo processed in Gusto payroll adjustment."
    }, headers=headers)
    assert trans2_res.status_code == 200
    assert trans2_res.json()["status"] == "RESOLVED"
    assert trans2_res.json()["resolution_notes"] == "Credit memo processed in Gusto payroll adjustment."

    # 5. Check Unified Timeline
    timeline_res = await client.get(f"/api/v1/crm/timeline/{emp_id}", headers=headers)
    assert timeline_res.status_code == 200
    events = timeline_res.json()
    event_types = [e["event_type"] for e in events]
    assert "CASE_OPENED" in event_types
    assert "CASE_RESOLVED" in event_types
