from datetime import datetime, timedelta

from services.currencies import get_today_currency, get_today_metals

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


def build_rates_message():
    '''
        Get the rates and format
    '''
    today_pretty = datetime.today().strftime("%d.%m.%Y")
    today = datetime.today().strftime("%Y-%m-%d")

    yesterday = (datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d")

    currency = get_today_currency(URL)
    metals = get_today_metals(today, yesterday)

    text = f"📊 *Курсы на {today_pretty}*\n\n"

    text += "💱 *Валюты:*\n"
    for name, value in currency.items():
        text += f"• {name}: {value}\n"

    if metals.get("Ошибка"):
        text += f"\n{metals['Ошибка']}"
    else:
        text += "\n🪙 *Драгоценные металлы:*\n"
        for name, value in metals.items():
            text += f"• {name}: {value}\n"

    return text
