from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ProductSchemaUpdate(BaseModel):
    name: Optional[str]
    alias: Optional[str]
    quantity: Optional[int]
    supply_date: Optional[datetime]
    client_cost: Optional[float]
    supply_cost: Optional[float]
    cost_diff: Optional[float]