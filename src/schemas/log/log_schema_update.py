from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class LogSchemaUpdate(BaseModel):
    date: Optional[datetime]
    client_id: Optional[int]
    info: Optional[str]
