import requests


def send_message_in_chat(data: dict):
    response_post = requests.post('http://127.0.0.1:8000/message/message_creation', json = data)
    
    data = response_post.json()
    print(data)
    return data
