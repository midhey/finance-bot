from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from app.config import load_config


config = load_config()

DATABASE_URL = (
    f"mysql+aiomysql://{config.db.user}:{config.db.password}"
    f"@{config.db.host}:{config.db.port}/{config.db.name}"
)


engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    echo=True,
)


async_session: async_sessionmaker[AsyncSession] = async_sessionmaker(
    engine, expire_on_commit=False
)
