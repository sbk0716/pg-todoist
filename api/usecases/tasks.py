from fastapi import HTTPException
from databases import Database
from typing import List
from api.core.logging import logger
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.schemas.task import (
    TaskDoneRead,
    TaskRead,
    TaskCreate,
    TaskUpdate,
)


class TasksUsecase:
    # def __init__(self, tasks_repo: TasksRepository) -> None:
    #     # Set TasksRepository instance to TasksUsecase instance.
    #     self.tasks_repo = tasks_repo
    def __init__(self, db: Database) -> None:
        self.db = db
        self.tasks_repo = TasksRepository(db)

    async def list_tasks(
        self,
    ) -> List[TaskDoneRead]:
        """
        list_tasks function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            task_read_list = await self.tasks_repo.get_all_task_with_done()
            resp = task_read_list
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp

    async def get_task(
        self,
        task_id: int,
    ) -> List[TaskDoneRead]:
        """
        get_task function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            task_read = await self.tasks_repo.get_task_with_done(task_id=task_id)
            if task_read is None:
                logger.error("Task not found")
                raise HTTPException(status_code=404, detail="Task not found")
            resp = task_read
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp

    async def create_task(
        self,
        task_body: TaskCreate,
    ) -> TaskRead:
        """
        create_task function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            created_task = await self.tasks_repo.create_task(task_body=task_body)
            resp = created_task
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp

    async def update_task(
        self,
        task_id: int,
        task_body: TaskUpdate,
    ) -> TaskRead:
        """
        update_task function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            updated_task = await self.tasks_repo.update_task_by_id(
                task_id=task_id, task_body=task_body
            )
            if updated_task is None:
                raise HTTPException(status_code=404, detail="Task not found")
            resp = updated_task
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp

    async def delete_task(
        self,
        task_id: int,
    ) -> TaskRead:
        """
        delete_task function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            deleted_task = await self.tasks_repo.delete_task_by_id(task_id=task_id)
            if deleted_task is None:
                raise HTTPException(status_code=404, detail="Task not found")
            resp = deleted_task
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp
