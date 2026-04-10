import os
import dotenv
from datetime import time
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.bot import start, get, send_daily_rates
from telegram.request import HTTPXRequest

PORT = int(os.environ.get("PORT", 10000))

dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

request = HTTPXRequest(
    connect_timeout=20,
    read_timeout=20
)


def main():
    application = ApplicationBuilder().token(TOKEN).request(request).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get", get))
    application.job_queue.run_daily(
        send_daily_rates,
        time=time(hour=18, minute=0)
    )

    application.run_polling()


if __name__ == "__main__":
    main()
