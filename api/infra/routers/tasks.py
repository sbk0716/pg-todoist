from fastapi import APIRouter, status, Depends
from typing import List, Dict, Any
from api.core.logging import logger
from api.dependencies.db import get_repository
from api.db.repositories.tasks import TasksRepository
from api.domain.models.task import Task
from api.interfaces.schemas.task import (
    TaskRead,
    TaskCreate,
    TaskCreateResponse,
    TaskUpdate,
    TaskUpdateResponse,
    TaskDeleteResponse,
)

router = APIRouter()


@router.get(
    "/",
    response_model=List[TaskRead],
    name="tasks:list_tasks",
    status_code=status.HTTP_200_OK,
)
async def list_tasks(
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
) -> List[TaskRead]:
    """
    list_tasks function
    """
    task_list = await tasks_repo.get_all_task_with_done()
    return task_list


@router.get(
    "/{task_id}/",
    response_model=TaskRead,
    name="tasks:get_task",
    status_code=status.HTTP_200_OK,
)
async def get_task(
    task_id: int, tasks_repo: TasksRepository = Depends(get_repository(TasksRepository))
) -> List[TaskRead]:
    """
    get_task function
    """
    task = await tasks_repo.get_task_with_done(task_id=task_id)
    return task


# @router.get("/tasks/{task_id}", response_model=task_schema.Task)
# async def get_task(
#         task_id: int,
#         db: AsyncSession = Depends(get_db)
#     ):
#     '''
#     get_task method
#     '''
#     task = await task_crud.get_task_with_done(db, task_id=task_id)
#     print(task)
#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found")

#     return task


@router.post(
    "/",
    response_model=TaskCreateResponse,
    name="tasks:create_task",
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    task_body: TaskCreate,
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
) -> Task:
    """
    create_task method
    """
    logger.info("tasks_repo")
    logger.info(tasks_repo)
    created_task = await tasks_repo.create_task(task_body=task_body)
    logger.info("created_task")
    logger.info(created_task)
    return created_task


# @router.post('/',
#              response_model=HedgehogPublic,
#              name='hedgehogs:create-hedgehog',
#              status_code=HTTP_201_CREATED)
# async def create_new_hedgehog(
#     new_hedgehog: HedgehogCreate = Body(..., embed=True),
#     hedgehogs_repo: HedgehogsRepository = Depends(get_repository(HedgehogsRepository)),
# ) -> HedgehogPublic:
#     created_hedgehog = await hedgehogs_repo.create_hedgehog(new_hedgehog=new_hedgehog)
#     return created_hedgehog


# @router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
# async def update_task(
#     task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
# ):
#     task = await task_crud.get_task(db, task_id=task_id)
#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found")

#     return await task_crud.update_task(db, task_body, original=task)


# @router.delete("/tasks/{task_id}", response_model=None)
# async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
#     task = await task_crud.get_task(db, task_id=task_id)
#     if task is None:
#         raise HTTPException(status_code=404, detail="Task not found")

#     return await task_crud.delete_task(db, original=task)
