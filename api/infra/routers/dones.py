from fastapi import APIRouter, Request, status, Depends, Path, Header
from typing import Optional
from api.core.logging import logger
from api.dependencies.db import get_repository
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.db.repositories.dones import DonesRepository
from api.interfaces.controllers.dones import DonesController
from api.interfaces.schemas.done import (
    DoneRead,
)

router = APIRouter()


@router.post(
    "/{task_id}/done/",
    response_model=DoneRead,
    name="tasks:mark_task_as_done",
    status_code=status.HTTP_201_CREATED,
)
async def mark_task_as_done(
    request: Request,
    user_agent: Optional[str] = Header(None),
    task_id: int = Path(..., title="The ID of the record to get.", gt=0, le=1000),
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
    dones_repo: DonesRepository = Depends(get_repository(DonesRepository)),
) -> DoneRead:
    """
    mark_task_as_done function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"user_agent: {user_agent}")
    # Set DonesRepository and TasksRepository to DonesController instance.
    dones_controller = DonesController(tasks_repo, dones_repo)
    return await dones_controller.mark_task_as_done(task_id=task_id)


@router.delete(
    "/{task_id}/done/",
    response_model=DoneRead,
    name="tasks:unmark_task_as_done",
    status_code=status.HTTP_200_OK,
)
async def unmark_task_as_done(
    request: Request,
    user_agent: Optional[str] = Header(None),
    task_id: int = Path(..., title="The ID of the record to get.", gt=0, le=1000),
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
    dones_repo: DonesRepository = Depends(get_repository(DonesRepository)),
) -> DoneRead:
    """
    unmark_task_as_done function
    """
    logger.info(f"request.headers: {request.headers}")
    logger.info(f"user_agent: {user_agent}")
    # Set DonesRepository and TasksRepository to DonesController instance.
    dones_controller = DonesController(tasks_repo, dones_repo)
    return await dones_controller.unmark_task_as_done(task_id=task_id)
