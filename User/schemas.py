from pydantic import BaseModel, ConfigDict

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


