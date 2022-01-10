# Import pydantic
# https://pydantic-docs.helpmanual.io/
from pydantic import BaseModel, Field

# Import typing
# https://docs.python.org/3/library/typing.html
from typing import Optional


# ====================
# Done | Create
# ====================
class DoneCreateResponse(BaseModel):
    """
    DoneCreateResponse Class
    This class inherits from BaseModel.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    message: Optional[str] = Field(None, example="create_done | ID: 1")

    class Config:
        orm_mode = True


# ====================
# Done | Delete
# ====================
class DoneDeleteResponse(BaseModel):
    """
    DoneDeleteResponse Class
    This class inherits from BaseModel.
    Enable ORM mode to convert a DB model instance to a schema instance.
    """

    message: Optional[str] = Field(None, example="delete_done | ID: 1")

    class Config:
        orm_mode = True
