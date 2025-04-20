from __future__ import annotations

from aiogram import Router
from aiogram import types

messages_handler = Router()


@messages_handler.message()
async def delete_messages_handler(message: types.Message):
    await message.reply('Hello from FastAPI template')
