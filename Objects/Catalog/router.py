from fastapi import APIRouter,  HTTPException, Depends

from sqlalchemy.orm import Session
from Objects.Catalog import schemas as CatalogSchemas
from Objects.Catalog import services as CatalogService
from Objects.User import schema as UserSchema

from Middlewares.TokenValidator import TokenValidator
from Objects.SessionToken.model import Session as SessionToken

router = APIRouter()


@router.post("/catalog", response_model=CatalogSchemas.CatalogSchema)
def create(catalog: CatalogSchemas.CatalogCreateSchema, sessionToken: SessionToken = Depends(TokenValidator())):
    return CatalogService.create(catalog=catalog, sessionToken=sessionToken)

@router.get("/catalogs", response_model=list[CatalogSchemas.CatalogSchema],)
def get(SessionToken = Depends(TokenValidator())):
    return CatalogService.get()

