from fastapi import HTTPException
from sqlalchemy.orm import Session
from SubUser import schemas
from SubUser.model import SubUser


def create_subuser(db: Session, subUser: schemas.SubUserCreate):
    db_sub_user = SubUser(name=subUser.name, user_id=subUser.user_id, type=subUser.type)
    db.add(db_sub_user)
    db.commit()
    db.refresh(db_sub_user)
    return db_sub_user


def get_subUsers(db: Session, user_id: int):
    return db.query(SubUser).filter(SubUser.user_id == user_id).all()

def delete_user(db: Session, sub_user_id: int):
    db_user = db.query(SubUser).filter(SubUser.id == sub_user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_user)
    db.commit()
    return db_user

