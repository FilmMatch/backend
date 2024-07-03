from datetime import  datetime

from pydantic import BaseModel, ConfigDict
from Objects.Item.schemas import ItemSchema
from Objects.Enums.UserType import UserType



class CatalogCreateSchema(BaseModel):
    id: int
    name: str
    subuser_id: int

class CatalogSchema(BaseModel):
    id: int
    name: str
    subuser_id: int
    created_at: datetime
    items: list[ItemSchema]
    class Config:
        from_attributes = True







