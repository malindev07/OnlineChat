from db_models.actions_user_db import insert_user, show_all_users_from_db, search_user_db, authorization_db
from py_models.user_model import UserLogin, User
from pydantic_models.pydantic_user_model import UserPydantic


class UsersStorage:
    
    @staticmethod
    async def create_user(new_user_pyd: UserPydantic) -> User | None | bool:
        if new_user_pyd.login == '':
            return False
        else:
            new_user = User(login = new_user_pyd.login, password = new_user_pyd.password)
            res = await insert_user(new_user)
            
            if res is not None:
                return new_user
            else:
                return res
        # searched_user = await self.search_user(new_user_pyd.login)
        # if searched_user is None:
        #     new_user = User(login = new_user_pyd.login, password = new_user_pyd.password)
        #     new_user.status = 'registered'
        #     self.users.append({new_user.login: new_user})
        #     print(new_user)
        #     return new_user
        #
        # elif not searched_user:
        #     print('Недопустимый логин')
        #     return False
        #
        # else:
        #     print(f'Такой пользователь уже зарегестрирован')
        #     return None
    
    # users: [dict[UserLogin, User]] = field(default_factory = list)
    # async def search_user(self, user: UserLogin) -> User | None | bool:
    #     for current_user in self.users:
    #         for k in current_user:
    #             if k == user:
    #                 searched_user = current_user[user]
    #                 print(searched_user)
    #                 return searched_user
    #     if user != '':
    #         return None
    #     else:
    #         return False
    @staticmethod
    async def show_all_users() -> [dict[UserLogin, User]]:
        res = await show_all_users_from_db()
        # print(res)
        return res
    
    @staticmethod
    async def user_authorization(user: UserPydantic):
        user_auth = User(login = user.login, password = user.password)
        res = await authorization_db(user_auth)
        return res
        
        # if searched_user is not None:
        #     if searched_user.password == user.password:
        #         return searched_user
        #     else:
        #         print(f'Для пользователя с логином {user.login} введен неверный пароль')
        #         return None
        # else:
        #     print('Пользователь не найден')
        #     return None
    
    @staticmethod
    async def search_user(user: UserLogin):
        res = await search_user_db(user)
        return res
    
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
