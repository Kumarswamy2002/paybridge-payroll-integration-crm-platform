"""
SOX-Compliant Payroll Audit & Financial Ledger Exporter
"""
import hashlib
import json
from typing import List, Dict, Any

class AuditExporterService:
    @staticmethod
    def generate_audit_package(ledger_entries: List[Dict[str, Any]], organization_id: str) -> Dict[str, Any]:
        payload_str = json.dumps(ledger_entries, sort_keys=True)
        checksum = hashlib.sha256(payload_str.encode('utf-8')).hexdigest()
        total_credit = sum(e.get("credit", 0.0) for e in ledger_entries)
        total_debit = sum(e.get("debit", 0.0) for e in ledger_entries)
        return {
            "organization_id": organization_id,
            "entry_count": len(ledger_entries),
            "total_credit": round(total_credit, 2),
            "total_debit": round(total_debit, 2),
            "balanced": round(total_credit, 2) == round(total_debit, 2),
            "checksum_sha256": checksum,
            "compliance_standard": "SOX-404-FINANCIAL"
        }
