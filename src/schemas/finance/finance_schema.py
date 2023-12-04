

from datetime import datetime
from typing import Optional
from base.base_schema import BaseSchema
from schemas.sale.sale_schema import SaleSchema
from schemas.schedule.schedule_schema import ScheduleSchema
from schemas.supply.supply_schema import SupplySchema


class FinanceSchema(BaseSchema):
    type: str
    sum: float
    date: datetime
    sale_id: Optional[int]
    schedule_id: Optional[int]
    supply_id: Optional[int]
    notes: Optional[str]

    sale: Optional[SaleSchema] = None
    schedule: Optional[ScheduleSchema] = None
    supply: Optional[SupplySchema] = None