from dataclasses import dataclass, field
from datetime import datetime

from py_models.user_model import UserLogin, UserID, User


@dataclass(frozen = True, slots = True)
class MessageText:
    msg_text: str


@dataclass(frozen = False, slots = True)
class Message:
    user: UserLogin
    user_id: UserID
    msg_text: MessageText
    created_at: datetime = field(default_factory = datetime.utcnow)
    
    # def create_message(self, current_user: User, txt: MessageText):
    #     self.user = current_user.login
    #     self.user_id = current_user.id
    #     self.msg_text = txt
    #     pass
