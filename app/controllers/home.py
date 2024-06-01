from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from app.database import database
from app.models.fan_details import FanDetails
from sqlalchemy import select

home_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@home_router.get("/")
async def read_fan_details(request: Request):
    # query = select([FanDetails])
    # result = await database.fetch_all(query)
    return templates.TemplateResponse("home.html", {"request": request})