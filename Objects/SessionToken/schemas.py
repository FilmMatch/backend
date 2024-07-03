from datetime import  datetime

from pydantic import BaseModel, ConfigDict




class SessionSchema(BaseModel):
    id: int
    token: str
    created_at: datetime
    subuser_id: int






