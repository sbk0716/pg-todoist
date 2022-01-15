import pytest
import starlette.status

pytestmark = pytest.mark.asyncio

class TestCrudTasks:
    async def test_create_and_read(self, async_client):
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
