from databases import Database
from api.usecases.dones import DonesUsecase
from api.interfaces.schemas.done import (
    DoneRead,
)


class DonesController:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def mark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        mark_task_as_done function
        """
        dones_usecase = DonesUsecase(self.db)
        return await dones_usecase.mark_task_as_done(task_id=task_id)

    async def unmark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        unmark_task_as_done function
        """
        dones_usecase = DonesUsecase(self.db)
        return await dones_usecase.unmark_task_as_done(task_id=task_id)
