from fastapi import APIRouter, Request, Response
from starlette import status

from pydantic_models.pydantic_user_model import UserPydantic, UserSearchPydantic

user_router = APIRouter(prefix = "/users", tags = ["Users"])


@user_router.post('/user_registration')
async def user_registration_handler(req: Request, response: Response, user: UserPydantic) -> UserPydantic | int:
    res = await req.state.storage.users_storage.add_user(user)
    
    if res is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response.status_code
    
    elif not res:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return response.status_code
    else:
        return await user.convert_to_ReturnModel(res)


@user_router.get('/users_get')
async def get_users_handler(req: Request):
    return await req.state.storage.users_storage.show_all_users()


@user_router.post('/user_authorization')
async def user_authorization_handler(req: Request, response: Response, user: UserPydantic) -> UserPydantic | int:
    if await req.state.storage.users_storage.authorization(user) is not None:
        return await user.convert_to_ReturnModel(await req.state.storage.users_storage.authorization(user))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return response.status_code


@user_router.post('/user_search')
async def user_search_handler(req: Request, user: UserSearchPydantic) -> UserSearchPydantic:
    return await user.convert_to_search_model(await req.state.storage.users_storage.search_user(user.login))


@user_router.delete('/delete_user')
async def user_search_handler(req: Request, user: UserSearchPydantic):
    return await req.state.storage.users_storage.delete_user(user.login)


@user_router.post('/change_user_login')
async def user_change_login(req: Request, old_login: UserSearchPydantic,
                            new_login: UserSearchPydantic) -> UserSearchPydantic:
    return await new_login.convert_to_search_model(
        await req.state.storage.users_storage.change_user_login(old_login = old_login.login,
                                                                new_login = new_login.login))
