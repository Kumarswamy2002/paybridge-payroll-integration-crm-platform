import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_full_paybridge_end_to_end_master_lifecycle(client: AsyncClient):
    """Master E2E Lifecycle Test verifying all 10 domains of PayBridge."""

    # 1. Tenant Provisioning
    tenant_res = await client.post("/api/v1/tenants/", json={
        "name": "Titanium Global",
        "slug": "titanium-global",
        "subscription_plan": "ENTERPRISE"
    })
    assert tenant_res.status_code == 200
    tenant_id = tenant_res.json()["id"]

    # 2. User Auth & Registration (Tenant Admin)
    reg_res = await client.post("/api/v1/auth/register", json={
        "email": "chief.admin@titanium.com",
        "password": "MasterSecurePassword2026!",
        "full_name": "Chief Admin",
        "tenant_id": tenant_id,
        "role": "TENANT_ADMIN"
    })
    assert reg_res.status_code == 200

    login_res = await client.post("/api/v1/auth/login", json={
        "email": "chief.admin@titanium.com",
        "password": "MasterSecurePassword2026!",
        "tenant_slug": "titanium-global"
    })
    assert login_res.status_code == 200
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Organization & Department Setup
    org_res = await client.post("/api/v1/orgs/orgs", json={"name": "Titanium Engineering"}, headers=headers)
    org_id = org_res.json()["id"]

    dept_res = await client.post("/api/v1/orgs/departments", json={
        "organization_id": org_id,
        "name": "Core Platform & Infrastructure"
    }, headers=headers)
    dept_id = dept_res.json()["id"]

    # 4. Employee CRM Registration
    emp_res = await client.post("/api/v1/employees/", json={
        "employee_code": "TITAN-001",
        "first_name": "Alexander",
        "last_name": "Hamilton",
        "email": "alex.h@titanium.com",
        "department_id": dept_id,
        "employment_type": "FULL_TIME"
    }, headers=headers)
    assert emp_res.status_code == 200
    emp_id = emp_res.json()["id"]

    # 5. Payroll Profile & PII Encryption
    prof_res = await client.post("/api/v1/payroll/profiles", json={
        "employee_id": emp_id,
        "payroll_provider": "GUSTO",
        "external_provider_employee_id": "GUSTO-TITAN-001",
        "payment_method": "DIRECT_DEPOSIT",
        "tax_identifier": "SSN-000-11-2222",
        "bank_account": "US9988776655443322"
    }, headers=headers)
    assert prof_res.status_code == 200

    # Verify PII Encryption / Role Decryption
    pii_res = await client.get(f"/api/v1/payroll/profiles/pii/{emp_id}", headers=headers)
    assert pii_res.status_code == 200
    assert pii_res.json()["tax_identifier"] == "SSN-000-11-2222"

    # 6. Compensation History Superseding
    comp1 = await client.post("/api/v1/payroll/compensation", json={
        "employee_id": emp_id,
        "pay_frequency": "MONTHLY",
        "currency": "USD",
        "base_salary": 120000.0,
        "effective_date": "2025-01-01"
    }, headers=headers)
    assert comp1.status_code == 200

    comp2 = await client.post("/api/v1/payroll/compensation", json={
        "employee_id": emp_id,
        "pay_frequency": "MONTHLY",
        "currency": "USD",
        "base_salary": 150000.0,  # $12,500 / month
        "effective_date": "2026-01-01"
    }, headers=headers)
    assert comp2.status_code == 200

    # 7. Provider Adapter Connection & Synchronization Run
    conn_res = await client.post("/api/v1/integrations/connections/test", json={
        "provider_name": "GUSTO",
        "config": {"api_key": "demo", "company_id": "demo"}
    }, headers=headers)
    assert conn_res.json()["connected"] is True

    sync_res = await client.post("/api/v1/integrations/sync/trigger", json={
        "provider_name": "GUSTO",
        "sync_type": "FULL_SYNC"
    }, headers=headers)
    assert sync_res.json()["status"] == "SUCCESS"

    # 8. Reconciliation & Automated Exception-to-CRM Pipeline
    recon_res = await client.post("/api/v1/reconciliation/run", json={
        "payroll_provider": "GUSTO",
        "payroll_run_id": "PAYRUN-JAN-2026",
        "provider_results": [
            {
                "payroll_run_id": "PAYRUN-JAN-2026",
                "external_employee_id": "GUSTO-TITAN-001",
                "gross_pay": 9500.00,  # $3,000 Mismatch ($12,500 vs $9,500)
                "net_pay": 7100.00,
                "tax_withheld": 1900.00,
                "deductions": 500.00,
                "direct_deposit_amount": 7100.00
            }
        ]
    }, headers=headers)
    assert recon_res.json()["discrepancies_count"] == 1

    # 9. Workflow Automation & Approval Engine
    await client.post("/api/v1/workflows/rules", json={
        "name": "High Variance Escalation Rule",
        "event_trigger": "ReconciliationMismatch",
        "actions": [{"type": "REQUEST_APPROVAL", "role": "PAYROLL_ADMIN"}]
    }, headers=headers)

    wf_res = await client.post("/api/v1/workflows/events/trigger", json={
        "event_trigger": "ReconciliationMismatch",
        "entity_type": "Discrepancy",
        "entity_id": emp_id
    }, headers=headers)
    approval_id = wf_res.json()["approvals"][0]["id"]

    # Approve request
    app_res = await client.post(f"/api/v1/workflows/approvals/{approval_id}/respond", json={
        "decision": "APPROVED",
        "notes": "Adjustment confirmed for February payroll."
    }, headers=headers)
    assert app_res.json()["status"] == "APPROVED"

    # 10. Notifications & Case Messaging
    notif_res = await client.post("/api/v1/notifications/send", json={
        "user_id": reg_res.json()["id"],
        "title": "Reconciliation Action Approved",
        "template_name": "PAYSLIP_AVAILABLE",
        "context": {"name": "Alexander", "period": "January"}
    }, headers=headers)
    assert notif_res.status_code == 200

    # 11. Developer API Key & Webhook Gateway
    key_res = await client.post("/api/v1/developers/api-keys", json={
        "name": "Production Enterprise Key",
        "scopes": ["*"]
    }, headers=headers)
    assert "pb_live_" in key_res.json()["api_key"]

    wh_res = await client.post("/api/v1/developers/webhooks/incoming/GUSTO", json={
        "event_id": "wh_e2e_101",
        "event_type": "payroll.approved"
    }, headers={"x-idempotency-key": "wh_e2e_101"})
    assert wh_res.json()["status"] == "PROCESSED"

    # 12. AI Case Summarizer & Anomaly Detector
    cases = (await client.get(f"/api/v1/crm/cases?employee_id={emp_id}", headers=headers)).json()
    case_id = cases[0]["id"]
    ai_sum = await client.post("/api/v1/ai/summarize-case", json={"case_id": case_id}, headers=headers)
    assert ai_sum.status_code == 200
    assert "Titanium" in ai_sum.json()["summary"] or "Reconciliation" in ai_sum.json()["summary"] or "OPEN" in ai_sum.json()["summary"]

    # 13. Analytics Overview Dashboard
    ana_res = await client.get("/api/v1/analytics/overview", headers=headers)
    assert ana_res.status_code == 200
    assert ana_res.json()["active_employees"] >= 1
