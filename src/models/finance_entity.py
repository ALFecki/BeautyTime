from sqlalchemy import REAL, DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from src.base.base_model import BaseEntity

class Finance(BaseEntity):
    type: Mapped[str] = mapped_column(String, nullable=False)
    sum: Mapped[REAL] = mapped_column(REAL, nullable=False)
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    sale_id: Mapped[int] = mapped_column(ForeignKey("sale.id"), nullable=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), nullable=True)
    supply_id: Mapped[int] = mapped_column(ForeignKey("supply.id"), nullable=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)