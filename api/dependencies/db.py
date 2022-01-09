from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
# Import logging | Logging package for Python.
import logging
from starlette.requests import Request
from api import environ
from databases import Database
from fastapi import Depends
from starlette.requests import Request
from api.db.repositories.base import BaseRepository
from databases import Database
from fastapi import Depends
from starlette.requests import Request
from typing import Callable, Type

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

# Define DB_URL
DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB

# DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

# async_engine = create_async_engine(DB_URL, echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
# )

# Base = declarative_base()


# async def get_db():
#     print(f"--- POSTGRES_DB: {POSTGRES_DB} ---")
#     async with async_session() as session:
#         yield session

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


# async def get_db():
#     try:
#         logger.info(f"--- POSTGRES_DB: {POSTGRES_DB} ---")
#         logger.info("--- [DB CONNECTION][CONSTRUCT]AsyncSession ---")
#         session = async_session() 
#         # FastAPI supports dependencies that do some extra steps after finishing.
#         # To do this, use `yield` instead of `return`, and write the extra steps after.
#         # https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/?h=yie#a-database-dependency-with-yield
#         yield session
#     except Exception as e:
#         logger.warn("--- [DB CONNECTION][ERROR]AsyncSession ---")
#         logger.warn(e)
#         raise e
#     # The code following the yield statement is executed after the response has been delivered.
#     finally:
#         logger.info("--- [DB CONNECTION][CLOSE]AsyncSession ---")
#         await session.close()