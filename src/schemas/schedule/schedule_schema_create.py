

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ScheduleSchemaCreate(BaseModel):
    client_id: int
    staff_id: int
    service_id: int
    start_date: datetime
    duration: float
    notes: Optional[str]