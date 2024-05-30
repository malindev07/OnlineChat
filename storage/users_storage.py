from dataclasses import dataclass, field

from py_models.user_model import UserLogin, User


@dataclass
class UsersStorage:
    users: [dict[UserLogin, User]] = field(default_factory = list)
    
    def search_user(self, user: UserLogin) -> dict[UserLogin, User] | None:
        for current_user in self.users:
            for k in current_user:
                if k == user:
                    return current_user
        
        return None
    
    def add_user(self, new_user: User) -> [dict[UserLogin, User]]:
        self.users.append({new_user.login: new_user})
        return self.users
