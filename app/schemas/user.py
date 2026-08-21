# app/schemas/user.py
from pydantic import BaseModel, EmailStr, ConfigDict
import datetime

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    role: str = "USER"
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime.datetime

    model_config = ConfigDict(from_attributes=True)