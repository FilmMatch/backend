from datetime import  datetime

from pydantic import BaseModel, ConfigDict

from Objects.Enums.UserType import UserType

from Objects.Enums.ItemStatus import ItemStatus 

class CreateItemSchema(BaseModel):
    name: str
    description: str
    price: float
    catalog_id: int

    class Config:
        from_attributes = True

class ItemSchema(BaseModel):
    name: str
    description: str
    catalog_id: int
    status: ItemStatus
    price: float
    class Config:
        from_attributes = True






