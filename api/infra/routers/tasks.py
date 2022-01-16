from fastapi import APIRouter, status, Depends
from typing import List
from api.dependencies.db import get_repository
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.controllers.tasks import TasksController
from api.interfaces.schemas.task import (
    TaskDoneRead,
    TaskRead,
    TaskCreate,
    TaskUpdate,
)

router = APIRouter()


@router.get(
    "/",
    response_model=List[TaskDoneRead],
    name="tasks:list_tasks",
    status_code=status.HTTP_200_OK,
)
async def list_tasks(
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
) -> List[TaskDoneRead]:
    """
    list_tasks function
    """
    # Set TasksRepository to TasksController instance.
    tasks_controller = TasksController(tasks_repo)
    return await tasks_controller.list_tasks()


@router.get(
    "/{task_id}/",
    response_model=TaskDoneRead,
    name="tasks:get_task",
    status_code=status.HTTP_200_OK,
)
async def get_task(
    task_id: int, tasks_repo: TasksRepository = Depends(get_repository(TasksRepository))
) -> List[TaskDoneRead]:
    """
    get_task function
    """
    # Set TasksRepository to TasksController instance.
    tasks_controller = TasksController(tasks_repo)
    return await tasks_controller.get_task(task_id=task_id)


@router.post(
    "/",
    response_model=TaskRead,
    name="tasks:create_task",
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    task_body: TaskCreate,
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
) -> TaskRead:
    """
    create_task function
    """
    # Set TasksRepository to TasksController instance.
    tasks_controller = TasksController(tasks_repo)
    return await tasks_controller.create_task(task_body=task_body)


@router.put(
    "/{task_id}/",
    response_model=TaskRead,
    name="tasks:update_task",
    status_code=status.HTTP_200_OK,
)
async def update_task(
    task_id: int,
    task_body: TaskUpdate,
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
) -> TaskRead:
    """
    update_task function
    """
    # Set TasksRepository to TasksController instance.
    tasks_controller = TasksController(tasks_repo)
    return await tasks_controller.update_task(task_id=task_id, task_body=task_body)


@router.delete(
    "/{task_id}/",
    response_model=TaskRead,
    name="tasks:delete_task",
    status_code=status.HTTP_200_OK,
)
async def delete_task(
    task_id: int,
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
) -> TaskRead:
    """
    delete_task function
    """
    # Set TasksRepository to TasksController instance.
    tasks_controller = TasksController(tasks_repo)
    return await tasks_controller.delete_task(task_id=task_id)
