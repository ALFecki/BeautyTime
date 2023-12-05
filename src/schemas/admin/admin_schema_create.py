

from pydantic import BaseModel


class AdminSchemaCreate(BaseModel):
    user_id: int
    unique_id: str