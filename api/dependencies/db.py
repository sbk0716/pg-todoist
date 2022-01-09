from fastapi import Depends
from starlette.requests import Request
from databases import Database
from typing import Callable, Type

from api.core import environ
from api.core.logging import logger
from api.db.repositories.base import BaseRepository

DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB


async def get_db(request: Request):
    logger.info("execute get_db function")
    logger.info("request.app.state._db")
    logger.info(request.app.state._db)
    return request.app.state._db


def get_repository(repo_class: Type[BaseRepository]) -> Callable:
    """
    Return get_repo function.
    """
    logger.info("execute get_repository function")

    def get_repo(db: Database = Depends(get_db)) -> Type[BaseRepository]:
        logger.info("execute get_repo function")
        logger.info("db")
        logger.info(db)
        logger.info("repo_class")
        logger.info(repo_class)
        logger.info("create target repository class instance")
        instance = repo_class(db)
        logger.info("instance")
        logger.info(instance)
        return instance

    return get_repo
