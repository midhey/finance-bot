import pytest
from sqlalchemy import text
from app.general.db import async_session


@pytest.mark.asyncio
async def test_database_connection():
    async with async_session() as session:
        result = await session.execute(text("SELECT 1"))
        assert result.scalar() == 1
