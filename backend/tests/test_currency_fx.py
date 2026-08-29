from backend.app.services.currency_fx_service import CurrencyFXService

def test_currency_conversion_eur_to_usd():
    res = CurrencyFXService.convert_amount(1000.0, "EUR", "USD")
    assert res["converted_amount"] == 1080.0

def test_currency_conversion_usd_to_inr():
    res = CurrencyFXService.convert_amount(100.0, "USD", "INR")
    assert res["converted_amount"] > 8000.0
