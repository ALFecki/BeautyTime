from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FinanceSchemaCreate(BaseModel):
    type: str
    sum: float
    date: datetime
    sale_id: Optional[int]
    schedule_id: Optional[int]
    supply_id: Optional[int]
    notes: Optional[str]
