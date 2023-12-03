from sqlalchemy import REAL, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity

class Product(BaseEntity):
    __tablename__ = 'product'

    name: Mapped[str] = mapped_column(String, nullable=False)
    alias: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    supply_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    client_cost: Mapped[REAL] = mapped_column(REAL, nullable=False)
    supply_cost: Mapped[REAL] = mapped_column(REAL, nullable=False)
    cost_diff: Mapped[REAL] = mapped_column(REAL, nullable=False)