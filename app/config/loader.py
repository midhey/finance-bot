import os
from dotenv import load_dotenv
from .base import DBConfig, BotConfig, Config

load_dotenv()


def require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def load_config() -> Config:
    return Config(
        bot=BotConfig(token=require_env("BOT_TOKEN")),
        db=DBConfig(
            host=require_env("DB_HOST"),
            port=int(require_env("DB_PORT")),
            root_password=require_env("DB_ROOT_PASSWORD"),
            name=require_env("DB_NAME"),
            user=require_env("DB_USER"),
            password=require_env("DB_PASSWORD"),
        ),
    )
