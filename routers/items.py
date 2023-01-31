from fastapi import APIRouter,Depends
from schemas import ItemCreate, ShowItem
from models import Item

from sqlalchemy.orm import Session
from database import get_db

from datetime import datetime


router = APIRouter()

@router.post("/item", tags=["products"],response_model=ShowItem)
def create_item(item: ItemCreate,db:Session=Depends(get_db)):
    date_posted = datetime.now().date()
    owner_id = 1
    item = Item(**item.dict(),date_posted=date_posted,owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/items",tags=["products"])
def get_items():
    return {"message": "Items"}
