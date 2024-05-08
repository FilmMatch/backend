from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import MetaData
import routes

app = FastAPI()
app.include_router(routes.router)


