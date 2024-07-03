from fastapi_sqlalchemy import db
from fastapi import HTTPException

import uuid

from Objects.User.model import User as UserModel
from Objects.SessionToken.model import Session as SessionModel

from Objects.User.schema import UserCreate as UserCreateSchema

from Objects.SubUser import service as SubUserService

from Utils import databaseService as databaseService

from Objects.SubUser import service as SubUserService

def login(email: str, password: str):
    user = db.session.query(UserModel).filter(UserModel.email == email, UserModel.password == password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales Incorrectas")
    else:
        db_subuser = SubUserService.get_first_subUser(user_id=user.id)
        return create_session(subuser_id=db_subuser.id)
    

def register(user: UserCreateSchema):
    db_user = UserModel(email=user.email, password=user.password, name=user.name, surname1=user.surname1,
                        surname2=user.surname2, age=user.age, phone=user.phone)
    databaseService.create(instance=db_user)
    SubUserService.create_subUser(user_id=db_user.id, name=user.name, type=user.type)
    return db_user


def create_session(subuser_id: int):
    db_session = SessionModel(subuser_id =subuser_id, token=uuid.uuid4())
    databaseService.create(instance=db_session)
    return db_session