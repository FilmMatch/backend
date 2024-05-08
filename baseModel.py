from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

from database import Base



class BaseModel(Base):
    __tablename__ = "users"
    crated_at = Column(Integer, primary_key=True)
