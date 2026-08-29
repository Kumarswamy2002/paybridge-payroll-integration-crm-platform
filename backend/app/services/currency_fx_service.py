"""
Multi-Currency FX Conversion & Cross-Border Payroll Service
"""
from decimal import Decimal
from typing import Dict, Any

class CurrencyFXService:
    BASE_RATES_TO_USD = {
        "USD": Decimal("1.0"),
        "EUR": Decimal("1.08"),
        "GBP": Decimal("1.26"),
        "CAD": Decimal("0.74"),
        "INR": Decimal("0.012")
    }

    @classmethod
    def convert_amount(cls, amount: float, from_currency: str, to_currency: str = "USD") -> Dict[str, Any]:
        amt = Decimal(str(amount))
        from_rate = cls.BASE_RATES_TO_USD.get(from_currency.upper(), Decimal("1.0"))
        to_rate = cls.BASE_RATES_TO_USD.get(to_currency.upper(), Decimal("1.0"))

        usd_val = amt * from_rate
        converted = usd_val / to_rate

        return {
            "original_amount": float(amt),
            "from_currency": from_currency.upper(),
            "to_currency": to_currency.upper(),
            "converted_amount": float(round(converted, 2)),
            "effective_rate": float(round(from_rate / to_rate, 4))
        }
