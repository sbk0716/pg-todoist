import logging
import os
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from api import environ

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

# Define ASYNC_DB_URL
ASYNC_DB_URL = environ.ASYNC_DB_URL
MYSQL_DATABASE = environ.MYSQL_DATABASE




async def connect_to_db(app: FastAPI) -> None:
    try:
        logger.info(f"--- MYSQL_DATABASE: {MYSQL_DATABASE} ---")
        logger.info("--- [DB CONNECTION][CONSTRUCT]AsyncSession ---")
        async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
        async_session = sessionmaker(
            autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
        )
        session = async_session() 
        app.state._db = session
    except Exception as e:
        logger.warn("--- [DB CONNECTION][ERROR]AsyncSession ---")
        logger.warn(e)
        raise e
    # The code following the yield statement is executed after the response has been delivered.
    finally:
        logger.info("--- [DB CONNECTION][CLOSE]AsyncSession ---")
        await session.close()


async def close_db_connection(app: FastAPI) -> None:
    try:
        logger.info(f"--- MYSQL_DATABASE: {MYSQL_DATABASE} ---")
        logger.info("--- [CLOSE][DB CONNECTION][CONSTRUCT]AsyncSession ---")
        session = app.state._db
        await session.close()
    except Exception as e:
        logger.warn("--- [CLOSE][DB CONNECTION][ERROR]AsyncSession ---")
        logger.warn(e)
        raise e
    # The code following the yield statement is executed after the response has been delivered.
    finally:
        logger.info("--- [DB CONNECTION][CLOSE]AsyncSession ---")
        await session.close()