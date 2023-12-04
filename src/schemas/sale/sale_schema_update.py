from datetime import datetime
from typing import Optional
from base.base_schema import BaseSchema


class SaleSchemaUpdate(BaseSchema):
    client_id: Optional[int]
    product_id: Optional[int]
    quantity: Optional[int]
    sale_date: Optional[datetime]