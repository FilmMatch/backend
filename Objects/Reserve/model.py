from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime,  Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, relationship

from Objects.Enums.UserType import UserType
from database import Base
from Objects.Item.model import Item


class Reserve(Base):
    __tablename__ = "reserves"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    subuser_id = Column(Integer, ForeignKey("subusers.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
    item = relationship("Item", foreign_keys=[item_id])