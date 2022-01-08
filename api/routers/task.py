from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
import api.schemas.task as task_schema
import api.cruds.task as task_crud
from api.db import get_db

router = APIRouter()

# GET /tasks は、スキーマに定義した Task クラスを複数返しますので、リストとして定義します。
# ここでは、 response_model=List[task_schema.Task] となります。
@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    '''
    list_tasks method
    '''
    return await task_crud.get_tasks_with_done(db)

# GET /tasks は、スキーマに定義した Task クラスを一つ返す。
# ここでは、 response_model=task_schema.Task となります。
@router.get("/tasks/{task_id}", response_model=task_schema.Task)
async def get_task(
        task_id: int,
        db: AsyncSession = Depends(get_db)
    ):
    '''
    get_task method
    '''
    task = await task_crud.get_task_with_done(db, task_id=task_id)
    print(task)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(
        task_body: task_schema.TaskCreate,
        db: AsyncSession = Depends(get_db)
    ):
    '''
    create_task method
    Depends は引数に関数を取りDependency Injectionを行う。
    DB接続部分にDIを利用することにより、ビジネスロジックとDBが密結合になることを防ぐ。
    '''
    return await task_crud.create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(
    task_id: int, task_body: task_schema.TaskCreate, db: AsyncSession = Depends(get_db)
):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.update_task(db, task_body, original=task)


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await task_crud.get_task(db, task_id=task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return await task_crud.delete_task(db, original=task)