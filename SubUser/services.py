from fastapi import HTTPException
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from SubUser import schemas
from SubUser.model import SubUser


def create_subuser(subUser: schemas.SubUserCreate):
    db_sub_user = SubUser(name=subUser.name, user_id=subUser.user_id, type=subUser.type)
    db.session.add(db_sub_user)
    db.session.commit()
    db.session.refresh(db_sub_user)
    return db_sub_user


def get_subUsers(user_id: int):
    return db.session.query(SubUser).filter(SubUser.user_id == user_id).all()

def delete_subuser(sub_user_id: int):
    db_user = db.session.query(SubUser).filter(SubUser.id == sub_user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.session.delete(db_user)
    db.session.commit()
    return db_user

# update _subuser
#



