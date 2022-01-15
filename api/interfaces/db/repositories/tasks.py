from datetime import datetime, timezone
from typing import List
from api.core.logging import logger
from api.interfaces.db.repositories.base import BaseRepository
from api.interfaces.schemas.task import (
    TaskDoneRead,
    TaskRead,
    TaskCreate,
    TaskUpdate,
)
from api.interfaces.db.queries.tasks import (
    CREATE_TASK_QUERY,
    GET_ALL_TASK_WITH_DONE_QUERY,
    GET_TASK_WITH_DONE_BY_ID_QUERY,
    GET_TASK_BY_ID_QUERY,
    UPDATE_TASK_BY_ID_QUERY,
    DELETE_TASK_BY_ID_QUERY,
)


class TasksRepository(BaseRepository):
    async def create_task(self, task_body: TaskCreate) -> TaskRead:
        """
        create_task method
        """
        logger.info("execute create_task method")
        try:
            query_values = task_body.dict()
            status_type_value = task_body.status_type.value
            query_values["status_type"] = status_type_value
            task = await self.db.fetch_one(query=CREATE_TASK_QUERY, values=query_values)
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(task.items()))
            task = TaskRead(**task)
            return task
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def get_all_task_with_done(self) -> List[TaskDoneRead]:
        """
        get_all_task_with_done method
        """
        logger.info("execute get_all_task_with_done method")
        try:
            task_list = await self.db.fetch_all(query=GET_ALL_TASK_WITH_DONE_QUERY)
            if len(task_list) != 0:
                # databases.backends.postgres.Record -> dict
                dict_task_list = [dict(task) for task in task_list]
                sorted_list = sorted(dict_task_list, key=lambda x: x["updated_at"], reverse=True)
                task_read_list: List[TaskDoneRead] = [TaskDoneRead(**task) for task in sorted_list]
                return task_read_list
            else:
                return task_list
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def get_task_with_done(self, task_id: int) -> TaskDoneRead:
        """
        get_task_with_done method
        """
        logger.info("execute get_task_with_done method")
        try:
            task = await self.db.fetch_one(
                query=GET_TASK_WITH_DONE_BY_ID_QUERY, values={"id": task_id}
            )
            if task is None:
                return None
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(task.items()))
            task_read = TaskDoneRead(**task)
            return task_read
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def get_task_by_id(self, task_id: int) -> TaskRead:
        """
        get_task_by_id method
        """
        logger.info("execute get_task_by_id method")
        try:
            task = await self.db.fetch_one(query=GET_TASK_BY_ID_QUERY, values={"id": task_id})
            if task is None:
                return None
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(task.items()))
            task = TaskRead(**task)
            return task

        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def update_task_by_id(self, task_id: int, task_body: TaskUpdate) -> TaskRead:
        """
        update_task_by_id method
        """
        logger.info("execute update_task_by_id method")
        try:
            task = await self.get_task_by_id(task_id=task_id)
            if task is None:
                return None
            update_data = task_body.dict(exclude_unset=True)
            dt_now_utc = datetime.now(timezone.utc)
            update_data["updated_at"] = dt_now_utc
            status_type_value = task_body.status_type.value
            update_data["status_type"] = status_type_value
            # execute pydantic BaseModel.copy method
            updated_params = task.copy(update=update_data)
            query_values = updated_params.dict()
            task = await self.db.fetch_one(query=UPDATE_TASK_BY_ID_QUERY, values=query_values)
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(task.items()))
            task = TaskRead(**task)
            return task
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def delete_task_by_id(self, task_id: int) -> TaskRead:
        """
        delete_task_by_id method
        """
        logger.info("execute delete_task_by_id method")
        try:
            task = await self.get_task_by_id(task_id=task_id)
            if task is None:
                return None
            task = await self.db.fetch_one(query=DELETE_TASK_BY_ID_QUERY, values={"id": task_id})
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(task.items()))
            task = TaskRead(**task)
            return task
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e
