from fastapi import APIRouter, Request

from action_handler.conv_pydantic_to_dataclass import convert_dataclass_chat_to_pyd
from pydantic_models.pydantic_chat_model import ChatPydantic
from pydantic_models.pydantic_user_model import UserSearchPydantic

chat_router = APIRouter(prefix = "/chats", tags = ["Chats"])


@chat_router.post('/chat_creation')
async def chat_creation(req: Request, users: list[UserSearchPydantic]) -> ChatPydantic | None | int:
    res = await req.state.storage.chats_storage.create_chat(users, req.state.storage.users_storage)
    
    if isinstance(res, int):
        return res
    else:
        return convert_dataclass_chat_to_pyd(res)


@chat_router.get('/show_chats')
async def show_chats(req: Request):
    return req.state.storage.chats_storage.chats


@chat_router.get('/show_chat_msg_storage')
async def show_chats(req: Request, chat_id: int) -> list:
    return req.state.storage.chats_storage.show_chat_msg(search_chat_id = chat_id)
# @chat_router.get('/chat')
# def get_chat_page(req:Request):
#     return req.state.
