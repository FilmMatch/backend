from fastapi import APIRouter,  HTTPException, Depends

from sqlalchemy.orm import Session
from . import schemas
from . import services
from database import SessionLocal

router = APIRouter()



@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    # db_user = services.get_user_by_email(db, email=user.email)
    #if db_user:
        # raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(user=user)


@router.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100):
    users = services.get_users(skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id: int):
    user = services.get_user_by_id(user_id=user_id)
    return user


@router.delete("/users/{user_id}", response_model=schemas.User)
def create_user(user_id: int):
    # db_user = services.get_user_by_email(db, email=user.email)
    #if db_user:
        # raise HTTPException(status_code=400, detail="Email already registered")
    return services.delete_user(user_id=user_id)

@router.post("/login/", response_model=schemas.User)
def create_user(user: schemas.UserLogin):
    # db_user = services.get_user_by_email(db, email=user.email)
    #if db_user:
        # raise HTTPException(status_code=400, detail="Email already registered")
    return services.login(email=user.email, password=user.password)