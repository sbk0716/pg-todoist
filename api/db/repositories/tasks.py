from sqlalchemy.ext.asyncio import AsyncSession

# import api.domain.models.task as task_model
# import api.interfaces.schemas.task as task_schema
from typing import List, Tuple, Optional, Dict, Any
from sqlalchemy import select
from sqlalchemy.engine import Result

from api.db.repositories.base import BaseRepository
import api.db.queries.tasks as query
from api.core.logging import logger
from api.interfaces.schemas.task import (
    TaskRead,
    TaskCreate,
    TaskCreateResponse,
    TaskUpdate,
    TaskUpdateResponse,
    TaskDeleteResponse,
)
from api.domain.models.task import Task


class TasksRepository(BaseRepository):
    async def create_task(self, task_body: TaskCreate) -> Task:
        """
        create_task method
        """
        logger.info("Execute create_task method")
        try:
            query_values = task_body.dict()
            task = await self.db.fetch_one(query=query.CREATE_TASK_QUERY, values=query_values)
            task_instance = Task(**task)
            return task_instance
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def get_all_task_with_done(self) -> List[TaskRead]:
        """
        get_all_task_with_done method
        """
        logger.info("Execute get_all_task_with_done method")
        try:
            task_list: List[Tuple[int, str, bool]] = await self.db.fetch_all(
                query=query.GET_ALL_TASK_WITH_DONE_QUERY
            )
            if len(task_list) != 0:
                dict_task_list: List[TaskRead] = [TaskRead(**task) for task in task_list]
                return dict_task_list
            else:
                return task_list
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def get_task_with_done(self, task_id: int) -> TaskRead:
        """
        get_task_with_done method
        """
        logger.info("Execute get_task_with_done method")
        try:
            task: Tuple[int, str, bool] = await self.db.fetch_one(
                query=query.GET_TASK_WITH_DONE_QUERY, values={"id": task_id}
            )
            task_instance = TaskRead(**task)
            return task_instance
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

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
