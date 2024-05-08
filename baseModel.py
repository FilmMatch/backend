from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import declarative_base

from database import Base



class DefaultModel(Base):
    created_at = Column(DateTime, default=func.now())

