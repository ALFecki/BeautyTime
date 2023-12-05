from typing import Optional
from pydantic import BaseModel


class ReviewSchemaCreate(BaseModel):
    schedule_id: int
    client_id: int
    rating: int
    comment: Optional[str]
