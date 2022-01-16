from fastapi import HTTPException
from databases import Database
from api.core.logging import logger
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.db.repositories.dones import DonesRepository
from api.interfaces.schemas.done import (
    DoneRead,
)


class DonesUsecase:
    def __init__(self, db: Database) -> None:
        self.db = db
        self.tasks_repo = TasksRepository(db)
        self.dones_repo = DonesRepository(db)

    async def mark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        mark_task_as_done function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            task_read = await self.tasks_repo.get_task_with_done(task_id=task_id)
            if task_read is None:
                logger.error("Task not found")
                raise HTTPException(status_code=404, detail="Task not found")
            done = await self.dones_repo.get_done_by_id(task_id=task_id)
            if done is not None:
                raise HTTPException(status_code=400, detail="Done already exists")
            resp = await self.dones_repo.create_done(task_id=task_id)
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp

    async def unmark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        unmark_task_as_done function
        """
        resp = None
        transaction = await self.db.transaction()
        try:
            task_read = await self.tasks_repo.get_task_with_done(task_id=task_id)
            if task_read is None:
                logger.error("Task not found")
                raise HTTPException(status_code=404, detail="Task not found")
            done = await self.dones_repo.get_done_by_id(task_id=task_id)
            if done is None:
                raise HTTPException(status_code=404, detail="Done not found")
            resp = await self.dones_repo.delete_done(task_id=task_id)
        except Exception as e:
            logger.error("transaction.rollback()")
            await transaction.rollback()
            raise e
        else:
            logger.info("transaction.commit()")
            await transaction.commit()
            return resp
