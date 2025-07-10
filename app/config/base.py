from dataclasses import dataclass


@dataclass
class DBConfig:
    host: str
    port: int
    root_password: str
    name: str
    user: str
    password: str


@dataclass
class BotConfig:
    token: str


@dataclass
class RedisConfig:
    host: str
    port: int


@dataclass
class Config:
    bot: BotConfig
    db: DBConfig
    redis: RedisConfig
