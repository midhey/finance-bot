from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, Boolean, ForeignKey


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    name: Mapped[str] = mapped_column(String(100))
    is_fixed: Mapped[bool] = mapped_column(default=False)
    monthly_limit: Mapped[float | None] = mapped_column(nullable=True)
