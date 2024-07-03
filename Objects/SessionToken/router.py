from fastapi import APIRouter,  HTTPException, Depends

from sqlalchemy.orm import Session
from Objects.SessionToken import schemas as SessionSchemas
from Objects.SessionToken import sevices as SessionService
from Objects.User import schema as UserSchema


router = APIRouter()


@router.post("/login", response_model=SessionSchemas.SessionSchema)
def create_user(user: UserSchema.UserLogin):
    return SessionService.login(email=user.email, password=user.password)

@router.post("/register", response_model=UserSchema.User)
def create_user(user: UserSchema.UserCreate):
    return SessionService.register(user=user)