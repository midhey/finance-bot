from app.general.db import async_session
from app.general.redis import redis
from app.config import load_config
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import async_sessionmaker


class AppState:
    def __init__(self):
        self.config = load_config()
        self.db: async_sessionmaker = async_session
        self.redis: Redis = redis


state = AppState()
