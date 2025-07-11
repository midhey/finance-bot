from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, BigInteger, Integer, DateTime, func, UniqueConstraint
from datetime import datetime


class GroupUser(Base):
    __tablename__ = "group_users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    joined_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    __table_args__ = (UniqueConstraint("user_id", "group_id", name="uix_user_group"),)
