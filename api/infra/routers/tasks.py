from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from api.core.logging import logger
from api.dependencies.db import get_repository
from api.db.repositories.tasks import TasksRepository
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
    task_read_list = await tasks_repo.get_all_task_with_done()
    return task_read_list


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
    task_read = await tasks_repo.get_task_with_done(task_id=task_id)
    if task_read is None:
        logger.error("Task not found")
        raise HTTPException(status_code=404, detail="Task not found")
    return task_read


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
    created_task = await tasks_repo.create_task(task_body=task_body)
    return created_task


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
    updated_task = await tasks_repo.update_task_by_id(task_id=task_id, task_body=task_body)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


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
    deleted_task = await tasks_repo.delete_task_by_id(task_id=task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task
