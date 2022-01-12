from fastapi import APIRouter, status, Depends, HTTPException
from api.core.logging import logger
from api.dependencies.db import get_repository
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.db.repositories.dones import DonesRepository
from api.interfaces.schemas.done import (
    DoneRead,
)

router = APIRouter()


@router.post(
    "/{task_id}/",
    response_model=DoneRead,
    name="tasks:mark_task_as_done",
    status_code=status.HTTP_201_CREATED,
)
async def mark_task_as_done(
    task_id: int,
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
    dones_repo: DonesRepository = Depends(get_repository(DonesRepository)),
) -> DoneRead:
    """
    mark_task_as_done function
    """
    task_read = await tasks_repo.get_task_with_done(task_id=task_id)
    if task_read is None:
        logger.error("Task not found")
        raise HTTPException(status_code=404, detail="Task not found")
    done = await dones_repo.get_done_by_id(task_id=task_id)
    if done is not None:
        raise HTTPException(status_code=400, detail="Done already exists")
    return await dones_repo.create_done(task_id=task_id)


# @router.delete("/tasks/{task_id}/done", response_model=None)
# async def unmark_task_as_done(task_id: int, db: AsyncSession = Depends(get_db)):
#     done = await done_crud.get_done(db, task_id=task_id)
#     if done is None:
#         raise HTTPException(status_code=404, detail="Done not found")

#     return await done_crud.delete_done(db, original=done)
