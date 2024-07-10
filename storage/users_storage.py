from dataclasses import dataclass, field

from py_models.user_model import UserLogin, User
from pydantic_models.pydantic_user_model import UserPydantic


@dataclass
class UsersStorage:
    users: [dict[UserLogin, User]] = field(default_factory = list)
    
    async def add_user(self, new_user_pyd: UserPydantic) -> User:
        
        searched_user = await self.search_user(new_user_pyd.login)
        
        if searched_user is None:
            
            new_user = User(login = new_user_pyd.login, password = new_user_pyd.password)
            new_user.status = 'registered'
            self.users.append({new_user.login: new_user})
            print(new_user)
            return new_user
        
        else:
            print(searched_user)
            return searched_user
    
    async def search_user(self, user: UserLogin) -> User | None:
        for current_user in self.users:
            for k in current_user:
                if k == user:
                    searched_user = current_user[user]
                    print(searched_user)
                    return searched_user
        
        return None
    
    async def authorization(self, user: UserPydantic) -> User | None:
        searched_user = await self.search_user(user.login)
        
        if searched_user is not None:
            if searched_user.password == user.password:
                return searched_user
            else:
                print(f'Для пользователя с логином {user.login} введен неверный пароль')
                return None
        else:
            print('Пользователь не найден')
            return None
    
    async def show_all_users(self) -> [dict[UserLogin, User]]:
        return self.users
    
    async def delete_user(self, user_login: UserLogin):
        for user in self.users:
            for key in user:
                if key == user_login:
                    user[key].status = 'deleted'
                    self.users.remove(user)
                    return user
    
    async def change_user_login(self, old_login: UserLogin, new_login: UserLogin) -> User | None:
        search_user = await self.search_user(old_login)
        
        if search_user is not None:
            search_user.login = new_login
            for user in self.users:
                for key in user:
                    if key == old_login:
                        if search_user.old_logins is None:
                            search_user.old_logins = [old_login]
                        else:
                            search_user.old_logins.append(old_login)
                        
                        self.users.remove(user)
                        self.users.append({search_user.login: search_user})
                        
                        return search_user
        else:
            print('No')
            return None
