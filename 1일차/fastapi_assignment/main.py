from typing import Annotated
from fastapi import FastAPI, Path, HTTPException
from fastapi.responses import FileResponse
from app.models.users import UserModel
from app.schemas.users import UserCreateRequest, UserUpdateRequest, UsersearchRequest

app = FastAPI()

UserModel.create_dummy() # API 테스트를 위한 더미를 생성하는 메서드 입니다.

@app.get('/users')
def get_users(users: UserModel):
    if users.all() is None:
        raise HTTPException(status_code=404)
    return users.all()

@app.post('/users')
def create_user(data: UserCreateRequest):
    user = UserModel.create(**data.model_dump())
    return user.id

@app.get('/users/{user_id}')
def get_user(user_id:int = Path(gt=0)):
    if user_id in UserModel.all():
        return UserModel.get(id = user_id)
    else:
        raise HTTPException(status_code=404)

@app.patch('/users/{user_id}')
def edit_user(data = UserUpdateRequest, user_id: int = Path(gt=0)):
    user = UserModel.get(id = user_id)
    user.update(**data.model_dump())
    return user

@app.delete('/users/{user_id}')
def delete_user(user_id:int = Path(gt=0)):
    user = UserModel.get(id = user_id)
    user.delete()
    return f'deleted {user}'

@app.get('/users/search/{user_id}')
def search_user(data = UsersearchRequest, user_id:int = Path(gt=0)):
    user = data.get(id = user_id)
    if user is None:
        raise HTTPException(status_code=404)
    else:
        return user





if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)