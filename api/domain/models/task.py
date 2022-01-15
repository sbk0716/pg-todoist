from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import relationship, registry
from datetime import timedelta, timezone

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


class Task(Base):
    """
    Task Class
    Inherit declarative base class.
    """

    # Define table name
    __tablename__ = "tasks"

    # PK
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(1024), nullable=False, index=True)
    detail = Column(String(4096), nullable=False)
    status_type = Column(Integer, nullable=False, index=True)
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
    # [The ON DELETE CASCADE]
    # Automatically deletes all the referencing rows in the child table when the referenced rows in the parent table are deleted.
    # [The ON UPDATE CASCADE]
    # Automatically updates all the referencing rows in the child table when the referenced rows in the parent table are updated.
    id = Column(
        Integer,
        ForeignKey("tasks.id", onupdate="CASCADE", ondelete="CASCADE"),
        primary_key=True,
        autoincrement=False,
    )
    note = Column(String(4096), nullable=False)
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
