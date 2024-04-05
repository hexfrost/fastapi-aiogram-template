import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_DOMAIN = os.getenv("BASE_DOMAIN")

ENABLE_TGBOT = os.getenv("ENABLE_TGBOT", True)
RETRY_TIMEOUT = int(os.getenv("RETRY_TIMEOUT", 60))
