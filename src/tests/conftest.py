import traceback
from collections.abc import Callable

import pytest
from asgi_lifespan import LifespanManager
from fastapi import FastAPI
from httpx import AsyncClient

from app import create_app


async def load_server(create_app: Callable[[], FastAPI]):
    try:
        app = create_app()
        """Async server client that handles lifespan and teardown"""
        async with LifespanManager(app):
            yield app
    except Exception:
        traceback.print_exc()
    finally:
        pass


async def load_client(server: FastAPI):
    async with AsyncClient(app=server, base_url="http://test") as _client:
        yield _client


@pytest.fixture(scope="function", autouse=True)
async def server():
    async for _server in load_server(create_app):
        yield _server


@pytest.fixture(scope="function")
async def client(server):
    async for _client in load_client(server):
        yield _client
