from fastapi_sqlalchemy import db
from fastapi import HTTPException

import uuid
from Objects.Catalog.model import Catalog as CatalogModel
from Objects.Catalog.schemas import CatalogCreateSchema as CatalogCreateSchema
from Objects.SessionToken.model import Session as SessionToken


from Utils import databaseService as databaseService

def create(catalog: CatalogCreateSchema, sessionToken: SessionToken):
    db_catalog = CatalogModel(name=catalog.name, subuser_id=sessionToken.subuser_id)
    return databaseService.create(instance=db_catalog)

def get():
    db_catalog = db.session.query(CatalogModel).all()
    return db_catalog


