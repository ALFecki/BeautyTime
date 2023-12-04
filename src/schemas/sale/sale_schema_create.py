from datetime import datetime
from base.base_schema import BaseSchema


class SaleSchemaCreate(BaseSchema):
    client_id: int
    product_id: int
    quantity: int
    sale_date: datetime