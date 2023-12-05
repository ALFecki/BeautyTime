from typing import Optional
from src.base.base_schema import BaseSchema
from src.schemas.client.client_schema import ClientSchema
from src.schemas.schedule.schedule_schema import ScheduleSchema

class ReviewSchema(BaseSchema):
    schedule_id: int
    client_id: int
    rating: int
    comment: Optional[str]
    client: ClientSchema
    schedule: ScheduleSchema