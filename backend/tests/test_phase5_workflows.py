import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_workflow_engine_and_approval_flow(client: AsyncClient):
    # 1. Setup Tenant and User
    tenant_res = await client.post("/api/v1/tenants/", json={"name": "Cyberdyne", "slug": "cyberdyne"})
    tenant_id = tenant_res.json()["id"]

    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "hr_lead@cyberdyne.com",
        "password": "Password123!",
        "full_name": "HR Lead",
        "tenant_id": tenant_id,
        "role": "TENANT_ADMIN"
    })
    headers = {"Authorization": f"Bearer {(await client.post('/api/v1/auth/login', json={'email': 'hr_lead@cyberdyne.com', 'password': 'Password123!', 'tenant_slug': 'cyberdyne'})).json()['access_token']}"}

    # 2. Create Workflow Rule for Salary Changes
    rule_res = await client.post("/api/v1/workflows/rules", json={
        "name": "High Salary Increase Approval Rule",
        "event_trigger": "SalaryChanged",
        "conditions": {"min_increase": 10000},
        "actions": [{"type": "REQUEST_APPROVAL", "role": "HR_MANAGER"}]
    }, headers=headers)
    assert rule_res.status_code == 200
    rule_data = rule_res.json()
    assert rule_data["name"] == "High Salary Increase Approval Rule"

    # 3. Trigger Workflow Event
    trig_res = await client.post("/api/v1/workflows/events/trigger", json={
        "event_trigger": "SalaryChanged",
        "entity_type": "Compensation",
        "entity_id": "EMP-CYBER-101",
        "payload": {"old_salary": 100000, "new_salary": 125000}
    }, headers=headers)
    assert trig_res.status_code == 200
    trig_data = trig_res.json()
    assert trig_data["approvals_created_count"] == 1
    approval = trig_data["approvals"][0]
    approval_id = approval["id"]
    assert approval["status"] == "PENDING"
    assert approval["approver_role"] == "HR_MANAGER"

    # 4. List Pending Approvals
    pending_res = await client.get("/api/v1/workflows/approvals/pending?role=HR_MANAGER", headers=headers)
    assert pending_res.status_code == 200
    pending_list = pending_res.json()
    assert len(pending_list) >= 1
    assert pending_list[0]["id"] == approval_id

    # 5. Approve Request
    resp_res = await client.post(f"/api/v1/workflows/approvals/{approval_id}/respond", json={
        "decision": "APPROVED",
        "notes": "Approved in executive board meeting on Jan 15"
    }, headers=headers)
    assert resp_res.status_code == 200
    resp_data = resp_res.json()
    assert resp_data["status"] == "APPROVED"
    assert resp_data["approval_notes"] == "Approved in executive board meeting on Jan 15"
