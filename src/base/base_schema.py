

from typing import Optional

from pydantic import BaseModel


class BaseSchema(BaseModel):
    id: Optional[int]

    class Config:
        use_enum_values = True
        orm_mode = True