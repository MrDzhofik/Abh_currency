import requests
import cbrapi as cbr
from datetime import datetime


# Получение курсов валют на сегодняшний день
# url - API adress
# return - dictionary
def get_today_currency(url: str) -> dict[str, float]:
    request = requests.get(url=url, timeout=5)  # Работаем со структурой JSON
    body = request.json()["Valute"]

    result = {}
    result[body['USD']['Name']] = body['USD']['Value']
    result[body['EUR']['Name']] = body['EUR']['Value']
    result[body['GBP']['Name']] = body['GBP']['Value']

    return result


# Получение курсов металлов на дату в виде словаря
# date - current date
# return - dictionary
def get_today_metals(date: str) -> dict[str, float]:
    print(date)
    metals = cbr.get_metals_prices(date)

    result = {}
    result['Золото'] = float(metals['GOLD'][date])
    result['Серебро'] = float(metals['SILVER'][date])
    result['Платина'] = float(metals['PLATINUM'][date])
    result['Палладий'] = float(metals['PALLADIUM'][date])

    return result
