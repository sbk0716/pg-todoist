from databases import Database
from typing import List
from api.usecases.tasks import TasksUsecase
from api.interfaces.schemas.task import (
    TaskDoneRead,
    TaskRead,
    TaskCreate,
    TaskUpdate,
)


class TasksController:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def list_tasks(self) -> List[TaskDoneRead]:
        """
        list_tasks function
        """
        tasks_usecase = TasksUsecase(self.db)
        return await tasks_usecase.list_tasks()

    async def get_task(self, task_id: int) -> List[TaskDoneRead]:
        """
        get_task function
        """
        tasks_usecase = TasksUsecase(self.db)
        return await tasks_usecase.get_task(task_id=task_id)

    async def create_task(self, task_body: TaskCreate) -> TaskRead:
        """
        create_task function
        """
        tasks_usecase = TasksUsecase(self.db)
        return await tasks_usecase.create_task(task_body=task_body)

    async def update_task(self, task_id: int, task_body: TaskUpdate) -> TaskRead:
        """
        update_task function
        """
        tasks_usecase = TasksUsecase(self.db)
        return await tasks_usecase.update_task(task_id=task_id, task_body=task_body)

    async def delete_task(self, task_id: int) -> TaskRead:
        """
        delete_task function
        """
        tasks_usecase = TasksUsecase(self.db)
        return await tasks_usecase.delete_task(task_id=task_id)
