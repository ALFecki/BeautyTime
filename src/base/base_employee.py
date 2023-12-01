from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.base.base_model import BaseEntity

class BaseEmployee(BaseEntity):
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    second_name: Mapped[str] = mapped_column(String(20), nullable=False)
    phone: Mapped[str] = mapped_column(String(17), nullable=True)