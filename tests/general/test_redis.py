import pytest
from app.general.redis import redis


@pytest.mark.asyncio
async def test_redis_connection():
    key = "test:redis:key"
    value = "hello"

    await redis.set(key, value, ex=10)
    result = await redis.get(key)

    assert result == value

    await redis.delete(key)
    assert await redis.get(key) is None
