from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.base.base_employee import BaseEmployee

class Staff(BaseEmployee):
    __tablename__ = "staff"

    position: Mapped[str] = mapped_column(String(20), nullable=True)