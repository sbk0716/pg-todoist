import pytest
from fastapi import HTTPException
from httpx import AsyncClient
import starlette.status
import json
import random

json_open = open("./tests/test_data.json", "r")
json_data = json.load(json_open)
test_data_list = sorted(json_data, key=lambda x: x["id"])

pytestmark = pytest.mark.asyncio


class TestCrudTasks:
    async def test_create_task_and_read_task(self, async_client: AsyncClient):
        print("###### execute test_create_task_and_read_task ######")
        test_data_list_len = len(test_data_list)
        i = random.randrange(test_data_list_len - 1)
        test_data = test_data_list[i]
        post_param = {
            "title": test_data["title"],
            "detail": test_data["detail"],
        }
        post_resp = await async_client.post("/api/tasks/", json=post_param)
        assert post_resp.status_code == starlette.status.HTTP_201_CREATED
        post_resp_obj = post_resp.json()
        assert post_resp_obj["title"] == test_data["title"]
        assert post_resp_obj["detail"] == test_data["detail"]
        get_resp = await async_client.get("/api/tasks/1/")
        assert get_resp.status_code == starlette.status.HTTP_200_OK
        get_resp_obj = get_resp.json()
        assert get_resp_obj["title"] == test_data["title"]
        assert get_resp_obj["detail"] == test_data["detail"]
        assert get_resp_obj["done"] is False

    async def test_create_task_and_update_task(self, async_client: AsyncClient):
        print("###### execute test_create_task_and_update_task ######")
        test_data_list_len = len(test_data_list)
        i = random.randrange(test_data_list_len - 1)
        test_data = test_data_list[i]
        post_param = {
            "title": test_data["title"],
            "detail": test_data["detail"],
        }
        post_resp = await async_client.post("/api/tasks/", json=post_param)
        assert post_resp.status_code == starlette.status.HTTP_201_CREATED
        post_resp_obj = post_resp.json()
        assert post_resp_obj["title"] == test_data["title"]
        assert post_resp_obj["detail"] == test_data["detail"]

        put_param = {
            "title": "[UPDATE]テストタスク1",
            "detail": "[UPDATE]テストタスク1詳細",
        }
        put_resp = await async_client.put("/api/tasks/1/", json=put_param)
        assert put_resp.status_code == starlette.status.HTTP_200_OK
        put_resp_obj = put_resp.json()
        assert put_resp_obj["title"] == "[UPDATE]テストタスク1"
        assert put_resp_obj["detail"] == "[UPDATE]テストタスク1詳細"

    async def test_create_task_and_delete_task(self, async_client: AsyncClient):
        print("###### execute test_create_task_and_delete_task ######")
        test_data_list_len = len(test_data_list)
        i = random.randrange(test_data_list_len - 1)
        test_data = test_data_list[i]
        post_param = {
            "title": test_data["title"],
            "detail": test_data["detail"],
        }
        post_resp = await async_client.post("/api/tasks/", json=post_param)
        assert post_resp.status_code == starlette.status.HTTP_201_CREATED
        post_resp_obj = post_resp.json()
        assert post_resp_obj["title"] == test_data["title"]
        assert post_resp_obj["detail"] == test_data["detail"]

        delete_resp = await async_client.delete("/api/tasks/1/")
        assert delete_resp.status_code == starlette.status.HTTP_200_OK
        delete_resp_obj = delete_resp.json()
        assert delete_resp_obj["title"] == test_data["title"]
        assert delete_resp_obj["detail"] == test_data["detail"]

    async def test_create_all_task_and_read_all_task(self, async_client: AsyncClient):
        print("###### execute test_create_all_task_and_read_all_task ######")
        test_data_list_len = len(test_data_list)
        for i in range(test_data_list_len):
            test_data = test_data_list[i]
            post_param = {
                "title": test_data["title"],
                "detail": test_data["detail"],
            }
            post_resp = await async_client.post("/api/tasks/", json=post_param)
            assert post_resp.status_code == starlette.status.HTTP_201_CREATED
            post_resp_obj = post_resp.json()
            assert post_resp_obj["title"] == test_data["title"]
            assert post_resp_obj["detail"] == test_data["detail"]

            get_resp = await async_client.get(f"/api/tasks/{i+1}/")
            assert get_resp.status_code == starlette.status.HTTP_200_OK
            get_resp_obj = get_resp.json()
            assert get_resp_obj["title"] == test_data["title"]
            assert get_resp_obj["detail"] == test_data["detail"]
            assert get_resp_obj["done"] is False

        get_all_resp = await async_client.get("/api/tasks/")
        assert get_all_resp.status_code == starlette.status.HTTP_200_OK
        get_resp_obj_list = get_all_resp.json()
        assert len(get_resp_obj_list) == test_data_list_len
        get_resp_obj_list_len = len(get_resp_obj_list)

        for i in range(get_resp_obj_list_len):
            sorted_list = sorted(get_resp_obj_list, key=lambda x: x["id"])
            response_obj = sorted_list[i]
            test_data = test_data_list[i]
            assert response_obj["title"] == test_data["title"]
            assert response_obj["detail"] == test_data["detail"]
            assert response_obj["done"] is False
