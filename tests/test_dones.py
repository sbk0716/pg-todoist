import pytest
import starlette.status

pytestmark = pytest.mark.asyncio

class TestCrudDones:
    async def test_done_flag(self, async_client):
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
