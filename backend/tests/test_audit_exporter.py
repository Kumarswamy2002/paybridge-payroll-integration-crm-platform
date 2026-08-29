from backend.app.services.audit_exporter_service import AuditExporterService

def test_audit_exporter_integrity():
    entries = [
        {"id": "tx_1", "account": "Payroll Expense", "debit": 15000.0, "credit": 0.0},
        {"id": "tx_2", "account": "Cash Clearing", "debit": 0.0, "credit": 15000.0}
    ]
    pkg = AuditExporterService.generate_audit_package(entries, "org_corp_99")
    assert pkg["entry_count"] == 2
    assert pkg["balanced"] is True
    assert len(pkg["checksum_sha256"]) == 64
