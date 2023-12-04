from typing import Optional

from pydantic import BaseModel


class SupplySchemaUpdate(BaseModel):
    product_id: Optional[int]
    type: Optional[int]
    quantity: Optional[int]
    sum: Optional[float]
