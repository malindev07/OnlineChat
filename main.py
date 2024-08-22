import contextlib

import uvicorn

from fastapi import FastAPI

from src.handlers.message_handler import message_router
from src.handlers import user_router
from src.handlers.chat_handler import chat_router
from src.logger import logger
from src.storage import ChatsStorage
from src.storage import MessageStorage
from src.storage import Storage
from src.storage.users_storage import UsersStorage


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    users_storage = UsersStorage()
    chats_storage = ChatsStorage()
    message_storage = MessageStorage()
    
    storage = Storage(users_storage = users_storage, chats_storage = chats_storage, message_storage = message_storage)
    
    yield {'storage': storage}


app = FastAPI(lifespan = lifespan)

app.include_router(user_router)
app.include_router(chat_router)
app.include_router(message_router)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    try:
        logger.info('server started')
        uvicorn.run("main:app")
    except KeyboardInterrupt:
        logger.info('server closed')
        pass
# mypy попрпаить

# tests

# logger разобраться
