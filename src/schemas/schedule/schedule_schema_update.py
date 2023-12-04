
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ScheduleSchemaUpdate(BaseModel):
    client_id: Optional[int]
    staff_id: Optional[int]
    service_id: Optional[int]
    start_date: Optional[datetime]
    duration: Optional[float]
    notes: Optional[str]