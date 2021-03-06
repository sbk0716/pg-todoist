from fastapi import APIRouter, Request, status, Depends, Path, Header, Body
from databases import Database
from typing import Optional, List
from api.core.logging import logger
from api.dependencies.db import get_repository, get_database
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
    request: Request,
    authorization: Optional[str] = Header(None),
    db: Database = Depends(get_database()),
) -> List[TaskDoneRead]:
    """
    list_tasks function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"authorization: {authorization}")
    tasks_controller = TasksController(db)
    return await tasks_controller.list_tasks()


@router.get(
    "/{task_id}/",
    response_model=TaskDoneRead,
    name="tasks:get_task",
    status_code=status.HTTP_200_OK,
)
async def get_task(
    request: Request,
    authorization: Optional[str] = Header(None),
    db: Database = Depends(get_database()),
    task_id: int = Path(..., title="The ID of the record to get.", gt=0, le=1000),
) -> List[TaskDoneRead]:
    """
    get_task function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"authorization: {authorization}")
    tasks_controller = TasksController(db)
    return await tasks_controller.get_task(task_id=task_id)


@router.post(
    "/",
    response_model=TaskRead,
    name="tasks:create_task",
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    request: Request,
    authorization: Optional[str] = Header(None),
    db: Database = Depends(get_database()),
    task_body: TaskCreate = Body(...),
) -> TaskRead:
    """
    create_task function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"authorization: {authorization}")
    tasks_controller = TasksController(db)
    return await tasks_controller.create_task(task_body=task_body)


@router.put(
    "/{task_id}/",
    response_model=TaskRead,
    name="tasks:update_task",
    status_code=status.HTTP_200_OK,
)
async def update_task(
    request: Request,
    authorization: Optional[str] = Header(None),
    db: Database = Depends(get_database()),
    task_id: int = Path(..., title="The ID of the record to get.", gt=0, le=1000),
    task_body: TaskUpdate = Body(...),
) -> TaskRead:
    """
    update_task function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"authorization: {authorization}")
    tasks_controller = TasksController(db)
    return await tasks_controller.update_task(task_id=task_id, task_body=task_body)


@router.delete(
    "/{task_id}/",
    response_model=TaskRead,
    name="tasks:delete_task",
    status_code=status.HTTP_200_OK,
)
async def delete_task(
    request: Request,
    authorization: Optional[str] = Header(None),
    db: Database = Depends(get_database()),
    task_id: int = Path(..., title="The ID of the record to get.", gt=0, le=1000),
) -> TaskRead:
    """
    delete_task function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"authorization: {authorization}")
    tasks_controller = TasksController(db)
    return await tasks_controller.delete_task(task_id=task_id)
