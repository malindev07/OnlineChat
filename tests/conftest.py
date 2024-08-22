import asyncio

import pytest

from src.db_config.db_helper import start


@pytest.fixture(scope = "session", autouse = True)
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope = "class")
async def setup_db():
    print('\nПеред созданием БД')
    await start()
    print('После созданием БД')
