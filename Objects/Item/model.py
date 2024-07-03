from datetime import datetime
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey, DateTime,  Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, relationship
from  Objects.Enums.ItemStatus import ItemStatus

from database import Base


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    catalog_id = Column(Integer, ForeignKey("catalogs.id"))
    name = Column(String(16))
    description = Column(String(255))
    subuser_id = Column(Integer, ForeignKey("subusers.id"))
    price = Column(Float)
    status = Column(SQLAlchemyEnum(ItemStatus), default=ItemStatus.published)
    catalog = relationship("Catalog", back_populates="items")

