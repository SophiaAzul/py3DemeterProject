import requests

BASE_CURRENCY = "USD"

CURRENCIES = ["USD", "CAD", "CHF", "CNY", "EUR", "GBP", "HKD", "INR", "JPY", "PHP"]

ENDPOINT = "https://api.exchangerate.host/latest"

params = {"base": BASE_CURRENCY, "symbols": ",".join(CURRENCIES)}

response = requests.get(ENDPOINT, params=params)

exchange_rates = {}
for currency in CURRENCIES:
    exchange_rate = response.json()["rates"][currency]
    exchange_rates[currency] = float(exchange_rate)

print(exchange_rates)
