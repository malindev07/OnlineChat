import pytest

from src.db_actions.actions_user_db import insert_user, search_user_db, authorization_db, show_all_users_from_db

from src.py_models import User, UserLogin


@pytest.fixture
def users():
    users = [
        User(login = '1', password = '123'),
        User(login = '123123', password = '123'),
        User(login = '123123123', password = '123'),
    ]
    return users


@pytest.fixture
def user_login():
    user: UserLogin = '1'
    return user


@pytest.fixture
def user():
    user: User = User(login = '123123', password = '1123')
    return user


@pytest.mark.usefixtures('setup_db')
class TestUser:
    async def test_insert_user(self, users):
        for user in users:
            res = await insert_user(user)
            assert res == user, 'User in DB' + ' ' + user.login
    
    async def test_search_user_db(self, user_login):
        res = await search_user_db(user_login)
        
        assert res == True, 'Response is not True'
    
    async def test_authorization_db(self, user):
        res = await authorization_db(user)
        
        try:
            assert res.login == user.login and res.password == user.password
            print('Верная авторизация')
        except AttributeError:
            print('Неверная авторизация')
    
    async def test_show_all_users_from_db(self):
        res = await show_all_users_from_db()
        
        assert type(res) is list, 'Где-то ошибка и вернулся не список'
        for user_in_res in res:
            assert type(user_in_res) is dict, 'Где-то ошибка и вернулся не словарь'
