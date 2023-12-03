
from sqlalchemy import String, Text, REAL
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity

class Service(BaseEntity):
    __tablename__ = "service"

    name: Mapped[str] = mapped_column(String(30), nullable=False)
    alias: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    cost: Mapped[float] = mapped_column(REAL, nullable=False)