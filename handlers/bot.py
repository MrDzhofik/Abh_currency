from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

from services.currencies import get_today_currency, get_today_metals

URL = "https://www.cbr-xml-daily.ru/daily_json.js"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.effective_message.reply_text(
        "Привет! Я слежу за курсом валют и могу предоставить курсы валют на сегодня. "
        "Для этого введи команду /get"
    )


async def get(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    wait_msg = await update.effective_message.reply_text(
        "⏳ Получаю актуальные курсы валют...\n" \
        "Пожалуйста, подождите"
    )

    today_pretty = datetime.today().strftime("%d.%m.%Y")
    today = datetime.today().strftime("%Y-%m-%d")
    currency = get_today_currency(URL)
    metals = get_today_metals(today)

    text = f"📊 *Курсы на {today_pretty}*\n\n"

    text += "💱 *Валюты:*\n"
    for name, value in currency.items():
        text += f"• {name}: {value}\n"

    text += "\n🪙 *Драгоценные металлы:*\n"
    for name, value in metals.items():
        text += f"• {name}: {value}\n"

    await wait_msg.edit_text(
        text,
        parse_mode="Markdown"
    )
