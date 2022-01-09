import logging
from databases import Database
from fastapi import FastAPI
from api import environ

# Set the logging level of this logger for uvicorn.
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

# Define DB_URL
DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB

async def connect_to_db(app: FastAPI) -> None:
    """
    connect_to_db
    """
    try:
        logger.info(f"--- POSTGRES_DB: {POSTGRES_DB} ---")
        logger.info("--- [DB CONNECTION][CONSTRUCT]AsyncSession ---")
        database = Database(DB_URL, min_size=2, max_size=5)
        logger.info(database)
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- [DB CONNECTION][ERROR]AsyncSession ---")
        logger.warn(e)
        raise e

async def close_db_connection(app: FastAPI) -> None:
    """
    close_db_connection
    """
    try:
        logger.info(f"--- POSTGRES_DB: {POSTGRES_DB} ---")
        logger.info("--- [CLOSE][DB CONNECTION][CONSTRUCT]AsyncSession ---")
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- [CLOSE][DB CONNECTION][ERROR]AsyncSession ---")
        logger.warn(e)
        raise e
