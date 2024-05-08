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


@router.post("/subUser/", response_model=schemas.SubUserCreate)
def create_subuser(subUser: schemas.SubUserCreate, db: Session = Depends(get_db)):
    return services.create_subuser(db=db, subUser=subUser)


