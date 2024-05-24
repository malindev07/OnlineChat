import json
from pathlib import Path

from auth.registration import check_user
from py_models.user_model import User


def authorization(login: str, password: str) -> User:
    user = User()
    user.login = login
    user.password = password
    
    file_path = Path.cwd().parent.joinpath('db_users.json')
    
    with open(file_path, 'r') as read_file:
        obj = json.load(read_file)
        res = filter(lambda person: person['login'] == user.login and person['password'] == user.password, obj['users'])
        
        if list(res):
            print('successful authorization')
        else:
            print('no such user')


authorization('Vlaimir', '1777723')
