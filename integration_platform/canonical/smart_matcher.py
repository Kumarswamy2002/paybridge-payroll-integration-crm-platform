"""
PayBridge Smart Reconciliation Matcher
Provides fuzzy attribute matching, variance categorization, and auto-resolution proposals.
"""
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from difflib import SequenceMatcher

@dataclass
class MatchCandidate:
    source_id: str
    target_id: str
    confidence_score: float
    match_type: str # EXACT, HIGH_CONFIDENCE_FUZZY, PARTIAL_NAME_MATCH
    reasons: List[str]

class SmartReconciliationMatcher:
    """Intelligent fuzzy record matcher for payroll and HRIS reconciliation."""

    @staticmethod
    def calculate_similarity(a: str, b: str) -> float:
        if not a or not b:
            return 0.0
        return SequenceMatcher(None, a.strip().lower(), b.strip().lower()).ratio()

    @classmethod
    def match_employee_record(
        cls,
        provider_record: Dict[str, Any],
        crm_records: List[Dict[str, Any]],
        threshold: float = 0.85
    ) -> Optional[MatchCandidate]:
        """Find best matching CRM employee record for an unmatched payroll line item."""
        p_email = provider_record.get("email", "").lower()
        p_name = f"{provider_record.get('first_name', '')} {provider_record.get('last_name', '')}".strip().lower()
        p_code = provider_record.get("employee_code", "").lower()

        best_score = 0.0
        best_target = None
        reasons = []

        for candidate in crm_records:
            c_email = candidate.get("email", "").lower()
            c_name = f"{candidate.get('first_name', '')} {candidate.get('last_name', '')}".strip().lower()
            c_code = candidate.get("employee_code", "").lower()

            # Exact match on email or employee code
            if p_email and c_email and p_email == c_email:
                return MatchCandidate(
                    source_id=provider_record.get("id", ""),
                    target_id=candidate.get("id", ""),
                    confidence_score=1.0,
                    match_type="EXACT_EMAIL",
                    reasons=["Exact email address match"]
                )

            if p_code and c_code and p_code == c_code:
                return MatchCandidate(
                    source_id=provider_record.get("id", ""),
                    target_id=candidate.get("id", ""),
                    confidence_score=1.0,
                    match_type="EXACT_CODE",
                    reasons=["Exact employee code match"]
                )

            # Fuzzy name comparison
            name_score = cls.calculate_similarity(p_name, c_name)
            if name_score > best_score:
                best_score = name_score
                best_target = candidate
                reasons = [f"Fuzzy name similarity score: {round(name_score * 100, 1)}%"]

        if best_target and best_score >= threshold:
            return MatchCandidate(
                source_id=provider_record.get("id", ""),
                target_id=best_target.get("id", ""),
                confidence_score=round(best_score, 3),
                match_type="HIGH_CONFIDENCE_FUZZY",
                reasons=reasons
            )

        return None

    @classmethod
    def evaluate_variance_severity(cls, expected: float, actual: float, tolerance: float = 1.0) -> Dict[str, Any]:
        """Categorize variance amount and generate auto-resolution action."""
        diff = round(abs(actual - expected), 2)
        pct_diff = round((diff / expected * 100), 2) if expected > 0 else 100.0

        if diff <= tolerance:
            severity = "NEGLIGIBLE"
            resolution = "AUTO_RESOLVE_WITHIN_TOLERANCE"
        elif diff < 50.0 and pct_diff < 5.0:
            severity = "LOW"
            resolution = "FLAG_FOR_MANAGER_REVIEW"
        elif diff < 500.0:
            severity = "MEDIUM"
            resolution = "OPEN_PAYROLL_INQUIRY_TICKET"
        else:
            severity = "CRITICAL"
            resolution = "ESCALATE_TO_PAYROLL_DIRECTOR"

        return {
            "expected_amount": expected,
            "actual_amount": actual,
            "difference": diff,
            "percentage_difference": pct_diff,
            "severity": severity,
            "suggested_action": resolution
        }
