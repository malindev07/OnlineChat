from sqlalchemy import select, update

from db_config.db_helper import db_helper
from py_models.chat_model import Chat
from py_models.user_model import UserLogin
from db_models import User as User_DB, Chat as Chat_DB


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
    print(res)
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
        # print('НЕльзяав создать с самим собой')
        return False
    else:
        # print('Chat is already created')
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


async def check_last_index_chat_db():
    async with db_helper.session_factory() as session_update:
        query = (
            select(Chat_DB.chat_id)
        )
        res = await session_update.execute(query)
        chats_ids_res = res.scalars().all()
        
        if not chats_ids_res:
            return 1
        
        return chats_ids_res[-1] + 1


async def return_chat_by_id_db(chat_id: int):
    async with db_helper.session_factory() as session:
        stmt = (
            select(Chat_DB).where(Chat_DB.chat_id == chat_id)
        )
        
        res = await session.execute(stmt)
        chat = res.scalar()
        
        print(chat)
        return chat

# asyncio.run(return_chat_by_id(chat_id = 2))
