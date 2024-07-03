from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import MetaData
import routers as routes
from Configurations import Configuration
from fastapi_sqlalchemy import DBSessionMiddleware 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(DBSessionMiddleware, db_url=Configuration.get_db_url())
app.include_router(routes.router)


