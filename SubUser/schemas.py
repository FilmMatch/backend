from datetime import  datetime

from pydantic import BaseModel, ConfigDict



class SubUserBase(BaseModel):
    name: str
    user_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class SubUserCreate(BaseModel):
    name: str
    user_id: int






