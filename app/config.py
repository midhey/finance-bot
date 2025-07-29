from pydantic_settings import BaseSettings
from pydantic import Field, AnyUrl


class Settings(BaseSettings):
    BOT_TOKEN: str = Field(..., env="BOT_TOKEN")
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: int = Field(..., env="DB_PORT")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_ROOT_PASSWORD: str = Field(..., env="DB_ROOT_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    REDIS_HOST: str = Field(..., env="REDIS_HOST")
    REDIS_PORT: int = Field(..., env="REDIS_PORT")
    WEBHOOK_HOST: AnyUrl = Field(..., env="WEBHOOK_HOST")
    WEBHOOK_PATH: str = Field(..., env="WEBHOOK_PATH")
    WEBHOOK_PORT: int = Field(..., env="WEBHOOK_PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def webhook_url(self) -> str:
        host = str(self.WEBHOOK_HOST).rstrip("/")
        return f"{host}{self.WEBHOOK_PATH}"


settings = Settings()
