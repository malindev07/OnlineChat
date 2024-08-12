from fastapi import APIRouter, Request, Response
from starlette import status

from pydantic_models.pydantic_user_model import UserSearchPydanticDb

chat_router = APIRouter(prefix = "/chats", tags = ["Chats"])


@chat_router.post('/chat_creation')
async def chat_creation(req: Request, users: list[UserSearchPydanticDb]):
    res = await req.state.storage.chats_storage.create_chat(users)
    
    return res


@chat_router.get('/show_chats')
async def show_chats(req: Request):
    return req.state.storage.chats_storage.chats


@chat_router.get('/show_chat_msg_storage/{chat_id}')
async def show_chats(req: Request, chat_id: int) -> list:
    return req.state.storage.chats_storage.show_chat_msg(search_chat_id = chat_id)


@chat_router.post('/check_users_in_chat')
async def check_users_in_chat(req: Request, response: Response, users: list[UserSearchPydanticDb]) -> int:
    res = await req.state.storage.chats_storage.check_users_in_storage(users)
    
    if res is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response.status_code
    else:
        response.status_code = status.HTTP_200_OK
        return response.status_code
