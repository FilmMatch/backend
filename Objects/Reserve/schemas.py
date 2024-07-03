from datetime import  datetime

from pydantic import BaseModel, ConfigDict
from Objects.Item import schemas as ItemSchema



class ReserveCreate(BaseModel):
    item_id: int


class ReserveSchema(BaseModel):
    created_at: datetime
    subuser_id: int
    item: ItemSchema.ItemSchema