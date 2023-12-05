from datetime import datetime
from typing import Optional
from base.base_schema import BaseSchema
from schemas.client.client_schema import ClientSchema

class LogSchema(BaseSchema):
    date: datetime
    client_id: int
    info: Optional[str]
    client: ClientSchema