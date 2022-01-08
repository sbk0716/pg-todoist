import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from starlette.requests import Request
from api.db import get_db, Base
from api.main import app
import starlette.status
from api import environ
from fastapi import FastAPI

ASYNC_DB_URL = environ.ASYNC_DB_URL
MYSQL_DATABASE = environ.MYSQL_DATABASE
print(f"MYSQL_DATABASE: {MYSQL_DATABASE}")

# ?ASYNC_DB_URL = "sqlite+aiosqlite:///:memory"

@pytest.fixture
def app() -> FastAPI:
    from api.main import app
    return app


# @pytest.fixture
# def db(app: FastAPI) -> AsyncSession:
#     return app.state._db

@pytest.fixture
async def async_client(app: FastAPI) -> AsyncClient:
    '''
    Async用のengineとsessionを作成
    テスト用にオンメモリのSQLiteテーブルを初期化（関数ごとにリセット）
    DIを使ってFastAPIのDBの向き先をテスト用DBに変更
    テスト用に非同期HTTPクライアントを返却
    '''
    # Async用のengineとsessionを作成
    async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
    async_session = sessionmaker(
        autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession
    )

    # テスト用にオンメモリのSQLiteテーブルを初期化（関数ごとにリセット）
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


    # DIを使ってFastAPIのDBの向き先をテスト用DBに変更
    async def get_test_db(request: Request):
        session = async_session()
        app.state._db = session
        return request.app.state._db
        # async with async_session() as session:
        #     yield session

    app.dependency_overrides[get_db] = get_test_db

    # テスト用に非同期HTTPクライアントを返却
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client



@pytest.mark.asyncio
async def test_create_and_read(async_client):
    response = await async_client.post("/tasks", json={"title": "テストタスク"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["title"] == "テストタスク"

    response = await async_client.get("/tasks")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 1
    assert response_obj[0]["title"] == "テストタスク"
    assert response_obj[0]["done"] is False

@pytest.mark.asyncio
async def test_done_flag(async_client):
    response = await async_client.post("/tasks", json={"title": "テストタスク2"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["title"] == "テストタスク2"

    # 完了フラグを立てる
    response = await async_client.put("/tasks/1/done")
    assert response.status_code == starlette.status.HTTP_200_OK

    # 既に完了フラグが立っているので400を返却
    response = await async_client.put("/tasks/1/done")
    assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST

    # 完了フラグを外す
    response = await async_client.delete("/tasks/1/done")
    assert response.status_code == starlette.status.HTTP_200_OK

    # 既に完了フラグが外れているので404を返却
    response = await async_client.delete("/tasks/1/done")
    assert response.status_code == starlette.status.HTTP_404_NOT_FOUND
