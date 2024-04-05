import os
import random
from string import ascii_letters, digits

from dotenv import load_dotenv

load_dotenv()

# Required
BOT_TOKEN=os.getenv("BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")
CHATS_TO_CLEAN= [int(x) for x in os.getenv("CHATS_TO_CLEAN").split(" ")]

# Optional
RANDON_WEBHOOK_PATH = "".join(random.choices(list(ascii_letters + digits), k=32))
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", RANDON_WEBHOOK_PATH)

ENABLE_TGBOT = os.getenv("ENABLE_TGBOT", True)
RETRY_TIMEOUT = int(os.getenv("RETRY_TIMEOUT", 60))
