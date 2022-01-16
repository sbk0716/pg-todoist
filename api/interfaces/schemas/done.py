from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")

# ====================
# DoneBase
# ====================
class DoneBase(BaseModel):
    """
    DoneBase Class
    This class inherits from Pydantic BaseModel.
    """

    pass


# ====================
# DoneDateTime
# ====================
class DoneDateTime(BaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.datetime.now(JST)


# ====================
# DoneRead | Read
# ====================
class DoneRead(DoneBase, DoneDateTime):
    """
    DoneRead Class
    This class inherits from TaskBase.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int
    note: Optional[str] = Field(None, example="Record created by create_done method | ID: 1")

    class Config:
        orm_mode = True
