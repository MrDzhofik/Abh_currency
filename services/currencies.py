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
    result[body['USD']['Name']] = round(body['USD']['Value'], 2)
    result[body['EUR']['Name']] = round(body['EUR']['Value'], 2)
    result[body['GBP']['Name']] = round(body['GBP']['Value'], 2)

    return result


# Получение курсов металлов на дату в виде словаря
# date - current date
# return - dictionary
def get_today_metals(date: str) -> dict:
    print(date)
    metals = cbr.get_metals_prices(date)

    result = {}

    try:
        result['Золото'] = round(float(metals['GOLD'][date]), 2)
        result['Серебро'] = round(float(metals['SILVER'][date]), 2)
        result['Платина'] = round(float(metals['PLATINUM'][date]), 2)
        result['Палладий'] = round(float(metals['PALLADIUM'][date]), 2)
    except KeyError:
        result['Ошибка'] = 'Не удалось получить курс металлов'

    return result
