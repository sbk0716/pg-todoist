from fastapi import HTTPException
from api.core.logging import logger
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.db.repositories.dones import DonesRepository
from api.interfaces.schemas.done import (
    DoneRead,
)


class DonesUsecase:
    def __init__(self, tasks_repo: TasksRepository, dones_repo: DonesRepository) -> None:
        # Set TasksRepository instance to DonesUsecase instance.
        self.tasks_repo = tasks_repo
        # Set DonesRepository instance to DonesUsecase instance.
        self.dones_repo = dones_repo

    async def mark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        mark_task_as_done function
        """
        task_read = await self.tasks_repo.get_task_with_done(task_id=task_id)
        if task_read is None:
            logger.error("Task not found")
            raise HTTPException(status_code=404, detail="Task not found")
        done = await self.dones_repo.get_done_by_id(task_id=task_id)
        if done is not None:
            raise HTTPException(status_code=400, detail="Done already exists")
        return await self.dones_repo.create_done(task_id=task_id)

    async def unmark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        unmark_task_as_done function
        """
        task_read = await self.tasks_repo.get_task_with_done(task_id=task_id)
        if task_read is None:
            logger.error("Task not found")
            raise HTTPException(status_code=404, detail="Task not found")
        done = await self.dones_repo.get_done_by_id(task_id=task_id)
        if done is None:
            raise HTTPException(status_code=404, detail="Done not found")
        return await self.dones_repo.delete_done(task_id=task_id)
