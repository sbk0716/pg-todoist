from databases import Database
from api.interfaces.db.repositories.tasks import TasksRepository
from api.interfaces.db.repositories.dones import DonesRepository
from api.usecases.dones import DonesUsecase
from api.interfaces.schemas.done import (
    DoneRead,
)


class DonesController:
    # def __init__(self, tasks_repo: TasksRepository, dones_repo: DonesRepository) -> None:
    #     # Set TasksRepository instance to TasksController instance.
    #     self.tasks_repo = tasks_repo
    #     # Set DonesRepository instance to DonesController instance.
    #     self.dones_repo = dones_repo
    def __init__(self, db: Database) -> None:
        self.db = db

    async def mark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        mark_task_as_done function
        """
        # Set DonesRepository and TasksRepository to DonesUsecase instance.
        # dones_usecase = DonesUsecase(
        #     dones_repo=self.dones_repo,
        #     tasks_repo=self.tasks_repo,
        # )
        # Set DonesRepository and TasksRepository to DonesUsecase instance.
        dones_usecase = DonesUsecase(self.db)
        return await dones_usecase.mark_task_as_done(task_id=task_id)

    async def unmark_task_as_done(
        self,
        task_id: int,
    ) -> DoneRead:
        """
        unmark_task_as_done function
        """
        # Set DonesRepository and TasksRepository to DonesUsecase instance.
        # dones_usecase = DonesUsecase(
        #     dones_repo=self.dones_repo,
        #     tasks_repo=self.tasks_repo,
        # )
        dones_usecase = DonesUsecase(self.db)
        return await dones_usecase.unmark_task_as_done(task_id=task_id)
