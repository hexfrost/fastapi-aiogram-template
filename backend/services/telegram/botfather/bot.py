import logging

from aiogram import Dispatcher, Bot

from backend import settings
from backend.services.telegram.botfather.handlers import messages_handler


logger = logging.getLogger(__name__)
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


async def register_webhook():
    await bot.set_webhook(url=f"{settings.BASE_DOMAIN}/webhook")
    webhook_info = await bot.get_webhook_info()
    logger.info(f"""Webhook info: {webhook_info}""")


async def activate_botfather_bot():

    dp.include_router(messages_handler)
    await register_webhook()


async def disable_botfather_bot():
    await bot.session.close()


async def update_feed_botfather(update):
    await dp.feed_update(bot=bot, update=update)
