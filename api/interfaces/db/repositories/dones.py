from typing import Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

import api.domain.models.task as task_model

from api.interfaces.db.repositories.base import BaseRepository

# class DonesRepository(BaseRepository):
# async def get_done(self, db: AsyncSession, task_id: int) -> Optional[task_model.Done]:
#     db = self.db
#     result: Result = await db.execute(
#         select(task_model.Done).filter(task_model.Done.id == task_id)
#     )
#     done: Optional[Tuple[task_model.Done]] = result.first()
#     return done[0] if done is not None else None

# async def create_done(self, db: AsyncSession, task_id: int) -> task_model.Done:
#     db = self.db
#     done = task_model.Done(id=task_id)
#     db.add(done)
#     await db.commit()
#     await db.refresh(done)
#     return done

# async def delete_done(self, db: AsyncSession, original: task_model.Done) -> None:
#     db = self.db
#     await db.delete(original)
#     await db.commit()
