from fastapi import APIRouter, Request

from action_handler.conv_pydantic_to_dataclass import convert_pyd_to_dataclass, convert_dataclass_to_pyd
from pydantic_models.pydantic_message_model import MessageEntryPydantic, MessageExitPydantic

message_router = APIRouter(prefix = "/message", tags = ["Messages"])


@message_router.post('/message_creation')
async def message_creation(req: Request, message: MessageEntryPydantic) -> MessageExitPydantic:
    convert_data = convert_pyd_to_dataclass(message)
    action = req.state.storage.message_storage.create_message(convert_data)
    return convert_dataclass_to_pyd(action)


@message_router.get('/message_storage')
async def show_message_storage(req: Request):
    return req.state.storage.message_storage.show_msg_storage()
