import requests
import json

def transferwise(money, currency_in, currency_out):
    currencies = {"EUR":1, "GBP":2, "USD":3}
    s = requests.Session()
    s.get("https://transferwise.com")
    data = {
        "fixType": "SOURCE",
        "sourceValue": money,
        "sourceCurrencyId": currencies[currency_in],
        "targetCurrencyId": currencies[currency_out]
    }
    r = s.post("https://transferwise.com/request/initiatePageRate?calculatorView=1&lang=en&invertSavings=", data=data).json()
    print r
    return float(str(r['targetValue']).replace(",", ""))

def azimo(money, currency_in, currency_out):
print transferwise(200, "EUR", "USD")