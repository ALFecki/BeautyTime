from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity

class Log(BaseEntity):
    __tablename__ = "log"
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    info: Mapped[str] = mapped_column(Text, nullable=True)
