from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from src.base.base_model import BaseEntity

class Sale(BaseEntity):
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    sale_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)