from datetime import datetime
from pydantic import BaseModel, EmailStr, constr


class User(BaseModel):
    email: str
    password: str



class UserResponseAuth(User):
    status_code: str
    email: str
    pass