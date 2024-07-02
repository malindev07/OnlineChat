import contextlib

import uvicorn

from fastapi import FastAPI

from handlers.user_handler import user_router
from handlers.chat_handler import chat_router
from storage.chats_storage import ChatsStorage
from storage.storage import Storage
from storage.users_storage import UsersStorage


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    users_storage = UsersStorage()
    chats_storage = ChatsStorage()
    
    storage = Storage(users_storage = users_storage, chats_storage = chats_storage)
    
    yield {'storage': storage}


app = FastAPI(lifespan = lifespan)

app.include_router(user_router)
app.include_router(chat_router)

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    uvicorn.run("main:app")
