from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from integration_platform.canonical.models import (
    CanonicalEmployee, CanonicalCompensation, CanonicalPayrollRun, CanonicalPayrollResult
)

class BasePayrollAdapter(ABC):
    """Unified Base Contract for all external Payroll Provider Adapters."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    async def test_connection(self) -> bool:
        """Verify API keys/tokens and connectivity to provider."""
        pass

    @abstractmethod
    async def get_employees(() -> List[CanonicalEmployee]:
        """Fetch all employees transformed into canonical model."""
        pass

    @abstractmethod
    async def get_employee(self, external_id: str) -> Optional[CanonicalEmployee]:
        """Fetch single employee transformed into canonical model."""
        pass

    @abstractmethod
    async def get_payroll_runs(self, limit: int = 50) -> List[CanonicalPayrollRun]:
        """Fetch pay runs from external provider."""
        pass

    @abstractmethod
    async def get_payroll_results(self, payroll_run_id: str) -> List[CanonicalPayrollResult]:
        """Fetch detailed pay run line item results per employee."""
        pass

    @abstractmethod
    async def process_webhook(self, payload: Dict[str, Any], headers: Dict[str, str]) -> Dict[str, Any]:
        """Process incoming provider webhooks."""
        pass
