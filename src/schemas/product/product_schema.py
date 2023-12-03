from datetime import datetime
from base.base_schema import BaseSchema

class ProductSchema(BaseSchema):
    name: str
    alias: str
    quantity: int
    supply_date: datetime
    client_cost: float
    supply_cost: float
    cost_diff: float