from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Enum, ForeignKey


class Wallet(Base):
    __tablename__ = "wallets"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    type: Mapped[str] = mapped_column(
        Enum("cash", "card", "deposit", "crypto", name="wallet_type")
    )
    balance: Mapped[float] = mapped_column(Float, default=0.0)
