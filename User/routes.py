from fastapi import APIRouter,  HTTPException, Depends

from sqlalchemy.orm import Session
from . import schemas
from . import services
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # db_user = services.get_user_by_email(db, email=user.email)
    #if db_user:
        # raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db=db, user=user)


@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = services.get_users(db, skip=skip, limit=limit)
    return users

@router.delete("/users/{user_id}", response_model=schemas.User)
def create_user(user_id: int, db: Session = Depends(get_db)):
    # db_user = services.get_user_by_email(db, email=user.email)
    #if db_user:
        # raise HTTPException(status_code=400, detail="Email already registered")
    return services.delete_user(db=db, user_id=user_id)
