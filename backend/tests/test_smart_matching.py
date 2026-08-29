import pytest
from integration_platform.canonical.smart_matcher import SmartReconciliationMatcher

def test_exact_email_match():
    provider_rec = {"id": "EXT-1", "email": "alice@company.com", "first_name": "Alice", "last_name": "Smith"}
    crm_records = [
        {"id": "CRM-1", "email": "alice@company.com", "first_name": "Alice", "last_name": "Smith"},
        {"id": "CRM-2", "email": "bob@company.com", "first_name": "Bob", "last_name": "Jones"}
    ]
    match = SmartReconciliationMatcher.match_employee_record(provider_rec, crm_records)
    assert match is not None
    assert match.target_id == "CRM-1"
    assert match.match_type == "EXACT_EMAIL"
    assert match.confidence_score == 1.0

def test_fuzzy_name_match():
    provider_rec = {"id": "EXT-2", "email": "diff@other.com", "first_name": "Robert", "last_name": "Williams"}
    crm_records = [
        {"id": "CRM-3", "email": "rw@corp.com", "first_name": "Rob", "last_name": "Williams"}
    ]
    match = SmartReconciliationMatcher.match_employee_record(provider_rec, crm_records, threshold=0.7)
    assert match is not None
    assert match.target_id == "CRM-3"
    assert match.confidence_score >= 0.7

def test_variance_severity_classification():
    negligible = SmartReconciliationMatcher.evaluate_variance_severity(1000.0, 1000.5)
    assert negligible["severity"] == "NEGLIGIBLE"
    assert negligible["suggested_action"] == "AUTO_RESOLVE_WITHIN_TOLERANCE"

    critical = SmartReconciliationMatcher.evaluate_variance_severity(1000.0, 1800.0)
    assert critical["severity"] == "CRITICAL"
    assert critical["suggested_action"] == "ESCALATE_TO_PAYROLL_DIRECTOR"
