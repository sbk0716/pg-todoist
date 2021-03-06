import pytest
from httpx import AsyncClient
import starlette.status

pytestmark = pytest.mark.asyncio


class TestCrudDones:
    async def test_done_flag(self, async_client: AsyncClient):
        print("###### execute test_done_flag ######")
        response = await async_client.post(
            "/api/tasks/", json={"title": "テストタスク2", "detail": "テストタスク2詳細", "status_type": 1}
        )
        assert response.status_code == starlette.status.HTTP_201_CREATED
        response_obj = response.json()
        assert response_obj["title"] == "テストタスク2"
        assert response_obj["detail"] == "テストタスク2詳細"
        assert response_obj["status_type"] == 1

        response = await async_client.post("/api/tasks/1/done/")
        assert response.status_code == starlette.status.HTTP_201_CREATED

        response = await async_client.post("/api/tasks/1/done/")
        assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST

        response = await async_client.delete("/api/tasks/1/done/")
        assert response.status_code == starlette.status.HTTP_200_OK

        response = await async_client.delete("/api/tasks/1/done/")
        assert response.status_code == starlette.status.HTTP_404_NOT_FOUND
