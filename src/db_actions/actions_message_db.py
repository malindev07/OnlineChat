import datetime
from logging import getLogger

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.db_models import Message as Message_DB, Chat as Chat_DB, User as User_DB
from src.db_config.db_helper import db_helper

logger_actions_messages_db = getLogger(__name__)


async def create_message_db(user_id: int, chat_id: int, text: str) -> dict:
    new_msg = Message_DB()
    new_msg.user_id = user_id
    new_msg.chat_id = chat_id
    new_msg.text = text
    new_msg.date = datetime.datetime.now()
    
    async with db_helper.session_factory() as session:
        async with db_helper.session_factory() as session_res:
            stmt = select(User_DB.login).where(User_DB.user_id == user_id)
            res = await session_res.execute(stmt)
            res_login = res.scalars().first()
            new_msg.user_login = res_login
            session.add(new_msg)
            
            await session.commit()
            logger_actions_messages_db.info('Message for chat id %s sent', chat_id)
            return {'user_login': res_login, 'text': text}


async def show_chat_msgs(chat_id: int) -> list[dict]:
    async with db_helper.session_factory() as session:
        stmt = select(Chat_DB).options(selectinload(Chat_DB.messages)).where(Chat_DB.chat_id == chat_id)
        
        result = await session.execute(stmt)
        chats = result.scalar()
        
        # for chat in chats:
        # print('**' * 10)
        # print(f'Chat id {chats.chat_id}, users = {chats.users}')
        # print(f'Сообщение в чате {chats.chat_id}')
        
        msg_storage = []
        for msg in chats.messages:
            msg_storage.append({msg.user_login: msg.text})
            # print(f' Пользователь {msg.user_login} написал : {msg.text}')
        
        return msg_storage

# asyncio.run(create_message_db(user_id = 2, chat_id = 2, text = 'Good!'))
# asyncio.run(show_chat_msgs(chat_id = 2))
