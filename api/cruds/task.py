from sqlalchemy.ext.asyncio import AsyncSession
import api.models.task as task_model
import api.schemas.task as task_schema
from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result

async def create_task(
        db: AsyncSession,
        task_create: task_schema.TaskCreate
    ) -> task_model.Task:
    '''
    引数としてスキーマ task_create: task_schema.TaskCreate を受け取る。
    これをDBモデルである task_model.Task に変換する
    DBにコミットする
    DB上のデータを元にTaskインスタンス task を更新する（この場合、作成したレコードの id を取得する）
    作成したDBモデルを返却する
    '''
    task = task_model.Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_tasks_with_done(
        db: AsyncSession
    ) -> List[Tuple[int, str, bool]]:
    '''
    get_tasks_with_done method
    '''
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done)
        )
    )
    return result.all()

async def get_task_with_done(
        db: AsyncSession, task_id: int
    ) -> Tuple[int, str, bool]:
    '''
    get_task_with_done method
    '''
    result: Result = await (
        db.execute(
            select(
                task_model.Task.id,
                task_model.Task.title,
                task_model.Done.id.isnot(None).label("done"),
            ).outerjoin(task_model.Done).filter(task_model.Task.id == task_id)
        )
    )
    print('### result ###')
    print(result)
    task: Optional[Tuple[task_model.Task]] = result.first()
    print('### task ###')
    print(task)
    return task

async def get_task(db: AsyncSession, task_id: int) -> Optional[task_model.Task]:
    '''
    get_task method
    '''
    result: Result = await db.execute(
        select(task_model.Task).filter(task_model.Task.id == task_id)
    )
    task: Optional[Tuple[task_model.Task]] = result.first()

    # return task[0] if task is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す
    if task is not None:
      resp = task[0]
    else:
      resp = None
    return resp

async def update_task(
        db: AsyncSession,
        task_create: task_schema.TaskCreate,
        original: task_model.Task
    ) -> task_model.Task:
    '''
    get_task method
    '''
    original.title = task_create.title
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original

async def delete_task(db: AsyncSession, original: task_model.Task) -> None:
    await db.delete(original)
    await db.commit()