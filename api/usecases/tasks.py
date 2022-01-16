from fastapi import HTTPException
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
    def __init__(self, tasks_repo: TasksRepository) -> None:
        # Set TasksRepository instance to TasksUsecase instance.
        self.tasks_repo = tasks_repo

    async def list_tasks(
        self,
    ) -> List[TaskDoneRead]:
        """
        list_tasks function
        """
        task_read_list = await self.tasks_repo.get_all_task_with_done()
        return task_read_list

    async def get_task(
        self,
        task_id: int,
    ) -> List[TaskDoneRead]:
        """
        get_task function
        """
        task_read = await self.tasks_repo.get_task_with_done(task_id=task_id)
        if task_read is None:
            logger.error("Task not found")
            raise HTTPException(status_code=404, detail="Task not found")
        return task_read

    async def create_task(
        self,
        task_body: TaskCreate,
    ) -> TaskRead:
        """
        create_task function
        """
        created_task = await self.tasks_repo.create_task(task_body=task_body)
        return created_task

    async def update_task(
        self,
        task_id: int,
        task_body: TaskUpdate,
    ) -> TaskRead:
        """
        update_task function
        """
        updated_task = await self.tasks_repo.update_task_by_id(task_id=task_id, task_body=task_body)
        if updated_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return updated_task

    async def delete_task(
        self,
        task_id: int,
    ) -> TaskRead:
        """
        delete_task function
        """
        deleted_task = await self.tasks_repo.delete_task_by_id(task_id=task_id)
        if deleted_task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return deleted_task
