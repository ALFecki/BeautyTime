from typing import Optional

from pydantic import BaseModel
from base.base_schema import BaseSchema


class SupplySchemaCreate(BaseModel):
    product_id: int
    type: Optional[int]
    quantity: int
    sum: float