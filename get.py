import requests
import json
import cbrapi as cbr
from datetime import datetime

TODAY = datetime.today().strftime("%Y-%m-%d")
URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_today_currency(url: str) -> str:
    request = requests.get(url=URL)  # Работаем со структурой JSON
    body = request.json()["Valute"]

    result = f"USD: {body['USD']}\n"
    result += f"EUR: {body['EUR']}\n"
    result += f"GBR: {body['GBP']}\n"

    return result


def get_today_metals(date: str) -> str:
    metals = cbr.get_metals_prices(TODAY)

    gold = metals["GOLD"]
    silver = metals["SILVER"]

    print(gold, silver)

    result = f"Metals:\n{metals}"  # Работаем со структурой из библиотеки pandas

    return result


print(get_today_currency(URL))
print(get_today_metals(TODAY))
