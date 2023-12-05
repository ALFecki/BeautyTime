from typing import Optional

from pydantic import BaseModel


class AdminSchemaUpdate(BaseModel):
    user_id: Optional[int]
    unique_id: Optional[str]