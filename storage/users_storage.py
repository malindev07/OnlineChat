from dataclasses import dataclass, field

from py_models.user_model import UserLogin, User
from pydantic_models.pydantic_user_model import UserPydantic


@dataclass
class UsersStorage:
    users: [dict[UserLogin, User]] = field(default_factory = list)
    
    def add_user(self, new_user_pyd: UserPydantic) -> User:
        
        searched_user = self.search_user(new_user_pyd.login)
        
        if searched_user is None:
            
            new_user = User(login = new_user_pyd.login, password = new_user_pyd.password)
            new_user.status = 'registered'
            self.users.append({new_user.login: new_user})
            print(new_user)
            return new_user
        
        else:
            print(searched_user)
            return searched_user
    
    def search_user(self, user: UserLogin) -> User | None:
        for current_user in self.users:
            for k in current_user:
                if k == user:
                    searched_user = current_user[user]
                    print(searched_user)
                    return searched_user
        
        return None
    
    def authorization(self, user: UserPydantic) -> User | None:
        searched_user = self.search_user(user.login)
        
        if searched_user is not None:
            if searched_user.password == user.password:
                return searched_user
            else:
                print(f'Для пользователя с логином {user.login} введен неверный пароль')
                return None
        else:
            print('Пользователь не найден')
            return None
    
    def show_all_users(self) -> [dict[UserLogin, User]]:
        return self.users
