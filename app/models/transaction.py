from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Float, String, Boolean, ForeignKey, DateTime, Enum
from datetime import timezone, datetime
from typing import Optional


def utcnow():
    return datetime.now(timezone.utc)


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)

    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    wallet_id: Mapped[int] = mapped_column(ForeignKey("wallets.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    user_id: Mapped[int]
    amount: Mapped[float]

    type: Mapped[str] = mapped_column(
        Enum("income", "expense", "transfer", name="transaction_type"),
        default="expense",
    )

    description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=utcnow, onupdate=utcnow)
