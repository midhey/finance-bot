import sys
import os
import asyncio
from logging.config import fileConfig

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from alembic import context
from app.general.db import engine
from app.models import Base

config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def do_run_migrations(sync_connection):
    context.configure(connection=sync_connection, target_metadata=target_metadata)
    context.run_migrations()


async def run_migrations_online():
    async with engine.begin() as conn:
        await conn.run_sync(do_run_migrations)


asyncio.run(run_migrations_online())
