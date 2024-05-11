from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from SubUser import schemas
from SubUser import services
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.post("/subUser/", response_model=schemas.SubUserBase)
def create_subuser(subUser: schemas.SubUserCreate, db: Session = Depends(get_db)):
    return services.create_subuser(db=db, subUser=subUser)

@router.get("/subUser/{user_id}", response_model=list[schemas.SubUserBase])
def create_subuser(user_id: int, db: Session = Depends(get_db)):
    return services.get_subUsers(db=db, user_id=user_id)

@router.delete("/subUser/{sub_user}", response_model=schemas.SubUserBase)
def create_subuser(sub_user: int, db: Session = Depends(get_db)):
    return services.delete_subuser(db=db, sub_user_id=sub_user)



