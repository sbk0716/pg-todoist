from fastapi import Depends
from starlette.requests import Request
from databases import Database
from typing import Callable, Type
from api.interfaces.db.repositories.base import BaseRepository


def get_db(request: Request):
    """
    Get the connection pool from `Starlette State instance`.
    `connect_to_db function` set the connection pool to `Starlette State instance`.
    """
    return request.app.state._db


def get_repository(repo_class: Type[BaseRepository]) -> Callable:
    """
    Return `get_repo` function.
    `get_repo` function returns the target repository class instance that set the connection pool.
    """

    def get_repo(db: Database = Depends(get_db)) -> Type[BaseRepository]:
        """
        Returns the target repository class instance that set the connection pool.
        """
        instance = repo_class(db)
        return instance

    return get_repo
