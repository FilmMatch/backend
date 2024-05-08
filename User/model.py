from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, relationship

from database import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(16), unique=True, index=True)
    name = Column(String(16))
    surname1 = Column(String(16))
    surname2 = Column(String(16))
    phone = Column(String(16))
    hashed_password = Column(String(16))
    is_active = Column(Boolean, default=True)
    age = Column(Integer)
    subUsers = relationship("SubUser", back_populates="user")



