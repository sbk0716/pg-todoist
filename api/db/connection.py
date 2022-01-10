from fastapi import FastAPI
from databases import Database
from api.core import environ
from api.core.logging import logger

DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB


async def connect_to_db(app: FastAPI) -> None:
    """
    Connect to the database
    """
    try:
        logger.info(f"--- [CONNECT][POSTGRES_DB: {POSTGRES_DB}] ---")
        database: Database = Database(DB_URL, min_size=2, max_size=5)
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn(f"--- [ERROR][CONNECT][POSTGRES_DB: {POSTGRES_DB}] ---")
        logger.warn(e)
        raise e


async def close_db_connection(app: FastAPI) -> None:
    """
    Close the database connection.
    """
    try:
        logger.info(f"--- [DISCONNECT][POSTGRES_DB: {POSTGRES_DB}] ---")
        database: Database = app.state._db
        await database.disconnect()
    except Exception as e:
        logger.warn(f"--- [ERROR][DISCONNECT][POSTGRES_DB: {POSTGRES_DB}] ---")
        logger.warn(e)
        raise e
