from aiogram import types
from fastapi import APIRouter

from backend.services.telegram.botfather.bot import update_feed_botfather

webhook_api_router = APIRouter()


@webhook_api_router.post("/webhook")
async def telegram_webhook(request: dict):
    update = types.Update(**request)
    await update_feed_botfather(update)
