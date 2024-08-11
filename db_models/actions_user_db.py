import asyncio

from sqlalchemy import select, update, ARRAY

from db_models.db_helper import db_helper
from py_models.chat_model import Chat
from py_models.user_model import User as User_PY, UserLogin
from db_models import User as User_DB, Chat as Chat_DB


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


## Првоеряем состоят ли пользователи уже в чате
async def check_chat_in_users_db(users: list[UserLogin]) -> None | int | bool:
    if len(set(users)) < len(users):
        ## нельзясоздать чат с самим собой
        return False
    
    async with db_helper.session_factory() as session:
        users_chats_id = []
        for user in users:
            query = select(User_DB.chats_id).where(User_DB.login == user)
            res = await session.execute(query)
            ## Получаем список чатов
            chats_res = res.scalar()
            
            if chats_res is None:
                chats_res = []
            
            for chat_id in chats_res:
                users_chats_id.append(chat_id)
        
        chat_id = await check_repeat_elem(users_chats_id)
        
        return chat_id


### Првоеряем состоят ли пользователи уже в чате
async def check_repeat_elem(elems: list) -> int | None:
    count = 0
    for x in elems:
        for y in elems:
            if x == y:
                count += 1
        if count > 1:
            return x
        else:
            count = 0
    # нет общих чатов
    return None


async def check_users_in_storage():
    pass


# asyncio.run(check_chat_in_users_db(['123', '1']))

async def create_chat_db(chat: Chat):
    res = await check_chat_in_users_db(chat.users)
    
    if res is None:
        async with db_helper.session_factory() as session:
            new_chat = Chat_DB()
            new_chat.chat_id = chat.id
            new_chat.users = chat.users
            
            for user in chat.users:
                await add_chat_id_to_user(user = user, chat_id = chat.id)
            
            session.add(new_chat)
            await session.commit()
            return chat
    
    elif not res:
        print('НЕльзяав создать с самим собой')
        return False
    else:
        print('Chat is already created')
        return res


async def add_chat_id_to_user(user: UserLogin, chat_id: int):
    async with db_helper.session_factory() as session:
        query = select(User_DB.chats_id).where(User_DB.login == user)
        res = await session.execute(query)
        
        chats_id = res.scalar()
        if chats_id is None:
            chats_id = []
        
        chats_id.append(chat_id)
        print(chats_id)
        
        async with db_helper.session_factory() as session_update:
            stmt = (
                select(User_DB).where(User_DB.login == user)
            )
            res = await session_update.execute(stmt)
            chats_res = res.scalar()
            chats_res.chats_id = chats_id
            stmt = update(User_DB).where(User_DB.login == user).values(chats_id = chats_id)
            await session.execute(stmt)
            await session.commit()

# asyncio.run(add_chat_id_to_user(user = '123', chat_id = 1))
