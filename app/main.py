from fastapi import FastAPI
from . import models, database
from .routers import items

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(items.router)