from pydantic import BaseModel
from sqlalchemy import DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase


class Base(DeclarativeBase):
    pass


class BaseEntity(Base):

    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    create_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
