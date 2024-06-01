from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.controllers.fan import fan_details_router
from app.controllers.home import home_router
from app.database import database, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(fan_details_router, prefix="/fan_details", tags=["fan_details"])
app.include_router(home_router, tags=["home"])