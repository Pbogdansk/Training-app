# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    name: str
    reps: int
    sets: int
    load: int
class UpdateItem(BaseModel):
    name: Optional[str] = None
    reps: Optional[int] = None
    sets: Optional[int] = None
    load: Optional[int] = None

toDoList = {
    1: {
        "Excercize name": "test",
        "Number of sets": 5,
        "number of reps": 5
    }

}

# http://127.0.0 .1:8000/docs dokumentacja
@app.get("/home")  # jsonowanie sobie automatycznie robi FastApi
def test():
    return {"test"}

@app.get("/get-excersize/{excercise_id}")
def get_excercize(excercise_id: int = Path(None, description="The id of the excersize:")):
    return toDoList[excercise_id]

#@app.get("/search/{item_id}")
#def get_excercize(name: Optional[str] = None):
#    for item_id in toDoList:
 #       if toDoList[item_id].name == name:
 #           return toDoList[item_id]
#    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in toDoList:
        return {"already dodaned"}

    toDoList[item_id] = {"name": item.name, "reps": item.reps, "sets": item.sets, "load": item.load}
    return toDoList[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in toDoList:
        return {"Error": "Item does not exist"}
    if item.name != None:
        toDoList[item_id].name = item.name
    if item.reps != None:
        toDoList[item_id].reps = item.reps
    if item.sets != None:
        toDoList[item_id].sets = item.sets
    if item.load != None:
        toDoList[item_id].load = item.load
    return toDoList[item_id]