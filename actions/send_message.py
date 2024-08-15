import requests

from actions.create_or_connect_chat import connect_to_chat


def send_message_in_chat(data: dict):
    response_post = requests.post('http://127.0.0.1:8000/message/message_creation', json = data)
    
    data = response_post.json()
    
    return data


def check_msg_storage(id: int) -> int:
    res = connect_to_chat(id)
    
    return len(res[id]['messages'])
