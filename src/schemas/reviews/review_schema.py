from typing import Optional
from base.base_schema import BaseSchema
from schemas.client.client_schema import ClientSchema
from schemas.schedule.schedule_schema import ScheduleSchema

class ReviewSchema(BaseSchema):
    schedule_id: int
    client_id: int
    rating: int
    comment: Optional[str]
    client: ClientSchema
    schedule: ScheduleSchema