from sqlalchemy.orm import Session
from fastapi import HTTPException

from User import schemas

from User.model import User as UserModel


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    # print("test")
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    # db_user = UserModel.User(**User.dict() is_active=False)
    db_user = UserModel(email=user.email, hashed_password=user.password, name=user.name, surname1=user.surname1,
                        surname2=user.surname2, age=user.age, phone=user.phone)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_user)
    db.commit()
    return db_user
