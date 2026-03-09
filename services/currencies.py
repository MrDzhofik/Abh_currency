import requests
import cbrapi as cbr


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
def get_today_metals(today: str, yesterday: str) -> dict:
    metals = cbr.get_metals_prices(yesterday, today)

    if metals is None or metals.empty:
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"Error at {today}: {metals}\n")

        return {"Ошибка": "Не удалось получить курс металлов"}

    row = metals.iloc[-1]

    return {
        "Золото": round(float(row["GOLD"]), 2),
        "Серебро": round(float(row["SILVER"]), 2),
        "Платина": round(float(row["PLATINUM"]), 2),
        "Палладий": round(float(row["PALLADIUM"]), 2),
    }
