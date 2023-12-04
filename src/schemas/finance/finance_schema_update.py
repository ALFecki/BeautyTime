
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FinanceSchemaUpdate(BaseModel):
    type: Optional[str]
    sum: Optional[float]
    date: Optional[datetime]
    sale_id: Optional[int]
    schedule_id: Optional[int]
    supply_id: Optional[int]
    notes: Optional[str]