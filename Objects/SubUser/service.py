from fastapi_sqlalchemy import db
from fastapi import HTTPException

import uuid

from Objects.SubUser.model import SubUser as SubUserModel
from Objects.SessionToken.model import Session as SessionModel

from Objects.User.schema import UserCreate as UserCreateSchema

def create_subUser(user_id: str, type: int, name: str):
    db_user = SubUserModel(user_id=user_id, name=name, type=type)
    db.session.add(db_user)
    db.session.commit()
    db.session.refresh(db_user)
    return db_user

def get_first_subUser(user_id: int):
    db_user = db.session.query(SubUserModel).filter(SubUserModel.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="SubUser not found")
    else:
        return db_user
    