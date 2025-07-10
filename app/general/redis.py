from redis.asyncio import Redis
from app.config import load_config

config = load_config()

redis = Redis(
    host=config.redis.host,
    port=config.redis.port,
    decode_responses=True,
)
