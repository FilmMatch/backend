from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from SubUser import schemas
from SubUser import services
from database import SessionLocal

router = APIRouter()


@router.post("/subUser/", response_model=schemas.SubUserBase)
def create_subuser(subUser: schemas.SubUserCreate):
    return services.create_subuser(subUser=subUser)

@router.get("/subUser/{user_id}", response_model=list[schemas.SubUserBase])
def create_subuser(user_id: int):
    return services.get_subUsers(user_id=user_id)

@router.delete("/subUser/{sub_user}", response_model=schemas.SubUserBase)
def create_subuser(sub_user: int):
    return services.delete_subuser(sub_user_id=sub_user)



