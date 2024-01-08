from typing import Optional
from pydantic import BaseModel, EmailStr, Field 

#create user
class UserCreateModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

#update user
class UpdateUserModel(BaseModel):
    fullname: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

#success response
def ResponseModel(data, message):
    return {
        "data" : [data],
        "code" : 200,
        "message": message
    }

#error response
def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
        }