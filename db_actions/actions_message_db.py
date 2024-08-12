import asyncio
import datetime

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from db_models import Message as Message_DB, Chat as Chat_DB
from db_config.db_helper import db_helper


async def create_message_db(user_id: int, chat_id: int, text: str):
    new_msg = Message_DB()
    new_msg.user_id = user_id
    new_msg.chat_id = chat_id
    new_msg.text = text
    new_msg.date = datetime.datetime.now()
    
    async with db_helper.session_factory() as session:
        session.add(new_msg)
        await session.commit()


async def show_chat_msgs(chat_id: int):
    async with db_helper.session_factory() as session:
        stmt = select(Chat_DB).options(selectinload(Chat_DB.messages)).where(Chat_DB.chat_id == chat_id)
        
        result = await session.execute(stmt)
        chats = result.scalars()
        
        for chat in chats:
            print('**' * 10)
            print(f'Chat id {chat.chat_id}, users = {chat.users}')
            print(f'Сообщение в чате {chat.chat_id}')
            
            for msg in chat.messages:
                print(f' Пользователь {msg.user_id} написал : {msg.text}')


# asyncio.run(create_message_db(user_id = 2, chat_id = 2, text = 'Good!'))
asyncio.run(show_chat_msgs(chat_id = 2))
