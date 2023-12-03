from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProductSchemaCreate(BaseModel):
    name: str
    alias: str
    quantity: int
    supply_date: Optional[datetime]
    client_cost: float
    supply_cost: float
    cost_diff: float