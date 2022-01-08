from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
# Import logging | Logging package for Python.
import logging
from starlette.requests import Request
from api import environ

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

# Define ASYNC_DB_URL
ASYNC_DB_URL = environ.ASYNC_DB_URL
MYSQL_DATABASE = environ.MYSQL_DATABASE

# ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
)

Base = declarative_base()


# async def get_db():
#     print(f"--- MYSQL_DATABASE: {MYSQL_DATABASE} ---")
#     async with async_session() as session:
#         yield session

async def get_db(request: Request):
    logger.info("get_db function")
    logger.info("request.app.state._db")
    logger.info(request.app.state._db)
    return request.app.state._db

# async def get_db():
#     try:
#         logger.info(f"--- MYSQL_DATABASE: {MYSQL_DATABASE} ---")
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