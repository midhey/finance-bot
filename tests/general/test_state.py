import pytest
from sqlalchemy import text
from app.general.state import state


@pytest.mark.asyncio
async def test_state_container():
    # Redis
    key = "test:state:redis"
    value = "ping"
    await state.redis.set(key, value, ex=10)
    redis_result = await state.redis.get(key)
    assert redis_result == value
    await state.redis.delete(key)

    # MySQL
    async with state.db() as session:
        result = await session.execute(text("SELECT 1"))
        db_result = result.scalar()
        assert db_result == 1
