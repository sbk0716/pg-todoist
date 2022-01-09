from fastapi import APIRouter, status, Depends
import api.interfaces.schemas.task as task_schema
from api.db.repositories.task import TasksRepository
from api.dependencies.db import get_repository

from api.core.logging import logger

router = APIRouter()

# @router.get("/tasks", response_model=List[task_schema.Task])
# async def list_tasks(db: AsyncSession = Depends(get_db)):
#     '''
#     list_tasks method
#     '''
#     return await task_crud.get_tasks_with_done(db)

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
    response_model=task_schema.TaskCreateResponse,
    name="tasks:create_task",
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    task_body: task_schema.TaskCreate,
    tasks_repo: TasksRepository = Depends(get_repository(TasksRepository)),
):
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
