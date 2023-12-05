from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class LogSchemaCreate(BaseModel):
    date: datetime
    client_id: int
    info: Optional[str]
