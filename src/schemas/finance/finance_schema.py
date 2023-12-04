

from datetime import datetime
from typing import Optional
from base.base_schema import BaseSchema


class FinanceSchema(BaseSchema):
    type: str
    sum: float
    date: datetime
    sale_id: Optional[int]
    schedule_id: Optional[int]
    supply_id: Optional[int]
    notes: Optional[str]