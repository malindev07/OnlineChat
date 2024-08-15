from sqlalchemy import select

from db_config.db_helper import db_helper

from py_models.user_model import User as User_PY, UserLogin
from db_models import User as User_DB


# Регистраия пользователя
async def insert_user(user_py: User_PY) -> None | User_PY:
    searched_user = await search_user_db(user_py.login)
    if searched_user is None:
        async with db_helper.session_factory() as session:
            user_db = User_DB()
            user_db.login = user_py.login
            user_db.password = user_py.password
            user_db.status = 'registered'
            
            session.add(user_db)
            
            await session.commit()
            return user_py
    else:
        print('User in DB')
        return None


# Поиск пользователя по логину
async def search_user_db(user: UserLogin) -> bool | None:
    async with db_helper.session_factory() as session:
        query = select(User_DB).where(User_DB.login == user)
        
        res = await session.execute(query)
        user_res = res.scalar()
        
        if user_res is not None:
            return True
        else:
            return None


# Авторизация
async def authorization_db(user: User_PY) -> User_PY | None | bool:
    searched_user = await search_user_db(user.login)
    
    if searched_user:
        async with db_helper.session_factory() as session:
            query = select(User_DB).where((User_DB.login == user.login) & (User_DB.password == user.password))
            res = await session.execute(query)
            user_res = res.scalar()
            
            if user_res is not None:
                user = User_PY(
                    id = user_res.user_id,
                    login = user_res.login,
                    password = user_res.password,
                    status = user_res.status,
                    chats_id = user_res.chats_id,
                    old_logins = user_res.old_logins
                )
                # accept auth
                return user
            else:
                # incorrect password for user
                return False
    else:
        # user is not found
        return None


# Показываем все пользовтаелей в чате
async def show_all_users_from_db():
    users = []
    
    async with db_helper.session_factory() as session:
        query = select(User_DB)
        res = await session.execute(query)
        
        users_res = res.scalars().all()
        
        for row in users_res:
            user = User_PY(
                id = row.user_id,
                login = row.login,
                password = row.password,
                status = row.status,
                chats_id = row.chats_id,
                old_logins = row.old_logins
            )
            
            users.append({user.login: user})
        
        return users


async def search_user_by_id(user_id: int):
    pass
