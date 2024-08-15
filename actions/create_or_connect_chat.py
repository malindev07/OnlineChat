import requests


def create_chat(data: list[dict]):
    response_post = requests.post('http://127.0.0.1:8000/chats/chat_creation', json = data)
    
    data = response_post.json()
    
    return data


def connect_to_chat(chat_id: int):
    response_get = requests.get(f'http://127.0.0.1:8000/chats/return_chat', params = {'chat_id': chat_id})
    data = response_get.json()
    
    return data
