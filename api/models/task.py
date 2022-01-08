from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    # relationship はテーブル（モデルクラス）同士の関係性を定義します。
    # Task オブジェクトから Done オブジェクト参照が可能になります。
    done = relationship("Done", back_populates="task")


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
    # relationship はテーブル（モデルクラス）同士の関係性を定義します。
    # Done オブジェクトから Task オブジェクト参照が可能になります。
    task = relationship("Task", back_populates="done")