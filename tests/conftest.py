import pytest
from fastapi import FastAPI
from databases import Database
from httpx import AsyncClient
from sqlalchemy import create_engine
from api.core import environ
from api.domain.models.task import Base
from api.infra.db.connection import connect_to_db

DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB
print(f"POSTGRES_DB: {POSTGRES_DB}")

@pytest.fixture
async def app() -> FastAPI:
    from api.main import app
    try:
        print("###### Set the connection pool to `app.state._db` ######")
        await connect_to_db(app)
        return app
    except Exception as e:
        print("--- [ERROR]connect_to_db ---")
        print(e)
        print("--- [ERROR]connect_to_db ---")
        raise e

# @pytest.fixture
# def db(app: FastAPI) -> Database:
#     return app.state._db


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    engine = create_engine(DB_URL, echo=True)
    # ================================================================================
    # Execute drop_all method | sqlalchemy.schema.MetaData.drop_all()
    # ================================================================================
    # Drop all tables stored in this metadata.
    Base.metadata.drop_all(bind=engine)
    # ================================================================================
    # Execute create_all method | sqlalchemy.schema.MetaData.create_all()
    # ================================================================================
    # Create all tables stored in this metadata.
    Base.metadata.create_all(bind=engine)
    # app: An ASGI application to send requests to, rather than sending actual network requests.
    # base_url: A URL to use as the base when building request URLs.
    async with AsyncClient(
        app=app,
        base_url="https://localhost:8000/",
    ) as client:
        try:
            print("--- [CONSTRUCT]AsyncClient ---")
            yield client
        except Exception as e:
            print("--- [ERROR]AsyncClient ---")
            print(e)
            print("--- [ERROR]AsyncClient ---")
            raise e
        finally:
            print("--- [CLOSE]AsyncClient ---")
            await client.aclose()