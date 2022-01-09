from sqlalchemy.ext.asyncio import AsyncSession
import api.domain.models.task as task_model
import api.interfaces.schemas.task as task_schema
from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result

from api.db.repositories.base import BaseRepository
import api.db.queries.tasks as query


class TasksRepository(BaseRepository):
    async def create_task(self, task_body: task_schema.TaskCreate) -> task_model.Task:
        """
        create_task
        """
        query_values = task_body.dict()
        print("query_values")
        print(query_values)
        task = await self.db.fetch_one(query=query.CREATE_TASK_QUERY, values=query_values)
        print("task")
        print(task)
        task_instance = task_model.Task(**task)
        print("task_instance")
        print(task_instance)
        return task_instance

    # async def get_tasks_with_done(
    #         self,
    #         db: AsyncSession
    #     ) -> List[Tuple[int, str, bool]]:
    #     '''
    #     get_tasks_with_done method
    #     '''
    #     result: Result = await (
    #         db.execute(
    #             select(
    #                 task_model.Task.id,
    #                 task_model.Task.title,
    #                 task_model.Done.id.isnot(None).label("done"),
    #             ).outerjoin(task_model.Done)
    #         )
    #     )
    #     return result.all()

    # async def get_task_with_done(
    #         self,
    #         db: AsyncSession, task_id: int
    #     ) -> Tuple[int, str, bool]:
    #     '''
    #     get_task_with_done method
    #     '''
    #     result: Result = await (
    #         db.execute(
    #             select(
    #                 task_model.Task.id,
    #                 task_model.Task.title,
    #                 task_model.Done.id.isnot(None).label("done"),
    #             ).outerjoin(task_model.Done).filter(task_model.Task.id == task_id)
    #         )
    #     )
    #     print('### result ###')
    #     print(result)
    #     task: Optional[Tuple[task_model.Task]] = result.first()
    #     print('### task ###')
    #     print(task)
    #     return task

    # async def get_task(self, db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    #     '''
    #     get_task method
    #     '''
    #     result: Result = await db.execute(
    #         select(task_model.Task).filter(task_model.Task.id == task_id)
    #     )
    #     task: Optional[Tuple[task_model.Task]] = result.first()

    #     # return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
    #     if task is not None:
    #         resp = task[0]
    #     else:
    #         resp = None
    #     return resp

    # async def update_task(
    #         self,
    #         db: AsyncSession,
    #         task_create: task_schema.TaskCreate,
    #         original: task_model.Task
    #     ) -> task_model.Task:
    #     '''
    #     get_task method
    #     '''
    #     original.title = task_create.title
    #     db.add(original)
    #     await db.commit()
    #     await db.refresh(original)
    #     return original

    # async def delete_task(self, db: AsyncSession, original: task_model.Task) -> None:
    #     db = self.db
    #     await db.delete(original)
    #     await db.commit()
