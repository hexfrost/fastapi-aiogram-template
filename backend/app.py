import logging

from aiogram import Bot, Dispatcher, Router, types
from aiogram.methods import DeleteMessage

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from . import settings

logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
webhook_api_router = APIRouter()
app.include_router(webhook_api_router)

bot = Bot(token=settings.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
messages_handler = Router()
TELEGRAM_WEBHOOK_URL = f"{settings.WEBHOOK_DOMAIN}/webhook"


@webhook_api_router.post("/webhook")
async def telegram_webhook(request: dict):
    update = types.Update(**request)
    await dp.feed_update(bot=bot, update=update)


@app.get("/")
async def root():
    return {"status": "ok"}


async def register_webhook():
    await bot.set_webhook(url=f"{settings.WEBHOOK_DOMAIN}/webhook")
    webhook_info = await bot.get_webhook_info()
    logger.info(f"""Webhook info: {webhook_info}""")


@messages_handler.message()
async def delete_messages_handler(message: types.Message):
    await message.reply("Hello from messages_handler")


@app.on_event("startup")
async def on_startup():
    logger.info("Starting up actions")
    await register_webhook()
    dp.include_router(messages_handler)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
