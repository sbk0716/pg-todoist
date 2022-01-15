import pytest
from httpx import AsyncClient
import starlette.status

pytestmark = pytest.mark.asyncio


class TestHealth:
    async def test_health_check(self, async_client: AsyncClient):
        print("###### execute test_health_check ######")
        response = await async_client.get("/api/healthcheck/")
        assert response.status_code == starlette.status.HTTP_200_OK
        response_obj = response.json()
        assert response_obj["message"] == "Container health check was successful!"
