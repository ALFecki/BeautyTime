from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.base.base_model import BaseEntity


class User(BaseEntity):
    __tablename__ = "user"

    login: Mapped[str] = mapped_column(String(30), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)