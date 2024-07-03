from datetime import  datetime

from pydantic import BaseModel, ConfigDict

from Objects.Enums.UserType import UserType



class SubUserBase(BaseModel):
    id: int
    name: str
    user_id: int
    created_at: datetime
    type: UserType
    class Config:
        from_attributes = True

class SubUserCreate(BaseModel):
    name: str
    user_id: int
    type: UserType






