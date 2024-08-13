from fastapi import APIRouter, Request

from action_handler.conv_pydantic_to_dataclass import convert_pyd_to_dataclass, convert_dataclass_to_pyd
from pydantic_models.pydantic_message_model import MessageEntryPydantic, MessageExitPydantic
from storage.message_storage import add_message_to_chat

message_router = APIRouter(prefix = "/message", tags = ["Messages"])


@message_router.post('/message_creation')
async def message_creation(req: Request, message: MessageEntryPydantic) -> MessageExitPydantic:
    res = await req.state.storage.message_storage.create_message(
        user_id = message.user_id, chat_id = message.user_id, text = message.text
    )
    
    return res
    # convert_data = await convert_pyd_to_dataclass(message)
    # action = await req.state.storage.message_storage.create_message(convert_data)
    # await add_message_to_chat(chat_storage = req.state.storage.chats_storage, message = action)
    # return await convert_dataclass_to_pyd(action)


@message_router.get('/message_storage')
async def show_message_storage(req: Request):
    return await req.state.storage.message_storage.show_msg_storage()
