from pydantic import BaseModel

class UserRegisterForm(BaseModel):
    email: str
    password: str
    nickname: str

class UserLoginForm(BaseModel):
    email: str
    password: str
