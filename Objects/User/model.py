from sqlalchemy import Column, Integer, String, Boolean, func, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime
from Objects.SubUser.model import SubUser

from database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    email = Column(String(16), unique=True, index=True)
    name = Column(String(16))
    surname1 = Column(String(16))
    surname2 = Column(String(16))
    phone = Column(String(16))
    password = Column(String(16))
    is_active = Column(Boolean, default=True)
    age = Column(Integer)
    subUsers = relationship("SubUser", back_populates="user", cascade="all, delete-orphan")


