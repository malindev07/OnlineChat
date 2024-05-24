import dataclasses


class User:
    id: int
    login: str
    password: str
    
    def hello_user(self):
        print(f'Hello, {self.login}')
