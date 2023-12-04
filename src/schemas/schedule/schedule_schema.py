from datetime import datetime
import repositories.client_repository
from base.base_schema import BaseSchema
from typing import Optional
from schemas.service.service_schema import ServiceSchema
from schemas.staff.staff_schema import StaffSchema
from schemas.client.client_schema import ClientSchema


class ScheduleSchema(BaseSchema):
    client_id: int
    staff_id: int
    service_id: int
    start_date: datetime
    duration: float
    notes: Optional[str]

    service: ServiceSchema
    staff: StaffSchema
    client: ClientSchema