from api.core.logging import logger
from api.interfaces.db.repositories.base import BaseRepository
from api.interfaces.schemas.done import (
    DoneRead,
)
from api.interfaces.db.queries.dones import (
    GET_DONE_BY_ID_QUERY,
    CREATE_DONE_QUERY,
    DELETE_DONE_BY_ID_QUERY,
)


class DonesRepository(BaseRepository):
    async def get_done_by_id(self, task_id: int) -> DoneRead:
        """
        get_done_by_id method
        """
        logger.info("execute get_done_by_id method")
        try:
            done = await self.db.fetch_one(query=GET_DONE_BY_ID_QUERY, values={"id": task_id})
            if done is None:
                return None
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(done.items()))
            done = DoneRead(**done)
            return done

        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e

    async def create_done(self, task_id: int) -> DoneRead:
        """
        create_done method
        """
        logger.info("execute create_done method")
        try:
            note = f"Record created by create_done method | ID: {task_id}"
            query_values = {
                "id": task_id,
                "note": note,
            }
            done = await self.db.fetch_one(query=CREATE_DONE_QUERY, values=query_values)
            logger.info("[databases.backends.postgres.Record]")
            logger.info(dict(done.items()))
            done = DoneRead(**done)
            return done
        except Exception as e:
            logger.error("--- [ERROR] ---")
            logger.error(e)
            logger.error("--- [ERROR] ---")
            raise e


# async def delete_done(self, db: AsyncSession, original: task_model.Done) -> None:
#     db = self.db
#     await db.delete(original)
#     await db.commit()
