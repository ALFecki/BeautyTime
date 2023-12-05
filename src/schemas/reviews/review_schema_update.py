from typing import Optional
from pydantic import BaseModel


class ReviewSchemaUpdate(BaseModel):
    schedule_id: Optional[int]
    client_id: Optional[int]
    rating: Optional[int]
    comment: Optional[str]
