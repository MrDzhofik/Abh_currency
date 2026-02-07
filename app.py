import os
import dotenv
import threading
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.bot import start, get
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 10000))

dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


# Простая "заглушка" HTTP-сервера, чтобы Render видел порт
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")


def run_http_server():
    httpd = HTTPServer(("0.0.0.0", PORT), Handler)
    httpd.serve_forever()


def main():
    threading.Thread(target=run_http_server, daemon=True).start()

    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get", get))

    application.run_polling()


if __name__ == "__main__":
    main()
