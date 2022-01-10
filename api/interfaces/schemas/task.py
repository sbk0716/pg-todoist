# Import pydantic
# https://pydantic-docs.helpmanual.io/
from pydantic import BaseModel, Field, validator

# Import typing
# https://docs.python.org/3/library/typing.html
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
# Task | Read
# ====================
class TaskRead(TaskBase):
    """
    TaskRead Class
    This class inherits from TaskBase.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int
    done: bool = Field(False, description="完了フラグ")
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

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


class TaskCreateResponse(TaskCreate):
    """
    TaskCreateResponse Class
    This class inherits from TaskCreate.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# ====================
# Task | Update
# ====================
class TaskUpdate(TaskBase):
    """
    TaskUpdate Class
    This class inherits from TaskBase.
    """

    pass


class TaskUpdateResponse(TaskUpdate):
    """
    TaskUpdateResponse Class
    This class inherits from TaskUpdate.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# ====================
# Task | Delete
# ====================
class TaskDelete(TaskBase):
    """
    TaskDelete Class
    This class inherits from TaskBase.
    """

    pass


class TaskDeleteResponse(TaskDelete):
    """
    TaskDeleteResponse Class
    This class inherits from TaskDelete.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
