from fastapi import APIRouter, Request

from pydantic_models.pydantic_user_model import UserPydantic, UserSearchPydantic

user_router = APIRouter(prefix = "/users", tags = ["Users"])


@user_router.post('/user_registration')
async def user_registration_handler(req: Request, user: UserPydantic) -> UserPydantic:
    return user.convert_to_ReturnModel(req.state.storage.users_storage.add_user(user))


@user_router.get('/users_get')
async def get_users_handler(req: Request):
    return req.state.storage.users_storage.show_all_users()


@user_router.post('/user_authorization')
async def user_authorization_handler(req: Request, user: UserPydantic) -> UserPydantic:
    return user.convert_to_ReturnModel(req.state.storage.users_storage.authorization(user))


@user_router.post('/user_search')
async def user_search_handler(req: Request, user: UserSearchPydantic) -> UserSearchPydantic:
    return user.convert_to_search_model(req.state.storage.users_storage.search_user(user.login))
