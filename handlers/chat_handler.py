from fastapi import APIRouter, Request
from pydantic_models.pydantic_user_model import UserSearchPydantic

chat_router = APIRouter(prefix = "/chats", tags = ["Chats"])


@chat_router.post('/chat_creation')
async def chat_creation(req: Request, users: list[UserSearchPydantic]):
    return req.state.storage.chats_storage.create_chat(users, req.state.storage.users_storage)

# @chat_router.post('/chat_check')
# async def chat_creation(req: Request, users: list[UserSearchPydantic]):
#     return req.state.storage.chats_storage.is_chat_created(users, req.state.storage.users_storage)
