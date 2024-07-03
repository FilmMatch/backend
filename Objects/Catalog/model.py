from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime,  Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, relationship
from Objects.Item.model import Item

from database import Base


class Catalog(Base):
    __tablename__ = "catalogs"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String(16), index=True)
    subuser_id = Column(Integer, ForeignKey("subusers.id"))

    items = relationship("Item", back_populates="catalog", cascade="all, delete-orphan")


