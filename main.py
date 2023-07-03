
print("This currency value is applicable only for 7/3/2023.")

exchange_rates = {
    'USD': {'BDT': 108.23, 'EUR': 0.92, 'CNY': 7.18, 'RUB': 84.18},
    'BDT': {'USD': 0.0092, 'EUR': 0.0085, 'CNY': 0.067, 'RUB': 0.79},
    'EUR': {'USD': 1.09, 'BDT': 117.55, 'CNY': 7.85, 'RUB': 92.52},
    'CNY': {'USD': 0.14, 'BDT': 14.97, 'EUR': 0.13, 'RUB': 11.79},
    'RUB': {'USD': 0.012, 'BDT': 1.29, 'EUR': 0.011, 'CNY': 0.086}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount

    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        conversion_rate = exchange_rates[from_currency][to_currency]
        converted_amount = amount * conversion_rate
        return converted_amount

    return None

print("Supported conversion : USD/BDT/EUR/CNY/RUB : ")
amount = float(input("Enter the amount to convert : "))
from_currency = input("Enter the currency to convert from : ").upper()
to_currency = input("Enter the currency to convert to : ").upper()


converted_amount = convert_currency(amount, from_currency, to_currency)


if converted_amount:
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
else:
    print("Conversion failed. Please try again.")
