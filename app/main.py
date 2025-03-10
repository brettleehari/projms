from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List  # Import List

app = FastAPI(
    title="Item Service",
    description="A simple microservice for managing items.",
    version="0.1.0",
)

# Data Model (Pydantic)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# In-memory data store (replace with a database in a real application)
items = {}
item_id_counter = 1

# --- API Endpoints ---

@app.post("/items/", response_model=Item, status_code=201)  # 201 Created
async def create_item(item: Item):
    """
    Create a new item.
    """
    global item_id_counter
    item_id = item_id_counter
    items[item_id] = item
    item_id_counter += 1
    return item

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Retrieve an item by its ID.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    """
    Update an existing item.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return item

@app.delete("/items/{item_id}", status_code=204) # 204 No Content
async def delete_item(item_id: int):
    """
    Delete an item by its ID.
    """
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return

@app.get("/items/", response_model=List[Item])  # Use List[Item]
async def list_items():
    """
    Retrieve a list of all items.
    """
    return list(items.values())


# --- Example Usage (Optional) ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
