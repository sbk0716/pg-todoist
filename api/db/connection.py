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
        logger.info(f"--- POSTGRES_DB: {POSTGRES_DB} ---")
        logger.info("--- [DB CONNECTION][CONNECT] ---")
        database: Database = Database(DB_URL, min_size=2, max_size=5)
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- [DB CONNECTION][CONNECT][ERROR] ---")
        logger.warn(e)
        raise e

async def close_db_connection(app: FastAPI) -> None:
    """
    Close the database connection.
    """
    try:
        logger.info(f"--- POSTGRES_DB: {POSTGRES_DB} ---")
        logger.info("--- [DB CONNECTION][DISCONNECT] ---")
        database: Database = app.state._db
        await database.disconnect()
    except Exception as e:
        logger.warn("--- [DB CONNECTION][DISCONNECT][ERROR] ---")
        logger.warn(e)
        raise e
