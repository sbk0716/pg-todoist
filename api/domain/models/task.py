from sqlalchemy import Column, Integer, String, Enum, ForeignKey, TIMESTAMP, DateTime, text
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship, registry
from datetime import timedelta, timezone
import enum
from sqlalchemy.orm import declarative_base

JST = timezone(timedelta(hours=+9), "JST")

# ================================================================================
# Execute __init__ method | sqlalchemy.orm.registry.__init__()
# ================================================================================
# Construct a new registry
mapper_registry = registry()

# ================================================================================
# Execute generate_base method | method sqlalchemy.orm.registry.generate_base()
# ================================================================================
# Generate a declarative base class.
Base = mapper_registry.generate_base()


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

    # ================================================================================
    # execute relationship function | sqlalchemy.orm.relationship()
    # ================================================================================
    # Provide a relationship between two mapped classes.
    # Allows Done object references from Task object.
    task = relationship("Task", back_populates="done")
