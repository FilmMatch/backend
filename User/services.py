from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from fastapi import HTTPException

from User import schemas

from User.model import User as UserModel


def get_user(user_id: int):
    return db.session.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_email(email: str):
    return db.session.query(UserModel).filter(UserModel.email == email).first()


def get_users(skip: int = 0, limit: int = 100):
    # print("test")
    return db.session.query(UserModel).offset(skip).limit(limit).all()

def get_user_by_id(user_id: int):
    user = db.session.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return user

# test
def create_user(user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    # db_user = UserModel.User(**User.dict() is_active=False)
    db_user = UserModel(email=user.email, hashed_password=user.password, name=user.name, surname1=user.surname1,
                        surname2=user.surname2, age=user.age, phone=user.phone)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user


def delete_user(user_id: int):
    db_user = db.session.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.session.delete(db_user)
    db.session.commit()
    return db_user

def login(email: str, password: str):
    user = db.session.query(UserModel).filter(UserModel.email == email, UserModel.hashed_password == password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales Incorrectas")
    else:
        return user