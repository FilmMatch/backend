from sqlalchemy.orm import Session
from SubUser import schemas
from SubUser.model import SubUser


def create_subuser(db: Session, subUser: schemas.SubUserCreate):
    db_sub_user = SubUser(name=subUser.name, user_id=subUser.user_id, type=subUser.type)
    db.add(db_sub_user)
    db.commit()
    db.refresh(db_sub_user)
    return db_sub_user
