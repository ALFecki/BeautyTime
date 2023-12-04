from sqlalchemy import REAL, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from base.base_model import BaseEntity


class Supply(BaseEntity):
    __tablename__ = "supply"

    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), nullable=False)
    type: Mapped[int] = mapped_column(Integer, nullable=True)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    sum: Mapped[REAL] = mapped_column(REAL, nullable=False)
