from fastapi import APIRouter,  HTTPException, Depends

from sqlalchemy.orm import Session
from Middlewares.TokenValidator import TokenValidator
from Objects.SessionToken import schemas as SessionSchemas
from Objects.SessionToken import sevices as SessionService
from Objects.Item import services as ItemService
from Objects.SessionToken.model import Session as SessionToken
from Objects.Item import schemas as ItemSchemas
from Objects.Enums.ItemStatus import ItemStatus

router = APIRouter()


@router.post("/item", response_model=ItemSchemas.ItemSchema)
def create(item: ItemSchemas.CreateItemSchema, sessionToken: SessionToken = Depends(TokenValidator())):
    return ItemService.create(item=item, sessionToken=sessionToken)

@router.get("/items", response_model=list[ItemSchemas.ItemSchema],)
def get(SessionToken = Depends(TokenValidator())):
    return ItemService.get()

@router.get("/items/{item_id}", response_model=ItemSchemas.ItemSchema)
def get_by_id(item_id: int, SessionToken = Depends(TokenValidator())):
    return ItemService.get_by_id(item_id=item_id)

@router.delete("/items/{item_id}", response_model=ItemSchemas.ItemSchema)
def delete(item_id: int, SessionToken = Depends(TokenValidator())):
    return ItemService.delete(item_id=item_id)

@router.post("/items/{item_id}/status", response_model=ItemSchemas.ItemSchema)
def update_status(item_id: int, status: ItemStatus, SessionToken = Depends(TokenValidator())):
    return ItemService.update_status(item_id=item_id, status=status)