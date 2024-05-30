from dataclasses import dataclass, field

from py_models.chat_model import ChatID, Chat


@dataclass
class ChatsStorage:
    chats: [dict[ChatID, Chat]] = field(default_factory = list)
    
    def add_chat(self, new_chat: Chat) -> [dict[ChatID, Chat]]:
        self.chats.append({new_chat.id: new_chat})
    
    def search_chat(self, chat_id: ChatID) -> Chat | None:
        for current_chat in self.chats:
            for current_id in current_chat:
                if current_id == chat_id:
                    return current_chat
        return None
