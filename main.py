#import fastapi and HTTPException
from fastapi import FastAPI, HTTPException
#import pydantic
from pydantic import BaseModel

# ----------------------------------------

# Create a class that describes the item
class Item(BaseModel):
    text: str = None # remove None (the value) to make it required
    is_done: bool = False

# Create the app object
app = FastAPI()


items = []


# Create a route
@app.get("/")
# Define a function that will be called when the route is accessed
def root():
    return {"message": "Hello World"}

# create a new endpoint to add items
@app.post("/items")
# accepts a string as input
def create_item(item: Item):
    # add the item to the list
    items.append(item)
    # return the items list
    return items

# create a new endpoint to get items by limit
@app.get("/items", response_model=list[Item])
def get_items(limit: int = 5):
    return items[0:limit]


# create a new endpoint to get items by id
@app.get("/items/{item_id}", response_model=Item)
def get_items(item_id: int) -> Item:
    # check if the item exists
    if item_id < len(items):
        # return the item
        return items[item_id]
    else:
        # raise an exception
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")