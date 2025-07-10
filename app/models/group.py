from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
