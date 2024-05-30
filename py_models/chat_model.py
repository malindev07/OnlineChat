from dataclasses import dataclass, field
from itertools import count
from typing import List

from py_models.message_model import Message

from py_models.user_model import UserLogin, User, UserID

from storage.users_storage import UsersStorage


@dataclass(frozen = True, slots = True)
class ChatID:
    value: int


@dataclass
class Chat:
    id: ChatID = field(default_factory = count(1).__next__)
    users: [dict[UserID, UserLogin]] = field(default_factory = list)
    messages: List[Message] = field(default_factory = list)
    
    def add_user(self, user: User) -> [dict[UserID, UserLogin]]:
        self.users.append({user.id: user.login})
        return self.users
    
    def create_chat(self, current_users: [User], storage: UsersStorage):
        is_true: bool = True
        for current_user in current_users:
            if storage.search_user(current_user.login) is not None:
                continue
            else:
                is_true = False
                break
        if is_true:
            for user in current_users:
                self.add_user(user)
            return self
    
    def check_users_in_chat(self, current_users: [User]) -> bool:
        ids = []
        is_true: bool = True
        for current_id in current_users:
            ids.append(current_id.id)
        
        # print(ids)
        
        for user in self.users:
            for k in user:
                if k in ids:
                    # print(True)
                    continue
                else:
                    # print(False)
                    is_true = False
        
        return is_true
    
    def add_message(self, current_users: [User], msg: Message):
        if self.check_users_in_chat(current_users):
            self.messages.append(msg)
            # print(self.messages)
            return self.messages
        else:
            print('Не все пользователи находятся в чате')
