from __future__ import annotations

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src import settings
from src.services.telegram.botfather.bot import activate_botfather_bot
from src.services.telegram.botfather.bot import disable_botfather_bot
from src.services.telegram.botfather.routing import webhook_api_router

logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'], )


@app.get('/')
async def root():
    return {'status': 'ok'}


@app.on_event('startup')
async def on_startup():
    logger.info('Starting up actions')
    if settings.ENABLE_TGBOT:
        app.include_router(webhook_api_router)
        await activate_botfather_bot()


@app.on_event('shutdown')
async def on_shutdown():
    await disable_botfather_bot()
