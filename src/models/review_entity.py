from sqlalchemy import ForeignKey, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity

class Review(BaseEntity):
    __tablename__ = "review"
    schedule_id: Mapped[int] = mapped_column(ForeignKey("schedule.id"), nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=True)