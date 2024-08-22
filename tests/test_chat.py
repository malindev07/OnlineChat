import pytest
import requests
from src.db_actions.actions_chat_db import create_chat_db, check_last_index_chat_db
from src.db_actions.actions_message_db import show_chat_msgs
from src.py_models.chat_model import Chat


@pytest.fixture
def users():
    users: list = [{
        "user_login": "1"
    }, {
        "user_login": "123123"
    }]
    return users


class TestChat:
    async def test_create_chat_db(self, users):
        response_post = requests.post('http://127.0.0.1:8000/chats/chat_creation', json = users)
        data = response_post.json()
        print(data)
        
        assert data is not None, 'Test is error'
