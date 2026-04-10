from telegram import Update
from telegram.ext import ContextTypes
from telegram.error import TimedOut
import asyncio

from services.format import build_rates_message

URL = "https://www.cbr-xml-daily.ru/daily_json.js"

CHAT = "1110162579"


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

    text = build_rates_message()

    await wait_msg.edit_text(
        text,
        parse_mode="Markdown"
    )


async def send_daily_rates(context: ContextTypes.DEFAULT_TYPE):
    text = build_rates_message()

    for i in range(3):
        try:
            return await context.bot.send_message(
                chat_id=CHAT,
                text=text,
                parse_mode="Markdown"
            )
        except TimedOut:
            print(f"Timeout, retry {i+1}")
            await asyncio.sleep(2)
