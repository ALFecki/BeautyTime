from sqlalchemy import REAL, DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from src.base.base_model import BaseEntity

class Schedule(BaseEntity):
    __tablename__ = "schedule"

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    staff_id: Mapped[int] = mapped_column(ForeignKey("staff.id"), nullable=True)
    service_id: Mapped[int] = mapped_column(ForeignKey("service.id"), nullable=False)
    start_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    duration: Mapped[REAL] = mapped_column(REAL, nullable=False)
    notes: Mapped[str] = mapped_column(Text, nullable=True)