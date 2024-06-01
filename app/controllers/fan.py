from fastapi import APIRouter, HTTPException, Request
from fastapi.templating import Jinja2Templates
from app.database import database
from app.models.fan_details import FanDetails
from sqlalchemy import select

fan_details_router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@fan_details_router.get("/")
async def read_fan_details(request: Request):
    query = select([FanDetails])
    result = await database.fetch_all(query)
    return templates.TemplateResponse("fan_details.html", {"request": request, "fans": result})

@fan_details_router.get("/{fan_id}")
async def read_fan_detail(fan_id: int, request: Request):
    query = select([FanDetails]).where(FanDetails.id == fan_id)
    result = await database.fetch_one(query)
    if not result:
        raise HTTPException(status_code=404, detail="Fan not found")
    return templates.TemplateResponse("fan_detail.html", {"request": request, "fan": result})
