from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime,  Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, relationship


from database import Base


class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    subuser_id = Column(Integer, ForeignKey("subusers.id"))
    token = Column(String(256))

