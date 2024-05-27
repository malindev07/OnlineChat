import json
from pathlib import Path
from typing import List

from py_models.chat_model import Chat, Message
from py_models.user_model import User


def create_chat(user_1, user_2: User) -> Chat:
    new_chat = Chat()
    
    file_path_chats = Path.cwd().parent.joinpath('db_chats.json')
    
    file_path_users = Path.cwd().parent.joinpath('db_users.json')
    
    with open(file_path_users, 'r') as read_file_users:
        obj = json.load(read_file_users)
        
        search_first_user = [*filter(lambda person: person['login'] == user_1.login, obj['users'])]
        search_second_user = [*filter(lambda person: person['login'] == user_2.login, obj['users'])]
        
        if search_first_user and search_second_user:
            new_chat.users = [*search_first_user, *search_second_user]
            
            with open(file_path_chats, 'r') as read_file_chats:
                
                obj = json.load(read_file_chats)
                search_chat = [*filter(lambda chat: chat['users'] == new_chat.users, obj['chats'])]
                
                if search_chat:
                    print('Такой чат уже существует')
                    print(json.dumps(search_chat, indent = 2))
                else:
                    new_chat.id = len(obj['chats']) + 1
                    
                    with open(file_path_chats, 'w') as outfile:
                        obj['chats'].append(new_chat.__dict__)
                        json.dump(obj, outfile, indent = 2)
                        print('Чат создан')
                        print(json.dumps(new_chat.__dict__, indent = 2))
        
        
        else:
            print('no such user')
    
    return new_chat


user1 = User()
user1.login = 'Vladimir'

user2 = User()
user2.login = 'Lid'
create_chat(user2, user1)
