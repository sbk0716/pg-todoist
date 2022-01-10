from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime, timedelta, timezone
from enum import IntEnum

JST = timezone(timedelta(hours=+9), "JST")


# ====================
# StatusType
# ====================
class StatusType(IntEnum):
    """
    StatusType Class
    """

    todo = 1
    doing = 2
    pending = 3
    review = 4


# ====================
# TaskBase
# ====================
class TaskBase(BaseModel):
    """
    TaskBase Class
    This class inherits from Pydantic BaseModel.
    """

    title: Optional[str] = Field(None, example="打ち合わせ")
    detail: Optional[str] = Field(None, example="今週の金曜日の13時からT社のUさんと打ち合わせを行う。")
    # status_type: Optional[StatusType] = Field(StatusType.todo, example="1", description="TODO=1|DOING=2|PENDING=3|REVIEW=4")


# ====================
# TaskDateTime
# ====================
class TaskDateTime(BaseModel):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    @validator("created_at", "updated_at", pre=True)
    def default_datetime(cls, value: datetime) -> datetime:
        return value or datetime.datetime.now(JST)


# ====================
# Task | Read
# ====================
class TaskRead(TaskBase, TaskDateTime):
    """
    TaskDoneRead Class
    This class inherits from TaskBase.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int

    class Config:
        orm_mode = True


# ====================
# TaskDone | Read
# ====================
class TaskDoneRead(TaskBase, TaskDateTime):
    """
    TaskDoneRead Class
    This class inherits from TaskBase.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int
    done: bool = Field(False, example="false", description="完了フラグ")

    class Config:
        orm_mode = True


# ====================
# Task | Create
# ====================
class TaskCreate(TaskBase):
    """
    TaskCreate Class
    This class inherits from TaskBase.
    """

    pass


# ====================
# Task | Update
# ====================
class TaskUpdate(TaskBase):
    """
    TaskUpdate Class
    This class inherits from TaskBase.
    """

    pass
