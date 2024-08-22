import pytest

from src.db_actions.actions_message_db import create_message_db, show_chat_msgs


@pytest.fixture
def chat_id():
    chat_id = 1
    return chat_id


@pytest.fixture
def user_id():
    user_id = 3
    return user_id


@pytest.fixture
def text_msg():
    text = 'Hello'
    return text


class TestMessages:
    
    async def test_create_message_db(self, user_id, chat_id, text_msg):
        res = await create_message_db(user_id = user_id, chat_id = chat_id, text = text_msg)
        
        assert type(res) is dict, 'Ошибка'
    
    async def test_show_chat_msgs(self, chat_id):
        # try:
        res = await show_chat_msgs(chat_id = chat_id)
        assert type(res) is list, 'Вернулся не список'
    # except AttributeError:
    #     print('Chat is not defined')
