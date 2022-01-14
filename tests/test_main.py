import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine

# from sqlalchemy.ext.asyncio import create_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from api.domain.models.task import Base
import starlette.status
from api.core import environ
from fastapi import FastAPI
from databases import Database
from api.infra.db.connection import connect_to_db

DB_URL = environ.DB_URL
POSTGRES_DB = environ.POSTGRES_DB
print(f"POSTGRES_DB: {POSTGRES_DB}")

# ASYNC_DB_URL = "sqlite+aiosqlite:///:memory"


@pytest.fixture
async def app() -> FastAPI:
    from api.main import app

    print("###### execute connect_to_db ######")
    await connect_to_db(app)
    print(app.state._db)
    return app


# @pytest.fixture
# def db(app: FastAPI) -> Database:
#     return app.state._db


@pytest.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    engine = create_engine(DB_URL, echo=True)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client


@pytest.mark.asyncio
async def test_create_and_read(async_client):
    print("###### execute test_create_and_read ######")
    response = await async_client.post(
        "/api/tasks/", json={"title": "テストタスク2", "detail": "テストタスク2詳細"}
    )
    assert response.status_code == starlette.status.HTTP_201_CREATED
    # response_obj = response.json()
    # assert response_obj["title"] == "テストタスク2"
    # assert response_obj["detail"] == "テストタスク2詳細"

    # response = await async_client.post("/tasks", json={"title": "テストタスク"})
    # assert response.status_code == starlette.status.HTTP_200_OK
    # response_obj = response.json()
    # assert response_obj["title"] == "テストタスク"

    # response = await async_client.get("/tasks")
    # assert response.status_code == starlette.status.HTTP_200_OK
    # response_obj = response.json()
    # assert len(response_obj) == 1
    # assert response_obj[0]["title"] == "テストタスク"
    # assert response_obj[0]["done"] is False


@pytest.mark.asyncio
async def test_done_flag(async_client):
    print("###### execute test_done_flag ######")
    response = await async_client.post(
        "/api/tasks/", json={"title": "テストタスク2", "detail": "テストタスク2詳細"}
    )
    assert response.status_code == starlette.status.HTTP_201_CREATED
    # response_obj = response.json()
    # assert response_obj["title"] == "テストタスク2"
    # assert response_obj["detail"] == "テストタスク2詳細"
    # response_obj = response.json()
    # assert response_obj["title"] == "テストタスク2"

    # # 完了フラグを立てる
    # response = await async_client.post("/tasks/1/done")
    # assert response.status_code == starlette.status.HTTP_200_OK

    # # 既に完了フラグが立っているので400を返却
    # response = await async_client.post("/tasks/1/done")
    # assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST

    # # 完了フラグを外す
    # response = await async_client.delete("/tasks/1/done")
    # assert response.status_code == starlette.status.HTTP_200_OK

    # # 既に完了フラグが外れているので404を返却
    # response = await async_client.delete("/tasks/1/done")
    # assert response.status_code == starlette.status.HTTP_404_NOT_FOUND
