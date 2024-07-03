from fastapi_sqlalchemy import db
from fastapi import HTTPException

import uuid
from Objects.Item.model import Item as ItemModel
from Objects.Item import schemas as ItemSchemas
from Objects.SessionToken.model import Session as SessionToken
from Objects.Enums.ItemStatus import ItemStatus

from Utils import databaseService as databaseService

def create(item: ItemSchemas.CreateItemSchema, sessionToken: SessionToken):
    db_instance = ItemModel(name=item.name, description=item.description, price=item.price, subuser_id=sessionToken.subuser_id, catalog_id=item.catalog_id, status=ItemStatus.published)
    return databaseService.create(instance=db_instance)

def get_by_catalogId(catalog_id: int):
    db_instance = db.session.query(ItemModel).filter(ItemModel.catalog_id == catalog_id).all()
    return db_instance

def get_by_subuserId(subuser_id: int):
    db_instance = db.session.query(ItemModel).filter(ItemModel.subuser_id == subuser_id).all()
    return db_instance

def get():
    db_instance = db.session.query(ItemModel).all()
    return db_instance

def delete(item_id: int):
    db_instance = db.session.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_instance:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return databaseService.delete(instance=db_instance)

def update_status(item_id: int, status: ItemStatus):
    db_instance = db.session.query(ItemModel).filter(ItemModel.id == item_id).first()
    if not db_instance:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        db_instance.status = status
        return databaseService.update(instance=db_instance)
