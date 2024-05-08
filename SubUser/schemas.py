from pydantic import BaseModel, ConfigDict


class SubUserCreate(BaseModel):
    name: str
    user_id: int

    class Config:
        from_attributes = True
