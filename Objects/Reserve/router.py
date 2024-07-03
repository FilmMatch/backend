from fastapi import APIRouter,  HTTPException, Depends

from sqlalchemy.orm import Session

from Middlewares.TokenValidator import TokenValidator
from Objects.Reserve import schemas as ReserveSchemas
from Objects.Reserve import services as ReserveService
from Objects.Reserve import model as ReserveModel

from Objects.SessionToken import model as SessionToken
from Objects.SessionToken import schemas as SessionSchemas

router = APIRouter()


@router.post("/reserve", response_model=ReserveSchemas.ReserveSchema)
def create_user(reserve: ReserveSchemas.ReserveCreate, sessionToken: SessionToken = Depends(TokenValidator())):
    return ReserveService.create(reserve=reserve, subuser_id=sessionToken.subuser_id)

@router.get("/reserves", response_model=list[ReserveSchemas.ReserveSchema],)
def get(sessionToken: SessionToken = Depends(TokenValidator())):
    return ReserveService.get(subuser_id=sessionToken.subuser_id)