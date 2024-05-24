import json

from pathlib import *

from py_models.user_model import User


def check_user(user: User) -> [bool, User]:
    file_path = Path.cwd().parent.joinpath('db_users.json')
    
    with open(file_path, 'r') as read_file:
        obj = json.load(read_file)
        res = filter(lambda person: person['login'] == user.login, obj['users'])
        
        if list(res):
            user.hello_user()
            user.password = list(res)[1]['password']
            return [True, user]


def registration(login: str, password: str) -> User:
    user = User()
    user.login = login
    user.password = password
    
    if len(user.login) != 0 or len(user.password) != 0:
        if user.login.find(' ') != False and user.password.find(' ') != False:
            file_path = Path.cwd().parent.joinpath('db_users.json')
            
            with open(file_path, 'r') as read_file:
                
                obj = json.load(read_file)
                
                a = filter(lambda person: person['login'] == user.login, obj['users'])
                
                is_registered = check_user(user)
                if not is_registered:
                    print('Successful registration')
                    
                    with open(file_path, 'w') as outfile:
                        obj['users'].append(user.__dict__)
                        user.id = len(obj['users'])
                        json.dump(obj, outfile, indent = 4)
                        user.hello_user()
                        
                        return user
                else:
                    print('You are already registered')
    
    else:
        print('error login or password')
    
    return user
