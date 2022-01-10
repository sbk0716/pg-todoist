from fastapi import Depends
from starlette.requests import Request
from databases import Database
from typing import Callable, Type
from api.core import environ
from api.core.logging import logger
from api.interfaces.db.repositories.base import BaseRepository

DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB


def get_db(request: Request):
    logger.info("execute get_db function")
    return request.app.state._db


def get_repository(repo_class: Type[BaseRepository]) -> Callable:
    """
    Return get_repo function.
    """
    logger.info("execute get_repository function")

    def get_repo(db: Database = Depends(get_db)) -> Type[BaseRepository]:
        """
        This function creates and returns a target repository class instance.
        """
        logger.info("execute get_repo function")
        instance = repo_class(db)
        return instance

    return get_repo
