from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from base.base_employee import BaseEmployee

class Client(BaseEmployee):
    __tablename__ = "client"

    surname: Mapped[str] = mapped_column(String(20), nullable=True)