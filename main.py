from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import MetaData
import routes
from Configurations import Configuration
from fastapi_sqlalchemy import DBSessionMiddleware 

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=Configuration.get_db_url())
app.include_router(routes.router)


