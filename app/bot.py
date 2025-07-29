from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.fsm.storage.redis import RedisStorage

from app.general.state import state
from app.config import settings
from app.middlewares.db_session import DBSessionMiddleware

from app.handlers.group import group_router


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(storage=RedisStorage(state.redis))

dp.message.middleware(DBSessionMiddleware(state.db))
dp.callback_query.middleware(DBSessionMiddleware(state.db))

dp.include_router(group_router)


async def handle_update(data: dict):
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
