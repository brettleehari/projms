from fastapi import APIRouter, HTTPException
from app.models.item import Item

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    return item

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
