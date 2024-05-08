from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime,  Enum as SQLAlchemyEnum
from sqlalchemy.orm import declarative_base, relationship


from Enums.UserType import UserType
from database import Base
class SubUser(Base):
    __tablename__ = "subusers"
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    name = Column(String(16), index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    type = Column(SQLAlchemyEnum(UserType), nullable=False, default=UserType.User)
    user = relationship("User", back_populates="subUsers")

