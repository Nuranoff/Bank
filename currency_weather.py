usd_to_rub = 73.5
usd_to_eur = 0.85

def convert_currency(amount, from_currency, to_currency):
    if from_currency == 'USD' and to_currency == 'RUB':
        return amount * usd_to_rub
    elif from_currency == 'USD' and to_currency == 'EUR':
        return amount * usd_to_eur
    elif from_currency == 'RUB' and to_currency == 'USD':
        return amount / usd_to_rub
    elif from_currency == 'EUR' and to_currency == 'USD':
        return amount / usd_to_eur
    elif from_currency == 'RUB' and to_currency == 'EUR':
        return amount / usd_to_rub * usd_to_eur
    elif from_currency == 'EUR' and to_currency == 'RUB':
        return amount / usd_to_eur * usd_to_rub
    else:
        return None

amount = float(input("Введите сумму: "))
from_currency = input("Введите исходную валюту (USD, RUB, EUR): ").upper()
to_currency = input("Введите целевую валюту (USD, RUB, EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)

if result is not None:
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
else:
    print("Конвертация этой валютной пары не поддерживается.")
