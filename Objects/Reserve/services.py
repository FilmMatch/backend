from fastapi_sqlalchemy import db
from fastapi import HTTPException

from Objects.Reserve.model import Reserve as Reserve
from Objects.Reserve import schemas as ReserveSchemas
from Objects.Reserve.model import Reserve as ReserveModel   

from Objects.Item import services as ItemService
from Objects.Enums.ItemStatus import ItemStatus

from Utils import databaseService as databaseService

def create(reserve: ReserveSchemas.ReserveCreate, subuser_id: int):
    db_reserve = Reserve(item_id=reserve.item_id, subuser_id=subuser_id)
    ItemService.update_status(item_id=reserve.item_id, status=ItemStatus.reserved)
    return databaseService.create(instance=db_reserve)

def get(subuser_id: int):
    db_instance = db.session.query(ReserveModel).filter(ReserveModel.subuser_id == subuser_id).all()
    return db_instance