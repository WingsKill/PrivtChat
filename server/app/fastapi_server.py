from fastapi import FastAPI
from enum import Enum

app = FastAPI()

"""
POST: to create data
GET: to read data
PUT: to update data
DELETE: to delete data
"""


class ItemModel(str, Enum):
    item_1 = "spagetto"
    item_2 = "bloob"
    item_3 = "piwpex"


@app.get("/")
async def root():
    return {"message": "Hello world!"}


@app.get("/item/{item_name}")
async def item_echo(item_name: str):
    return {"item": item_name}


@app.get("/get_item/{item_id}")
async def get_item_by_id(item_id: ItemModel):
    if item_id.value == "bloob":
        return "Yes"


@app.get("/user/me")
async def read_actual_user():
    return {"user": "you"}
