from pydantic import BaseModel
from enum import Enum

class GenderEnum(str, Enum):
    male = 'male'
    female = 'female'

class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum

class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None

class UsersearchRequest(BaseModel):
    user_id: int
    username: str | None = None
    age: int | None = None
    gender: GenderEnum
