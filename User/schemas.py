from pydantic import BaseModel, ConfigDict


from typing import List

from datetime import datetime


from SubUser.schemas import SubUserBase


class UserLogin(BaseModel):
    email: str
    password: str


class UserBase(BaseModel):
    email: str

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    password: str
    age: int
    name: str
    surname1: str
    surname2: str
    phone: str



class User(UserBase):
    is_active: bool
    id: int
    age: int
    name: str
    surname1: str
    surname2: str
    phone: str
    created_at: datetime
    subUsers: List[SubUserBase]


