import pytest
from httpx import AsyncClient


class TestRoot:
    @pytest.mark.asyncio
    async def test_root(self, client: AsyncClient):
        response = await client.get("/")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
