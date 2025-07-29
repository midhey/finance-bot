from app.general.db import async_session
from app.general.redis import redis
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import async_sessionmaker
from app.config import settings


class AppState:
    def __init__(self):
        self.config = settings
        self.db: async_sessionmaker = async_session
        self.redis: Redis = redis


state = AppState()
