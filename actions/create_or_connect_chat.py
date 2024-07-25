import requests


def create_chat(data: list[dict]):
    response_post = requests.post('http://127.0.0.1:8000/chats/chat_creation', json = data)
    
    data = response_post.json()
    print(data)
    return data


def connect_to_chat(id: str):
    response_get = requests.get('http://127.0.0.1:8000/chats/show_chats')
    data = response_get.json()
    
    for item in data:
        if id in item.keys():
            return item
