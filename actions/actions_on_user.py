import requests


def reg_rest(data: dict) -> dict | int:
    response_post = requests.post('http://127.0.0.1:8000/users/user_registration', json = data)
    
    data = response_post.json()
    
    return data


def auth_rest(data: dict) -> dict | int:
    response_post = requests.post('http://127.0.0.1:8000/users/user_authorization', json = data)
    
    data = response_post.json()
    
    return data
