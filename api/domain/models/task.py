from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP, DateTime, text
from sqlalchemy.sql.functions import current_timestamp
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, validator
from sqlalchemy.sql import func

# Import relationship function
from sqlalchemy.orm import relationship
import enum
from typing import Optional
from sqlalchemy.orm import declarative_base

JST = timezone(timedelta(hours=+9), "JST")

Base = declarative_base()


class StatusType(int, enum.Enum):
    """
    StatusType Class
    Inherit Enum class.
    """

    todo = 1
    doing = 2
    pending = 3
    review = 4


class Task(Base):
    """
    Task Class
    Inherit declarative base class.
    """

    # Define table name
    __tablename__ = "tasks"

    # PK
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024), nullable=False)
    detail = Column(String(4096), nullable=False)
    # created_date = Column("created_date", DateTime, default=func.now(), nullable=True)
    # status_type = Column("status_type", Enum(StatusType), nullable=False)
    created_at = Column(
        "created_at",
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=current_timestamp(),
    )
    updated_at = Column(
        "updated_at",
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=current_timestamp(),
    )
    # created_at = Column(
    #     "created_at",
    #     TIMESTAMP(timezone=True),
    #     nullable=False,
    #     server_default=current_timestamp(),
    # )
    # updated_at = Column(
    #     "updated_at",
    #     TIMESTAMP(timezone=True),
    #     nullable=False,
    #     server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    # )

    # ================================================================================
    # execute relationship function | sqlalchemy.orm.relationship()
    # ================================================================================
    # Provide a relationship between two mapped classes.
    # Allows Task object references from Done object.
    done = relationship("Done", back_populates="task")


class Done(Base):
    """
    Done Class
    Inherit declarative base class.
    """

    # Define table name
    __tablename__ = "dones"

    # PK&FK: Defines a dependency between two columns.(tasks.id <--> dones.id)
    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True, autoincrement=True)
    created_at = Column(
        "created_at",
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=current_timestamp(),
    )
    updated_at = Column(
        "updated_at",
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=current_timestamp(),
    )
    # created_at = Column(
    #     "created_at",
    #     TIMESTAMP(timezone=True),
    #     nullable=False,
    #     server_default=current_timestamp(),
    # )
    # updated_at = Column(
    #     "updated_at",
    #     TIMESTAMP(timezone=True),
    #     nullable=False,
    #     server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    # )

    # ================================================================================
    # execute relationship function | sqlalchemy.orm.relationship()
    # ================================================================================
    # Provide a relationship between two mapped classes.
    # Allows Done object references from Task object.
    task = relationship("Task", back_populates="done")
